from .Usuario import Usuario, db

class Jardinero(Usuario):
    """Clase concreta para el tipo de usuario Jardinero."""
    def __init__(self, experiencia, empresa, id_usuario):
        super().__init__(id_usuario)
        self.experiencia = experiencia
        self.empresa = empresa
        # self.id_usuario = id_usuario
    

    def getClassName(self):
        return self.__name__
    
    def crear_usuario(self):
        db.insert(self.obtener_tipo(),[self.__dict__.values()])

    # Getters
    def getIdJardinero(self):
        result = db.select(
            columns=['id_jardinero'],
            table=self.obtener_tipo(),
            conditions={'id_usurio':self.id_usuario}
            )
        return result

    def getExperiencia(self):
        result = db.select(
            columns=[self.experiencia],
            table=self.obtener_tipo(),
            conditions={'id_usurio':self.id_usuario}
            )
        return result
    
    def getEmpresa(self):
        result = db.select(
            columns=[self.empresa],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        return result

    def getColumns(self):
        result = db.select(
            columns=['*'],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        return result
    
    # Setters
    def setExperiencia(self, experiencia):
        db.update(
            table=tabla,
            set_values=experiencia,
            conditions={'id_usurio':self.id_usuario}
            )
    
    def setEmpresa(self, empresa):
        db.update(
            table=tabla,
            set_values=empresa,
            conditions={'id_usurio':self.id_usuario}
            )
