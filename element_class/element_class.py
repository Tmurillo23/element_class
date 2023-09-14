from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre


class Conjuntos:
    contador: int

    def __init__(self, nombre: str):
        self.elementos: list[Elemento] = []
        self.nombre = nombre
        Conjuntos.contador += 1
        self.__id = Conjuntos.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return elemento.nombre in self.elementos

    def agregrar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, conjunto_a_unir: 'Conjuntos'):
        conjunto_nuevo = Conjuntos('Conjunto Unión')
        conjunto_nuevo.elementos = self.elementos.copy()
        for elementos in conjunto_a_unir.elementos:
            if not conjunto_nuevo.contiene(elementos):
                conjunto_nuevo.agregrar_elemento(elementos)

    def __add__(self, other):
        for i in range(len(self.elementos)):
            if self.elementos[i] in other.elementos:
                del other.elementos[i]

        return self.elementos + other.elementos

