from app.extensions import db

class Ejercicio(db.Model):
    __tablename__ = "ejercicios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    musculo_principal = db.Column(db.String(50))

    # Relación con entrenamientos
    entrenamientos = db.relationship("Entrenamiento", back_populates="ejercicio")

    #NO LO USO POR QUE YA SERIALIZE EN MAPPING
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "nombre": self.nombre,
    #         "musculo_principal": self.musculo_principal,
    #     }
