from flask import redirect, render_template, request, session
from app import app
from app.forms import SearchForm

# Attempting to load the root page will redirect the user to the search page
@app.route('/')
def loadDict():
    # Tutorial on storing session variables in Flask:
    # https://pythonbasics.org/flask-sessions/
    session['wordlist'] = []
    return redirect("/search")

# Loads the search and display page
@app.route('/search')
def search():

    # Janky way to define Wordlist if it is not defined
    try:
        i = 0
        for word in session['wordlist']:
            i = i+1
    except:
        session['wordlist'] = []
        return redirect("/")

    # Create a search form to send to the browser
    form = SearchForm()
    return render_template('search.html', title='Search Dictionary', words=session['wordlist'], form=form)

# Searches the dictionary for matching words
@app.route('/look', methods = ['POST'])
def look():
    # Load the word from the search textbox
    word = request.form['sf']
    # Scan the dictionary for matching words
    session['wordlist'] = scanForWords(word)
    # Redirect the user to the search bar and display the output data
    return redirect('/search')

### Regular Python Code ###

# https://github.com/dwyl/english-words
path = "app/words.txt" 

def scanForWords(word):
    dictionary = []
    # Loop through the file recording each line as a word
    with open(path, 'r') as file:
        for line in file:
            dictionary.append(line)

    found_words = []
    for item in dictionary:
        # Check if the current word is equal to or greater in length
        # than the fragment
        if len(item) >= len(word):
            # If the first n characters are equal to the n characters of the
            # input fragment add the full word to the list of found matches
            # https://www.programiz.com/python-programming/methods/string/lower
            if item[0:len(word)].lower().__eq__(word.lower()): 
                found_words.append(item)
    return found_words
        

