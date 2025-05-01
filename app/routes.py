from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Task

main = Blueprint('main', __name__)

# Strona główna z formularzem
@main.route('/')
def index():
    tasks = Task.query.all()  # Pobieramy wszystkie zadania z bazy danych
    return render_template('index.html', tasks=tasks)

# Obsługa dodawania zadania
@main.route('/add', methods=['POST'])
def add_task():
    task_description = request.form['task']  # Pobieramy dane z formularza
    new_task = Task(task=task_description)  # Tworzymy nowe zadanie (kolumna 'task' zamiast 'description')
    db.session.add(new_task)  # Dodajemy zadanie do sesji
    db.session.commit()  # Zatwierdzamy zmiany w bazie
    print(f'Zadanie dodane: {task_description}')  # Na razie tylko drukujemy w terminalu
    return redirect(url_for('main.index'))  # Po dodaniu zadania wracamy na stronę główną

# Obsługa usuwania zadania
@main.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task_to_delete = Task.query.get(id)  # Pobieramy zadanie po ID
    if task_to_delete:
        db.session.delete(task_to_delete)  # Usuwamy zadanie
        db.session.commit()  # Zatwierdzamy zmiany w bazie
    return redirect(url_for('main.index'))  # Po usunięciu zadania wracamy na stronę główną
