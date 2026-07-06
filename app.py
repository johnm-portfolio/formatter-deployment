from flask import Flask, request, send_file
from note_formatter import format_file
import tempfile
import os

app = Flask(__name__, static_folder="website", static_url_path="")

# Serve frontend
@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/<path:path>")
def static_files(path):
    return app.send_static_file(path)


# API endpoint
@app.post("/format")
def format_note():
    file = request.files["file"]

    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as f:
        input_path = f.name
        file.save(input_path)

    output_path = input_path + "_out.md"

    format_file(input_path, output_path)

    return send_file(output_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)