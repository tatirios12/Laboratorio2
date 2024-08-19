class Vehiculo:
   def __init__(self, marca, modelo, categoria, color, motor, transmision, combustible, año, kilometraje, costo_adquisicion):
       self.ruedas = 4
       self.capacidad = 5
       self.marca = marca
       self.modelo = modelo
       self.categoria = categoria  # Nacional o Importado
       self.color = color
       self.motor = motor
       self.transmision = transmision
       self.combustible = combustible
       self.año = año
       self.kilometraje = kilometraje
       self.costo_adquisicion = costo_adquisicion
       self.precio_venta = self.calcular_precio_venta()
   def calcular_precio_venta(self):
       return self.costo_adquisicion * 1.4
   def mostrar_detalles(self):
       detalles = [
           f"Marca: {self.marca}",
           f"Modelo: {self.modelo}",
           f"Categoría: {self.categoria}",
           f"Color: {self.color}",
           f"Motor: {self.motor}",
           f"Transmisión: {self.transmision}",
           f"Combustible: {self.combustible}",
           f"Año: {self.año}",
           f"Kilometraje: {self.kilometraje} km",
           f"Costo de adquisición: ${self.costo_adquisicion:.2f}",
           f"Precio de venta: ${self.precio_venta:.2f}",
           f"Ruedas: {self.ruedas}",
           f"Capacidad: {self.capacidad} pasajeros"
       ]
       return detalles

class Agencia:
   def __init__(self):
       self.vehiculos = []  # Lista para almacenar los vehículos
   def agregar_vehiculo(self):
       marca = input("Ingrese la marca del vehículo: ")
       modelo = input("Ingrese el modelo del vehículo: ")
       categoria = input("Ingrese la categoría del vehículo (Nacional/Importado): ")
       color = input("Ingrese el color del vehículo: ")
       motor = input("Ingrese el tipo de motor (Ej. V6, V8, etc.): ")
       transmision = input("Ingrese el tipo de transmisión (Manual/Automática): ")
       combustible = input("Ingrese el tipo de combustible (Gasolina/Diésel/Eléctrico): ")
       año = input("Ingrese el año del vehículo: ")
       kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
       costo_adquisicion = float(input("Ingrese el costo de adquisición del vehículo: "))
       vehiculo = Vehiculo(marca, modelo, categoria, color, motor, transmision, combustible, año, kilometraje, costo_adquisicion)
       self.vehiculos.append(vehiculo)
       print(f"\nEl vehículo {marca} {modelo} ha sido registrado con éxito.\n")
   def mostrar_vehiculos(self):
       if not self.vehiculos:
           print("No hay vehículos registrados.\n")
       else:
           print("Vehículos registrados:\n")
           for vehiculo in self.vehiculos:
               for detalle in vehiculo.mostrar_detalles():
                   print(detalle)
               print("")  # Espacio entre vehículos
   def buscar_por_modelo(self):
       modelo_buscar = input("Ingrese el modelo del vehículo a buscar: ")
       encontrados = [vehiculo for vehiculo in self.vehiculos if vehiculo.modelo.lower() == modelo_buscar.lower()]
       if not encontrados:
           print(f"No se encontraron vehículos del modelo '{modelo_buscar}'.\n")
       else:
           print(f"Vehículos encontrados del modelo '{modelo_buscar}':\n")
           for vehiculo in encontrados:
               for detalle in vehiculo.mostrar_detalles():
                   print(detalle)
               print("")  # Espacio entre vehículos

# Ejemplo de uso
agencia = Agencia()
while True:
   print("1. Agregar un vehículo")
   print("2. Mostrar todos los vehículos")
   print("3. Buscar vehículos por modelo")
   print("4. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       agencia.agregar_vehiculo()
   elif opcion == "2":
       agencia.mostrar_vehiculos()
   elif opcion == "3":
       agencia.buscar_por_modelo()
   elif opcion == "4":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")