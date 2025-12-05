"""
MANEJO DE FUNCIONES EN PYTHON.

Las funciones son bloques de codigo que realizan tareas especificas, se reutilizan para evitar repetir codigo, y que sea mas 
facil de mantener y de organizar.

Los parámetros de la función son los que se colocan al definir la función.
Los argumentos son los valores que paasas a la funcion al llamarla.

Las funciones pueden albergar procesos logicos, y estos se utilizan para que el código sea mas facil de entender, y además se 
mantenga organizado.

En el presente arechivo se cubrirán ejercicios de manejo de funciones, todos los ejemplos contaran con instrucciones, desarrollo
del mismo y casos de prueba.
"""

"""
POBLEMA 1: Rectangle area and perimeter (basic functions).
Genera 2 funciones una para area y la otra para perimetro, y hay que mandarlas a llamar con valores ingresados por el usuario,
la unica validación solicitada es que los input no pueden ser menores a cero.
"""
while True:
    def calculate_area (b, h):
        return b * h
    def calculate_perimeter(b, h):
        return 2*(b+h)

    print("Rectangle.")
    base = int(input("Set the width: "))

    heigth = int(input("Set the heigth: "))

    if base <=0 or heigth <= 0:
        print("Invalid input.")
        break

    area = calculate_area(base, heigth)
    perimeter = calculate_perimeter(base, heigth)
    print("Area: ")
    print(area)
    print("Perimeter: ")
    print(perimeter)

    break
"""
CASOS DE PRUEBA:
- Normal .-
input: 4 / 2
Output: 8

- Borde .-
input: 3000 / 1500
Output: 4500000

- Error .-
input: -4 / -2
Output: Invalid input.
"""

"""
PROBLEMA 2: Grade classifier (function with return string).
Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
"A" si score >= 90, "B" si 80 <= score < 90, "C" si 70 <= score < 80, "D" si 60 <= score < 70, "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.
"""
def classify_grade (score):
    if score >= 90:
        return("Your grade is in A class.")

    elif 80 <= score and score < 90:
        return("Your grade is in B class.")

    elif 70 <= score and score < 80:
        return("Your grade is in C class.")
        
    elif 60 <= score and score < 70:
        return("Your grade is in D class.")

    elif score < 60:
        return("Your grade is in F class.")

score = int(input("Set your grade: "))
result = classify_grade(score)
print(result)
"""
CASOS DE PRUEBA:
- Normal .-
input: 80
Output: Your grade is in B class.

- Borde .-
input: 1
Output: Your grade is in F class.

- Error .-
input: -1
Output: Your grade is in F class.
"""

"""
PROBLEMA 3:  List statistics function (min, max, average).
Genera una funcion que reciba una lista de numeros y regrese un diccionario, con maximo, minimo y promedio.
input: lista de numeros
output: max, min, average.
"""
def summarize_numbers(numbers_list):
    summary = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return summary

numbers_text = input("Write your numbers separated by commas: ").strip()

if not numbers_text:
    print("Error: empty input")
else:
    parts = numbers_text.split(",")
    numbers_list = []

    try:
        for p in parts:
            num = float(p)
            numbers_list.append(num)

        if not numbers_list:
            print("Error: no numbers found")
        else:
            result = summarize_numbers(numbers_list)

            print("Min:", result["min"])
            print("Max:", result["max"])
            print("Average:", result["average"])

    except ValueError:
        print("Error: invalid input")
"""
CASOS DE PRUEBA:
- Normal .-
input: 22,22,33,45,20
Output:
Min: 20.0
Max: 45.0
Average: 28.4

- Borde .-
input: 100000000000000000, 1
Output:
Min: 1.0
Max: 1e+17
Average: 5e+16

- Error .-
input:  -21,33-45,87,-90,0.2
Output: 
Error: invalid input
""" 

