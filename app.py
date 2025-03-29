from flask import Flask, render_template, jsonify, send_file
import csv

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

if __name__ == "__main__":
    app.run(debug=True)
