<<<<<<< HEAD
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

INTENTS_FILE = "intents.json"
MODEL_FILE = "intent_model.joblib"
VECTORIZER_FILE = "vectorizer.joblib"
LABELS_FILE = "labels.json"

def load_intents():
    """Load intents from the JSON file."""
    with open(INTENTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["intents"]

def prepare_data(intents):
    """Prepare texts and labels from intents for training."""
    texts = []
    labels = []
    for intent in intents:
        tag = intent["tag"]
        for pattern in intent["patterns"]:
            texts.append(pattern.lower())
            labels.append(tag)
    return texts, labels

def main():
    """Train the intent classification model and save it."""
    intents = load_intents()
    texts, labels = prepare_data(intents)

    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(texts)

    unique_labels = sorted(list(set(labels)))
    label_to_id = {label: i for i, label in enumerate(unique_labels)}
    y = np.array([label_to_id[l] for l in labels])

    clf = LogisticRegression(max_iter=200)
    clf.fit(X, y)

    joblib.dump(clf, MODEL_FILE)
    joblib.dump(vectorizer, VECTORIZER_FILE)
    with open(LABELS_FILE, "w", encoding="utf-8") as f:
        json.dump({"labels": unique_labels}, f, indent=2, ensure_ascii=False)

    print("Model, vectorizer, and labels saved.")

if __name__ == "__main__":
=======
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

INTENTS_FILE = "intents.json"
MODEL_FILE = "intent_model.joblib"
VECTORIZER_FILE = "vectorizer.joblib"
LABELS_FILE = "labels.json"

def load_intents():
    with open(INTENTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["intents"]

def prepare_data(intents):
    texts = []
    labels = []
    for intent in intents:
        tag = intent["tag"]
        for pattern in intent["patterns"]:
            texts.append(pattern.lower())
            labels.append(tag)
    return texts, labels

def main():
    intents = load_intents()
    texts, labels = prepare_data(intents)

    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(texts)

    unique_labels = sorted(list(set(labels)))
    label_to_id = {label: i for i, label in enumerate(unique_labels)}
    y = np.array([label_to_id[l] for l in labels])

    clf = LogisticRegression(max_iter=200)
    clf.fit(X, y)

    joblib.dump(clf, MODEL_FILE)
    joblib.dump(vectorizer, VECTORIZER_FILE)
    with open(LABELS_FILE, "w", encoding="utf-8") as f:
        json.dump({"labels": unique_labels}, f, indent=2, ensure_ascii=False)

    print("Model, vectorizer, and labels saved.")

if __name__ == "__main__":
>>>>>>> b73bcc27db597c3ef6a96410f7a146a0d94dbe86
    main()