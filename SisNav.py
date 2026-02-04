
class NavegadorWeb:
    def __init__(self):
        # Se inicializa back_stack y forward_stack como listas vacías 
        self.paginasAnteriores = []
        self.paginasSiguientes = []

        #Se inicializa como 'None' dado que no hay una página actual
        self.paginaActual = None

#Carga una nueva página
    def loadPage(self, url):
        # Si no es la primera página, se agrega a la pila de páginas anteriores
        if self.paginaActual is not None:
            #Se agrega la página actual a la pila de páginas anteriores
            self.paginasAnteriores.append(self.paginaActual)
        
        #Se actualiza la página actual
        self.paginaActual = url
        self.paginasSiguientes.clear()
        print(f"Navegando a.......{self.paginaActual}")

#Regresa a la página anterior
    def goBack(self):
        # Si no hay páginas anteriores, se muestra un mensaje
        if not self.paginasAnteriores:
        
            print("No hay paginas anteriores")
            return

        self.paginasSiguientes.append(self.paginaActual)
        self.paginaActual = self.paginasAnteriores.pop()

        print(f"Regresando a.......{self.paginaActual}")
# Avanza a la página siguiente
    def goForward(self):
# Si no hay páginas siguientes, se muestra un mensaje
        if not self.paginasSiguientes:
            print("No hay paginas siguientes")
            return
# Se agrega la página actual a la pila de páginas anteriores
        self.paginasAnteriores.append(self.paginaActual)
        self.paginaActual = self.paginasSiguientes.pop()

        print(f"Avanzando a.......{self.paginaActual}")

if __name__ == "__main__":
    
    firefox = NavegadorWeb()
    
    print("BIENVENIDO A FIREFOX")
    print("----------------------")
    
    firefox.loadPage("google.com")
    firefox.loadPage("youtube.com")
    firefox.loadPage("facebook.com")
    firefox.loadPage("instagram.com")
    firefox.loadPage("x.com")

   
    print("Regresando a la pagina anterior")
    firefox.goBack()
    firefox.goBack()
    
    print("Avanzando a la pagina siguiente")
    firefox.goForward()
    firefox.goForward()
 
    
    print("Probando Nueva Ruta")
    firefox.loadPage("discord.com")

    print("Avanzado Fallido")
    firefox.goForward()