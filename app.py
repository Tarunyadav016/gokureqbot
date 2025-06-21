from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@goku_bhai001'


if __name__ == "__main__":
    app.run()

# Owner: @goku_bhai001
# Developer: @goku_bhai001
# Ask Doubt on telegram @goku_bhai001
