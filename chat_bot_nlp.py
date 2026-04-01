<<<<<<< HEAD
import json
import os
import re
import random
import joblib

MEMORY_FILE = "memory_nlp.json"
INTENTS_FILE = "intents.json"
MODEL_FILE = "intent_model.joblib"
VECTORIZER_FILE = "vectorizer.joblib"
LABELS_FILE = "labels.json"

def normalize(text: str) -> str:
    """Normalize text by converting to lowercase and removing extra spaces."""
    return re.sub(r"\s+", " ", text.strip().lower())

def load_memory():
    """Load conversation memory from JSON file."""
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []
    except Exception:
        return []

def save_memory(memory_list):
    """Save conversation memory to JSON file."""
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(memory_list, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"(Memory warning) Could not save memory: {e}")

def remember(memory_list, user_text, bot_text):
    """Add a conversation pair to memory and save."""
    memory_list.append({"user": user_text, "bot": bot_text})
    save_memory(memory_list)

def load_nlp_assets():
    """Load intents, labels, model, and vectorizer for NLP processing."""
    with open(INTENTS_FILE, "r", encoding="utf-8") as f:
        intents_data = json.load(f)["intents"]

    with open(LABELS_FILE, "r", encoding="utf-8") as f:
        labels_data = json.load(f)
    labels = labels_data["labels"]

    model = joblib.load(MODEL_FILE)
    vectorizer = joblib.load(VECTORIZER_FILE)

    tag_to_intent = {intent["tag"]: intent for intent in intents_data}
    return model, vectorizer, labels, tag_to_intent

def choose_response(intent_obj):
    """Choose a random response from the intent's responses list."""
    responses = intent_obj.get("responses", [])
    if not responses:
        return "I understand, but I don't have a good answer yet. Could you ask in another way?"
    return random.choice(responses)

def print_welcome():
    """Print the welcome message for the chatbot."""
    print("=" * 70)
    print("   🤖 Cyber Helper NLP Bot (with JSON memory)")
    print("=" * 70)
    print("Hello 😊 I'm your calm NLP assistant for cybersecurity, education, Python and Git.")
    print("You can ask me in your own words; I will try to detect your intent using NLP.")
    print("Type 'help' to see what I can do.")
    print("Type 'history' to see how many messages I remember.")
    print("Type 'exit' or 'quit' to leave the chat.")
    print("-" * 70)

def main():
    """Main function to run the NLP chatbot."""
    model, vectorizer, labels, tag_to_intent = load_nlp_assets()
    memory = load_memory()
    print_welcome()

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue

            low = normalize(user_input)

            if low in {"exit", "quit", "bye", "goodbye"}:
                intent_obj = tag_to_intent.get("goodbye")
                if intent_obj:
                    bot_reply = choose_response(intent_obj)
                else:
                    bot_reply = "Thank you for chatting with me. Goodbye! 👋"
                print(f"Bot: {bot_reply}")
                remember(memory, user_input, bot_reply)
                break

            if low == "help":
                print("Bot: I can help with greetings, registration, fees, scholarships, cybersecurity basics, study tips, Python basics, and Git/GitHub usage.")
                continue

            if low == "history":
                if not memory:
                    print("Bot: I don't have any saved history yet in memory_nlp.json.")
                else:
                    print(f"Bot: I currently remember {len(memory)} message pairs in memory_nlp.json.")
                continue

            X = vectorizer.transform([low])
            probs = model.predict_proba(X)[0]
            pred_id = probs.argmax()
            confidence = probs[pred_id]
            tag = labels[pred_id]

            if confidence < 0.4:
                intent_obj = tag_to_intent.get("default_fallback")
            else:
                intent_obj = tag_to_intent.get(tag, tag_to_intent.get("default_fallback"))

            bot_reply = choose_response(intent_obj)
            print(f"Bot: {bot_reply}")
            remember(memory, user_input, bot_reply)

        except KeyboardInterrupt:
            print("\n\nBot: Thank you for chatting. Goodbye! 👋")
            break
        except Exception as e:
            print(f"Bot: Oops, something went wrong: {e}. Please try again.")

