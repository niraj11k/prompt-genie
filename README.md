# Prompt Genie 🧞‍♂️

A simple Python web app that takes a task in plain English and returns an optimized prompt using Free access to models like mistralai/Mistral-7B-Instruct-v0.1

---

## 🔧 How It Works

- You enter a task like:  
  _"Write a summary of this blog post for LinkedIn"_
- The app calls OpenAI GPT API behind the scenes
- It returns a refined and optimized prompt

---

## 📦 Project Structure
prompt-genie/
├── app/
│   ├── static/
│   │   └── style.css       👈 final Tailwind output
│   ├── templates/
│   │   └── index.html      👈 uses Tailwind classes
│   ├── main.py             👈 FastAPI backend
│   ├── prompt_creator.py
├── requirements.txt
└── README.md


---

## 🚀 Running the App

1. Clone the repo  
   `git clone <your-repo-url>`

2. Create a virtual environment  
   `python -m venv venv && source venv/bin/activate` (Linux/Mac)  
   `venv\Scripts\activate` (Windows)

3. Install dependencies  
   `pip install -r requirements.txt`

4. Add your API key  
   Create a `.env` file and add:  
   `TOGETHER_API_KEY=your_key_here`

5. Run the app  
   `uvicorn app.main:app --reload`

6. Open your browser and go to  
   `http://127.0.0.1:8000`

---

## 📘 Tips for Beginners

- `FastAPI` is used to build the web server (API)
- Use `Together.ai` as support OpenAI-style APIs
-  Get Together API key
   . Go to `https://together.ai`
   . Sign up → Go to API keys → Copy your free key
- `index.html` is served directly by FastAPI
- The frontend JavaScript calls your `/generate` API
- GPT response is shown right in the browser

---

## ❓ Need Help?
Message your mentor or read the FastAPI and OpenAI documentation to understand each part.
