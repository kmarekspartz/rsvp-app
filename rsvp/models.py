from sqlalchemy import Column, String, Enum, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from wtforms.ext.sqlalchemy.orm import model_form


Base = declarative_base()


class RSVP(Base):
    __tablename__ = 'rsvps'
    id = Column(Integer, primary_key=True)
    guest_names = Column(Text, nullable=False)
    attending = Column(Enum(name='attending', 'Yes', 'No'), nullable=False)
    mailing_address = Column(Text)
    email = Column(String(50))
    food_preferences = Column(Enum(name='food_preferences','Vegan', 'None'), nullable=False)
    hotel = Column(Enum(name='hotel', 'Here', 'There'), nullable=False)
    notes = Column(Text)

RSVPForm = model_form(RSVP)
