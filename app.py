import json
from flask import Flask, request
from my_util import train_model, predict_spam
import logging


app = Flask(__name__)

cv, clf = train_model()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route('/predict',methods=['POST'])
def predict():
    # return render_template('result.html')
    app.logger.info('/predict POST')
    body = request.get_data()
    data = json.loads(body.decode())
    message = data.get('message')
    if message is None:
        return "No message found"
    # my_prediciton == 1: spam
    # my_prediciton == 0: ham
    my_prediction = predict_spam(cv, clf, message)
    # return render_template('result.html',prediction = my_prediction)

    if my_prediction == 1:
        return "SPAM\n"
    else:
        return "HAM\n"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
