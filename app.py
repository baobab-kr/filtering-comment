from model_py3 import toxicCommentFilteringPredict
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, Baobab-kr Filtering Flask API!'

@app.route('/predict', methods=['POST'])
def predict():
    params = request.get_json()
    inputComment = params['comment']
    outputComment = toxicCommentFilteringPredict(inputComment);
    return outputComment

if __name__ == '__main__':
    app.run()