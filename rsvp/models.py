from sqlalchemy import Column, String, Enum, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from wtforms.ext.sqlalchemy.orm import model_form


Base = declarative_base()


class RSVP(Base):
    __tablename__ = 'rsvps'
    id = Column(Integer, primary_key=True)
    guest_names = Column(Text, nullable=False)
    attending = Column(Enum('Yes', 'No', name='attending'), nullable=False)
    mailing_address = Column(Text)
    email = Column(String(50))
    food_preferences = Column(Enum('Vegan', 'None', name='food_preferences'), nullable=False)
    hotel = Column(Enum('Here', 'There', name='hotel'), nullable=False)
    notes = Column(Text)

RSVPForm = model_form(RSVP)
