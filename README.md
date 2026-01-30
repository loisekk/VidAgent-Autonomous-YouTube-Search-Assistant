🎯 VidAgent – Autonomous YouTube Search Assistant
<p align="center"> An intelligent CLI-based automation agent that searches, plays, and navigates YouTube content autonomously </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/Selenium-WebAutomation-green?style=for-the-badge&logo=selenium" /> <img src="https://img.shields.io/badge/CLI-InquirerPy-orange?style=for-the-badge" /> <img src="https://img.shields.io/badge/Agent-Autonomous-red?style=for-the-badge" /> <img src="https://img.shields.io/badge/Author-Yash%20Brahmankar-success?style=for-the-badge" /> </p>
🔥 Tagline

“An autonomous agent that finds and plays YouTube content—so you don’t have to.” 🤖▶️

📝 Project Description

VidAgent is a Python-based autonomous YouTube automation agent that allows users to search and play content on YouTube using interactive CLI menus.

Instead of typing search queries manually, users simply select a category, topic, and context, and VidAgent intelligently constructs and executes the search—then automatically plays the most relevant video.

This project demonstrates:

Intelligent automation workflows

Agent-like decision making

Real-world usage of Selenium + CLI UX

Clean and modular Python architecture

Perfect for automation portfolios, AI agent demos, and advanced Python projects.

🚀 Key Features

🎯 Category-based intelligent search
🧠 Autonomous query generation
🤖 Automated YouTube navigation
⌨️ Interactive CLI using InquirerPy
⚡ Real-time browser automation with Selenium

🔍 Cleaned & optimized search queries

🧩 Modular and extensible architecture

🧠 Supported Content Categories

🏎️ F1 (Year, Grand Prix, Stage)

🍥 Anime (Intro, Clips, Trailer, Movies)

🎬 Movies

📺 Web Series

🎮 Gaming Videos

🎨 Animations

🐭 Cartoons

📘 Study & Tech Content

Each category dynamically builds a smart YouTube search query.

⚙️ How It Works (High Level)

User selects a category via CLI

VidAgent asks contextual questions

Query is cleaned and optimized

Selenium opens YouTube automatically

First relevant video is selected and played

Agent continues navigation autonomously

🧰 Tech Stack

Python 3.x

Selenium WebDriver

InquirerPy (CLI UX)

dotenv (Environment handling)

Regex (Query cleaning)

ChromeDriver

📂 Project Structure (Conceptual)
VidAgent/
│
├── agent.py
├── flows/
│   ├── anime_flow.py
│   ├── f1_flow.py
│   ├── gaming_flow.py
│   └── study_flow.py
│
├── utils/
│   └── query_cleaner.py
│
└── .env


┌──────────────┐
│   User CLI   │
│ (InquirerPy) │
└──────┬───────┘
       │
       ▼
┌─────────────────────┐
│ Category Selection  │
│  (F1 / Anime / etc) │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Contextual Flow     │
│ (Year, Stage, Type)│
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Query Cleaner       │
│ (Regex Optimization)│
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Selenium Agent      │
│ - Open YouTube      │
│ - Search Video      │
│ - Auto Play         │
└─────────────────────┘


🎯 Use Cases

Automation demos

AI / Agentic systems learning

Python + Selenium practice

CLI UX design

YouTube research automation

Portfolio showcase project

👨‍💻 Author

Yash Brahmankar
Python Developer | Automation | AI & Agentic Systems

🔖 Hashtags
#VidAgent #PythonAutomation #YouTubeAutomation #Selenium
#AgenticAI #AutonomousAgent #CLIApplications #AIProjects
#DeveloperTools #OpenSource #BuildInPublic #PythonDeveloper
