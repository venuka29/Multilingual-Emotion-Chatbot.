import random
from responses import responses, content

last_response = {}


def detect_emotion(text):

    text = text.lower()

    happy_words = ["happy", "good", "great", "awesome", "love", "excited", "bought", "success", "nice"]
    sad_words = ["sad", "lonely", "cry", "hurt", "bad", "lost", "upset", "depressed"]
    stress_words = ["stress", "tired", "busy", "pressure", "work", "deadline", "exhausted"]
    anger_words = ["angry", "mad", "hate", "annoyed", "furious"]

    if any(w in text for w in happy_words):
        return "happy"

    if any(w in text for w in sad_words):
        return "sad"

    if any(w in text for w in stress_words):
        return "stress"

    if any(w in text for w in anger_words):
        return "anger"

    return "neutral"


def get_response(emotion, lang):

    key = f"{lang}_{emotion}"

    replies = responses[lang][emotion]

    if key not in last_response:
        last_response[key] = None

    reply = random.choice(replies)

    # avoid repetition
    attempts = 0
    while reply == last_response[key] and attempts < 5:
        reply = random.choice(replies)
        attempts += 1

    last_response[key] = reply
    return reply


def get_suggestions(lang, emotion):

    return content.get(lang, {}).get(emotion, None)