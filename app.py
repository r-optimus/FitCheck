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

    groesse_m = groesse_cm / 100
    bmi = gewicht / (groesse_m ** 2)
    bmi_gerundet = round(bmi, 2)

    if bmi < 18.5:
        bewertung = "Untergewicht"
    elif bmi < 25:
        bewertung = "Normalgewicht"
    elif bmi < 30:
        bewertung = "Übergewicht"
    else:
        bewertung = "BERATung erforderrlich"

    wasser_ml = gewicht * 35
    wasser_liter = round(wasser_ml / 1000, 2)

    protein = round(gewicht * 1.5, 1)

    return template(
        'ergebnis',
        bmi=bmi_gerundet,
        bewertung=bewertung,
        wasser_liter=wasser_liter,
        protein=protein
    )


@app.route('/about')
def about():
    return template('about')


@app.route('/static/<filename:path>')
def static_files(filename):
    return static_file(filename, root='./static')


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)