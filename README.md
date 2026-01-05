# 🛡️ Insider Threat Detection System with AI Chatbot

An advanced, end-to-end security analytics platform that utilizes **Machine Learning** to identify high-risk behavioral patterns within an organization. This project compares two high-performance models (**Random Forest** and **XGBoost**) and features an interactive **Streamlit Dashboard** with an integrated **AI Security Assistant**.

---

## 🌟 Key Features
* **Dual-Model Intelligence**: Compares Random Forest and XGBoost for maximum detection accuracy.
* **Behavioral Analytics**: Processes 10,000+ logs including login times, sensitive file access, and USB usage.
* **Interactive Dashboard**: Real-time risk scoring and visual data distribution using Plotly.
* **AI Chatbot**: A built-in security assistant to explain risk factors and security metrics.
* **Scientific Evaluation**: Detailed performance reports including Precision, Recall, and Confusion Matrices.

---

## 📂 Project Structure
```text
Insider_Threat_Detection/
├── data/
│   ├── raw/                # Original dataset (CSV)
│   └── processed/          # Cleaned data for AI training
├── models/                 # Saved .pkl models (RF & XGBoost)
├── src/                    # Python Source Code
│   ├── preprocess.py       # Data cleaning & encoding
│   ├── train_model.py      # Dual-model training logic
│   └── evaluate.py         # Performance comparison script
├── dashboard/
│   └── app.py              # Streamlit Web App & Chatbot
├── requirements.txt        # Project dependencies
└── README.md               # Documentation
ofessional! Do you need help with the "LICENSE" file or the "requirements.txt" to finish the repo?**

🚀 Step-by-Step Setup
1. Clone the Repository

      git clone [https://github.com/YOUR_USERNAME/Insider_Threat_Detection.git]
      (https://github.com/YOUR_USERNAME/Insider_Threat_Detection.git)
      cd Insider_Threat_Detection

2. Create a Virtual Environment (Recommended)

      python -m venv venv

# Activate on Windows:

      venv\Scripts\activate

# Activate on Mac/Linux:

      source venv/bin/activate

3. Install Dependencies

      pip install -r requirements.txt

🛠️ Execution Pipeline
Follow these steps in order to initialize the system:

Step 1: Preprocessing
Clean the raw data and prepare it for the AI models.

      python src/preprocess.py

Step 2: Training
Train both the Random Forest and XGBoost models simultaneously.

      python src/train_model.py

Step 3: Evaluation
Compare the accuracy and recall of both models to see which performs better.

      python src/evaluate.py

Step 4: Launch the Dashboard
Run the interactive web interface and start detecting threats!

      streamlit run dashboard/app.py

📊 How It Works

Data Input: The system takes features like login_hour, usb_insertions, and sensitive_files_accessed.

AI Analysis: The selected model (RF or XGB) calculates a probability score.

Risk Flagging: If the probability exceeds a threshold, a 🚨 HIGH RISK alert is triggered.

Assistance: Users can interact with the Security Chatbot to understand the specific dangers of the flagged activities.

