import json
from note_formatter.formatter import format_text

def handler(event, context):
    try:
        body = json.loads(event["body"])
        text = body.get("text", "")

        formatted = format_text(text, generate_toc=True)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/plain; charset=utf-8",
                "Access-Control-Allow-Origin": "*"
            },
            "body": formatted
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }