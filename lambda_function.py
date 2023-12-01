import json
import logging
import json
import requests

def lambda_handler(event, context):
    text = event['text']

    client_id = "k67mhpzvaq"
    client_secret = "1gdJOKKmebWbKdLFVsp3H3xQqS6eerIZi3Ys7jeq"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/json",
    }

    data = {
        "document": {"title": text, "content": text},
        "option": {
            "language": "ko",
            "model": "general",
            "tone": "0",
            "summaryCount": "3",
        },
    }

    response = requests.post("https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize", data=json.dumps(data), headers=headers)
    result_json = response.json()

    if response.status_code == 200:
        summaries = result_json["summary"]
        summarized_text = " ".join(summaries)
        response_data = {
            "isSuccess": True,
            "code": 200,
            "message": "요청에 성공하였습니다.",
            "data": summarized_text
        }
    else:
        error_message = result_json['error']['message']
        response_data = {
            "isSuccess": False,
            "code": response.status_code,
            "message": error_message
        }

    return {
        'statusCode': 200,
        'body': response_data
    }
