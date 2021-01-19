from flask import Flask
from flask import request
import random
app = Flask(__name__)

@app.route("/en")
def mainen():
    f = open("main.html", "r", encoding="UTF-8")
    temp = f.read()
    return temp.replace("{lang}", "en").replace("{chlang}", "<a href=\"/\">한글</a>").replace("{제출}", "submit")

@app.route("/")
def mainko():
    f = open("main.html", "r", encoding="UTF-8")
    temp = f.read()
    return temp.replace("{lang}", "ko").replace("{chlang}", "<a href=\"/en\">English</a>").replace("{제출}", "제출")

@app.route("/en/result")
def resulten():
    f = open("result.html", "r", encoding="UTF-8")
    temp = f.read()
    min = request.args.get("min", "0")
    max = request.args.get("max", "100")
    results = random.randrange(int(min), int(max))
    return temp.replace("{result}", f"{results}").replace("{lang}", "en").replace("{결과}", "result").replace("{새로고침}", "reload").replace("{새로 만들기}", "new").replace("{ch}", "en")

@app.route("/ko/result")
def resultko():
    f = open("result.html", "r", encoding="UTF-8")
    temp = f.read()
    min = request.args.get("min", "0")
    max = request.args.get("max", "100")
    results = random.randrange(int(min), int(max))
    return temp.replace("{result}", f"{results}").replace("{lang}", "en").replace("{결과}", "결과").replace("{새로고침}", "새로고침").replace("{새로 만들기}", "새로 만들기").replace("{ch}", "")



if __name__ == "__main__":
    app.run()