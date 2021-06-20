from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a d Docker container!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)