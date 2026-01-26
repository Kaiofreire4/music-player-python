# 🎵 Music Player in Python (CLI)

A command-line music player developed in **Python**, designed to demonstrate practical programming skills such as file handling, concurrency, user interaction via terminal, and code organization.

This project focuses on **real-world problem solving**, clean control flow, and safe execution without blocking user input.

---

## 🚀 Key Features

- 📂 Automatically loads audio files from a directory
- 🎧 Plays `.mp3` files using the `pygame` library
- 📋 Interactive and user-friendly CLI menu
- ⏹️ Allows stopping playback at any time via user input
- 🔁 Handles playback lifecycle (start, stop, finish) gracefully
- 📦 Ready for distribution as an executable (PyInstaller-compatible)

---

## 🛠 Technologies & Concepts

- **Python 3**
- **Pygame** (audio handling)
- **Threading & concurrency**
- **File system manipulation**
- **Event-based control flow**
- **Error handling and input validation**
- **Git & GitHub (version control)**

---

## 📁 Project Structure

music-player-python/
│
├── main.py # Application logic
├── README.md # Project documentation
├── requirements.txt # Dependencies
└── musicas/ # Audio files directory

---

## ▶️ How to Run

git clone https://github.com/kaiofreire4/music-player-python.git
cd music-player-python
pip install -r requirements.txt
python main.py

Add .mp3 files to the musicas/ directory before running the program.

🧠 Technical Highlights (for Recruiters)

Implemented non-blocking user input using Python threads to allow real-time playback control

Designed a clean CLI interface focused on usability and clarity

Applied defensive programming, validating inputs and handling missing files or folders

Structured the project for easy packaging and distribution

Followed best practices for version control and documentation

📌 Notes

Currently supports .mp3 files only

Runs in the terminal (CLI-based application)

Developed and tested on Windows, but compatible with other platforms supported by Python and Pygame

👨‍💻 Author

Kaio Freire
Aspiring software developer focused on Python and practical projects

🔗 GitHub: https://github.com/kaiofreire4
