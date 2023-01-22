import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("MY_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        age = request.form["age"]
        user = request.form["user"]
        prompt = "Explain" + user + "to a" + age + "year old"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(prompt),
            temperature=0,
            max_tokens=3000,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(user):
    return """
User: {}
Explanation:""".format(
        user.capitalize()
    )
