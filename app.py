from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddSnackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/snacks/new' , methods=["GET" , "POST"])
def add_snack_form():
    form = AddSnackForm() # name of the class in form.py

    if form.validate_on_submit():
        name = form.name.data  # in flask i tis equilavent to request.form['name']
        price = form.price.data
        flash(f'Added new snack: Snack name:{name} with price ${price}')
        return redirect ('/')
    else:
        return render_template('add_snack.html' , form=form)


