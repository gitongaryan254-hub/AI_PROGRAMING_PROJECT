# simple_chat_faq_bot.py

import re
import json
import os
import random

MEMORY_FILE = "memory_simple.json"
INTENTS_FILE = "../intents.json"  # Path relative to the subfolder

def normalize(text: str) -> str:
    """Lowercase and remove extra spaces."""
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

def load_intents():
    """Load intents from the JSON file."""
    try:
        with open(INTENTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data["intents"]
    except Exception as e:
        print(f"Error loading intents: {e}")
        return []

def get_response(user_input: str, intents) -> str:
    text = normalize(user_input)

    # Exit handled outside
    if text in {"exit", "quit", "bye", "goodbye"}:
        return "Thank you for chatting with me. I wish you a smooth learning journey in cybersecurity. 🌱"

    # Check for matches in intents
    for intent in intents:
        for pattern in intent["patterns"]:
            pattern_words = normalize(pattern).split()
            if any(word in text for word in pattern_words):
                responses = intent.get("responses", [])
                if responses:
                    return random.choice(responses)

    # Default fallback
    return "I'm not sure I understand. Could you rephrase? Or type 'help' to see what I can do."

def print_welcome():
    print("=" * 70)
    print("   🤖 Cyber Helper Bot")
    print("=" * 70)
    print("Hello 😊 I'm your calm cybersecurity & registration assistant.")
    print("You can ask me in your own words; I will try to detect your intent using intents data.")
    print("Type 'help' to see what I can do.")
    print("Type 'history' to see how many messages I remember.")
    print("Type 'exit' or 'quit' to leave the chat.")
    print("-" * 70)

def main():
    intents = load_intents()
    memory = load_memory()
    print_welcome()
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue

            low = normalize(user_input)

            if low in {"exit", "quit", "bye", "goodbye"}:
                intent_obj = next((i for i in intents if i["tag"] == "goodbye"), None)
                if intent_obj:
                    bot_reply = random.choice(intent_obj.get("responses", ["Thank you for chatting with me. Goodbye! 👋"]))
                else:
                    bot_reply = "Thank you for chatting with me. Goodbye! 👋"
                print(f"Bot: {bot_reply}")
                remember(memory, user_input, bot_reply)
                break

            if low == "help":
                intent_obj = next((i for i in intents if i["tag"] == "help_info"), None)
                if intent_obj:
                    bot_reply = random.choice(intent_obj.get("responses", ["I can help with various topics. Ask away!"]))
                else:
                    bot_reply = "I can help with greetings, registration, fees, scholarships, cybersecurity basics, study tips, Python basics, and Git/GitHub usage."
                print(f"Bot: {bot_reply}")
                continue

            if low == "history":
                if not memory:
                    print("Bot: I don't have any saved history yet.")
                else:
                    print(f"Bot: I currently remember {len(memory)} message pairs.")
                continue

            response = get_response(user_input, intents)
            print(f"Bot: {response}")
            remember(memory, user_input, response)

        except KeyboardInterrupt:
            print("\n\nBot: Thank you for chatting. Goodbye! 👋")
            break
        except Exception as e:
            print(f"Bot: Oops, something went wrong: {e}. Please try again.")

if __name__ == "__main__":
    main()