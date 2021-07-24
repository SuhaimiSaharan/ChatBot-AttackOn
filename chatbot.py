from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

with open('file.txt', 'r') as file:
    conversation = file.read()

botname = "PetroBot"
bot = ChatBot(
    botname,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation",
                    "chatterbot.logic.BestMatch"
                    ])
bot.storage.drop()

mosque = [
    "where is mosque?",
    "Drive straight from the UTP entrance gate and you can see the mosque",
    "where is annur?",
    "Drive straight from the UTP entrance gate and you can see the mosque"
]
greetings = [
    "Hi",
    "Hello",
    "Hi",
    "Hello",
    "Morning",
    "Good morning",
    "Afternoon",
    "Good afternoon",
    "Thank you",
    "My pleasure",
    "Assalamualaikum",
    "Waalaikumsalam",
    "Bye",
    "Have a nice day",
    " ?",
    "Sorry, I cant understand. Please ask more specifically."
    " ?",
    "Where do you want to go?",
    " ?",
    "How can i help you? Are you looking for cafe, mosque or RV?"
]
cafeQuest = [
    "How many cafes are there in UTP?",
    "There are 11 cafes available in UTP such as V1 V2 V3 V4 V5 V6 Cafe Sayang Pocket C Al-Marjan TEEPEE Cafe Pocket D",
    "Usual operation hours for cafes?",
    "Most cafes are available starting from 7:00AM till 12:00PM",
    "V1 cafe",
    "V1 cafe is located near UTP bus station",
    "V4 cafe location",
    "V4 cafe is located near UTP post office station",
    "V2 cafe menu for today",
    "There are roti canai, nasi lemak, mee goreng and more!",
    "The nearest cafe around Block K?",
    "Nearest cafe around Block K are Cafe Sayang & Al-Marjan",
    "Cafe that sell pizza?",
    "V1 cafe are selling various types of pizza Lets give a visit!"
]
rv = [
    "How many RV?",
    "There is 6 RV in UTP",
    "What is hotline number for RV?",
    "This is it: 011-21542918",
    "Where is V5 RV?",
    "Above V5 Cafe near V5E (man) or V5A (woman) block",
    "Where is V6 RV?",
    "Block number 2 in V6 area",
    "Where is V4 RV?",
    "Near V4 cafe and in front of poslaju utp",
    "Where is V3 RV?",
    "Above of V3 cafe",
    "Where is V2 RV?",
    "Need to go to V5 RV. Above V5 Cafe near V5E (man) or V5A (woman) block",
    "Where is V1 RV?",
    "Need to go to V5 RV. Above V5 Cafe near V5E (man) or V5A (woman) block",
    "Where to pick parcel?",
    "Poslaju UTP located in front of V4 Cafe and beside V4 mart",
    "Where can I drop my key?",
    "You can drop to RV that you stay",
    "Working hours for poslaju?",
    "From monday to friday, 10 am until 4 pm",
    "Do poslaju avail on weekend?",
    "No, poslaju only avail during weekdays",
]
sport_facility = [
    "Where can I play badminton?",
    "At block A, block A is in front Masjid An Nur",
    "Where can I swim?",
    "You can go to pool in front Masjid An'Nur",
    "Where can I play Futsal",
    "We have Futsal court at village 5 and at block A",
    "Gym Utp",
    "You can find our gym at curriculum block",
    "Where can I play football?",
    "We have 3 fields that you can reach from UTP's Gate",
    "UTP have Kayak sport?",
    "You can play Kayak at Oval Park",
    "Oval Park",
    "Anyone can jog or picnic at Oval Park",
    "Is there any squash court?",
    "We do have squash court at Block A",
    "When can I enter swimming pool?",
    "Monday is for male, Tuesday is for female and continue"
]

trainer = ListTrainer(bot)
for items in (greetings, mosque, cafeQuest, rv, sport_facility, conversation):
    trainer.train(items)

# corpus_trainer = ChatterBotCorpusTrainer(bot)
# corpus_trainer.train("chatterbot.corpus.english")

trainer.export_for_training('./my_export.json')


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
