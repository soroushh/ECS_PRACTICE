from configparser import ConfigParser
import os

if __name__ == "__main__":
    parser = ConfigParser()
    parser.read('alembic.ini')
    parser.set(
        'alembic',
        'sqlalchemy.url',
        os.environ['DATABASE']
    )
    with open('alembic.ini', 'w') as configfile:
        parser.write(configfile)


