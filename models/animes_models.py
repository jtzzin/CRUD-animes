from db import db
 
class Anime(db.Model):
    __tablename__ = 'animes'
 
    id= db.Column(db.Integer, primary_key=True)
    titulo= db.Column(db.String(100), nullable= False)
    genero= db.Column(db.String(100), nullable=False)
    estudio= db.Column(db.String, nullable=False)
    temporada= db.Column(db.String, nullable=False)
    
    
    
    
    
    def json(self):
        return {
            'id': self.id,          
            'titulo': self.titulo,    
            'genero': self.genero,
            'estudio': self.estudio,
            'temporada': self.temporada
        }