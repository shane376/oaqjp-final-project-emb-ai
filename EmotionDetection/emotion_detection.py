import requests
#Emotion Detector Function
def emotion_detection(text_to_analyse: str) -> str:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse} }
    header = header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)

    if response.status_code == 200:
        formatted_response = response.json()
        emotions = {
            'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
            'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness'],
        }
        emotions['dominant_emotion'] = max(emotions, key = emotions.get)
        return emotions
    elif response.status_code == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotions
