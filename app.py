import os
from flask import Flask, request, send_file, jsonify, render_template
from werkzeug.utils import secure_filename
from io import BytesIO
import tempfile

from note_formatter.formatter import format_text

app = Flask(
    __name__,
    static_folder="website",
    static_url_path="/"
)

# Optional upload limit (10MB)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/website/<path:path>")
def website_files(path):
    return app.send_static_file(path)

@app.route("/format", methods=["POST"])
def format_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)

    try:
        raw_text = file.read().decode("utf-8")
    except Exception:
        return jsonify({"error": "File must be UTF-8 encoded text"}), 400

    # Run your formatter
    formatted_text = format_text(raw_text, generate_toc=True)

    # Write to temporary file for download
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".md")
    tmp.write(formatted_text.encode("utf-8"))
    tmp.close()

    return send_file(
        tmp.name,
        as_attachment=True,
        download_name="formatted.md",
        mimetype="text/markdown"
    )

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)