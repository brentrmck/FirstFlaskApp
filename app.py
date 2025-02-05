from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
    return "Hello from {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return render_template("add.html", num1=num1, num2=num2)

app.run(debug=True, port=8000, host='0.0.0.0')

#if __name__ == '__main__':
#    app.run()

# Test commit / push