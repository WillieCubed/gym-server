from flask import Blueprint

ws = Blueprint('ws', __name__)


@ws.route('/experiment/<string:experiment_id>')
def connect_to_experiment(experiment_id: str, socket):
    while not socket.closed:
        message = socket.receive()
        socket.send('test')
