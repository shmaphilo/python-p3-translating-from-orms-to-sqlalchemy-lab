from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

def create_table(Base):
    engine = create_engine('sqlite:///dogs.db')
    Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()

engine = create_engine('sqlite:///dogs.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_dog = Dog(name='Fido', breed='Labrador')
save(session, new_dog)

all_dogs = get_all(session)
for dog in all_dogs:
    print(f"ID: {dog.id}, Name: {dog.name}, Breed: {dog.breed}")

found_dog = find_by_name(session, 'Fido')
if found_dog:
    print(f"Found dog with ID {found_dog.id}: {found_dog.name}, {found_dog.breed}")

update_breed(session, found_dog, 'Golden Retriever')
print(f"Updated breed to: {found_dog.breed}")
