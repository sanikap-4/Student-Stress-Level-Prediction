# Student Stress Level Prediction Using Machine Learning

## 📌 Project Overview

Student Stress Level Prediction is a Machine Learning project that predicts students' stress levels based on social media usage and lifestyle factors.

The system classifies student stress into four categories:
- Low
- Medium
- High
- Very High

The project aims to create awareness about the relationship between students' lifestyle habits, social media usage, and stress levels.

## 🎯 Objectives

- Analyze student lifestyle and social media usage.
- Perform Exploratory Data Analysis (EDA).
- Build and compare Machine Learning classification models.
- Predict student stress categories.
- Develop an interactive web application using Streamlit.

## 📊 Dataset Information

- Total Records: 5,000
- Total Original Features: 13
- Target Variable: Stress_Level

### Input Features
- Age
- Gender
- Country
- Academic Level
- Most Used Platform
- Purpose of Use
- Average Daily Usage Hours
- Daily Unlocks
- Study Hours
- Physical Activity Hours
- Sleep Hours Per Night

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest
- Streamlit
- Plotly
- Joblib

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Feature Encoding and Scaling
6. Train-Test Split (80:20)
7. Model Training
8. Model Evaluation
9. Model Saving
10. Streamlit Application Development

## 🤖 Models Used

Three classification algorithms were compared:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

### Model Performance

| Algorithm | Accuracy |
|---|---:|
| Logistic Regression | 74.30% |
| Decision Tree | 82.10% |
| Random Forest | 91.00% |

**Best Performing Model:** Random Forest Classifier

## 📈 Model Evaluation

The final model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## 🌐 Web Application

An interactive Streamlit application allows users to enter student lifestyle information and receive:

- Predicted stress category
- Model confidence percentage
- General lifestyle recommendations

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Student-Stress-Level-Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
Student-Stress-Level-Prediction/
│
├── app.py
├── student_stress_model.joblib
├── requirements.txt
├── README.md
├── Untitled.ipynb
└── .gitignore
```

## 🔮 Future Scope

- Explore additional Machine Learning algorithms.
- Improve model performance using further experimentation.
- Add more student-related lifestyle features.
- Improve the user interface and recommendations.

## ⚠️ Disclaimer

This project is developed for educational and research purposes only. It is not a medical diagnosis or mental health assessment system.

## 👩‍💻 Author

**Sanika R. Patil**

Computer Engineering Student
