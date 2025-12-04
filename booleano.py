"""
Alumno:Angel Gabriel Ruiz Torres, Matricula: 2530449, Grupo: 1-1

Manejo de números y booleanos en Python.
En el presente documento trataremos con el manejo de valores numericos y valores booleanos (true/false) para crear condiciones, 
generar parametros o inicializar acciones.
"""

"""
PROBLEMA 1:  Temperature converter and range flag.
Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin.
Además, determina un valor booleano is_high_temperature que sea true si la temperatura en Celsius es mayor o igual que 30.0 
y false en caso contrario.

input: temp_c (float; temperatura en °C).

Output:
"Fahrenheit:" <temp_f>
"Kelvin:" <temp_k>
"High temperature:" true|false

Validaciones:
Verificar que temp_c pueda convertirse a float.
No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).
"""
temp_c= int(input("Enter temperature in Celsius: ").strip())

try:
    temp_k = temp_c + 273.15
    temp_f = temp_c * 9 / 5 + 32

    if temp_k < 0:
        print("Error: invalid temperature (Kelvin < 0)")
    else:
        high_temperature = (temp_c >= 30.0)

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", str(high_temperature).lower())

except ValueError:
    print("Error: invalid input")

"""
CASOS DE PRUEBA:
NORMAL:
input.- 12
output.-
Fahrenheit: 53.6
Kelvin: 285.15
High temperature: false

BORDE:
input.- 31
output.-
Fahrenheit: 87.8
Kelvin: 304.15
High temperature: true

ERROR:
input.- lol
output.- ValueError
"""

