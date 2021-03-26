import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app import blueprint

# For manager to detect our models
from app.main.model import user, card, card_list, role, comment, blacklist

"""
create the application instance with the required parameter from the environment variable which can be 
either of the following - dev, prod, test. If none is set in the environment variable, the default dev is used.
"""
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.register_blueprint(blueprint)

app.app_context().push()

# expose  database migration commands through Flask-Script.
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
