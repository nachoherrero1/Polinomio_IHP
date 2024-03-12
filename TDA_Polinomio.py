class Nodo:
    def __init__(self):
        self.info = None
        self.sig = None

def TDA_Polinomio():
    aux = Nodo()
    aux.info = "Primer nodo"
    palabra = input('Ingrese una palabra: ')
    naux = aux
    while palabra != "":
        nodo = Nodo()
        nodo.info = palabra
        naux.sig = nodo
        naux = nodo
        palabra = input('Ingrese una palabra: ')

    while aux is not None:
        print(aux.info)
        aux = aux.sig

TDA_Polinomio()

polinomio1 = TDA_Polinomio()
polinomio2 = TDA_Polinomio()

class datoPolinomio (object):
    """Clase dato polinomio."""
   
    def_init_(self, valor, termino):
        """Crea un dato polinomio con valor y termino."""
        self.valor=valor
        self.termino=termino
    
class Polinomio (object):
    """Clase polinomio."""

    def _init_ (self):
        """Crea un polinomio del grado cero."""
        self.termino_mayor = None
        self.grado=-1