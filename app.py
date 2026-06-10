import random

from bottle import Bottle, request, response, run, static_file, template
from calculation import build_export_text, get_result_context

app = Bottle()


def rows(text):
    return [line.split("|") for line in text.strip().splitlines()]


QUIZ_QUESTIONS = [
    {"question": q, "answers": answers, "correct": answers[0]}
    for q, *answers in [
        ("Was bedeutet BMI?", "Body-Mass-Index", "Basis-Muskel-Intensität", "Bewegungs-Mess-Index"),
        ("Was beschreibt der Gesamtumsatz?", "Deinen täglichen Kalorienverbrauch", "Nur deinen Proteinbedarf", "Nur deinen BMI"),
        ("Was unterstützt Protein besonders?", "Muskeln und Regeneration", "Nur den Wasserbedarf", "Die Körpergröße"),
        ("Was hilft beim Abnehmen?", "Ein moderates Kaloriendefizit", "Beliebig viele Snacks", "Gar kein Wasser trinken"),
        ("Warum ist Wasser wichtig?", "Es unterstützt viele Körperfunktionen", "Es ersetzt Schlaf", "Es macht Protein unnötig"),
        ("Was bedeutet Muskelaufbau beim Kalorienziel?", "Meist ein leichter Kalorienüberschuss", "Immer ein starkes Defizit", "Keine Kalorien beachten"),
        ("Wovon hängt der Proteinbedarf in FitCheck ab?", "Gewicht und Ziel", "Nur vom Alter", "Nur von der Körpergröße"),
        ("Was ist ein Aktivitätslevel?", "Wie aktiv du im Alltag bist", "Deine Schuhgröße", "Deine Schlafenszeit"),
        ("Was ist ein gutes tägliches Ziel?", "Regelmäßige Bewegung", "Nie Pausen machen", "Immer Mahlzeiten auslassen"),
        ("Was ist FitCheck hauptsächlich?", "Ein Rechner für einfache Fitnesswerte", "Ein Arzttermin", "Ein Lieferservice"),
    ]
]

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
    return template('start', challenge=None)


@app.route('/challenge')
def challenge():
    return template('start', challenge=random.choice(CHALLENGES)[0])


@app.route('/eingabe')
def eingabe():
    return template('eingabe')


@app.route('/ergebnis', method='POST')
def ergebnis():
    return template('ergebnis', **get_result_context(request.forms))


@app.route('/export', method='POST')
def export():
    response.content_type = 'text/plain; charset=utf-8'
    response.set_header('Content-Disposition', 'attachment; filename="fitcheck-ergebnis.txt"')
    return build_export_text(request.forms)


for view in ('about', 'impressum', 'datenschutz', 'agb', 'tipps'):
    app.route(f'/{view}')(lambda view=view: template(view))


@app.route('/workout')
def workout_form():
    return template('workout', workout=None, error=None)


@app.route('/workout', method='POST')
def workout_result():
    workout_options = WORKOUTS.get((request.forms.get('ort'), request.forms.get('level')))
    if workout_options is None:
        return template('workout', workout=None, error="Bitte wähle Trainingsort und Fitnesslevel aus.")
    return template('workout', workout=random.choice(workout_options), error=None)


@app.route('/quiz', method=['GET', 'POST'])
def quiz():
    question_index = int(request.forms.get('question_index', 0))
    score = int(request.forms.get('score', 0))
    if request.method == 'POST':
        score += request.forms.get('answer') == QUIZ_QUESTIONS[question_index]["correct"]
        question_index += 1

    finished = question_index >= len(QUIZ_QUESTIONS)
    return template(
        'quiz',
        question=None if finished else QUIZ_QUESTIONS[question_index],
        question_index=question_index,
        question_number=question_index + 1,
        total_questions=len(QUIZ_QUESTIONS),
        score=score,
        finished=finished
    )


@app.route('/static/<filename:path>')
def static_files(filename):
    return static_file(filename, root='./static')


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
