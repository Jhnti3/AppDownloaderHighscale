from flask import Flask, request, jsonify, send_file, render_template
from downloader import download_video
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "static")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    data = request.json
    url = data.get("url")
    format_type = data.get("format")  # "mp3" ou "mp4"

    if not url or format_type not in ["mp3", "mp4"]:
        return jsonify({"error": "Parâmetros inválidos."}), 400

    try:
        print(f"Baixando {format_type} do URL: {url}")
        file_path = download_video(url, format_type, DOWNLOAD_FOLDER)
        print(f"Arquivo salvo em: {file_path}")
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        print(f"Erro no download: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
