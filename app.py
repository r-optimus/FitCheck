from bottle import route, run, template

@route('/')
def start():
    return template('start')

run(host='localhost', port=8080, debug=True)