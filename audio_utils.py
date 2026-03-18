import librosa
import numpy as np


def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=16000, mono=True)

    # Energy
    energy = np.mean(librosa.feature.rms(y=y))

    # Pitch
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch_values = pitches[magnitudes > np.median(magnitudes)]
    pitch = np.mean(pitch_values) if len(pitch_values) > 0 else 0

    return {
        "energy": float(energy),
        "pitch": float(pitch)
    }