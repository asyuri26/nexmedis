# FastAPI JSON Manager 

A simple backend system using **FastAPI** to send, receive, and display JSON data with a basic HTML frontend.

---

## Features

- 📄 View stored JSON data
- 📬 Submit new JSON data via form
- 🛑 Prevent duplicate IDs
- ✏️ Edit existing data by ID
- ✅ Input validation with Pydantic

---

## Project Structure

```
fastapi-json-project/
├── main.py              # FastAPI app
├── models.py            # Pydantic model
├── templates/index.html 
├── static/style.css    
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Jinja2

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Run Locally

```bash
uvicorn main:app --reload
```
---
## How to Use the Web App

1. **Open the page** at `http://127.0.0.1:8000/`
2. **View stored items** in the list displayed on the page
3. **Add new data** using the form (ID must be unique)
   - Fill in `ID`, `Name`, and `Description`
   - Click **Send**
   - If ID already exists, an alert will show
4. **Edit existing data**
   - Click **Edit** next to an item in the list
   - The form will autofill with the selected item's data
   - Click **Update** to submit changes
5. Page will automatically reload to show updates
---

## API Endpoints (testing using swaggy)

| Method | Endpoint        | Description                        |
|--------|------------------|------------------------------------|
| GET    | `/`              | UI showing stored items            |
| GET    | `/send-json`     | Sample JSON from backend           |
| POST   | `/receive-json`  | Submit new JSON data               |
| POST   | `/modify-json`   | Modify existing JSON by ID         |

---

## 📌 Notes

- All data is stored in `data.json`
- `id` field must be unique
- If you submit a duplicate ID, you’ll get an alert

---

## Author

Created by Asyarie — Biomedical Engineer & Python Developer