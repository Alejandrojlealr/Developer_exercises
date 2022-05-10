# Escribir una clase en python llamada círculo que contenga un radio, con un método que
# devuelva el área y otro que devuelva el perímetro del círculo.
# Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
# usuario e impidiendo la instanciación.
# Si printeamos el objeto creado debe mostrarse una representación amigable.
# El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
# mostrar un error y no permitir modificación.
# Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
# multiplicado por n. No permitir la multiplicación por números <= 0

PI = 3.14159

class Circulo():
    
    def __init__(self, radio):
        self.radio = radio
        
    
    def area_circulo(self):
        area = PI * self.radio ** 2
        print('El area del circulo es: ', round(area, 2), 'm\u00b2')
        
    def perimetro_circulo(self):
        perimetro = 2 * PI * self.radio
        print('El perimetro del circulo es: ', round(perimetro, 2), 'm')
        
radio = float(input('Introduzca el radio en metros: ', ))
while radio <= 0:
    print('Introduzca una valor mayor a', radio)
    radio = float(input('Por favor introduzca el radio nuevamente en metros : ', ))
if radio > 0:
    circulo1 = Circulo(radio)
    print(f'Este es el objeto creado: {circulo1}')
    circulo1.area_circulo()
    circulo1.perimetro_circulo()
    
numero = float(input('Introduzca un numero mayor a 0 para multiplicar por el radio del circulo anterior: ', ))
while numero <= 0:
    print('Introduzca una numero mayor a', numero)
    numero = float(input('Por favor introduzca un numero nuevamente  : ', ))
if numero > 0:
    circulo2 = Circulo(radio*numero)
    print(f'Este es otro objeto creado: {circulo2}')
    circulo2.area_circulo()
    circulo2.perimetro_circulo()

    
