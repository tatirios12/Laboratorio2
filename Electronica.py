class Electronico:
   def __init__(self, categoria, marca, modelo, color, almacenamiento, procesador, costo_adquisicion):
       self.categoria = categoria    # Celular, Tablet, o Laptop
       self.marca = marca            # En este caso, siempre será PHR
       self.modelo = modelo
       self.color = color
       self.almacenamiento = almacenamiento  # Memoria RAM o almacenamiento
       self.procesador = procesador
       self.costo_adquisicion = costo_adquisicion
       self.precio_venta = self.calcular_precio_venta()
   def calcular_precio_venta(self):
       return self.costo_adquisicion * 1.7
   def obtener_detalles(self):
       detalles = [
           f"Categoría: {self.categoria}",
           f"Marca: {self.marca}",
           f"Modelo: {self.modelo}",
           f"Color: {self.color}",
           f"Almacenamiento: {self.almacenamiento}",
           f"Procesador: {self.procesador}",
           f"Costo de adquisición: ${self.costo_adquisicion:.2f}",
           f"Precio de venta: ${self.precio_venta:.2f}"
       ]
       return detalles

class Inventario:
   def __init__(self):
       self.electronicos = []  # Lista para almacenar los electrónicos
   def agregar_electronico(self):
       categoria = input("Ingrese la categoría del electrónico (Celular/Tablet/Laptop): ")
       marca = "PHR"  # Marca fija para todos los electrónicos
       modelo = input("Ingrese el modelo del electrónico: ")
       color = input("Ingrese el color del electrónico: ")
       almacenamiento = input("Ingrese el almacenamiento del electrónico (Ej. 4GB RAM, 128GB almacenamiento): ")
       procesador = input("Ingrese el procesador del electrónico: ")
       costo_adquisicion = float(input("Ingrese el costo de adquisición del electrónico: "))
       electronico = Electronico(categoria, marca, modelo, color, almacenamiento, procesador, costo_adquisicion)
       self.electronicos.append(electronico)
       print(f"\nEl electrónico {modelo} ha sido registrado con éxito.\n")
   def mostrar_electronicos(self):
       if not self.electronicos:
           print("No hay electrónicos registrados.\n")
       else:
           print("Electrónicos registrados:\n")
           for electronico in self.electronicos:
               for detalle in electronico.obtener_detalles():
                   print(detalle)
               print("")  # Espacio entre electrónicos

# Ejemplo de uso
inventario = Inventario()
while True:
   print("1. Agregar un electrónico")
   print("2. Mostrar todos los electrónicos")
   print("3. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       inventario.agregar_electronico()
   elif opcion == "2":
       inventario.mostrar_electronicos()
   elif opcion == "3":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")