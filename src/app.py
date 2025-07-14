
from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    #return '<h1>Hello World</h1>'
    return jsonify({'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
                    'hostname': socket.gethostname(),
                    'message': 'Hi CWS Team, You are doing great!'
                  })

@app.route('/api/v1/health')

def health():
    #return '<h1>Hello World</h1>'
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")

#'api/v1/details'
#'api/v1/health'