import random

from bottle import Bottle, run, template, static_file, request, response
from calculation import build_export_text, get_result_context

app = Bottle()


QUIZ_QUESTIONS = [
    {
        "question": "Was bedeutet BMI?",
        "answers": ["Body-Mass-Index", "Basis-Muskel-Intensität", "Bewegungs-Mess-Index"],
        "correct": "Body-Mass-Index"
    },
    {
        "question": "Was beschreibt der Gesamtumsatz?",
        "answers": ["Deinen täglichen Kalorienverbrauch", "Nur deinen Proteinbedarf", "Nur deinen BMI"],
        "correct": "Deinen täglichen Kalorienverbrauch"
    },
    {
        "question": "Was unterstützt Protein besonders?",
        "answers": ["Muskeln und Regeneration", "Nur den Wasserbedarf", "Die Körpergröße"],
        "correct": "Muskeln und Regeneration"
    },
    {
        "question": "Was hilft beim Abnehmen?",
        "answers": ["Ein moderates Kaloriendefizit", "Beliebig viele Snacks", "Gar kein Wasser trinken"],
        "correct": "Ein moderates Kaloriendefizit"
    },
    {
        "question": "Warum ist Wasser wichtig?",
        "answers": ["Es unterstützt viele Körperfunktionen", "Es ersetzt Schlaf", "Es macht Protein unnötig"],
        "correct": "Es unterstützt viele Körperfunktionen"
    },
    {
        "question": "Was bedeutet Muskelaufbau beim Kalorienziel?",
        "answers": ["Meist ein leichter Kalorienüberschuss", "Immer ein starkes Defizit", "Keine Kalorien beachten"],
        "correct": "Meist ein leichter Kalorienüberschuss"
    },
    {
        "question": "Wovon hängt der Proteinbedarf in FitCheck ab?",
        "answers": ["Gewicht und Ziel", "Nur vom Alter", "Nur von der Körpergröße"],
        "correct": "Gewicht und Ziel"
    },
    {
        "question": "Was ist ein Aktivitätslevel?",
        "answers": ["Wie aktiv du im Alltag bist", "Deine Schuhgröße", "Deine Schlafenszeit"],
        "correct": "Wie aktiv du im Alltag bist"
    },
    {
        "question": "Was ist ein gutes tägliches Ziel?",
        "answers": ["Regelmäßige Bewegung", "Nie Pausen machen", "Immer Mahlzeiten auslassen"],
        "correct": "Regelmäßige Bewegung"
    },
    {
        "question": "Was ist FitCheck hauptsächlich?",
        "answers": ["Ein Rechner für einfache Fitnesswerte", "Ein Arzttermin", "Ein Lieferservice"],
        "correct": "Ein Rechner für einfache Fitnesswerte"
    }
]


@app.route('/')
def start():
    return template('start', challenge=None)


@app.route('/challenge')
def challenge():
    challenges = [
    "Trinke heute nur Wasser statt Softdrinks.",
    "Gehe heute 20 Minuten spazieren.",
    "Iss heute zu jeder Mahlzeit etwas Gemüse.",
    "Verzichte heute auf Fast Food.",
    "Gehe heute 30 Minuten früher ins Bett.",
    "Mache heute einen Spaziergang nach dem Abendessen.",
    "Lass heute eine unnötige Autofahrt weg und gehe zu Fuß.",
    "Trinke direkt nach dem Aufstehen ein Glas Wasser.",
    "Verzichte heute auf Süßigkeiten.",
    "Stehe heute jede Stunde einmal kurz auf.",
    "Mache heute etwas Sport, egal wie kurz.",
    "Iss heute bewusst und ohne Handy oder Fernseher.",
    "Nimm heute die Treppe statt den Aufzug.",
    "Verbringe heute mindestens 30 Minuten draußen.",
    "Achte heute auf eine aufrechte Haltung.",
    "Trinke heute mindestens 2 Liter Wasser.",
    "Mache heute einen kleinen Abendspaziergang.",
    "Lass heute ein zuckerhaltiges Getränk weg.",
    "Iss heute eine extra Portion Obst.",
    "Plane heute deine Sporteinheit für die Woche.",
    "Gehe heute mindestens 8.000 Schritte.",
    "Mache heute 10 Minuten Dehnübungen.",
    "Verzichte heute auf einen späten Mitternachtssnack.",
    "Koche heute eine Mahlzeit selbst.",
    "Iss heute langsam und ohne Eile.",
    "Gehe heute für frische Luft nach draußen, auch wenn du keine Lust hast.",
    "Stehe heute beim Telefonieren auf und bewege dich.",
    "Trinke vor jeder Mahlzeit ein Glas Wasser.",
    "Verbringe heute 30 Minuten ohne Social Media.",
    "Mache heute etwas, das deinen Stress reduziert.",
    "Gehe heute eine Haltestelle früher aus Bus oder Bahn.",
    "Achte heute darauf, genug Protein zu essen.",
    "Mache heute einen kurzen Spaziergang in deiner Mittagspause.",
    "Lüfte heute mehrmals deine Wohnung.",
    "Versuche heute mindestens 7 Stunden zu schlafen.",
    "Iss heute keine Chips oder Snacks aus Langeweile.",
    "Bewege dich heute insgesamt mindestens 30 Minuten.",
    "Starte den Tag mit einem gesunden Frühstück.",
    "Gehe heute bewusst ein paar Minuten in die Sonne.",
    "Räume heute deinen Trainings- oder Arbeitsbereich auf."
]

    return template('start', challenge=random.choice(challenges))


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


