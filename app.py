import hashlib
import hmac
import random
import secrets
import sqlite3
from datetime import date
from pathlib import Path

from bottle import Bottle, request, response, run, static_file, template
from calculation import build_export_text, get_result_context

app = Bottle()
DATABASE = Path(__file__).with_name('fitcheck_progress.db')
COOKIE_SECRET = "fitcheck-local-login-secret"
PASSWORD_ITERATIONS = 120_000

def rows(text):
    return [line.split("|") for line in text.strip().splitlines()]

def init_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS progress_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                entry_date TEXT NOT NULL,
                weight REAL NOT NULL,
                bmi REAL,
                note TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)

def get_database_connection():
    init_database()
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

def redirect_to(location):
    response.status = 303
    response.set_header('Location', location)
    return ""

def normalize_username(username):
    return (username or '').strip().lower()

def hash_password(password):
    salt = secrets.token_hex(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), PASSWORD_ITERATIONS).hex()
    return f"{salt}${password_hash}"

def verify_password(password, stored_hash):
    try:
        salt, expected_hash = stored_hash.split('$', 1)
    except ValueError:
        return False
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), PASSWORD_ITERATIONS).hex()
    return hmac.compare_digest(password_hash, expected_hash)

def login_user(user_id):
    response.set_cookie('fitcheck_user', str(user_id), secret=COOKIE_SECRET, path='/', httponly=True, samesite='Lax')

