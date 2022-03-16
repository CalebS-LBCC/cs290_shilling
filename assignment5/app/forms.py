from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Creates the structure for the search form
class SearchForm(FlaskForm):
    searchbar = StringField('', name="sf", validators=[DataRequired()])
    submit = SubmitField('Search')
    items = []