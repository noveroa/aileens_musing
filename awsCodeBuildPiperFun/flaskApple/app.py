from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, appley-goodness \U0001F34E"!'

if __name__ == '__main__':
    app.run()

