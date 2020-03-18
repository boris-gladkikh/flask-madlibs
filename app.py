from flask import Flask, request,render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html",
    prompts = story.prompts
    )

@app.route("/story")
def generate_story():

    return render_template("story.html",
    text = story.generate(request.args)
    )



