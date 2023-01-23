import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("MY_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        recipient= request.form["recipient"]
        recipientPosition= request.form["recipientPosition"]
        sender= request.form["sender"]
        ##senderPosition= request.form["senderPosition"]
        reason = request.form["reason"]
        prompts = "Write a structured corporate email from "+ sender+ ", to " + recipient + ", who is a " + recipientPosition+ " stating" + reason 
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(prompts),
            temperature=0.8,
            max_tokens=4000,
        )
        print("?????????????????????????????????????????????????????????????????????????????????????")
        print (prompts)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(prompts):
    return """
User: {}
Mail:""".format(
        prompts.capitalize()
    )

