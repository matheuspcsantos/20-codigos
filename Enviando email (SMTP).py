import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
# server.login("email", "senha")  # Descomente
# server.sendmail("de", "para", "mensagem")
print("Conexão OK")
