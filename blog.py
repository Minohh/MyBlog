from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '096913adac12bc33ea241bd9874d7a39'

posts = [
    {
        'author': 'Minohh',
        'title': 'Blog Post',
        'content': 'First post content',
        'date': 'Apail 17th',
        'category': 'H.264'
    },
    {
        'author': 'Mino',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date': 'Apail 17th',
        'category': 'Linux'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
