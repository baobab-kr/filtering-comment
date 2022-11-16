from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, Baobab-kr Filtering Flask API!'
    
if __name__ == '__main__':
    app.run()