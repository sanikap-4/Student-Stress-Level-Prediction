# ============================================================
# STUDENT STRESS LEVEL PREDICTION
# Machine Learning Streamlit Application
# ============================================================

import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Stress Predictor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 2. LOAD TRAINED MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("student_stress_model.joblib")


model = load_model()


# ============================================================
# 3. APPLICATION TITLE
# ============================================================

st.title("🧠 Student Stress Level Predictor")

st.markdown(
    "Predict student stress level using social media and lifestyle factors."
)

st.info(
    "ℹ️ This application is developed for educational and research purposes. "
    "It does not provide a medical diagnosis."
)


# ============================================================
# 4. SIDEBAR
# ============================================================

with st.sidebar:

    st.header("📌 About the Project")

    st.write(
        """
        This Machine Learning project predicts a student's
        stress category using social media behavior and
        lifestyle factors.
        """
    )

    st.divider()

    st.subheader("🤖 Machine Learning Model")

    st.write("Random Forest Classifier")

    st.subheader("🎯 Prediction Levels")

    st.write("🟢 Low Stress")
    st.write("🟡 Medium Stress")
    st.write("🟠 High Stress")
    st.write("🔴 Very High Stress")

    st.divider()

    st.metric(
        label="Model Accuracy",
        value="91.00%"
    )

    st.caption(
        "Accuracy obtained on the held-out test dataset."
    )


# ============================================================
# 5. STUDENT INFORMATION
# ============================================================

st.header("👤 Student Information")

col1, col2, col3, col4 = st.columns(4)


with col1:

    age = st.number_input(
        "Age",
        min_value=15,
        max_value=40,
        value=21,
        step=1
    )


with col2:

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )


with col3:

    country = st.selectbox(
        "Country",
        [
            "Other",
            "India",
            "Canada",
            "USA",
            "Australia",
            "UK",
            "Germany",
            "Bangladesh",
            "Brazil",
            "Japan",
            "Pakistan",
            "Nepal",
            "Sri Lanka"
        ]
    )


with col4:

    academic_level = st.selectbox(
        "Academic Level",
        [
            "High School",
            "Undergraduate",
            "Graduate"
        ]
    )


# ============================================================
# 6. SOCIAL MEDIA INFORMATION
# ============================================================

st.header("📱 Social Media Usage")

col1, col2, col3, col4 = st.columns(4)


with col1:

    platform = st.selectbox(
        "Most Used Platform",
        [
            "Facebook",
            "LinkedIn",
            "Instagram",
            "Snapchat",
            "Twitter",
            "YouTube",
            "TikTok",
            "LINE",
            "KakaoTalk",
            "VKontakte",
            "WhatsApp",
            "WeChat"
        ]
    )


with col2:

    purpose = st.selectbox(
        "Purpose of Use",
        [
            "Networking",
            "Education",
            "Entertainment",
            "News"
        ]
    )


with col3:

    avg_daily_usage_hours = st.number_input(
        "Daily Social Media Usage (Hours)",
        min_value=0.0,
        max_value=24.0,
        value=4.0,
        step=0.1
    )


with col4:

    daily_unlocks = st.number_input(
        "Daily Phone Unlocks",
        min_value=0,
        max_value=1000,
        value=134,
        step=1
    )


# ============================================================
# 7. LIFESTYLE INFORMATION
# ============================================================

st.header("📚 Lifestyle Information")

col1, col2, col3 = st.columns(3)


with col1:

    study_hours = st.number_input(
        "Study Hours Per Day",
        min_value=0.0,
        max_value=24.0,
        value=4.5,
        step=0.1
    )


with col2:

    physical_activity_hours = st.number_input(
        "Physical Activity Hours Per Day",
        min_value=0.0,
        max_value=24.0,
        value=2.2,
        step=0.1
    )


with col3:

    sleep_hours_per_night = st.number_input(
        "Sleep Hours Per Night",
        min_value=0.0,
        max_value=24.0,
        value=6.7,
        step=0.1
    )


# ============================================================
# 8. PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🔮 PREDICT MY STRESS LEVEL",
    type="primary",
    use_container_width=True
)


