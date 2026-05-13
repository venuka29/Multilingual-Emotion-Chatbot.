from chatbot_base import detect_emotion, get_response, get_suggestions

languages = {
    "1": ("தமிழ்", "Tamil"),
    "2": ("English", "English"),
    "3": ("සිංහල", "Sinhala")
}

ui = {
    "English": {
        "greet": "Hi, I’m here with you. How are you feeling today?",
        "prompt": "You: ",
        "share": "Would you like to talk more? (yes/no): ",
        "suggest": "Would you like suggestions? (yes/no): ",
        "exit": "Take care 👋"
    },

    "Tamil": {
        "greet": "வணக்கம், நான் உங்களுடன் இருக்கிறேன். இன்று எப்படி இருக்கிறீர்கள்?",
        "prompt": "நீங்கள்: ",
        "share": "மேலும் பேச விரும்புகிறீர்களா? (yes/no): ",
        "suggest": "சில பரிந்துரைகள் வேண்டுமா? (yes/no): ",
        "exit": "கவனமாக இருங்கள் 👋"
    },

    "Sinhala": {
        "greet": "හෙලෝ, මම ඔබ සමඟ ඉන්නවා. අද ඔබට කොහොමද?",
        "prompt": "ඔබ: ",
        "share": "තව කතා කරන්න කැමතිද? (yes/no): ",
        "suggest": "යෝජනා අවශ්‍යද? (yes/no): ",
        "exit": "සැලකිලිමත් වන්න 👋"
    }
}

print("👋 Welcome to Emotion Chatbot")

print("\nChoose language:")
print("1. தமிழ்")
print("2. English")
print("3. සිංහල")

choice = input("\nEnter choice (1/2/3): ")

if choice not in languages:
    lang_display, lang = "English", "English"
else:
    lang_display, lang = languages[choice]

print(f"\n🌐 Selected Language: {lang_display}")

print("\nBot:", ui[lang]["greet"])
print("(Type 'exit' to stop)\n")

while True:

    user = input(ui[lang]["prompt"]).strip().lower()

    if user == "exit":
        print("\nBot:", ui[lang]["exit"])
        break

    if user in ["why", "why?", "?", "how", "what"]:
        print("\nBot: I’m here to understand you. Can you tell me more?")
        continue

    if user == "":
        print("\nBot: Please type something.")
        continue

    emotion = detect_emotion(user)

    print("\nBot:", get_response(emotion, lang))

    share = input("\n" + ui[lang]["share"]).strip().lower()

    if share in ["yes", "y", "ok", "yeah"]:

        more = input(ui[lang]["prompt"]).strip().lower()

        if more == "exit":
            print("\nBot:", ui[lang]["exit"])
            break
        emotion = detect_emotion(more)

        print("\nBot:", get_response(emotion, lang))

        if emotion in ["sad", "stress", "anger"]:

            ask = input("\n" + ui[lang]["suggest"]).strip().lower()

            if ask in ["yes", "y", "ok", "yeah"]:

                sug = get_suggestions(lang, emotion)

                if sug:
                    print("\n💡 Suggestions:")
                    print("🎵 Song:", sug["song"])
                    print("🎬 Movie:", sug["movie"])
                    print("🧠 Tip:", sug["tip"])

    else:
        print("\nBot: I’m here if you need me.")
