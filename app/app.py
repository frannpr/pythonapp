from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>Prueba de Python en Docker!</h1>
    """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')