import os
import re
import pandas as pd
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection (use env variable)
client = MongoClient(os.getenv("MONGO_URI"))
db = client["spam_db"]
collection = db["predictions"]

# Load dataset
df = pd.read_csv('spam.csv', encoding='latin-1')
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Clean text
def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    return text.lower()

df['message'] = df['message'].apply(clean_text)

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(df['message'])

# Train model
model = MultinomialNB()
model.fit(X, df['label'])

# Accuracy
y_pred = model.predict(X)
print("Model Accuracy:", accuracy_score(df['label'], y_pred))

# Cross-validation
scores = cross_val_score(model, X, df['label'], cv=5)
print("Cross-val accuracy:", scores.mean())


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    user_message = request.form['message']

    cleaned = clean_text(user_message)
    vector = tfidf.transform([cleaned])
    prediction = model.predict(vector)[0]

    # Save to MongoDB
    collection.insert_one({
        "message": user_message,
        "prediction": prediction,
        "timestamp": datetime.now()
    })

    result = "Spam" if prediction.lower() == 'spam' else "Not Spam"
    return render_template('index.html', prediction=result, user_input=user_message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)