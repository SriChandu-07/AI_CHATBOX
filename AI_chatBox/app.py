from flask import Flask, render_template, request
app=Flask(__name__)
responses={
    "hi":"Hello! How can I help you today?",
    "hello":"Hey there! What can I do for you?",
    "hey":"Hi! Feel free to ask me anything.",
    "bye":"Goodbye! Have a great day!",
    "goodbye":"See you later! Take care.",
    "how are you":"I'm just a bot, but I'm doing great! Thanks for asking.",
    "how are you doing":"Running smoothly! How about you?",
    "help":"Sure! You can ask me about greetings, jokes, time, or just chat.",
    "what can you do": "I can chat, tell jokes, answer basic questions, and more!",
    "tell me a joke":"Why don't scientists trust atoms? Because they make up everything!",
    "joke":"I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
    "who are you":"I'm a simple rule-based chatbot built using Python dictionaries!",
    "what are you":"I'm a chatbot powered by a hash map knowledge base.",
    "what time is it":"I don't have a clock, but your device does! Check the corner of your screen.",
    "what day is it":"I can't access real-time data, but your phone or computer knows!",
    "thanks":"You're welcome!",
    "thank you":"Happy to help! Anything else?",
    "i am sad":"I'm sorry to hear that. Remember, tough times don't last!",
    "i am happy":"That's wonderful! Keep spreading the good vibes!",
    "i am bored":"Let's fix that! Ask me for a joke or just start chatting."
}
chat_history = []
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["message"].lower().strip()
        bot_response = responses.get(
            user_input,
            "Sorry, I'm not sure about that.try asking something else"
            )
        chat_history.append({
            "user": user_input,
            "bot": bot_response
        })
    return render_template(
        "index.html",
        chats=chat_history
    )
if __name__=="__main__":
    app.run(debug=True)