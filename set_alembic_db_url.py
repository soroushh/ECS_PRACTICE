from configparser import ConfigParser
import os

if __name__ == "__main__":
    parser = ConfigParser()
    parser.read('alembic.ini')
    parser.set(
        'alembic',
        'sqlalchemy.url',
        'postgresql://postgres:Kati8212579!@my-database.cvgmzutcx9w8.eu-west-1.rds.amazonaws.com/postgres'
    )
    with open('alembic.ini', 'w') as configfile:
        parser.write(configfile)


