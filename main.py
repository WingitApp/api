from neomodel import config 
from neo4j import GraphDatabase
from app.models import User
import logging, os
from neo4j.exceptions import ServiceUnavailable
from app import app
import uvicorn

print("Starting database...")
config.DATABASE_URL = os.environ["NEO4J_BOLT_URL"]
print(config.DATABASE_URL)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
