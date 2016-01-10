

from flask.ext.script import Command, prompt

from evepilots.capsuleers.utils import update_multiple_capsuleers, load_capsuleers_file


class UpdateExistingCapsuleers(Command):
    """ Triggers the updating of capsuleers from the CLI. """

    def run(self):
        quantity = int(prompt('Quantity to update: '))
        update_multiple_capsuleers(quantity)


class LoadCapsuleers(Command):
    """ Loads capsuleers from a given file to the DB. """

    def run(self):
        file_path = prompt('File Path: ')

        load_capsuleers_file(file_path)