"""
PROBLEMA 4: Apply discount list (pure function).
Define una función que reciba una lista de precios y una tasa de descuento, y retorne una nueva lista con el descuento aplicado 
sin modificar la lista original.

input.-
price_string 
discount_rate

output.-
original_prices
discount_prices

Tomar en cuenta que el input no pueden ser unicamente ceros
"""
def discount(prices, dis_int):
    example_list = prices.split(",")

    discounted_prices = []

    for x in example_list:
        num = float(x)
        disc_rate = dis_int / 100
        num_dis = num - (num * disc_rate)
        discounted_prices.append(num_dis)

    print(f"Your prices: {example_list}")
    print(f"Your discounted prices: {discounted_prices}")

prices = input("Set your prices separated by commas: ").strip()
dis_int = int(input("Set your discount rate: "))

discount(prices, dis_int)

"""
CASOS DE PRUEBA:

- Normal .-
input: 100,200,300 / 10
Output:
Your prices: ['100', '200', '300']
Your discounted prices: [90.0, 180.0, 270.0]

- Borde .-
input: 0.5,1,2  (descuento 10%)
Output:
Your prices: ['0.5', '1', '2']
Your discounted prices: [0.45, 0.9, 1.8]

- Error .-
input: hola,20,30
Output:
Error: invalid input
"""

"""
PROBLEMA 5: Greeting function with default parameters.
Define una función greet(name, title="") que:
Si title está vacío, solo usar el nombre. El código principal debe llamar a la función usando argumentos posicionales y nombrados.

Input: name, title (opcional)

output: "Greeting:" <greeting_message>

Validaciones:
- name no vacío tras strip().
- title puede estar vacío, pero si no lo está, también se normaliza con strip().
"""
def greeting(name, title): 
    if name == "":
        print("Not valid empty input.")
        return
    print (f"Hello {name.strip()} {title.strip()}")

name_int = input("Write your name: ")
title_int = input("your title: ")

final_print = (greeting(name_int, title_int))
"""
CASOS DE PRUEBA:

- Normal .-
input:
name: Juan / Sr.
Output:
Hello Juan Sr.

- Borde .-
input:
name: Ana
title:      (solo espacios)
Output:
Hello Ana

- Error .-
input:
name:     (vacío o solo espacios)
title: Profesor
Output:
Not valid empty input.
"""

"""
PROBLEMA 6: Factorial function (iterative or recursive).
Define una función factorial(n) que regrese n! (n factorial).
El código principal debe:

Leer/definir n.
Validar n.
Llamar a factorial(n).
Mostrar el resultado.

n debe ser mayor a cero.
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n_text = input("Enter n: ").strip()

try:
    n = int(n_text)
except:
    print("Error: invalid input (not an integer)")
    exit()

if n < 0:
    print("Error: n must be >= 0")
    exit()

fact_value = factorial(n)

print("n:", n)
print("Factorial:", fact_value)

"""
CASOS DE PRUEBA:

- Normal .-
input: 10
Output:
n: 10
Factorial: 3628800

- Borde .-
input: 1
Output:
n: 1
Factorial: 1

- Error .-
input: hola
Output:
Error: invalid input (not an integer)
"""

"""
CONCLUSIONES:
Las funciones son una herramienta que nos ayuda bastante a organizar y mantener nuestro código legible y ordenado, la cualidad de 
poder almacenar y reutilizar la lógica en un programa reduce considerablemente la carga de trabajao pues se tiene que escribir
menos utilizando bloques escritos previamente, asi mismo optimiza el tiempo ahorrando el tiempo de escribir multiples veces la
misma logica.
"""

"""
REFERENCIAS:
1)https://www.programiz.com/python-programming/function
2)https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions
3)https://recursospython.com/guias-y-manuales/funciones/
4) apuntes de la clase.
5) Ayuda de ChatGPT (OpenAI), 2025.
github link: https://github.com/AngelRuiz167/Tareas_python/edit/main/tuplas.py#L466C35
"""