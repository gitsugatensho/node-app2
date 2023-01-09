from flask import Flask, render_template

import random
#import emoji

app = Flask(__name__)

#static values
words = ['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'not', 'word', 'but', 'what', 'some', 'we', 'can', 'out', 'other', 'were', 'all', 'market', 'degree', 'populate', 'chick', 'dear', 'enemy', 'reply', 'drink', 'occur', 'support', 'speech', 'nature', 'range', 'steam', 'motion', 'path', 'liquid', 'log', 'meant', 'teeth', 'shell', 'neck']

@app.route('/')
def index():
    # choosing a random gif
    # numm = str(random.randint(1,16))
    imageurl = "https://www.gasta.org/wordpress/wp-content/uploads/2021/11/Anim0"+numm+"_dribbble.gif"
    # making user + comments                                                             
    comments = []
    for x in range(random.randint(2,6)):
        user = "User" + str(random.randint(0,9999))
        comment = ''
        comment = ' '.join([random.choice(words) for y in range(random.randint(2,9))])#+(' \U0001F602'*random.randint(0,4))
        #em = ' &#128514; ' * random.randint(0,4)
        #em = emoji.emojize(':joy:') * random.randint(0,4)
        amount = random.randint(0,4)
        comments.append([user, comment, amount])
    return render_template('index.html', url=imageurl, comments=comments)

if __name__ == "__main__": 
    app.run(host="0.0.0.0")
