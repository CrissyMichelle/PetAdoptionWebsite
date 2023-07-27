from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptapet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config["SECRET_KEY"] = "ohRight.shh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def home_page():
    """The home page lists the pets"""
    pets = Pet.query.all()
    return render_template("/home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Shows form for adding a pet and handles form submission"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added pet {name} the {species}!")
        return redirect("/")
    else:
        return render_template("add.html", form = form)

@app.route("/<int:pet_id_number>", methods=["GET", "POST"])
def edit_pet(pet_id_number):
    """Shows deets for given pet and handles edit deets form"""
    pet = Pet.query.get_or_404(pet_id_number)
    form = EditPetForm()

    if form.validate_on_submit():
        if not form.photo_url.data:
            pet.photo_url = pet.photo_url
        else:
            pet.photo_url = form.photo_url.data
        if not form.notes.data:
            pet.notes = pet.notes
        else:
            pet.notes = form.notes.data
            
        pet.available = form.available.data            
            
        db.session.commit()

        flash(f"Updated pet {pet.name} the {pet.species}!")
        return redirect(f"/{pet.id}")
    else:
        return render_template("/[pet-id-number].html", pet=pet, form=form)