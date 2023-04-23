import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

def train_model():
    df = pd.read_csv("spam.csv", encoding="latin-1")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    df['label'] = df['class'].map({'ham': 0, 'spam': 1})
    X = df['message']
    y = df['label']
    cv = CountVectorizer()
    X = cv.fit_transform(X)
    clf = MultinomialNB()
    clf.fit(X, y)
    joblib.dump(clf, 'NB_spam_model.pkl')
    return cv, clf

def predict_spam(cv, clf, message):
    data = [message]
    vect = cv.transform(data).toarray()
    my_prediction = clf.predict(vect)
    return my_prediction