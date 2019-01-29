class Persona(object):
    """
    """

    def __init__(self, n, ape, ed):
        """
        """
        self.nombre = n
        self.apellido = ape
        self.edad = int(ed)


    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad

    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)


    def obtener_apellido(self):
        """
        """
        return self.apellido

    def __str__(self):
        """
        """
        return "%s - %s - %d" % (self.nombre, self.apellido,self.edad)

class OperacionesArchivo(object):

    def __init__(self,):
        """
        """

    def Presentar(self, lista):
        for d in lista:
            p = Persona(d[0], d[1], d[2])
            print(p)

    def ListaEdad(self, lista):
        listaObj=[]
        listaEdad=[]
        for d in lista:
            p = Persona(d[0], d[1], d[2])
            listaObj.append(p)

        for d in listaObj:
            listaEdad.append(d.edad)
        return listaEdad
