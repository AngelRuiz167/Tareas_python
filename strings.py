"""
Alumno: Angel Gabriel Ruiz Torres Matricula: 2530449, Grupo: 1-1.

Manejo de strings en python.

En el presente archivo se busca comprender el uso de strings en python y las acciones que podemos realizar con esto
cosas como crear, leer, concatenar, indexación, slicing, búsqueda, reemplazo, división, unión y formato de texto.

¿Qué es un string?
en pocas palabras un string es cualquier caracter que se encuentre entre comillas (" "), y este valor cuenta con acciones u 
operaciones a las que se puede someter.

Podemos alterar el tipo de caracteres que conforman el string como volverlos mayusculas (uppercase), minusculas (lowercase), 
poner la primer letra del string en mayuscula y el resto en minuscula (title), unir strings (concatenar), entre otras, pues
es un tipo de dato muy versatil.
"""
 
"""
PROBLEMA 1: Full name formatter (name + initials).

Tras ingresar en un solo string un nombre completo, el programa normaliza el texto y muestra el nombre formateado en title además
de las iniciales del nombre.

input: nombre completo (string unico).
output:
Nombre formateado.
Iniciales del nombre.
"""
name = input("Set your full name: ")

name = name.strip()
name = " ".join(name.split())

name_formated = name.title()

initials = "".join([word[0].upper() for word in name.split()])

print("Name formated:", name_formated)
print("Initials:", initials)

"""
CASOS DE PRUEBA:
NORMAL:
Input.- angel gabriel ruiz torres
Output.-
Name formated: Angel Gabriel Ruiz Torres
Initials: AGRT

BORDE:
Input.- angelgabrielruiztorres
Output.-
Name formated: Angelgabrielruiztorres
Initials: A

ERROR:
Input.- 121316351
Output.-
Name formated: 121316351
Initials: 1
"""

"""
PROBLEMA 2: Simple email validator (structure + domain).
valida una direccion de correo electronico revisando que contenga un @ y al menos un "." despues del @.
"""
def email_check():
    e-mail = input("Enter your e-mail: ")

    if e-mail.strip() == "":
        print("Empty input not valid.")
        return
    e-mail = e-mail.strip()

    if " " in e-mail:
        print("Spaces are not allowed in the e-mail.")
        return
    at_count = e-mail.count("@")
   
    if at_count != 1:
        print("Email must contain one '@'.")
        return
    
    Position_Domain = e-mail.find("@")
    domain = e-mail[Position_Domain + 1:]

    if "." not in domain:
        print("The domain doesn't contain a dot.")
        return

    print("E-mail valid.")
    print("Full e-mail: ", e-mail)
email_check()
"""
CASOS DE PRUEBA:
NORMAL:
Input.- lol@lol.lol
Output.-
E-mail valid.
Full email:  lol@lol.lol

BORDE:
Input.-lol@@lol.xd
Output.-
Email must contain exactly one '@'.

ERROR:
Input.- xd
Output.-
Email must contain exactly one '@'.
"""

""" 
PROBLEMA 3: Palindrome checker (ignoring spaces and case).
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, 
ignorando espacios y mayúsculas/minúsculas.
input.- string
output.- palndromo y/n

"""
def palindrome(text_int):
    if text_int.strip() == "":
               print("Empty input not valid.")
               return
    
    normalize = text_int.lower().replace(" ", "")

    if len(normalize) < 3:
     print("The phrase must have at least 3 characters.") #error
     return

    palindrome_tf = normalize == normalize[::-1]

    print(f"Phrase: {normalize}")
    print(f"Is palindrome: {palindrome_tf}")


text = input("Enter a phrase: ")
palindrome(text)

"""
CASOS DE PRUEBA:
NORMAL:
Input.- oso
Output.-
Is palindrome: True

BORDE:
Input.-  no es palindromo
Output.-
Phrase: noespalindromo
Is palindrome: False

ERROR:
Input.- xd
Output.-
The phrase must have at least 3 characters.
"""

"""
PROBLEMA 4: Sentence word stats (lengths and first/last word).
Tras recibir una oración el progrma normaliza el texto y separa las palabras por espacios.
input.- frase
output.-
Total de palabras.
Primera palabra.
Última palabra.
Palabra más corta y más larga (por longitud).
"""
sentence = input("Write a sentence: ")

