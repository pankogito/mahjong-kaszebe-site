import flask
app = flask.Flask(__name__)
@app.route('/')
def index():
    content = flask.render_template('index_content.html')

    return flask.render_template('page.html', content=content)

@app.route('/style.css')
def style():
    return flask.send_file('static/style.css')
@app.route('/tournament')
def tournament():
    # mock participants
    participants = [
        {'name':'Jan Kowalski', 'country':"PL",},
        {'name': 'Jaonna Kowalska', 'country': "PL", },
    ]

    participants_content = ""

    for number,participant in enumerate(participants, 1):
        participants_content += flask.render_template(
            'participant_content.html',
            number = number,
            **participant
        )

    content = flask.render_template('tournament_content.html', participants = participants_content)

    return flask.render_template('page.html', content=content)

if __name__ == '__main__':
    app.run("0.0.0.0")