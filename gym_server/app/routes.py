"""Routes used to communicate with a client.

To start the server in debug mode, run the server with environment variable
DEBUG_FLAG set to true (1).
"""

from . import app


@app.route('/')
def index():
    # noinspection PyUnresolvedReferences
    return render_template('index.html', title='')
