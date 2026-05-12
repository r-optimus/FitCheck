from bottle import Bottle, run, template, static_file, request

app = Bottle()


@app.route('/')
def start():
    return template('start')


@app.route('/eingabe')
def eingabe():
    return template('eingabe')


@app.route('/ergebnis', method='POST')
def ergebnis():

    gewicht = float(request.forms.get('gewicht'))
    groesse_cm = float(request.forms.get('groesse'))
    alter = int(request.forms.get('alter'))
    geschlecht = request.forms.get('geschlecht')
    aktivitaet = request.forms.get('aktivitaet')
    ziel = request.forms.get('ziel')

    #Berechnungen

    groesse_m = groesse_cm / 100
    bmi = gewicht / (groesse_m ** 2)
    bmi_gerundet = round(bmi, 2)
    

    if geschlecht == "maennlich":
        grundumsatz = 10 * gewicht + 6.25 * groesse_cm - 5 * alter + 5
    else:
        grundumsatz = 10 * gewicht + 6.25 * groesse_cm - 5 * alter - 161

    if bmi < 18.5:
        bewertung = "Untergewicht"
        bmi_klasse = "bmi-orange"
    elif bmi < 25:
        bewertung = "Normalgewicht"
        bmi_klasse = "bmi-green"
    elif bmi < 30:
        bewertung = "Übergewicht"
        bmi_klasse = "bmi-orange"
    else:
        bewertung = "Adipositas"
        bmi_klasse = "bmi-red"

    wasser_ml = gewicht * 35
    wasser_liter = round(wasser_ml / 1000, 2)

    protein = round(gewicht * 1.5, 1)

    return template(
        'ergebnis',
        bmi=bmi_gerundet,
        bewertung=bewertung,
        bmi_klasse=bmi_klasse,
        wasser_liter=wasser_liter,
        protein=protein,
        grundumsatz=round(grundumsatz)
        
    )


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

@app.route('/static/<filename:path>')
def static_files(filename):
    return static_file(filename, root='./static')


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
