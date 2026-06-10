import json
import smtplib
from email.mime.text import MIMEText

sender = "python.play@gmx.de"
password = "E5ERBPDHGZFVY4GUSOWP"

# Empfänger aus Datei lesen
with open("recipient.json", "r") as f:
    data = json.load(f)
recipient = data["email"]

msg = MIMEText("Testnachricht von GitHub Actions über GMX SMTP.")
msg["Subject"] = "ITSF Backend Test"
msg["From"] = sender
msg["To"] = recipient

with smtplib.SMTP("mail.gmx.net", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

print(f"Mail erfolgreich an {recipient} gesendet!")
