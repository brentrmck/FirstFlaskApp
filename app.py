from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def index(name="Treehouse"):
    return "Hello from {}".format(name)

app.run(debug=True, port=8000, host='0.0.0.0')

#if __name__ == '__main__':
#    app.run()

# Test commit / push