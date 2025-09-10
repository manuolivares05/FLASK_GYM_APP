from datetime import date
from app import db

class Entrenamiento(db.Model):
    __tablename__ = "entrenamientos"

    id = db.Column(db.Integer, primary_key=True)
    grupo_muscular_id = db.Column(db.Integer, db.ForeignKey("grupos_musculares.id"))
    ejercicio_id = db.Column(db.Integer, db.ForeignKey("ejercicios.id"))
    fecha = db.Column(db.Date, default=date.today, nullable=False)
    repeticiones = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float)
    # Relaciones
    grupo_muscular = db.relationship("GrupoMuscular", back_populates="entrenamientos")
    ejercicio = db.relationship("Ejercicio", back_populates="entrenamientos")
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    # Relación inversa
    usuario = db.relationship("Usuario", back_populates="entrenamientos")

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "grupo_muscular": self.grupo_muscular.nombre if self.grupo_muscular else None,
    #         "ejercicio": self.ejercicio.nombre if self.ejercicio else None,
    #         "fecha": self.fecha.isoformat(),
    #         "repeticiones": self.repeticiones,
    #         "peso": self.peso,
    #     }
