from flask import Flask

app = Flask(__name__)
PORT = 1323

# catches all urls
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=PORT)
