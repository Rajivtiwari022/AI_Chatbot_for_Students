# 🎓 AI Student Support Chatbot

An AI-powered Student Support Chatbot built using **Python, TensorFlow, NLP, and Streamlit**.  
The chatbot helps students get instant answers related to college services such as admissions, fees, scholarships, examinations, hostel facilities, placements, and other academic queries.

The system uses **Natural Language Processing (NLP)** and an **Intent Classification Neural Network** to understand student queries and provide relevant responses.

---

# 🚀 Features

✨ **AI-Based Conversation**
- Understands natural language student queries
- Predicts user intent using a trained neural network

🎓 **Student Support Categories**
- Admissions
- Fee Information
- Scholarships
- Hostel Services
- Examination Queries
- Library Services
- Placements
- Academic Support
- General Information

🖥️ **Interactive Web Dashboard**
- Built using Streamlit
- Modern chat interface
- Real-time responses
- Easy-to-use UI

🧠 **Machine Learning Pipeline**
- Text preprocessing
- Feature extraction using CountVectorizer
- Intent classification using TensorFlow/Keras
- Response generation from knowledge base

---
## 🚀 Key Highlights

* **Efficient Intent Mapping:** Leverages a trained neural network to minimize response errors.
* **Responsive Interface:** The streamlit-powered dashboard is optimized for both desktop and mobile web browsers.
* **Scalable Knowledge Base:** Easily expand the system's capabilities by updating the intents.json

# 🏗️ System Architecture

```
             Student Query
                  |
                  ▼
          Streamlit Dashboard
                  |
                  ▼
             chatbot.py
                  |
                  ▼
        Text Feature Extraction
          (Vectorizer.pkl)
                  |
                  ▼
        Neural Network Model
       (chatbot_model.keras)
                  |
                  ▼
        Intent Prediction
                  |
                  ▼
          Response Generation
          (intents.json)
                  |
                  ▼
              AI Response
```

---

# 📂 Project Structure

```
AIChatbot/

│
├── app.py
│   └── Streamlit application interface
│
├── chatbot.py
│   └── Chatbot inference and response generation
│
├── train.py
│   └── Model training pipeline
│
├── model.py
│   └── Neural network architecture
│
├── utils.py
│   └── Helper functions
│
├── data/
│   └── intents.json
│       └── Training dataset
│
├── models/
│   ├── chatbot_model.keras
│   │   └── Trained neural network
│   │
│   ├── vectorizer.pkl
│   │   └── Text feature extractor
│   │
│   └── label_encoder.pkl
│       └── Intent label encoder
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Machine Learning | TensorFlow / Keras |
| Natural Language Processing | Scikit-learn |
| Text Processing | CountVectorizer |
| Dataset Format | JSON |
| Model Format | Keras (.keras) |

---

# 🧠 How It Works

## 1. Dataset

The chatbot learns from:

```
data/intents.json
```

Each training example contains:

- Category (Intent)
- User input
- Expected response


Example:

```json
{
  "category": "Hostel",
  "input": "How can I apply for hostel?",
  "output": "You can apply through the hostel portal."
}
```

---

## 2. Model Training

Run:

```bash
python train.py
```

The training process:

```
intents.json

      ↓

Text Vectorization

      ↓

Intent Encoding

      ↓

Neural Network Training

      ↓

Saved Model Files
```

Generated files:

```
models/

├── chatbot_model.keras
├── vectorizer.pkl
└── label_encoder.pkl
```

---

# ▶️ Installation & Setup

## 1. Clone Repository

```bash
git clone <repository-url>

cd AIChatbot
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Train the Chatbot

Before running the application, train the model:

```bash
python train.py
```

After successful training, model files will be created inside:

```
models/
```

---

## 4. Run Streamlit Application

Start the chatbot:

```bash
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

# 📸 Application Preview

```
+--------------------------------+

       🎓 Student Support AI

  Ask your college-related query

----------------------------------

Student:
How can I apply for scholarship?

AI:
Scholarship applications are
available through the student portal.

----------------------------------

        Type your message...

+--------------------------------+
```

---

# 🔮 Future Enhancements

- 🔊 Voice-based interaction
- 🌐 Multi-language support
- 📚 PDF-based knowledge extraction
- 🔍 RAG-based intelligent answering
- 👨‍🎓 Student authentication
- 📊 Admin analytics dashboard
- 💬 WhatsApp/Telegram integration
- 🗂️ Database integration for student services

---
## 🧑‍💻 Developed By
* **Name:** Rajiv Kumar Tiwari
* **Course:** B.Tech (Computer Science & Engineering)

# 👨‍💻 Development Workflow

```
Modify intents.json

        ↓

Run train.py

        ↓

Generate model files

        ↓

Run Streamlit App

        ↓

Interact with AI Chatbot
```

---

# 🤝 Contribution

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a new branch
3. Make improvements
4. Submit a pull request

---

# 📜 License

This project is created for educational and research purposes.

---

# ⭐ Acknowledgement

Built using:

- Python
- TensorFlow
- Streamlit
- Scikit-learn
- Natural Language Processing techniques
