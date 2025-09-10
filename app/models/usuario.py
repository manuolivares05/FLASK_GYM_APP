from app.extensions import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=True)
    password  = db.Column(db.String(255), nullable=False)  # hashed en lo posible

    
    # Relación: un usuario puede tener muchos entrenamientos
    entrenamientos = db.relationship("Entrenamiento", back_populates="usuario", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
        }
