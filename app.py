from flask import Flask

app = Flask(__name__)
PORT = 8000

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=PORT)
