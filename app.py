from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb+srv://shivjot:shiv007@cluster0.mrltthq.mongodb.net/?appName=Cluster0")
db = client["spam_db"]
collection = db["predictions"]

import pandas as pd
import re
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# 🔹 Load dataset
df = pd.read_csv('spam.csv', encoding='latin-1')

# Fix columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# 🔹 Clean text
def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    return text.lower()

df['message'] = df['message'].apply(clean_text)

# 🔹 TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(df['message'])

# 🔹 Train model
model = MultinomialNB()
model.fit(X, df['label'])
#checking the accuracy:-
from sklearn.metrics import accuracy_score
y_pred = model.predict(X)
accuracy = accuracy_score(df['label'], y_pred)

print("Model Accuracy:", accuracy)

#Cross-Validation:-
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, df['label'], cv=5)
print("Cross-val accuracy:", scores.mean())


# 🔹 Home page
@app.route('/')
def home():
    return render_template('index.html')


# 🔹 Prediction
@app.route('/predict', methods=['POST'])
def predict():
    user_message = request.form['message']

    cleaned = clean_text(user_message)
    vector = tfidf.transform([cleaned])

    prediction = model.predict(vector)[0]
    collection.insert_one({
    "message": user_message,
    "prediction": prediction,
    "timestamp": datetime.now()
})

    if prediction.lower() == 'spam':
        result = "Spam"
    else:
        result = "Not Spam"

    return render_template('index.html', prediction=result, user_input=user_message)


# 🔹 Run app
import os
client = MongoClient(os.getenv("MONGO_URI"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))