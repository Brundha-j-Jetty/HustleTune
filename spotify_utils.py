import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


def get_access_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    encoded = base64.b64encode(auth_string.encode()).decode()

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {encoded}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={"grant_type": "client_credentials"}
    )

    data = response.json()
    return data.get("access_token")


# ==============================
# 🔍 SEARCH HELPER
# ==============================
def spotify_search(token, query, limit=5):
    response = requests.get(
        "https://api.spotify.com/v1/search",
        headers={"Authorization": f"Bearer {token}"},
        params={
            "q": query,
            "type": "playlist",
            "limit": limit
        }
    )

    items = response.json().get("playlists", {}).get("items", [])
    results = []

    for p in items:
        if not p:
            continue
        results.append({
            "name": p["name"],
            "url": p["external_urls"]["spotify"]
        })

    return results


# ==============================
# 🎧 MOOD + LANGUAGE RECOMMENDER
# ==============================
def get_playlist_for_mood(mood, language):
    token = get_access_token()
    if not token:
        return []

    curated_queries = {
        "Happy": {
            "English": [
                "today's top hits", "feel good pop", "happy vibes",
                "uplifting songs", "good vibes only"
            ],
            "Hindi": [
                "bollywood party songs", "happy hindi songs",
                "feel good bollywood", "bollywood dance hits",
                "hindi upbeat songs"
            ],
            "Tamil": [
                "tamil happy songs", "tamil party hits",
                "tamil feel good", "tamil dance songs",
                "tamil upbeat hits"
            ],
            "Telugu": [
                "telugu party hits", "telugu happy songs",
                "telugu feel good", "telugu dance hits",
                "telugu top hits"
            ],
            "Kannada": [
                "kannada party hits", "kannada happy songs",
                "kannada upbeat hits", "kannada dance songs",
                "kannada top hits"
            ],
            "Malayalam": [
                "feel good malayalam", "malayalam party hits",
                "malayalam dance hits", "malayalam upbeat songs",
                "malayalam top hits"
            ],
            "Mixed": [
                "feel good hits", "happy vibes",
                "party hits", "dance hits",
                "good vibes playlist"
            ]
        },

        "Sad": {
            "English": [
                "sad songs", "heartbreak playlist",
                "emotional english songs", "melancholic music",
                "crying songs"
            ],
            "Hindi": [
                "sad bollywood songs", "heartbreak hindi",
                "emotional hindi songs", "bollywood sad melodies",
                "hindi breakup songs"
            ],
            "Tamil": [
                "tamil sad songs", "tamil melody",
                "tamil heartbreak", "tamil emotional songs",
                "tamil love failure"
            ],
            "Telugu": [
                "telugu sad songs", "telugu sad melodies",
                "telugu heartbreak", "emotional telugu songs",
                "telugu love failure"
            ],
            "Kannada": [
                "kannada sad songs", "kannada emotional songs",
                "kannada melody sad", "kannada heartbreak",
                "kannada melancholic"
            ],
            "Malayalam": [
                "malayalam sad songs", "malayalam emotional",
                "malayalam heartbreak", "malayalam melody sad",
                "malayalam melancholic"
            ],
            "Mixed": [
                "sad songs", "emotional music",
                "heartbreak playlist", "melancholic vibes",
                "breakup songs"
            ]
        },

        "Calm": {
            "English": [
                "chill vibes", "lofi beats",
                "relaxing acoustic", "peaceful music",
                "calm songs"
            ],
            "Hindi": [
                "hindi lofi", "peaceful bollywood",
                "relaxing hindi songs", "hindi acoustic",
                "calm hindi songs"
            ],
            "Tamil": [
                "tamil melody", "tamil chill songs",
                "tamil relaxing music", "tamil acoustic",
                "peaceful tamil songs"
            ],
            "Telugu": [
                "telugu melody", "telugu chill",
                "telugu relaxing music", "telugu acoustic",
                "peaceful telugu songs"
            ],
            "Kannada": [
                "kannada melody", "kannada chill",
                "kannada relaxing", "kannada acoustic",
                "peaceful kannada songs"
            ],
            "Malayalam": [
                "malayalam melody", "malayalam chill",
                "malayalam relaxing", "malayalam acoustic",
                "peaceful malayalam songs"
            ],
            "Mixed": [
                "chill music", "lofi beats",
                "relaxing music", "peaceful vibes",
                "calm playlist"
            ]
        },

        "Angry": {
            "English": [
                "workout motivation", "rock workout",
                "gym rage", "intense workout",
                "beast mode"
            ],
            "Hindi": [
                "bollywood workout", "intense hindi songs",
                "hindi gym playlist", "bollywood motivation",
                "hindi power songs"
            ],
            "Tamil": [
                "tamil workout songs", "tamil mass hits",
                "tamil gym playlist", "tamil intense songs",
                "tamil power songs"
            ],
            "Telugu": [
                "telugu workout", "telugu mass songs",
                "telugu gym playlist", "telugu intense",
                "telugu power songs"
            ],
            "Kannada": [
                "kannada workout", "kannada mass songs",
                "kannada gym playlist", "kannada intense",
                "kannada power songs"
            ],
            "Malayalam": [
                "malayalam workout", "malayalam gym songs",
                "malayalam intense", "malayalam adrenaline",
                "malayalam power songs"
            ],
            "Mixed": [
                "workout playlist", "intense music",
                "gym motivation", "power songs",
                "adrenaline music"
            ]
        }
    }

    queries = curated_queries.get(mood, {}).get(language, [])
    playlists = []
    seen = set()

    for q in queries:
        results = spotify_search(token, q)
        for p in results:
            if p["url"] not in seen:
                playlists.append(p)
                seen.add(p["url"])
        if len(playlists) >= 5:
            break

    # 🛟 FINAL FALLBACK (guaranteed)
    if not playlists:
        playlists = spotify_search(token, "popular playlists", limit=5)

    return playlists[:5]