if sentence.strip() == "":
    print("Not valid an empty input.")
else:

 words = sentence.strip().split()
if len(words) == 0:
 print("Error: The sentence must contain at least one valid word.")
else:
 word_counter = len(words)

first_word = words[0]
last_word = words[-1]
shortest_word = min(words, key=len)
longest_word = max(words, key=len)

print(f"Total words: {word_counter}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Shortest word: {shortest_word}")
print(f"Longest word: {longest_word}")

"""
CASOS DE PRUEBA:
NORMAL:
Input.- una frase con muchas palabras
Output.-
Total words: 5
First word: una
Last word: palabras
Shortest word: una
Longest word: palabras

BORDE:
Input.- palabra
Output.-
First word: palabra
Last word: palabra
Shortest word: palabra
Longest word: palabra

ERROR:
Input.- 
Output.-
Not valid an empty input.
"""

"""
PROBLEMA 5: Password strength classifier.
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas.
reglas:
Weak: longitud < 8 o todo en minúsculas o muy simple.
Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
Strong: longitud >= 8 y contiene al menos:
- una letra mayúscula,
- una letra minúscula,
- un dígito,
-un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

"""
password_input = input("Enter your password: ")

if password_input.strip() == "":
    print("Not valid: empty input.")
else:
    length = len(password_input)
    has_upper = any(c.isupper() for c in password_input)
    has_lower = any(c.islower() for c in password_input)
    has_digit = any(c.isdigit() for c in password_input)
    has_special = any(not c.isalnum() for c in password_input)

    if length <= 6:
        strength = "weak"
    elif length >= 8 and has_upper and has_lower and has_digit and has_special:
        strength = "strong"
    elif length >= 8 and (has_upper or has_lower) and has_digit:
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")
"""
CASOS DE PRUEBA:
NORMAL:
Input.-  abc123
Output.- weak

BORDE:
Input.- Abcd1234
Output.- medium

ERROR:
Input.- Cntrl+C
Output.- KeyboardInterrupt
"""

"""
PROBLEMA 6: Product label formatter (fixed-width text).
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:
Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
Si es más corta, rellena con espacios al final.
Si es más larga, recorta hasta 30 caracteres.

input: product_name (string) / price_value (puede leerse como string o número; conviértelo a string para mostrarlo).

output: "Label: <exactly 30 characters>" (Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)
"""
product = input("Set your product name: ")
cost = input("Enter product price: ")


if product.strip() == "":
    print("Invalid empty input.")
else:
    try:
        amount = float(cost)
        
        toshow = str(amount)

        label = f"{product.strip()} - ${toshow}"

        if len(label) < 30:
            label = label + " " * (30 - len(label))
        else:
            label = label[:30]

        print(f'Label: "{label}"')

    except ValueError:
        print("Error: Price must be a valid number.")

"""
CASOS DE PRUEBA:
NORMAL:
Input.- coca/23
Output.- "lol - $23.0                   "

BORDE:
Input.-  treinta_caracteres           x / 12
Output.-  "treinta_caracteres           x"

ERROR:
Input.- xd / -20
Output.- Label: "xd - $-20.0                   "
"""

"""
CONCLUSIONES:
Los strings son nnuestro recurso de presentacion mas basico y comprender las formas de manipular y utilizar este recurso en
nuestro codigo nos permitira vovlernos mas versatles y agiles a la hora de hacer nuestros codigos pues utilizariamoas nuestros
recursos de mejor manera.
"""

""""
REFERENCIAS:
1) https://youtu.be/CCUNuqqn7PQ?si=HltURE4xKIDyQjm9
2) https://youtu.be/9k91jETchkI?si=3jr1oLLRh44mghYe
3) https://youtu.be/Pr-9wkSJDJk?si=ekXXTMe1kblZUbZ_
4) https://youtu.be/OvafT2HL0uU?si=tbUWDtTrdG60q3xk
5) https://youtu.be/WSQvaPHsm64?si=EJurIIuAx-bDLgl5
github link: https://github.com/AngelRuiz167/Tareas_python/edit/main/tuplas.py#L466C35
"""