# 🎧 HustleTune

HustleTune is a voice-driven mood-based music recommendation web application that connects human emotions with music using simple audio analysis and real-time Spotify playlist suggestions.

---

## 💡 Why I Built This

As an AIML student, I wanted to build a practical project that combines AI concepts with real-world user interaction. Music is closely tied to emotions, so I explored how voice input can be used to detect mood and recommend playlists accordingly.

---

## 🚀 Features

- 🎙️ Voice-based mood detection  
- 🧠 Emotion classification:
  - Happy  
  - Sad  
  - Calm  
  - Angry  
- 🌍 Language-based playlist selection:
  - English, Hindi, Tamil, Telugu, Kannada, Malayalam  
  - Mixed (All Languages)  
- 🎧 Spotify playlist recommendations based on mood and language  
- ⚡ Lightweight system (no heavy ML models)

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **Audio Processing:** Librosa  
- **API:** Spotify Web API  
- **Environment Handling:** python-dotenv  

---

## 🧠 How It Works

1. User records voice using the browser  
2. Audio is sent to the Flask backend  
3. Audio features (like energy and pitch) are extracted  
4. Mood is determined using rule-based logic  
5. Spotify API fetches playlists based on:
   - Detected mood  
   - Selected language  
6. Playlists are displayed on the UI  

---

## ⚡ Challenges Faced

- Handling browser-based audio recording  
- Converting audio into a usable format  
- Tuning mood detection using audio features  
- Securing API credentials using environment variables  

---

## 📂 Project Structure

```
MoodMusicAI/
├── app.py
├── model.py
├── audio_utils.py
├── spotify_utils.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository  
2. Create virtual environment:

```
python -m venv venv
```

3. Activate environment:

```
venv\Scripts\activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Create a `.env` file and add:

```
CLIENT_ID=your_spotify_client_id  
CLIENT_SECRET=your_spotify_client_secret  
```

6. Run the application:

```
python app.py
```

7. Open in browser:

```
http://127.0.0.1:5000
```

---

## 📌 Future Improvements

- Improve mood detection using advanced ML models  
- Add user personalization  
- Deploy the application online  
- Enhance UI/UX  

---

## 👨‍💻 About

Built as a learning project to explore AI integration with web applications and real-time APIs.