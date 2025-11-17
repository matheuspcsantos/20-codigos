from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}

app.run(debug=True)
