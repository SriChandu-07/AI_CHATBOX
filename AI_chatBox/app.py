from flask import Flask, render_template, request
app = Flask(__name__)
chat_history = []
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["message"].lower().strip()
        if user_input == "hi":
            bot_response = "Hello! How can I help you today?"
        elif user_input == "hello":
            bot_response = "Hey there! What can I do for you?"
        elif user_input == "hey":
            bot_response = "Hi! Feel free to ask me anything."
        elif user_input == "bye":
            bot_response = "Goodbye! Have a great day!"
        elif user_input == "goodbye":
            bot_response = "See you later! Take care."
        elif user_input == "how are you":
            bot_response = "I'm just a bot, but I'm doing great! Thanks for asking."
        elif user_input == "how are you doing":
            bot_response = "Running smoothly! How about you?"
        elif user_input == "help":
            bot_response = "Sure! You can ask me about greetings, jokes, time, or just chat."
        elif user_input == "what can you do":
            bot_response = "I can chat, tell jokes, answer basic questions, and more!"
        elif user_input == "tell me a joke":
            bot_response = "Why don't scientists trust atoms? Because they make up everything!"
        elif user_input == "joke":
            bot_response = "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads."
        elif user_input == "who are you":
            bot_response = "I'm a simple rule-based chatbot built using Python!"
        elif user_input == "what are you":
            bot_response = "I'm a chatbot powered by if-elif conditions!"
        elif user_input == "what time is it":
            bot_response = "I don't have a clock, but your device does! Check the corner of your screen."
        elif user_input == "what day is it":
            bot_response = "I can't access real-time data, but your phone or computer knows!"
        elif user_input == "thanks":
            bot_response = "You're welcome!"
        elif user_input == "thank you":
            bot_response = "Happy to help! Anything else?"
        elif user_input == "i am sad":
            bot_response = "I'm sorry to hear that. Remember, tough times don't last!"
        elif user_input == "i am happy":
            bot_response = "That's wonderful! Keep spreading the good vibes!"
        elif user_input == "i am bored":
            bot_response = "Let's fix that! Ask me for a joke or just start chatting."
        else:
            bot_response = "Sorry, I'm not sure about that. Try asking something else!"
        chat_history.append({
            "user": user_input,
            "bot": bot_response
        })
    return render_template("index.html", chats=chat_history)
if __name__ == "__main__":
    app.run(debug=True)