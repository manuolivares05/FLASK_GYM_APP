from app.extensions import db

class GrupoMuscular(db.Model):
    __tablename__ = "grupos_musculares"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    # Relación con entrenamientos
    entrenamientos = db.relationship("Entrenamiento", back_populates="grupo_muscular")

    # def to_dict(self):
    #     return {"id": self.id, "nombre": self.nombre}
