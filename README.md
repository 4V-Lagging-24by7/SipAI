# 💧 SipAI — AI Hydration Assistant

SipAI is an **AI-powered hydration tracking app** that helps users log their daily water intake and receive **smart hydration feedback** using a **Large Language Model (LLM)**.

The project demonstrates how to integrate an AI model into a simple, real-world application using **Streamlit**, **FastAPI**, and **SQLite**.

---

## 🚀 Features

- Log daily water intake (ml)
- AI-generated hydration feedback
- Interactive Streamlit dashboard
- Water intake history with charts
- Local data persistence using SQLite
- Secure API key handling

---

## 🧱 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **AI:** Groq (LangChain)  
- **Database:** SQLite  
- **Language:** Python  

---

## 📁 Project Structure
SipAI/
├── src/
│ ├── agent.py
│ ├── api.py
│ ├── dashboard.py
│ ├── database.py
│ ├── logger.py
│ └── assets/
│ └── pfp.jpg
├── requirements.txt
├── README.md
├── .gitignore

## 🖼️ Screenshots

Screenshots can be added in the `screenshots/` folder.

- Welcome Screen
- Dashboard View
- AI Feedback
- Water Intake History

## ⚙️ Setup (Local)

### Clone the repository

git clone https://github.com/4V-Lagging-24by7/SipAI.git  
cd SipAI

### Install dependencies

pip install -r requirements.txt

### Create .env file

GROQ_API_KEY=your_groq_api_key

### Run the app

streamlit run src/dashboard.py

## 🧠 How It Works

- User logs water intake
- Data is saved in SQLite
- Intake is sent to the AI agent
- LLM returns hydration feedback
- History is visualized in the dashboard

## ☁️ Deployment

- Deployable on Streamlit Community Cloud
- API keys must be added via Secrets
- SQLite works locally; cloud storage may reset on restart

## 📌 Future Improvements

- User accounts
- Cloud database
- Personalized hydration goals
- Notifications and reminders


