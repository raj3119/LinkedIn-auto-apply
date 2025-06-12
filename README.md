# 🔗 LinkedIn Auto Apply Bot

This is a Python automation bot that logs into LinkedIn and auto-applies to jobs using Selenium.

---

## 🔧 Features
- Auto login using environment variables
- Search for jobs
- Auto fill and submit simple applications
- Skips multi-step forms
- Handles Save/Discard popups

---

## 📁 File Structure

```bash
├── main.py           # Main bot script
├── .env.example      # Example environment config (no secrets!)
├── .gitignore
└── README.md

---

## 🚀 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/raj3119/Linkedin-auto-apply.git
cd Linkedin-auto-apply

⚠️Limitations
This automation bot:
•Works on simple one click applications on LinkedIn.

•Skips or fails on multi-step applications that required:
   ◦Resume Re-uploads
   ◦Application review before submission
You ca manuualy complete these skipped applications
or contribute improvements to handle such.   