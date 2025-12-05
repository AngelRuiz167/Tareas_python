"""
Alumno:Angel Gabriel Ruiz Torres, Matricula: 2530449, Grupo: 1-1

CRUD.

CRUD siglas de Create, Read, Update, Delete consiste en las 4 operaciones básicas que puede realizar un sistema.
Create.- crear nueva información o 'items' en el sistema.
Read.- Se refiere a visualizar o consultar la información o 'items' almacenados previamente en el sistema.
Update.- Actualizar o modificar información o 'items' preexistes.
Delete.- Eliminar información o 'items' del sistema.
"""
"""
GESTOR DE CRUD:
El siguiente gestor modifica elementos de una lista, 'x' y 'x' , es realizado a partir de lista pues solo requiere de 2 datos
 key: item].

 El programa costa de un ciclo que repite la seleccion de una accion add, search, delete, update, y exit
 estas acciones se realizan sobre un diccionario que almacena productos y precios, al seleccionar y realizar cada acción 
 retorna un mensaje que indica si se realizo de buena forma.
"""

inventary = {
    "Bread":2,
    "Soda":4,
    "Xbox":1000,
    "Alien":10000,
    }

#Bloques lógicos (funciones).

def adding(prod, price):
    inventary[prod] = price
    print("New item added sucesfully. ")

def searching (searched):
    if searched in inventary:
        print(searched)
        print("Price:")
        print(inventary[searched])
    else:
        print("Error: item not found.")

def deleting (deleted_p):
    removed = inventary.pop(deleted_p, None)
    if removed is None:
        print("Error: contact not found.")
    else:
        print(f"Deleted: {deleted_p} -> {removed}")

def updating (updated_p):
    if updated_p in inventary:
        print(updated_p)
        np = int(input("New price: "))
        inventary[updated_p] = np
        print(inventary[updated_p])
    else:
        print("Error: item not found.")

#Código del programa.
while True:
    print("What action do you wanna do? ")
    wanna = input("Add, Search, Delete, Update, Exit: ")
    wanna = wanna.lower()

    if wanna == "add":
        new_product = input("New item name: ").title()
        new_price = int(input("New item price: "))
        add_result = adding(new_product, new_price)
        continue

    if wanna == "search":
        searched_product = input("Name to search: ").title()
        search_result = searching(searched_product)
        continue

    if wanna == "delete":
        item_del = input("Contact for delete (name): ").title()
        del_result = deleting(item_del)
        continue

    if wanna == "update":
        item_update = input("Search a product to update price: ").title()
        update_result = updating(item_update)
        continue

    if wanna == "exit":
        print("Goodbye :)")
        break

    else:
        print("Ivalid action.")

# Casos de prueba (ADD)
"""
- Normal .-
input:
add
Milk
15
Output:
New item added successfully.

- Borde .-
input:
add
Pen
0
Output:
New item added successfully.

- Error .-
input:
add
Laptop
lol
Output:
Error: invalid input
"""

# Casos de prueba (SEARCH)
"""
- Normal .-
input:
search
Bread
Output:
Bread
Price:
2

- Borde .-
input:
search
bread
Output:
Error: item not found.

- Error .-
input:
search
UnknownItem
Output:
Error: item not found.
"""

# Casos de prueba (DELETE)
"""
- Normal .-
input:
delete
Soda
Output:
Deleted: Soda -> 4

- Borde .-
input:
delete
soda
Output:
Error: contact not found.

- Error .-
input:
delete
1234
Output:
Error: contact not found.
"""

# Casos de prueba (UPDATE)
"""
- Normal .-
input:
update
Xbox
1500
Output:
Xbox
1500

- Borde .-
input:
update
Xbox
0
Output:
Xbox
0

- Error .-
input:
update
Nintendo
Output:
Error: item not found.
"""

"""
CONCLUSIONES:
Crud al ser funciones basicas será algo con lo que siempre estaremos lidiando, por ende comprender como realizar
esas acciones básicas a estructuras de datos nos permitirá agilizar nuestro flujo de trabajo, y este se verá aun mas beneficiado
utilizando funciones para delegar unicamente bloques de lógica reusables a las acciones en el código.
"""

"""
REFERENCIAS:
1) https://docs.python.org/es/3.7/tutorial/datastructures.html
2) https://www.w3schools.com/python/python_lists.asp
3) Apuntes de la clase.
github link: https://github.com/AngelRuiz167/Tareas_python/edit/main/tuplas.py#L466C35
"""