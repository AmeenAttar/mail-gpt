import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("MY_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        user = request.form["user"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(user),
            temperature=0.3,
            max_tokens=3000,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(user):
    return """Pretend to be Taylor Swift, respond in her style.
User: {}
Taylor:""".format(
        user.capitalize()
    )
