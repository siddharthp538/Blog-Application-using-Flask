from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {
        'author':'Siddharth',
        'title':'Blogging woah',
        'content':'First blog ever',
        'date':'Jan 10, 2019'
    },
        {
            'author':'David',
            'title':'Travelling to India',
            'content':'How rich is India in terms of history',
            'date':'Jan 10, 2019'
        }
]

@app.route("/")
def hello():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html' , title='About')
