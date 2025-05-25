# 💰 Expense Tracking System

A full-stack Python application to **track daily expenses**, view **category-wise and monthly analytics**, and manage financial data with ease. Built using **FastAPI** for the backend and **Streamlit** for the frontend.

---

## 🚀 Features

- ✅ Add and update daily expenses
- 📅 Fetch expenses by date
- 📊 Visualize expense analytics:
  - By **category** (with percentage breakdown)
  - By **month** (monthly summaries)
- 🔁 Clean and modular codebase using Python classes and API routing
- ⚡ Fast and interactive user interface using Streamlit tabs

---

## 🛠 Tech Stack

| Layer      | Tech Used              |
|------------|------------------------|
| Backend    | FastAPI, Pydantic      |
| Frontend   | Streamlit              |
| Database   | Custom SQL via `db_connector` |
| Others     | Python standard libs (`datetime`, `typing`) |

---

## 📂 Project Structure

```bash
.
├── main.py                 # FastAPI backend logic
├── ui_app.py              # Streamlit UI app
├── db_connector.py        # Database connection and query logic
├── add_update_ui.py       # Streamlit tab: Add/Update Expenses
├── analytics_ui.py        # Streamlit tabs: Category & Monthly Analytics
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