@app.route('/about')
def about():
    return template('about')


@app.route('/impressum')
def impressum():
    return template('impressum')


@app.route('/datenschutz')
def datenschutz():
    return template('datenschutz')


@app.route('/agb')
def agb():
    return template('agb')

@app.route('/tipps')
def tipps():
    return template('tipps')


@app.route('/workout')
def workout_form():
    return template('workout', workout=None, error=None)


@app.route('/workout', method='POST')
def workout_result():
    ort = request.forms.get('ort')
    level = request.forms.get('level')
    workouts = {

    ("zuhause", "anfaenger"): [
        ["10 Kniebeugen", "8 Liegestütze", "20 Sekunden Plank", "10 Ausfallschritte"],
        ["15 Kniebeugen", "10 Sit-ups", "30 Sekunden Plank", "20 Hampelmänner"],
        ["20 Kniebeugen", "10 Liegestütze", "15 Ausfallschritte", "30 Sekunden Plank"]
    ],

    ("zuhause", "fortgeschritten"): [
        ["25 Kniebeugen", "20 Liegestütze", "45 Sekunden Plank", "20 Ausfallschritte"],
        ["30 Kniebeugen", "15 Burpees", "60 Sekunden Plank", "30 Hampelmänner"],
        ["20 Burpees", "25 Liegestütze", "60 Sekunden Plank", "30 Kniebeugen"]
    ],

    ("zuhause", "profi"): [
        ["40 Kniebeugen", "20 Liegestütze", "90 Sekunden Plank", "40 Ausfallschritte"],
        ["50 Kniebeugen", "25 Burpees", "120 Sekunden Plank", "50 Hampelmänner"],
        ["30 Burpees", "30 Liegestütze", "2 Minuten Plank", "60 Kniebeugen"]
    ],

    ("gym", "anfaenger"): [
        ["Beinpresse 3x10", "Brustpresse 3x10", "Latzug 3x10", "Plank 3x30 Sekunden"],
        ["Rudern 3x10", "Schulterpresse 3x10", "Beinbeuger 3x10", "10 Minuten Fahrrad"],
        ["Beinstrecker 3x12", "Brustpresse 3x12", "Latzug 3x12", "Bauchmaschine 3x15"]
    ],

    ("gym", "fortgeschritten"): [
        ["Kniebeugen 4x8", "Bankdrücken 4x8", "Rudern 4x10", "Schulterdrücken 3x10"],
        ["Kreuzheben 4x6", "Latzug 4x10", "Beinpresse 4x10", "Bizepscurls 3x12"],
        ["Schrägbankdrücken 4x8", "Rudern Kabelzug 4x10", "Beinstrecker 3x12", "Trizepsdrücken 3x12"]
    ],

    ("gym", "profi"): [
        ["Kniebeugen 5x5", "Bankdrücken 5x5", "Kreuzheben 5x5", "Klimmzüge 4xMax"],
        ["Schrägbankdrücken 4x8", "Rudern 4x10", "Beinpresse 4x10", "Schulterdrücken 4x10"],
        ["Kreuzheben 4x6", "Klimmzüge 4xMax", "Bulgarian Split Squats 3x12", "Bizepscurls 3x12"],
        ["Bankdrücken 4x8", "Latzug 4x10", "Beinstrecker 3x12", "Trizepsdrücken 3x12"],
        ["Frontkniebeugen 4x6", "Kurzhantel-Bankdrücken 4x10", "Rudern Kabelzug 4x10", "Seitheben 3x15"]
    ],

    ("outdoor", "anfaenger"): [
        ["15 Minuten Spaziergang", "10 Kniebeugen", "10 Ausfallschritte", "5 Minuten Dehnen"],
        ["20 Minuten zügiges Gehen", "15 Kniebeugen", "10 Liegestütze", "5 Minuten Dehnen"],
        ["2 km Spaziergang", "15 Kniebeugen", "15 Ausfallschritte", "30 Sekunden Plank"]
    ],

    ("outdoor", "fortgeschritten"): [
        ["3 km Joggen", "20 Kniebeugen", "15 Liegestütze", "10 Ausfallschritte"],
        ["20 Minuten Intervalllauf", "25 Kniebeugen", "20 Liegestütze", "60 Sekunden Plank"],
        ["4 km Lauf", "20 Ausfallschritte", "20 Liegestütze", "45 Sekunden Plank"]
    ],

    ("outdoor", "profi"): [
        ["5 km Lauf", "30 Liegestütze", "50 Kniebeugen", "90 Sekunden Plank"],
        ["10 Sprintintervalle", "40 Ausfallschritte", "30 Liegestütze", "2 Minuten Plank"],
        ["8 km Lauf", "50 Kniebeugen", "40 Liegestütze", "2 Minuten Plank"]
    ]
}
    workout_options = workouts.get((ort, level))
    if workout_options is None:
        return template('workout', workout=None, error="Bitte wähle Trainingsort und Fitnesslevel aus.")

    workout = random.choice(workout_options)
    return template('workout', workout=workout, error=None, ort=ort, level=level)


@app.route('/quiz', method=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        question_index = int(request.forms.get('question_index'))
        score = int(request.forms.get('score'))
        answer = request.forms.get('answer')

        previous_question = QUIZ_QUESTIONS[question_index]
        if answer == previous_question["correct"]:
            score += 1

        question_index += 1
    else:
        question_index = 0
        score = 0

    finished = question_index >= len(QUIZ_QUESTIONS)
    current_question = None if finished else QUIZ_QUESTIONS[question_index]

    return template(
        'quiz',
        question=current_question,
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
