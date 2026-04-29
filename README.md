akeyloger 🎹
A lightweight, efficient keylogger written in Python. This tool captures keystrokes and saves them to a local log file for auditing or educational purposes.

[!WARNING]

Ethical Use Only: This tool is intended for educational research, authorized security auditing, or personal backups. Unauthorized monitoring of devices you do not own is illegal and unethical.

🚀 Features
Real-time Capture: Monitors keyboard input instantly using the pynput library.

Local Logging: Automatically writes keystrokes to a .txt file.

Background Operation: Can be configured to run silently.

Special Key Handling: Properly formats keys like Space, Enter, and Shift.

🛠️ Installation
Clone the repository:

Bash
git clone [https://github.com/yourusername/akeyloger](https://github.com/ExcelenceCodes/akeyloger).git
cd akeyloger
Install dependencies:

Bash
pip install pynput
🖥️ Usage
Run the script using Python:

Bash
python akeyloger.py
The captured keystrokes will be saved to keylog.txt in the same directory by default.
