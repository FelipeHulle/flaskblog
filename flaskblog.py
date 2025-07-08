from flask import Flask, render_template

app = Flask(__name__,template_folder='templates',static_folder='static')

posts = [
    {
        'author' : 'Felipe Hulle',
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
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)