def get_current_user():
    user_id = request.get_cookie('fitcheck_user', secret=COOKIE_SECRET)
    if not user_id:
        return None
    try:
        user_id = int(user_id)
    except ValueError:
        return None

    with get_database_connection() as connection:
        return connection.execute(
            "SELECT id, username FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()

def render(view, **context):
    context["current_user"] = get_current_user()
    return template(view, **context)

def parse_optional_float(value):
    return float(value) if value not in (None, '') else None

def change_text(value, unit):
    if value is None:
        return "-"
    sign = "+" if value > 0 else ""
    return f"{sign}{round(value, 1)}{' ' + unit if unit else ''}"

def format_short_date(iso_date):
    try:
        _year, month, day = iso_date.split('-')
    except ValueError:
        return iso_date
    return f"{day}.{month}"

def build_progress_context(user_id, error=None):
    with get_database_connection() as connection:
        entries = connection.execute("""
            SELECT id, entry_date, weight, bmi, note
            FROM progress_entries
            WHERE user_id = ?
            ORDER BY entry_date DESC, id DESC
        """, (user_id,)).fetchall()

    oldest = entries[-1] if entries else None
    newest = entries[0] if entries else None
    weight_change = newest["weight"] - oldest["weight"] if len(entries) >= 2 else None
    bmi_entries = [entry for entry in entries if entry["bmi"] is not None]
    bmi_change = bmi_entries[0]["bmi"] - bmi_entries[-1]["bmi"] if len(bmi_entries) >= 2 else None
    weights = [entry["weight"] for entry in entries]
    min_weight = min(weights) if weights else 0
    max_weight = max(weights) if weights else 0
    weight_range = max(max_weight - min_weight, 1)
    chart_entries = [
        {
            "date": entry["entry_date"],
            "label": format_short_date(entry["entry_date"]),
            "weight": entry["weight"],
            "height": 24 + ((entry["weight"] - min_weight) / weight_range) * 96,
        }
        for entry in reversed(entries[:12])
    ]

    stats = [
        ("Einträge", str(len(entries))),
        ("Aktuelles Gewicht", f'{newest["weight"]} kg' if newest else "-"),
        ("Aktueller BMI", str(newest["bmi"]) if newest and newest["bmi"] is not None else "-"),
        ("Gewicht seit Start", change_text(weight_change, "kg")),
        ("BMI seit Start", change_text(bmi_change, "")),
    ]

    return {
        "entries": entries,
        "stats": stats,
        "chart_entries": chart_entries,
        "today": date.today().isoformat(),
        "error": error,
    }

CHALLENGES = rows("""
Trinke heute nur Wasser statt Softdrinks.
Gehe heute 20 Minuten spazieren.
Iss heute zu jeder Mahlzeit etwas Gemüse.
Verzichte heute auf Fast Food.
Gehe heute 30 Minuten früher ins Bett.
Mache heute einen Spaziergang nach dem Abendessen.
Lass heute eine unnötige Autofahrt weg und gehe zu Fuß.
Trinke direkt nach dem Aufstehen ein Glas Wasser.
Verzichte heute auf Süßigkeiten.
Stehe heute jede Stunde einmal kurz auf.
Mache heute etwas Sport, egal wie kurz.
Iss heute bewusst und ohne Handy oder Fernseher.
Nimm heute die Treppe statt den Aufzug.
Verbringe heute mindestens 30 Minuten draußen.
Achte heute auf eine aufrechte Haltung.
Trinke heute mindestens 2 Liter Wasser.
Mache heute einen kleinen Abendspaziergang.
Lass heute ein zuckerhaltiges Getränk weg.
Iss heute eine extra Portion Obst.
Plane heute deine Sporteinheit für die Woche.
Gehe heute mindestens 8.000 Schritte.
Mache heute 10 Minuten Dehnübungen.
Verzichte heute auf einen späten Mitternachtssnack.
Koche heute eine Mahlzeit selbst.
Iss heute langsam und ohne Eile.
Gehe heute für frische Luft nach draußen, auch wenn du keine Lust hast.
Stehe heute beim Telefonieren auf und bewege dich.
Trinke vor jeder Mahlzeit ein Glas Wasser.
Verbringe heute 30 Minuten ohne Social Media.
Mache heute etwas, das deinen Stress reduziert.
Gehe heute eine Haltestelle früher aus Bus oder Bahn.
Achte heute darauf, genug Protein zu essen.
Mache heute einen kurzen Spaziergang in deiner Mittagspause.
Lüfte heute mehrmals deine Wohnung.
Versuche heute mindestens 7 Stunden zu schlafen.
Iss heute keine Chips oder Snacks aus Langeweile.
Bewege dich heute insgesamt mindestens 30 Minuten.
Starte den Tag mit einem gesunden Frühstück.
Gehe heute bewusst ein paar Minuten in die Sonne.
Räume heute deinen Trainings- oder Arbeitsbereich auf.
""")

WORKOUTS = {
    ("zuhause", "anfaenger"): rows("""10 Kniebeugen|8 Liegestütze|20 Sekunden Plank|10 Ausfallschritte
15 Kniebeugen|10 Sit-ups|30 Sekunden Plank|20 Hampelmänner
20 Kniebeugen|10 Liegestütze|15 Ausfallschritte|30 Sekunden Plank"""),
    ("zuhause", "fortgeschritten"): rows("""25 Kniebeugen|20 Liegestütze|45 Sekunden Plank|20 Ausfallschritte
30 Kniebeugen|15 Burpees|60 Sekunden Plank|30 Hampelmänner
20 Burpees|25 Liegestütze|60 Sekunden Plank|30 Kniebeugen"""),
    ("zuhause", "profi"): rows("""40 Kniebeugen|20 Liegestütze|90 Sekunden Plank|40 Ausfallschritte
50 Kniebeugen|25 Burpees|120 Sekunden Plank|50 Hampelmänner
30 Burpees|30 Liegestütze|2 Minuten Plank|60 Kniebeugen"""),
    ("gym", "anfaenger"): rows("""Beinpresse 3x10|Brustpresse 3x10|Latzug 3x10|Plank 3x30 Sekunden
Rudern 3x10|Schulterpresse 3x10|Beinbeuger 3x10|10 Minuten Fahrrad
Beinstrecker 3x12|Brustpresse 3x12|Latzug 3x12|Bauchmaschine 3x15"""),
    ("gym", "fortgeschritten"): rows("""Kniebeugen 4x8|Bankdrücken 4x8|Rudern 4x10|Schulterdrücken 3x10
Kreuzheben 4x6|Latzug 4x10|Beinpresse 4x10|Bizepscurls 3x12
Schrägbankdrücken 4x8|Rudern Kabelzug 4x10|Beinstrecker 3x12|Trizepsdrücken 3x12"""),
    ("gym", "profi"): rows("""Kniebeugen 5x5|Bankdrücken 5x5|Kreuzheben 5x5|Klimmzüge 4xMax
Schrägbankdrücken 4x8|Rudern 4x10|Beinpresse 4x10|Schulterdrücken 4x10
Kreuzheben 4x6|Klimmzüge 4xMax|Bulgarian Split Squats 3x12|Bizepscurls 3x12
Bankdrücken 4x8|Latzug 4x10|Beinstrecker 3x12|Trizepsdrücken 3x12
Frontkniebeugen 4x6|Kurzhantel-Bankdrücken 4x10|Rudern Kabelzug 4x10|Seitheben 3x15"""),
    ("outdoor", "anfaenger"): rows("""15 Minuten Spaziergang|10 Kniebeugen|10 Ausfallschritte|5 Minuten Dehnen
20 Minuten zügiges Gehen|15 Kniebeugen|10 Liegestütze|5 Minuten Dehnen
2 km Spaziergang|15 Kniebeugen|15 Ausfallschritte|30 Sekunden Plank"""),
    ("outdoor", "fortgeschritten"): rows("""3 km Joggen|20 Kniebeugen|15 Liegestütze|10 Ausfallschritte
20 Minuten Intervalllauf|25 Kniebeugen|20 Liegestütze|60 Sekunden Plank
4 km Lauf|20 Ausfallschritte|20 Liegestütze|45 Sekunden Plank"""),
    ("outdoor", "profi"): rows("""5 km Lauf|30 Liegestütze|50 Kniebeugen|90 Sekunden Plank
10 Sprintintervalle|40 Ausfallschritte|30 Liegestütze|2 Minuten Plank
8 km Lauf|50 Kniebeugen|40 Liegestütze|2 Minuten Plank"""),
}

@app.route('/')
def start():
    return render('start', challenge=None)

@app.route('/challenge')
def challenge():
    return render('start', challenge=random.choice(CHALLENGES)[0])

@app.route('/eingabe')
def eingabe():
    return render('eingabe')

@app.route('/ergebnis', method='POST')
def ergebnis():
    return render('ergebnis', **get_result_context(request.forms))

@app.route('/export', method='POST')
def export():
    response.content_type = 'text/plain; charset=utf-8'
    response.set_header('Content-Disposition', 'attachment; filename="fitcheck-ergebnis.txt"')
    return build_export_text(request.forms)

for view in ('about', 'impressum', 'datenschutz', 'agb', 'tipps'):
    app.route(f'/{view}')(lambda view=view: render(view))

@app.route('/workout')
def workout_form():
    return render('workout', workout=None, error=None)

@app.route('/workout', method='POST')
def workout_result():
    workout_options = WORKOUTS.get((request.forms.get('ort'), request.forms.get('level')))
    if workout_options is None:
        return render('workout', workout=None, error="Bitte wähle Trainingsort und Fitnesslevel aus.")
    return render('workout', workout=random.choice(workout_options), error=None)

@app.route('/login')
def login_form():
    if get_current_user():
        return redirect_to('/fortschritt')
    return render('login', error=None)

@app.route('/login', method='POST')
def login():
    username = normalize_username(request.forms.get('username'))
    password = request.forms.get('password') or ''

    with get_database_connection() as connection:
        user = connection.execute(
            "SELECT id, username, password_hash FROM users WHERE username = ?",
            (username,)
        ).fetchone()

    if user is None or not verify_password(password, user["password_hash"]):
        return render('login', error="Benutzername oder Passwort ist falsch.")

    login_user(user["id"])
    return redirect_to('/fortschritt')

@app.route('/registrieren', method='POST')
def register():
    username = normalize_username(request.forms.get('username'))
    password = request.forms.get('password') or ''

    if len(username) < 3 or len(password) < 4:
        return render('login', error="Benutzername braucht mindestens 3 Zeichen, Passwort mindestens 4.")

    try:
        with get_database_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, hash_password(password))
            )
            user_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        return render('login', error="Dieser Benutzername ist schon vergeben.")

    login_user(user_id)
    return redirect_to('/fortschritt')

