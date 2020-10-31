from flask_migrate import Migrate, MigrateCommand
import logging
from logging.handlers import RotatingFileHandler

from project import create_app, db

app = create_app()
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

migrate = Migrate(app, db)
app.cli.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()
