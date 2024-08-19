class ArticuloPapeleria:
   def __init__(self, tipo, especificacion, costo_base):
       self.tipo = tipo
       self.especificacion = especificacion
       self.costo_base = costo_base
       self.marca = self.asignar_marca()
       self.precio_final = self.calcular_precio_final()
   def asignar_marca(self):
       if self.tipo == "cuaderno":
           return "HOJITAS"
       elif self.tipo == "lapiz":
           return "RAYAS"
       else:
           return "Desconocida"
   def calcular_precio_final(self):
       return self.costo_base * 1.30
   def obtener_informacion(self):
       detalles = [
           f"Tipo: {self.tipo.capitalize()}",
           f"Especificación: {self.especificacion}",
           f"Marca: {self.marca}",
           f"Costo Base: ${self.costo_base:.2f}",
           f"Precio Final: ${self.precio_final:.2f}"
       ]
       return detalles

class Papeleria:
   def __init__(self):
       self.inventario = []  # Lista para almacenar los artículos
   def agregar_articulo(self):
       tipo = input("Ingrese el tipo de artículo (cuaderno/lapiz): ").lower()
       if tipo not in ["cuaderno", "lapiz"]:
           print("Tipo de artículo no válido.")
           return
       if tipo == "cuaderno":
           especificacion = input("Ingrese la cantidad de hojas (50/100): ")
           if especificacion not in ["50", "100"]:
               print("Cantidad de hojas no válida. Debe ser 50 o 100.")
               return
       elif tipo == "lapiz":
           especificacion = input("Ingrese el tipo de lápiz (grafito/colores): ").lower()
           if especificacion not in ["grafito", "colores"]:
               print("Tipo de lápiz no válido. Debe ser grafito o colores.")
               return
       costo_base = float(input("Ingrese el costo base del artículo: "))
       articulo = ArticuloPapeleria(tipo, especificacion, costo_base)
       self.inventario.append(articulo)
       print(f"\nEl {tipo} ha sido registrado con éxito.\n")
   def mostrar_inventario(self):
       if not self.inventario:
           print("No hay artículos registrados.\n")
       else:
           print("Artículos registrados:\n")
           for articulo in self.inventario:
               for detalle in articulo.obtener_informacion():
                   print(detalle)
               print("")  # Espacio entre artículos

# Ejemplo de uso
papeleria = Papeleria()
while True:
   print("1. Agregar un artículo")
   print("2. Mostrar todos los artículos")
   print("3. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       papeleria.agregar_articulo()
   elif opcion == "2":
       papeleria.mostrar_inventario()
   elif opcion == "3":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")