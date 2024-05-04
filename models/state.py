#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel):
    """ State class """
    # name = ""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
