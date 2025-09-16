def evaluar_tc_cliente(edad, ingresos):
    # Edad o ingresos no válidos
    if edad < 18 or ingresos < 1000:
        return {"califica": False, "categoria": None, "linea": 0} 
    
    # Premium: Ingresos altos y edad mayor/igual a 25
    if ingresos >= 5000 and edad >= 25:
        return {"califica": True, "categoria": "Tarjeta OH Premium", "linea": 10000}
    
    # Defecto: Tarjeta OH
    return {"califica": True, "categoria": "Tarjeta OH", "linea": 2000}
    
# print(evaluar_tc_cliente(25, 10000))