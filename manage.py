import click
from flask_migrate import Migrate
from post_it_note import create_app, db

app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    from post_it_note.models import User, Note
    return dict(app=app, db=db, User=User, Note=Note)

@app.cli.command()
def deploy():
    from flask_migrate import upgrade
    upgrade()
    db.create_all()


if __name__ == '__main__':
    app.run()