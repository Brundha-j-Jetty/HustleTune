const recordBtn = document.getElementById("recordBtn");
const statusText = document.getElementById("status");
const moodText = document.getElementById("moodText");
const moodDesc = document.getElementById("moodDesc");
const playlistEl = document.getElementById("playlist");
const languageSelect = document.getElementById("languageSelect");

let mediaRecorder;
let audioChunks = [];

recordBtn.onclick = async () => {
    moodText.innerText = "";
    moodDesc.innerText = "";
    playlistEl.innerHTML = "";
    statusText.innerText = "🎙️ Listening...";

    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    audioChunks = [];

    mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
    mediaRecorder.start();

    setTimeout(() => {
        mediaRecorder.stop();
        statusText.innerText = "🧠 Analyzing mood...";
    }, 4000);

    mediaRecorder.onstop = async () => {
        const blob = new Blob(audioChunks, { type: "audio/wav" });
        const formData = new FormData();
        formData.append("audio", blob);
        formData.append("language", languageSelect.value);

        const response = await fetch("/record", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        statusText.innerText = "🎶 Recommendations ready";
        moodText.innerText = `Mood: ${data.mood}`;

        switch (data.mood) {
            case "Happy":
                moodDesc.innerText = "You sound energetic and positive 😊";
                break;
            case "Sad":
                moodDesc.innerText = "You sound soft and emotional 😔";
                break;
            case "Angry":
                moodDesc.innerText = "You sound intense and forceful 😠";
                break;
            default:
                moodDesc.innerText = "You sound calm and relaxed 😌";
        }

        data.playlists.forEach(p => {
            const link = document.createElement("a");
            link.href = p.url;
            link.target = "_blank";
            link.innerText = p.name;
            playlistEl.appendChild(link);
        });
    };
};