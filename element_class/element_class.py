from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre


class Conjuntos:
    contador: int = 0

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

    @classmethod
    def intersectar(cls, conjunto1: 'Conjuntos', conjunto2: 'Conjuntos'):
        nuevo_conjunto = cls(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in conjunto1.elementos:
            if conjunto1.contiene(elemento) and conjunto2.contiene(elemento) and not nuevo_conjunto.contiene(elemento):
                nuevo_conjunto.agregrar_elemento(elemento)

    def __str__(self):
        elementos_nombre = ', '.join(elemento.nombre for elemento in self.elementos)
        return f"{self.nombre}: {elementos_nombre}"
