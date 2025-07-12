from datetime import datetime

from flask import Flask, render_template,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm
from config import SECRET_KEY

app = Flask(__name__,template_folder='templates',static_folder='static')
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.image_file}')" 


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
posts = [
    {
        'author' : 'Felipe aa',
        'title' : 'How to become a modern python dev',
        'date'   : '2025-07-02',
        'content': 'lore ipsum'
    },
    {
        'author' : 'Lorrayne',
        'title' : 'Fisioterapy Studies',
        'date'   : '2025-07-02',
        'content': 'blablablabla'
    },
    {
        'author' : 'Jefferson',
        'title' : 'Science',
        'date'   : '2025-01-02',
        'content': 'U have to study science'
    }

]

@app.route('/')
def home():
    return render_template('home.html', posts=posts,title='Homepage')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash(f'Login requested for {form.username.data}')
        return redirect(url_for('home'))

    return render_template('login.html',form=form,title='Sign In')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)