from flask import Flask, render_template

import random

app = Flask(__name__)

# list of cat images
images = [
   "https://media0.giphy.com/media/tIeCLkB8geYtW/giphy.gif",
"https://media2.giphy.com/media/oOCbcGBJjlXJL8imGO/giphy.gif",
"https://media1.giphy.com/media/tY6gYNe4G0i2s/giphy.gif"]


@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
