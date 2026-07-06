from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import sys
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS for Netlify

try:
    from note_formatter.formatter import format_text
except ImportError:
    # Fallback: implement minimal formatter if package not installed
    def format_text(text: str, generate_toc: bool = True) -> str:
        """Fallback formatter if note_formatter package isn't installed"""
        import re
        
        # Load symbols from JSON
        try:
            with open('symbols.json', 'r') as f:
                symbols_data = json.load(f)
        except FileNotFoundError:
            return text
        
        for symbol in symbols_data.get("symbols", []):
            for alias in symbol.get("inputs", []):
                text = text.replace(alias, symbol["output"])
        
        for formulae in symbols_data.get("formulae", []):
            pattern = formulae.get("pattern", "")
            replacement = formulae.get("replacement", "")
            try:
                text = re.sub(pattern, replacement, text)
            except:
                pass
        
        return text


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200


@app.route('/format', methods=['POST'])
def format_file():
    """
    Format text using the Symbol Formatter
    
    Request body:
    {
        "text": "raw text to format",
        "generateToc": true
    }
    
    Response:
    {
        "success": true,
        "formatted": "formatted text",
        "error": null
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "formatted": None,
                "error": "No JSON data provided"
            }), 400
        
        text = data.get('text', '')
        generate_toc = data.get('generateToc', True)
        
        if not text:
            return jsonify({
                "success": False,
                "formatted": None,
                "error": "No text provided"
            }), 400
        
        formatted = format_text(text, generate_toc)
        
        return jsonify({
            "success": True,
            "formatted": formatted,
            "error": None
        }), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "formatted": None,
            "error": str(e)
        }), 500


@app.route('/format-file', methods=['POST'])
def format_file_upload():
    """
    Format uploaded file
    
    Multipart form data with:
    - file: the file to format
    - generateToc: true/false (optional, defaults to true)
    
    Response: formatted file as plain text with proper Content-Disposition
    """
    try:
        if 'file' not in request.files:
            return jsonify({
                "error": "No file provided"
            }), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({
                "error": "No file selected"
            }), 400
        
        text = file.read().decode('utf-8')
        generate_toc = request.form.get('generateToc', 'true').lower() == 'true'
        
        formatted = format_text(text, generate_toc)
        
        original_name = Path(file.filename).stem
        output_filename = f"{original_name}_formatted.md"
        
        return formatted, 200, {
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Disposition': f'attachment; filename="{output_filename}"'
        }
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)