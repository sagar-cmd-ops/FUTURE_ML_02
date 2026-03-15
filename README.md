# 🎫 Support Ticket Classification & Prioritization
🚀 This project was developed as part of the **Machine Learning Internship at Future Interns**.
The goal of this project is to build a **Machine Learning system that automatically classifies customer support tickets and assigns priority levels**, helping support teams respond faster and manage issues efficiently.
---

# 📌 Project Objective
Customer support teams receive **hundreds of tickets daily**.  
Manually sorting them is slow and inefficient.

This system automatically:
✅ Classifies support tickets into categories  
✅ Assigns priority levels (High / Medium / Low)  
✅ Helps businesses respond faster to urgent issues
---

# 🧠 Machine Learning Workflow
The project follows a complete NLP pipeline:
1️⃣ Ticket text preprocessing  
2️⃣ Text feature extraction using **TF-IDF**  
3️⃣ Training a **Logistic Regression classification model**  
4️⃣ Evaluating performance using ML metrics  
5️⃣ Predicting category & priority for new tickets
---

# 🛠️ Technologies Used
💻 Python  
📊 Pandas & NumPy  
🤖 Scikit-learn  
🧹 NLTK (Text preprocessing)  
📓 Jupyter Notebook / Google Colab  
---

# 📂 Dataset
Support ticket dataset containing fields like:
- Subject
- Body
- Ticket Type
- Priority
- Tags
The **subject and body were combined** to create the ticket text used for classification.
---

# 🔍 Text Preprocessing
The following NLP steps were applied:
✔ Lowercasing text  
✔ Removing punctuation  
✔ Removing stopwords  
✔ Text tokenization  
---

# ⚙️ Feature Engineering
To convert text into machine-readable format:
📌 **TF-IDF Vectorization** was used.
This technique converts ticket text into numerical features suitable for machine learning models.
---

# 🤖 Model Used
The classification model used in this project:
**Logistic Regression**
This model was trained to classify support tickets into categories such as:
- Request
- Incident
- Problem
- Change
---

# 📊 Model Performance
📈 Accuracy: **~59%**
Evaluation metrics used:
✔ Accuracy  
✔ Precision  
✔ Recall  
✔ F1 Score  

A **Confusion Matrix** was also generated to analyze classification performance.

---

# 🧪 Example Prediction

**Input Ticket**
