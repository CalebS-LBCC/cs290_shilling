from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Creates the structure for the search form
class LandingForm(FlaskForm):
    searchbar = StringField('', name="sf", validators=[DataRequired()])
    submit = SubmitField('Search')
    items = []
    prices = []
    cart_size = 0