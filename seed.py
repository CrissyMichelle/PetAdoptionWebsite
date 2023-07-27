"""Seed file to make sample data for adoptapet database"""
from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Create sample pet objects
fluffy = Pet(name="Fluffy", species="Rabbit", photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRelWVX4pJ8upbwceRWjSIu7AbxKDpDwIKMTuPbujOyfazZWf0XX2Jtj3ttu6uHf9gJSp8&usqp=CAU")
ralph = Pet(name="Ralphie", species="Turtle", photo_url="https://media.kare11.com/assets/KARE/images/181c35aa-0a7e-40d4-8ff6-ae283bb14ef8/181c35aa-0a7e-40d4-8ff6-ae283bb14ef8_1140x641.jpg",
            age=56, notes="Tortoises can live up to 100 years or more!")
liam = Pet(name="Liam", species="Dog", photo_url="https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcS27hGq-bwiNWm2LX2R_gcwfQEidoPMtMsZW3Tp6D3QeiN7Elxrue-AN-XunFIFZFFj5-6Ou_aJEvfRS08",
           age=4)
cali = Pet(name="Cali", species="Cat", photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReJmHseQBIPmA1oyLWlUrRwPiKBWW1YqUzQw&usqp=CAU",
           age=1)
tal = Pet(name="Tal", species="Hedgehog", photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGImAHUmVKEH2r9rsYkJj_Yaa6-3DMRg76Sg&usqp=CAU")
sal = Pet(name='Sally', species='Dog', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAFK8XH-zXSWAIDeGs5E0oboBLapmnGAsXqOkXf3kMc8qLKOVXxkaotglX8vajkdfe1rI&usqp=CAU',
          age=6)
whisk = Pet(name='whiskers', species='Cat', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAfWWIjgaKiPb7NrJApJJCgydX1GL7-EUa8w&usqp=CAU',
            age=22, notes="she's purrty", available = False)

# Add and commit pets
db.session.add(fluffy)
db.session.add(ralph)
db.session.add(liam)
db.session.add(cali)
db.session.add(tal)
db.session.add(sal)
db.session.add(whisk)

db.session.commit()