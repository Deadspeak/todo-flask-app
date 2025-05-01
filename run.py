from app import create_app, db
from app.models import Task

app = create_app()

# Uruchomienie aplikacji i tworzenie bazy danych
with app.app_context():
    db.create_all()  # Tworzymy tabelę w bazie danych, jeśli nie istnieje

if __name__ == '__main__':
    app.run(debug=True, port=5001)
