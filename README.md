# 🤖 LinkedIn Auto Apply Bot

This is a Python automation bot that auto-applies to LinkedIn jobs using Selenium WebDriver.  
It handles job searches, fills out simple applications (like phone and city), and skips complex multi-step forms — saving time for job seekers.

---

## 📌 Features

- 🔐 Automates LinkedIn login securely using environment variables
- 🔎 Searches for jobs using custom keywords
- 🖱️ Clicks “Easy Apply” buttons
- 📄 Fills in simple job forms (phone, city)
- ❌ Skips or discards complex or multi-step job applications
- 🔁 Loops through up to 5 jobs per session (customizable)

---

## 🛠️ Tech Stack

- 🐍 Python
- 🌐 Selenium WebDriver
- 📦 dotenv for credential management
- 🧪 WebDriverWait & Expected Conditions for stable interaction

---

## 📁 Project Structure

LinkedIn-auto-apply/ ├── bot.py              # Main bot script ├── .env.example        # Example env file (no private data) ├── .gitignore          # Prevents pushing secrets or cache ├── requirements.txt    # List of required Python packages └── README.md           # This file

---

## 🚀 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/raj3119/LinkedIn-auto-apply.git
cd LinkedIn-auto-apply

2. Create your .env file

Rename .env.example to .env and add your details:

Linkedin_Username=youremail@example.com
Linkedin_Password=yourpassword
Job=Python Developer
Phone=9876543210
City=Delhi

> ⚠️ Do not share your .env file publicly.




---

3. Install required libraries

Make sure you’re using Python 3.x.

pip install -r requirements.txt


---

4. Run the bot

python bot.py

The browser will open, log in to LinkedIn, search for your job, and apply to the first 5 “Easy Apply” jobs it can find.


---

🚧 Limitations

❌ Doesn’t handle complex or multi-step applications

⏱️ Set to apply to 5 jobs per run (you can change the limit in code)

🧪 May break if LinkedIn UI changes — check for updates regularly

💻 Requires your system to have ChromeDriver installed and added to PATH



---

📌 Topics

python selenium linkedin-automation job-bot job-apply linkedin-bot web-automation selenium-webdriver


---

✍️ Author

Made with  by Raj Kisley