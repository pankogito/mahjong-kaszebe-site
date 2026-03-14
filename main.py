import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    content = flask.render_template('index_content.html')

    return flask.render_template('page.html', content=content)


@app.route('/tournament')
def tournament():
    content = flask.render_template('tournament_content.html')

    return flask.render_template('page.html', content=content)

if __name__ == '__main__':
    app.run()