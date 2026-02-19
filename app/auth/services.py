from app.auth.models import Usuario

def autenticar_usuario(username, password):
    usuario = Usuario.query.filter_by(username=username, activo=True).first()
    
    if usuario and usuario.check_password(password):
        return usuario
    
    return None
