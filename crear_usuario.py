from app import create_app, db
from app.auth.models import Usuario

app = create_app()

with app.app_context():
    db.create_all()  # Crea las tablas en la base de datos


    existe = Usuario.query.filter_by(username='admin').first()

    if not existe:
        u = Usuario(username='admin', nombre='Administrador', rol='admin')
        u.set_password('admin123')  # Establece la contraseña

        db.session.add(u)
        db.session.commit()

        print("Usuario 'admin' creado correctamente.")
    else:
        print("El usuario 'admin' ya existe.")