from flask import Flask, render_template, request, jsonify
import os

from audio_utils import extract_features
from model import detect_mood
from spotify_utils import get_playlist_for_mood

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/record", methods=["POST"])
def record():
    if "audio" not in request.files:
        return jsonify({"error": "No audio received"}), 400

    audio_file = request.files["audio"]
    language = request.form.get("language", "Mixed")

    file_path = os.path.join(UPLOAD_FOLDER, "recorded.wav")
    audio_file.save(file_path)

    features = extract_features(file_path)
    mood = detect_mood(features)

    playlists = get_playlist_for_mood(mood, language)

    return jsonify({
        "mood": mood,
        "language": language,
        "playlists": playlists
    })


if __name__ == "__main__":
    app.run(debug=True)