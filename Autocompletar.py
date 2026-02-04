class PTreeNode:
    """
    Esta clase representa un pequeño nodo o en el árbol de palabras.
Cada nodo actúa como una letra    """
    def __init__(self):
        self.hijo = {}
        
        self.fin_de_palabra = False

class AutocompletarSistema:
    """
    Se encarga de construir el árbol de palabras y de buscar sugerencias.
    """
    def __init__(self):
        # Creamos la raíz del árbol. El punto de partida vacío.
        self.root = PTreeNode()

    def insertar(self, palabra):
        """
        Esta función toma una palabra nueva y la guarda en el árbol letra por letra.
        """
        nodo = self.root
        
        for letra in palabra:
            # Si la letra no existe en los hijos del nodo actual, creamos un nuevo camino.
            if letra not in nodo.hijo:
                nodo.hijo[letra] = PTreeNode()
            # Avanzamos al siguiente nodo (la siguiente letra).
            nodo = nodo.hijo[letra]
            
        # Cuando terminamos todas las letras, marcamos el último nodo como "fin de palabra".
        # Así sabemos que hasta aquí hay una palabra válida.
        nodo.fin_de_palabra = True

    def Autocompletar(self, prefijo):
        
        nodo = self.root

        # --- PASO 1: Navegar hasta el final del prefijo ---
        # Primero bajamos por el árbol siguiendo las letras que el usuario ya escribió.
        for caracter in prefijo:
            # Si en algún momento no encontramos la letra, significa que ninguna palabra empieza así.
            if caracter not in nodo.hijo:
                return [] 
            nodo = nodo.hijo[caracter]
        
        #  hay que buscar todos los caminos que salen de aquí hacia abajo.
        resultados = []
        self._recorrer(nodo, prefijo, resultados)
        return resultados

    def _recorrer(self, nodo, palabra_actual, resultados):
        """
        Esta es una función auxiliar (recursiva) que explora todas las ramas hacia abajo.
        Es como un explorador que va por todos los caminos posibles recolectando palabras completas.
        """
        # Si el nodo actual está marcado como fin de palabra, la guardamos en la lista de resultados.
        if nodo.fin_de_palabra:
            resultados.append(palabra_actual)
        
        # Revisamos todos los hijos (las siguientes letras posibles).
        for letra, nodo_hijo in nodo.hijo.items():
            self._recorrer(nodo_hijo, palabra_actual + letra, resultados)

if __name__ == "__main__":
    print("BIENVENIDO AL SISTEMA DE AUTOCOMPLETAR")
    print("--------------------------------------")
    
    motor = AutocompletarSistema()
    
    palabras = ["auto", "automatico", "automovil", "autobus", "arbol", "avion", "gato"]
    print("Las palabras insertadas son: ", palabras)
    print("--------------------------------------")
    
    for palabra in palabras:
        motor.insertar(palabra)

    consulta = "auto"
    print(f"Buscando prefijo: '{consulta}'")
    print("Resultados:", motor.Autocompletar(consulta))

    consulta2 = "a"
    print(f"\nBuscando prefijo: '{consulta2}'")
    print("Resultados:", motor.Autocompletar(consulta2))

    consulta3 = "mp"
    print(f"\nBuscando prefijo: '{consulta3}'")
    print("Resultados:", motor.Autocompletar(consulta3))
    
    print("\nFIN DEL PROGRAMA")