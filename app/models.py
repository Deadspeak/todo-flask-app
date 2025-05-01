from . import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unikalny identyfikator
    task = db.Column(db.String(200), nullable=False)  # Treść zadania
    done = db.Column(db.Boolean, default=False)  # Status zadania (czy wykonane?)

    def __repr__(self):
        return f'<Task {self.task}>'
