#Evaluacion 1 - Calculadora de Enteros
#Realizado por: Ubeimar Lizardo Yepes Portilla
#Fecha: 06/10/2023
#Version 0.1

class Calculadora:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def obtener_valores(self):
        try:
            self.valor1 = int(input("Ingrese el primer valor entero: "))
            self.valor2 = int(input("Ingrese el segundo valor entero: "))
            self.resultado = 0  # Reiniciar el resultado a cero
            
        except ValueError:
            print("Por favor, ingrese valores enteros válidos.")

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 == 0:
            return "Error: No se puede dividir por cero, Intente nuevamente"
        return self.valor1 / self.valor2

# Crear una instancia de la clase Calculadora
mi_calculadora = Calculadora()
mi_calculadora.obtener_valores()

# Realizar operaciones e imprimir resultados
print(f"La Suma es: {mi_calculadora.suma()}")
print(f"La Resta de los valores es: {mi_calculadora.resta()}")
print(f"La Multiplicación es: {mi_calculadora.multiplicacion()}")
print(f"La División de los valores dados es: {mi_calculadora.division()}")
