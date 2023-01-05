from flask import Flask, render_template

import random

app = Flask(__name__)

# list of cat images
numm = str(random.randint(0,8))
imageurl = "https://www.gasta.org/wordpress/wp-content/uploads/2021/11/Anim0"+numm+"_dribbble.gif"
                                                                
words = ['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'not', 'word', 'but', 'what', 'some', 'we', 'can', 'out', 'other', 'were', 'all', 'market', 'degree', 'populate', 'chick', 'dear', 'enemy', 'reply', 'drink', 'occur', 'support', 'speech', 'nature', 'range', 'steam', 'motion', 'path', 'liquid', 'log', 'meant', 'teeth', 'shell', 'neck']
comments = []
for x in range(random.randint(2,6)):
   comment = ''
   comment = ' '.join([random.choice(words) for y in range(random.randint(2,7))])+('&#128514;'*random.randint(0,4))
   comments.append(comment)


@app.route('/')
def index():
    return render_template('index.html', url=imageurl, comments=comments)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
