
import optparse
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def launch():
    return app.send_static_file('calculator.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="80", debug=True)

'''
def flaskrun(app, default_host="localhost", default_port="789"):
    """
    Takes a flask.Flask instance and runs it. Parses
    command-line flags to configure the app.
    """

    # Set up the command-line options
    parser = optparse.OptionParser()
    msg = 'Hostname of Flask app [{}]'.format(default_host)
    parser.add_option("-H", "--host",
                      help=msg,
                      default=default_host)
    msg = 'Port for Flask app [{}]'.format(default_port)
    parser.add_option("-P", "--port",
                      help=msg,
                      default=default_port)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=optparse.SUPPRESS_HELP)

    options, _ = parser.parse_args()

    app.run(
        debug=True,
        host=options.host,
        port=int(options.port)
    )
    '''

