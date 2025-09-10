from app import create_app, db
app = create_app()
app.app_context().push()


with app.app_context():
    from app.models import usuario, ejercicio, entrenamiento, grupo_muscular
    db.create_all()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)