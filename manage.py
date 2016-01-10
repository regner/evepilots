

from flask.ext.script import Manager, Server, prompt_bool
from flask.ext.migrate import MigrateCommand

from evepilots.app import create_app
from evepilots.extensions import db
from evepilots.capsuleers.scripts import UpdateExistingCapsuleers, LoadCapsuleers
from evepilots.corporations.scripts import UpdateExistingCorporations

app = create_app()
manager = Manager(app)

@manager.command
def drop_db():
    if prompt_bool('Are you sure you want to lose all your data!?'):
        db.drop_all()

manager.add_command("runserver", Server("localhost", port=8000))
manager.add_command("runserver_c9", Server("0.0.0.0", port=8080))
manager.add_command('db', MigrateCommand)
manager.add_command('update_capsuleers', UpdateExistingCapsuleers())
manager.add_command('load_capsuleers', LoadCapsuleers())
manager.add_command('update_corporations', UpdateExistingCorporations())

if __name__ == "__main__":
    manager.run()
