from bottle import route, run, template, request #route=URL , run=server , template=html , request=eingabe

@route('/') #/ ist Startseite von localhost
def start(): #Funktion wür die Startseite
    return template('start') #start.tpl wird benutzt

@route('/eingabe') #eingabe seite: localhost8000/eingabe
def eingabe():
    return template('eingabe') #eingabe.tpl

@route('/ergebnis', method='POST') #POST -> Eingabe verabreitet
def ergebnis():
    alter = request.forms.get('alter') #request.form=formular , get alter in tpl definiert (name=alter)
    return f"Du bist {alter} Jahre alt." #normaler f string mit alter als ausgabe

run(host='localhost', port=8080, debug=True)