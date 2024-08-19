from neo4j import GraphDatabase
from datetime import datetime
from neomodel import (StringProperty, 
                      IntegerProperty, 
                      DateTimeProperty,
                      UniqueIdProperty,
                      ZeroOrMore,
                      OneOrMore,
                      RelationshipTo,
                      UniqueIdProperty,
                      StructuredNode,
                      db,
                      config)

from configparser import ConfigParser

config_data = ConfigParser()
config_data.read('src/config_db.ini')

USERNAME = config_data['DATABASE_CREDENTIALS']['username']
PASSWORD = config_data['DATABASE_CREDENTIALS']['password']

config.DATABASE_URL = f'bolt://{USERNAME}:{PASSWORD}@localhost:7687'  # default

class User(StructuredNode):
    unique_id = UniqueIdProperty()
    username = StringProperty(unique_index=True, required=True)
    email = StringProperty(required=True)
    age = IntegerProperty()
    created_at = DateTimeProperty()
    updated_at = DateTimeProperty()


