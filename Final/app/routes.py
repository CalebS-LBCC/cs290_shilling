from ctypes import sizeof
from flask import redirect, render_template, request, session, url_for
from app import app
from app.forms import LandingForm

# Loading the main page will load the state of all files in the shopping_items directory
@app.route('/')
def start():
    # Set the value that determines if the last page was a successful search
    session['search'] = 0

    # Reset the cart array
    session["cart"] = []

    # Load items from a file into their respective arrays
    session['items'], session['prices'] = load_items()
    
    # Redirect to the main page
    return redirect("/landing")

# This script loads the main page of the website
@app.route('/landing')
def land():
    # Determines the size of the cart
    size = len(session["cart"])
    
    form = LandingForm()
    if session['search'] == 0:
        # If we are not coming back from a search, load the page as normal
        session['search'] = 0
        return render_template('landingpage.html', title='Landing Page', items=session['items'], prices=session['prices'], cart_size=size, form=form)
    else:
        # If we are coming back from a search, only display the identified items
        session['search'] = 0
        return render_template('landingpage.html', title='Landing Page', items=session['items_match'], prices=session['prices_match'], cart_size=size, form=form)

# Adds a product to the cart
@app.route('/add', methods = ['POST'])
def add_to_cart():

    cart = session["cart"]
    cart.append(request.form['clone_link'])
    session["cart"] = cart

    # Redirects back to the main page
    return redirect("/landing")

# Performs the search and returns the results to the landing page
@app.route('/search', methods = ['POST'])
def search():

    session['items_match'], session['prices_match'] = match_items(request.form['sf'])
    
    # Basic input validation: if all inputs match or no results are provided ignore the search
    if len(session['items_match']) == 0 or len(session['items_match']) == len(session['items']):
        session['search'] = 0
    else:
        session['search'] = 1

    # Return to the main page
    return redirect("/landing")

def load_items():
   
    path = "shopping_items.txt"
    line_num = 0
    names = []
    prices = []

    with open(path, 'r') as file:
        for line in file:
            if line_num % 2 == 0:
                names.append(line)
            else:
                prices.append(line)
            line_num = line_num + 1

    return names, prices


def match_items(phrase):

    # I would argue this could be considered a form of input validation:
    # Checking if the string is contained in anything else.

    path = "shopping_items.txt"
    potential_matches = []
    line_num = 0
    matches = []
    prices = []
    match = 0

    with open(path, 'r') as file:
        for line in file:
            if line_num % 2 == 0:
                potential_matches.append(line)
                match = 1
            elif match == 1:
                match = 0
                prices.append(line)
            line_num = line_num + 1

    for item in potential_matches:
        # Check if the current word is equal to or greater in length
        # than the fragment
        if len(item) >= len(phrase):
            # If the first n characters are equal to the n characters of the
            # input fragment add the full word to the list of found matches
            # https://www.programiz.com/python-programming/methods/string/lower
            if item[0:len(phrase)].lower().__eq__(phrase.lower()): 
                matches.append(item)
    
    return matches, prices
