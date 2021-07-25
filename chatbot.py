from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

botname = "PetroBot"
bot = ChatBot(
    botname,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation",
                    "chatterbot.logic.BestMatch"
                    ])

with open('file.txt', 'r') as file:
    conversation = file.read()

bot.storage.drop()

ignore_words = ["?", "!", "/"]


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
    "Where can I play Futsal?",
    "We have Futsal court at village 5 and at block A",
    "Where is Gym in Utp?",
    "You can find our gym at curriculum block",
    "Where can I play football?",
    "We have 3 fields that you can reach from UTP's Gate",
    "Do UTP have Kayak sport?",
    "You can play Kayak at Oval Park",
    "Where can I jog?",
    "Anyone can jog at Oval Park",
    "Where can I picnic?",
    "Anyone can picnic at Oval Park"
]
academic_block = [
    "Where is foundation block?",
    "It is located at Block I, J and K. In front of CETAL",
    "Where is IT/IS block?",
    "Located at Block 1 and Block 2, near the chancellor hall",
    "Where is civil engineering block?",
    "Near at pocket C",
    "Where is chemical engineering block?",
    "Located at Block 3 and Block 4",
    "Where is master student block?",
    "Located near at the back of chancellor hall, left side of gate 3",
    "Where is common exam hall located?",
    "Usually it will be located at Main Hall, Chancellor Hall, Undercroft or CETAL",
    "Where can I find security office?",
    "At Block O",
    "Is there any clinic in UTP?",
    "Yes, it is located at Pocket C named Klinik Redza and it operate 24 hours",
    "Where is library in UTP?",
    "It is called IRC (Information Resource Center) located in front of Chancellor Hall",
]

trainer = ListTrainer(bot)
for items in (greetings, mosque, cafeQuest, rv, sport_facility, conversation, academic_block):
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
