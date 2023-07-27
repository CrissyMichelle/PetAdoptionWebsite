from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange
from wtforms.widgets import TextArea

class AddPetForm(FlaskForm):
    """Form for adding pets."""
    @property
    def iterables(self): 
        return[self.pet_name, self.species, self.photo_url]
    
    pet_name = StringField("pet name", validators=[InputRequired()])
    species = SelectField("species", validators=[InputRequired()],
                          choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("photo", validators=[Optional(), URL()])
    age = IntegerField("age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing some pet details."""
    photo_url = StringField("photo", validators=[Optional(), URL()])
    notes = StringField("notes", validators=[Optional()])
    available = BooleanField("available?", validators=[Optional()])