# ============================================================
# 9. PREDICTION PROCESS
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # Create input DataFrame
    # --------------------------------------------------------

    student_data = pd.DataFrame({

        "Age": [age],

        "Gender": [gender],

        "Country": [country],

        "Academic_Level": [academic_level],

        "Most_Used_Platform": [platform],

        "Purpose_Of_Use": [purpose],

        "Avg_Daily_Usage_Hours": [
            avg_daily_usage_hours
        ],

        "Daily_Unlocks": [
            daily_unlocks
        ],

        "Study_Hours": [
            study_hours
        ],

        "Physical_Activity_Hours": [
            physical_activity_hours
        ],

        "Sleep_Hours_Per_Night": [
            sleep_hours_per_night
        ]
    })


    # --------------------------------------------------------
    # Model prediction
    # --------------------------------------------------------

    prediction = model.predict(
        student_data
    )[0]


    # --------------------------------------------------------
    # Model probabilities
    # --------------------------------------------------------

    probabilities = model.predict_proba(
        student_data
    )[0]

    classes = model.classes_

    probability_dict = dict(
        zip(
            classes,
            probabilities
        )
    )


    # --------------------------------------------------------
    # Confidence of predicted class
    # --------------------------------------------------------

    confidence = (
        probability_dict[prediction] * 100
    )


    # ========================================================
    # 10. RESULT SETTINGS
    # ========================================================

    if prediction == "Low":

        gauge_color = "#22c55e"
        icon = "🟢"
        result_text = "LOW STRESS"
        explanation = (
            "The model predicts a Low stress level based on "
            "the provided information."
        )

    elif prediction == "Medium":

        gauge_color = "#eab308"
        icon = "🟡"
        result_text = "MEDIUM STRESS"
        explanation = (
            "The model predicts a Medium stress level based on "
            "the provided information."
        )

    elif prediction == "High":

        gauge_color = "#f97316"
        icon = "🟠"
        result_text = "HIGH STRESS"
        explanation = (
            "The model predicts a High stress level based on "
            "the provided information."
        )

    else:

        gauge_color = "#ef4444"
        icon = "🔴"
        result_text = "VERY HIGH STRESS"
        explanation = (
            "The model predicts a Very High stress level based on "
            "the provided information."
        )


    # ========================================================
    # 11. PREDICTION RESULT
    # ========================================================

    st.divider()

    st.header("🎯 Prediction Result")

    # --------------------------------------------------------
    # Create circular gauge
    # --------------------------------------------------------

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=confidence,

            number={
                "suffix": "%",
                "font": {
                    "size": 42
                }
            },

            title={
                "text": "Model Confidence",
                "font": {
                    "size": 18
                }
            },

            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1,
                    "tickcolor": "#64748b"
                },

                "bar": {
                    "color": gauge_color,
                    "thickness": 0.25
                },

                "bgcolor": "#f8fafc",

                "borderwidth": 2,

                "bordercolor": "#e2e8f0",

                "steps": [
                    {
                        "range": [0, 100],
                        "color": "#f1f5f9"
                    }
                ],

                "threshold": {
                    "line": {
                        "color": gauge_color,
                        "width": 5
                    },

                    "thickness": 0.75,

                    "value": confidence
                }
            }
        )
    )


    gauge.update_layout(
        height=330,
        margin={
            "l": 40,
            "r": 40,
            "t": 60,
            "b": 20
        },

        paper_bgcolor="rgba(0,0,0,0)",

        font={
            "family": "Arial"
        }
    )


    # --------------------------------------------------------
    # Result layout
    # --------------------------------------------------------

    result_col1, result_col2 = st.columns(
        [1, 1.4]
    )


    # --------------------------------------------------------
    # Circular gauge
    # --------------------------------------------------------

    with result_col1:

        st.plotly_chart(
            gauge,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )


    # --------------------------------------------------------
    # Prediction information
    # --------------------------------------------------------

    with result_col2:

        st.subheader(
            f"{icon} Predicted Stress Level"
        )

        # Large native metric
        st.metric(
            label="Prediction",
            value=result_text
        )

        st.metric(
            label="Confidence",
            value=f"{confidence:.2f}%"
        )

        st.info(
            explanation
        )


    # ========================================================
    # 12. PERSONALIZED SUGGESTIONS
    # ========================================================

    st.divider()

    st.header("💡 Personalized Suggestions")


    recommendations = []


    # --------------------------------------------------------
    # Stress-based recommendations
    # --------------------------------------------------------

    if prediction == "Low":

        recommendations.append(
            "Maintain your current healthy routine and consistent sleep schedule."
        )

        recommendations.append(
            "Continue balancing study, social media, physical activity, "
            "and personal time."
        )


    elif prediction == "Medium":

        recommendations.append(
            "Try to maintain a consistent daily routine with planned "
            "study and rest periods."
        )

        recommendations.append(
            "Consider taking regular breaks during long study sessions."
        )


    elif prediction == "High":

        recommendations.append(
            "Consider creating a structured daily routine with dedicated "
            "study and rest periods."
        )

        recommendations.append(
            "Try reducing unnecessary social media use and frequent "
            "phone checking."
        )

        recommendations.append(
            "Include regular physical activity and adequate sleep "
            "in your daily routine."
        )


    else:

        recommendations.append(
            "Prioritize a consistent sleep and daily routine."
        )

        recommendations.append(
            "Consider reducing unnecessary social media usage and "
            "frequent phone checking."
        )

        recommendations.append(
            "Break large academic tasks into smaller manageable tasks "
            "with regular breaks."
        )

        recommendations.append(
            "If stress feels persistent or overwhelming, consider "
            "talking to a trusted person, college counselor, "
            "or qualified professional."
        )


    # --------------------------------------------------------
    # Lifestyle-based recommendations
    # --------------------------------------------------------

    if sleep_hours_per_night < 6:

        recommendations.append(
            "Your reported sleep duration is relatively low. "
            "Consider working toward a more consistent sleep routine."
        )


    if avg_daily_usage_hours > 6:

        recommendations.append(
            "Your reported social media usage is relatively high. "
            "Consider setting specific screen-free periods."
        )


    if daily_unlocks > 200:

        recommendations.append(
            "Your phone unlock frequency is high. "
            "Consider turning off non-essential notifications."
        )


    if study_hours < 2:

        recommendations.append(
            "Consider using short, focused study sessions "
            "with planned breaks."
        )


    if physical_activity_hours < 1.5:

        recommendations.append(
            "Consider adding some regular physical activity "
            "to your daily routine."
        )


    # --------------------------------------------------------
    # Display recommendations
    # --------------------------------------------------------

    for i, recommendation in enumerate(
        recommendations,
        1
    ):

        st.write(
            f"**💡 Suggestion {i}:** {recommendation}"
        )


    # ========================================================
    # 13. INPUT SUMMARY
    # ========================================================

    st.divider()

    st.header("📋 Input Summary")

    summary_col1, summary_col2 = st.columns(2)


    with summary_col1:

        st.write(
            f"**Age:** {age}"
        )

        st.write(
            f"**Gender:** {gender}"
        )

        st.write(
            f"**Country:** {country}"
        )

        st.write(
            f"**Academic Level:** {academic_level}"
        )

        st.write(
            f"**Most Used Platform:** {platform}"
        )


    with summary_col2:

        st.write(
            f"**Purpose:** {purpose}"
        )

        st.write(
            f"**Daily Social Media Usage:** "
            f"{avg_daily_usage_hours:.1f} hours"
        )

        st.write(
            f"**Daily Phone Unlocks:** "
            f"{daily_unlocks}"
        )

        st.write(
            f"**Study Hours:** "
            f"{study_hours:.1f} hours"
        )

        st.write(
            f"**Physical Activity:** "
            f"{physical_activity_hours:.1f} hours"
        )

        st.write(
            f"**Sleep:** "
            f"{sleep_hours_per_night:.1f} hours"
        )


    # ========================================================
    # 14. DISCLAIMER
    # ========================================================

    st.divider()

    st.warning(
        "⚠️ Important: This prediction is based on patterns learned "
        "from the project dataset. It is not a medical diagnosis or "
        "professional mental health assessment."
    )


# ============================================================
# 15. FOOTER
# ============================================================

st.divider()

st.caption(
    "Student Stress Level Prediction Using Machine Learning | "
    "Random Forest Classifier | Educational & Research Project"
)