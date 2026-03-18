def detect_mood(features):
    energy = features["energy"]
    pitch = features["pitch"]

    LOW_ENERGY = 0.02
    HIGH_ENERGY = 0.035
    HIGH_PITCH = 180
    LOW_PITCH = 150

    if energy < LOW_ENERGY:
        return "Sad"

    if energy > HIGH_ENERGY and pitch > HIGH_PITCH:
        return "Happy"

    if energy > HIGH_ENERGY and pitch < LOW_PITCH:
        return "Angry"

    return "Calm"