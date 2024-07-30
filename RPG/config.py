from dotenv import load_dotenv
import os

load_dotenv()  # this is a better practice, it takes environment variables from .env.


# Environment variables
class Config:  # BaseSettings reads variables itself without the need to use 'environ.get',
    # the name must match what it would look for
    APP_NAME = os.environ.get("APP_NAME", "Dice game")
    SECRET_KEY = os.environ.get("SECRET_KEY", "20B1FAC1B79B6BA380AB8297C6E0F4B6")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    #     os.path.abspath(os.path.dirname(__file__)), "database.sqlite"
    # ) # This creates a database locally in project files

    # This connects to a database that is hosted through postgres image in docker
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres"

# serialize / deserialize
# print(settings.model_dump())  # 'model_dump' turns class into a dictionary
# print(settings.model_dump_json())  # 'model_dump_json' turns class into string that JSON can process