"""
PROBLEMA 2:  Work hours and overtime payment.
Calcula el pago total semanal de un trabajador.
Hasta 40 horas se pagan a hourly_rate (float). 
Las horas extra (> 40) se pagan al 150% de la tarifa normal. 
Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.

inputs:
hours_worked (float; horas trabajadas en la semana).
hourly_rate (float; pago por hora).

outputs:
"Regular pay:" <regular_pay>
"Overtime pay:" <overtime_pay>
"Total pay:" <total_pay>
"Has overtime:" true|false

Validaciones:
hours_worked >= 0
hourly_rate > 0
Si alguno no cumple, mostrar "Error: invalid input".
"""
try:
    hours = int(input("Enter hours worked: ").strip())
    rate = int(input("Enter hourly rate: ").strip())

    if hours < 0 or rate <= 0:
        print("Error: invalid input")
    else:
        # Sustituimos hours_worked por hours (tu variable real)
        r_hours = min(40, hours)
        overtime = max(0, hours - 40)

        r_pay = r_hours * rate
        overtime_pay = overtime * rate * 1.5
        total_pay = r_pay + overtime_pay

        has_overtime = (hours > 40)

        print("Regular pay:", r_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", str(has_overtime).lower())

except:
    print("Error: invalid input")

"""
CASOS DE PRUEBA:
NORMAL:
input.- 38 / 100
output.-
Regular pay: 3800
Overtime pay: 0.0
Total pay: 3800.0
Has overtime: false

BORDE:
input.- 40 / 1
output.-
Regular pay: 40
Overtime pay: 0.0
Total pay: 40.0
Has overtime: false

ERROR:
input.- -1 / 0
output.- Error: invalid input

"""

"""
PROBLEMA 3: Discount eligibility with booleans.
Determina si un cliente obtiene un descuento en su compra. La regla es:
is_student es true OR
is_senior es true OR
purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

input:
purchase_total (float; total de la compra).
is_student_text (string; "YES" o "NO").
is_senior_text (string; "YES" o "NO").

output:
"Discount eligible:" true|false
"Final total:" <final_total>
"""
try:
    purchase = float(input("Set your purchase total: ").strip())
    student = input("Are you a student? (YES/NO): ").strip().upper()
    senior = input("Is senior? (YES/NO): ").strip().upper()

    if purchase < 0:
        print("Error: invalid input")
    elif student not in ("YES", "NO") or senior not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        is_student = (student == "YES")
        is_senior = (senior == "YES")

        discount_eligible = (
            is_student or is_senior or purchase >= 1000.0
        )

        if discount_eligible:
            final_total = purchase * 0.9   # 10% OFF
        else:
            final_total = purchase

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", final_total)

except:
    print("Error: invalid input")

"""
CASOS DE PRUEBA:
NORMAL:
input.- 1200 /no/no
output.-
Discount eligible: true
Final total: 1080.0

BORDE:
input.- 1000/yes/yes
output.-
Discount eligible: true
Final total: 900.0

ERROR:
input.- lol
output.- Error: invalid input
"""

"""
PROBLEMA 4: Basic statistics of three integers.
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo y un booleano all_even 
que indique si los tres números son pares.

Inputs:
n1 (int), n2 (int), n3 (int)

outputs:
"Sum:" <sum_value>
"Average:" <average_value>
"Max:" <max_value>
"Min:" <min_value>
"All even:" true|false
"""
try:
    n1 = int(input("Enter your first number: "))
    n2 = int(input("Enter your second number: "))
    n3 = int(input("Enter your third number: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

except:
    print("Error: invalid input")

"""
CASOS DE PRUEBA:
NORMAL:
input.- 3 / 6 / 9
output.-
all_even: false

BORDE:
input.- 2 / 4 / 6
output.-
all_even: true

ERROR:
input.- text
output.- Error: invalid input
"""

"""
PROBLEMA 5: Loan eligibility (income and debt ratio).
- Determina si una persona es elegible para un préstamo con base en:
monthly_income (float)
monthly_debt (float)
credit_score (int)
- La regla es:
debt_ratio = monthly_debt / monthly_income
eligible es true si:
monthly_income >= 8000.0 AND
debt_ratio <= 0.4 AND
credit_score >= 650

Entradas:
monthly_income (float; ingreso mensual).
monthly_debt (float; pagos mensuales de deuda).
credit_score (int; puntaje de crédito).

Salidas:
"Debt ratio:" <debt_ratio>
"Eligible:" true|false
"""

income_text = input("Enter monthly income: ").strip()
debt_text = input("Enter monthly debt: ").strip()
score_text = input("Enter credit score: ").strip()

try:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0 and
            debt_ratio <= 0.4 and
            credit_score >= 650
        )

        print("Debt ratio:", debt_ratio)
        print("Eligible:", str(eligible).lower())

except:
    print("Error: invalid input")

"""
CASOS DE PRUEBA:
NORMAL:
input.- 10000 / 2000 / 700
output.-
eligible: true

BORDE:
input.- 8000 / 3200 / 650
output.-
eligible: true

ERROR:
input.- 0
output.- Error: invalid input
"""

"""
PROBLEMA 6:  Body Mass Index (BMI) and category flag.
Calcula la masa corporal de alguien y genera booleanso para indicar lo sig:
is_underweight (bmi < 18.5)
is_normal (18.5 <= bmi < 25.0)
is_overweight (bmi >= 25.0)

"""
weight = int(input("Enter weight (kg): ").strip())
height = int(input("Enter height (m): ").strip())

if weight == "" or height == "":
    print("Error: invalid input")
    exit()

try:
    if weight <= 0 or height <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height ** 2)
        bmi_rounded = round(bmi, 2)

        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)
except ValueError:
     print("Carácter inválido.")
        
    print("BMI:", bmi_rounded)
    print("Underweight:", str(is_underweight).lower())
    print("Normal:", str(is_normal).lower())
    print("Overweight:", str(is_overweight).lower())

"""
CASOS DE PRUEBA:
NORMAL:
input.- 70 / 1.75
output.-
BMI: 22.86
Underweight: false
Normal: true
Overweight: false

BORDE:
input.- 90 / 1.70
output.-
BMI: 31.14
Underweight: false
Normal: false
Overweight: true

ERROR:
input.- 70 / 0
output.- Error: invalid input
"""

"""
CONCLUSIONES: 
Los booleanos son una herramienta que nos sirve para generar condiciones y situaciones que se adapten a lo que necesita nuestro
codigo, siempre y cuando sea un filtro de una pregunta de si o no.
"""

"""
1) https://docs.python.org/es/3/library/stdtypes.html
2)https://recursospython.com/guias-y-manuales/logica-tipo-booleano/
3)https://www.geeksforgeeks.org/python/boolean-data-type-in-python/
4)apuntes en clase.
5) Ayuda de ChatGPT (OpenAI), 2025.
github link: https://github.com/AngelRuiz167/Tareas_python/edit/main/tuplas.py#L466C35
"""