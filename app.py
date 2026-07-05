from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

history = []

# 🔥 Strong keyword lists
spam_keywords = ["win", "money", "free", "click", "offer", "urgent", "hacking", "hack", "whatsapp", "earn"]
toxic_keywords = ["fuck", "fck", "idiot", "stupid", "hate", "dumb", "bitch"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "")

    text = message.lower()
    print("Message:", text)

    # 🔴 Spam check
    if any(word in text for word in spam_keywords):
        print("Detected: SPAM")
        result = "Spam 🚨 (Rule-based)"

    # 🟠 Toxic check
    elif any(word in text for word in toxic_keywords):
        print("Detected: TOXIC")
        result = "Toxic ⚠️ (Rule-based)"

    # 🤖 ML model
    else:
        vect = vectorizer.transform([message])
        prediction = model.predict(vect)[0]
        prob = model.predict_proba(vect)[0]

        confidence = round(max(prob) * 100, 2)

        if prediction == 1:
            print("Detected: TOXIC (ML)")
            result = f"Toxic ⚠️ ({confidence}%)"
        else:
            print("Detected: SAFE (ML)")
            result = f"Safe ✅ ({confidence}%)"

    history.append({"msg": message, "result": result})

    return jsonify({"result": result})


@app.route("/history")
def get_history():
    return jsonify(history)

if __name__ == "__main__":
    app.run(debug=True)