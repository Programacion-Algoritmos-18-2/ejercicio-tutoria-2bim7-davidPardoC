import codecs


class MiArchivo:
    """
    """

    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/ejemplo.txt", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    """
    """

    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%d \n" % (p.nombre, p.apellido, p.edad))

    def cerrar_archivo(self):
        self.archivo.close()
