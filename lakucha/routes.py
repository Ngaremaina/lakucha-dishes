from lakucha import app
from flask import render_template
from lakucha.model import Foods
#define root page
@app.route('/')

#define home page
@app.route('/home')
def home_page():
	return render_template('home.html')

#define menu page
@app.route('/menu')
def menu_page():
    foods=Foods.query.all()
    return render_template('menu.html')

#define about page
@app.route('/about')
def about_page():
    return render_template('about.html')

#define privacy policy
@app.route('/policy')
def policy_page():
    return render_template('policy.html')

#define contact page
@app.route('/contact')
def contact_page():
    return render_template('contact.html')

#define register page
@app.route('/register')
def register_page():
    return render_template('register.html', form=form)