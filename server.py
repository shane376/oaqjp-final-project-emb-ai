"""
This module serves as the server for the application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector():
    """
    Routes the data incoming from the index page to the backend and back
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_response = emotion_detection(text_to_analyze)
    if not emotion_response['dominant_emotion']:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger': { emotion_response['anger'] }, 'disgust': { emotion_response['disgust'] }, 'fear': {emotion_response['fear'] }, 'joy': { emotion_response['joy'] }, and 'sadness': { emotion_response['sadness'] }. The dominant emotion is { emotion_response['dominant_emotion'] }."

@app.route("/")
def render_index_page():
    """
    Renders the index page so users can input data
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
