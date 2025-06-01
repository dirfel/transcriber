from flask import Flask, render_template, jsonify, send_file, request
import csv
from utils import salvar_audio_validado
from database import criar_tabelas, inserir_transcricao
criar_tabelas()


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/dados")
def dados():
    registros = []
    with open("database.csv", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            registros.append({
                "data_hora": row["data-hora"],
                "transcricao": row["transcrição"],
                "audio": row["caminho_audio"]
            })
    return jsonify(registros)

@app.route("/backup")
def backup():
    return send_file("database.csv", as_attachment=True)

@app.route("/upload", methods=["POST"])
def upload_audio():
    if 'file' not in request.files:
        return jsonify(success=False)

    file = request.files['file']
    if file.filename == '':
        return jsonify(success=False)

    if salvar_audio_validado(file):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

if __name__ == "__main__":
    app.run(debug=True)
