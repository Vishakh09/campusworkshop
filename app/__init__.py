"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa94ak728r8862pdn0-a.oregon-postgres.render.com",
        database="todo_eg9q",
        user="todo_eg9q_user",
        password="apPK4qFk6oXsCySaIuVopo4WxxoVZlIw")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
