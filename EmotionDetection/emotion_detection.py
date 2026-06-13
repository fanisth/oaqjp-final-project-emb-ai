import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        response_emotions = {
            "anger": formatted_response["emotionPredictions"][0]["emotion"]["anger"],
            "disgust": formatted_response["emotionPredictions"][0]["emotion"]["disgust"],
            "fear": formatted_response["emotionPredictions"][0]["emotion"]["fear"],
            "joy": formatted_response["emotionPredictions"][0]["emotion"]["joy"],
            "sadness": formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
        }
        dominant_emotion = max(response_emotions, key=response_emotions.get)
        response_emotions["dominant_emotion"] = dominant_emotion
        return response_emotions
    
    return "Error"+