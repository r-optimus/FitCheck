from bottle import Bottle, run, template, static_file, request
from calculation import get_result_context

app = Bottle()


@app.route('/')
def start():
    return template('start')


@app.route('/eingabe')
def eingabe():
    return template('eingabe')


@app.route('/ergebnis', method='POST')
def ergebnis():
    return template('ergebnis', **get_result_context(request.forms))


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
