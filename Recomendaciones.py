class SistemaRecomendacion:
    """
    Se encarga de guardar quién compró qué y de sugerir nuevos productos.
    """
    def __init__(self):
        # Aquí guardamos dos "diccionarios" (como agendas):
        
        # 1. compras: Para saber qué productos tiene cada usuario.
        self.compras = {}
        
        # 2. compradores: Para saber quiénes compraron un producto específico.
        self.compradores = {}

    def addPurchase(self, usuario, producto):
        """
        Esta función registra una compra.
        """
        
        # Registrar la compra en el historial del usuario ---
        # Si es la primera vez que el usuario compra algo, crear espacio
        if usuario not in self.compras:
            self.compras[usuario] = set()
        # Agregamos el producto a su lista de compras.
        self.compras[usuario].add(producto)

        if producto not in self.compradores:
            self.compradores[producto] = set()
        self.compradores[producto].add(usuario)
        
        print(f"Compra registrada: {usuario} compró {producto}")

    def getRecommendations(self, usuario):
        """
Se generan recomendaciones dependiendo de los productos que el usuario ya ha comprado.
        """
        
        # Si el usuario no ha comprado nada, no podemos recomendarle nada.
        if usuario not in self.compras:
            return []

        # Obtenemos los productos que ya tiene el usuario.
        mis_prod = self.compras[usuario]
        recomendaciones = set()

        # Recorremos cada producto que el usuario ya compró.
        for producto in mis_prod:
            # Buscamos a OTRAS personas que también compraron ese mismo producto.
            otros = self.compradores.get(producto, set())
            
            for otro_usuario in otros:
                if otro_usuario != usuario:
                    prod_otro = self.compras[otro_usuario]
                    recomendaciones.update(prod_otro)

        # Quitamos de las recomendaciones los productos que el usuario YA compró.
        finales = recomendaciones - mis_prod
        
        return list(finales)

if __name__ == "__main__":
    print("--- SISTEMA DE RECOMENDACIONES ---")
    
    # Creamos una 'instancia' o copia funcional de nuestro sistema.
    unilago = SistemaRecomendacion()

    unilago.addPurchase("Juan", "Laptop")
    unilago.addPurchase("Juan", "Mouse")

    unilago.addPurchase("Ana", "Laptop")
    unilago.addPurchase("Ana", "Mouse")
    unilago.addPurchase("Ana", "Cable HDMI")

    unilago.addPurchase("Pedro", "Monitor")

    print("\n--- GENERANDO RECOMENDACIONES ---")
    
    recos_juan = unilago.getRecommendations("Juan")
    print(f"Recomendaciones para Juan: {recos_juan}")

    recos_ana = unilago.getRecommendations("Ana")
    print(f"Recomendaciones para Ana:  {recos_ana}")

    recos_pedro = unilago.getRecommendations("Pedro")
    print(f"Recomendaciones para Pedro: {recos_pedro}")