if __name__ == "__main__":
=======
import json
import os
import re
import random
import joblib

MEMORY_FILE = "memory_nlp.json"
INTENTS_FILE = "intents.json"
MODEL_FILE = "intent_model.joblib"
VECTORIZER_FILE = "vectorizer.joblib"
LABELS_FILE = "labels.json"

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []
    except Exception:
        return []

def save_memory(memory_list):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(memory_list, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"(Memory warning) Could not save memory: {e}")

def remember(memory_list, user_text, bot_text):
    memory_list.append({"user": user_text, "bot": bot_text})
    save_memory(memory_list)

def load_nlp_assets():
    with open(INTENTS_FILE, "r", encoding="utf-8") as f:
        intents_data = json.load(f)["intents"]

    with open(LABELS_FILE, "r", encoding="utf-8") as f:
        labels_data = json.load(f)
    labels = labels_data["labels"]

    model = joblib.load(MODEL_FILE)
    vectorizer = joblib.load(VECTORIZER_FILE)

    tag_to_intent = {intent["tag"]: intent for intent in intents_data}
    return model, vectorizer, labels, tag_to_intent

def choose_response(intent_obj):
    responses = intent_obj.get("responses", [])
    if not responses:
        return "I understand, but I don't have a good answer yet. Could you ask in another way?"
    return random.choice(responses)

def print_welcome():
    print("=" * 70)
    print("   🤖 Cyber Helper NLP Bot (with JSON memory)")
    print("=" * 70)
    print("Hello 😊 I'm your calm NLP assistant for cybersecurity, education, Python and Git.")
    print("You can ask me in your own words; I will try to detect your intent using NLP.")
    print("Type 'help' to see what I can do.")
    print("Type 'history' to see how many messages I remember.")
    print("Type 'exit' or 'quit' to leave the chat.")
    print("-" * 70)

def main():
    model, vectorizer, labels, tag_to_intent = load_nlp_assets()
    memory = load_memory()
    print_welcome()

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue

            low = normalize(user_input)

            if low in {"exit", "quit", "bye", "goodbye"}:
                intent_obj = tag_to_intent.get("goodbye")
                if intent_obj:
                    bot_reply = choose_response(intent_obj)
                else:
                    bot_reply = "Thank you for chatting with me. Goodbye! 👋"
                print(f"Bot: {bot_reply}")
                remember(memory, user_input, bot_reply)
                break

            if low == "help":
                print("Bot: I can help with greetings, registration, fees, scholarships, cybersecurity basics, study tips, Python basics, and Git/GitHub usage.")
                continue

            if low == "history":
                if not memory:
                    print("Bot: I don't have any saved history yet in memory_nlp.json.")
                else:
                    print(f"Bot: I currently remember {len(memory)} message pairs in memory_nlp.json.")
                continue

            X = vectorizer.transform([low])
            probs = model.predict_proba(X)[0]
            pred_id = probs.argmax()
            confidence = probs[pred_id]
            tag = labels[pred_id]

            if confidence < 0.4:
                intent_obj = tag_to_intent.get("default_fallback")
            else:
                intent_obj = tag_to_intent.get(tag, tag_to_intent.get("default_fallback"))

            bot_reply = choose_response(intent_obj)
            print(f"Bot: {bot_reply}")
            remember(memory, user_input, bot_reply)

        except KeyboardInterrupt:
            print("\n\nBot: Thank you for chatting. Goodbye! 👋")
            break
        except Exception as e:
            print(f"Bot: Oops, something went wrong: {e}. Please try again.")

if __name__ == "__main__":
>>>>>>> b73bcc27db597c3ef6a96410f7a146a0d94dbe86
    main()