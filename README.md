# SpamShield AI 🛡️

> A machine learning web app that detects spam messages in real-time using NLP techniques.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online-brightgreen?style=for-the-badge)](https://spamshield-ai-m5cs.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?style=for-the-badge&logo=mongodb)](https://mongodb.com)

---

## 🌐 Live Demo

**[https://spamshield-ai-m5cs.onrender.com](https://spamshield-ai-m5cs.onrender.com)**

---

## 📌 What is SpamShield AI?

SpamShield AI is a full-stack machine learning web application that classifies SMS messages as **Spam** or **Not Spam** using Natural Language Processing. Built with Flask and scikit-learn, it provides real-time predictions through a clean, modern UI and stores every scan in MongoDB Atlas.

---

## 🚀 Features

- ✅ Real-time spam detection
- ✅ Machine learning powered (Naive Bayes + TF-IDF)
- ✅ Clean and modern responsive UI
- ✅ MongoDB Atlas integration — every scan is logged
- ✅ Cross-validation for model evaluation
- ✅ Deployed live on Render

---

## 🧠 How It Works

```
User Input → Text Cleaning → TF-IDF Vectorization → Naive Bayes → Spam / Not Spam
```

### NLP Pipeline

| Step | Description |
|---|---|
| Text Cleaning | Removes special characters, numbers, converts to lowercase |
| Stop Word Removal | Removes common words like "the", "is", "and" |
| TF-IDF Vectorization | Converts text into numerical vectors |
| Classification | Multinomial Naive Bayes predicts Spam or Ham |

---

## 📊 Model Performance

| Metric | Score |
|---|---|
| Training Accuracy | ~98% |
| Cross-Validation (5-fold) | ~97% |
| Dataset Size | 5,574 messages |

> Cross-validation confirms the model is **not overfitting** — consistent accuracy across all 5 folds with low standard deviation.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Machine Learning | scikit-learn (TF-IDF, Multinomial Naive Bayes) |
| Database | MongoDB Atlas |
| Frontend | HTML, CSS |
| Deployment | Render |

---

## ⚙️ Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/ShivjotChoudhary/spamshield-ai.git
cd spamshield-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set environment variable
export MONGO_URI="your-mongodb-atlas-uri"

# 4. Run the app
python app.py

# 5. Open in browser
http://localhost:8080
```

---

## 📁 Project Structure

```
spamshield-ai/
├── app.py              → Flask backend + ML model
├── spam.csv            → SMS Spam Collection Dataset
├── requirements.txt    → Python dependencies
├── Procfile            → Render deployment config
└── templates/
    └── index.html      → Frontend UI
```

---

## ⚡ Uptime

The app is kept alive 24/7 using a **GitHub Actions workflow** that automatically pings the Render URL every 5 minutes — preventing it from sleeping on the free tier.

```yaml
on:
  schedule:
    - cron: '*/5 * * * *'  # pings every 5 minutes
```

---

## 🗄️ Database

Every message scanned is saved to **MongoDB Atlas** with:

```json
{
  "message": "Win a free iPhone now!",
  "prediction": "spam",
  "timestamp": "2026-04-03T08:30:00"
}
```

---

## 👨‍💻 Author

**Shivjot Choudhary**

[![GitHub](https://img.shields.io/badge/GitHub-ShivjotChoudhary-black?style=flat&logo=github)](https://github.com/ShivjotChoudhary)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-shivjot007-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/shivjot007)
[![Instagram](https://img.shields.io/badge/Instagram-shivjot__2004-pink?style=flat&logo=instagram)](https://www.instagram.com/shivjot_2004)

---

⭐ **If you found this project useful, give it a star!**