@app.route('/logout')
def logout():
    response.delete_cookie('fitcheck_user', path='/')
    return redirect_to('/')

@app.route('/fortschritt')
def progress():
    user = get_current_user()
    if user is None:
        return redirect_to('/login')
    return render('fortschritt', **build_progress_context(user["id"]))

@app.route('/fortschritt', method='POST')
def save_progress():
    user = get_current_user()
    if user is None:
        return redirect_to('/login')

    try:
        entry_date = request.forms.get('entry_date') or date.today().isoformat()
        weight = float(request.forms.get('weight'))
        bmi = parse_optional_float(request.forms.get('bmi'))
        note = (request.forms.get('note') or '').strip()
    except ValueError:
        return render('fortschritt', **build_progress_context(user["id"], "Bitte prüfe deine Eingaben."))

    with get_database_connection() as connection:
        connection.execute("""
            INSERT INTO progress_entries (user_id, entry_date, weight, bmi, note)
            VALUES (?, ?, ?, ?, ?)
        """, (user["id"], entry_date, weight, bmi, note))

    return redirect_to('/fortschritt')

@app.route('/fortschritt/<entry_id:int>/loeschen', method='POST')
def delete_progress_entry(entry_id):
    user = get_current_user()
    if user is None:
        return redirect_to('/login')

    with get_database_connection() as connection:
        connection.execute(
            "DELETE FROM progress_entries WHERE id = ? AND user_id = ?",
            (entry_id, user["id"])
        )

    return redirect_to('/fortschritt')

@app.route('/static/<filename:path>')
def static_files(filename):
    return static_file(filename, root='./static')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
