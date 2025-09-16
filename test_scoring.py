from scoring import evaluar_tc_cliente

def test_rechazo_por_edad():
    resultado = evaluar_tc_cliente(edad = 16, ingresos = 2000)
    assert resultado["califica"] is False

def test_rechazo_por_ingresos():
    resultado = evaluar_tc_cliente(edad = 25, ingresos = 500)
    assert resultado["califica"] is False

def test_tarjeta_oh_regular():
    resultado = evaluar_tc_cliente(edad = 20, ingresos = 2000)
    assert resultado["califica"] is True
    assert resultado["categoria"] == "Tarjeta OH"
    assert resultado["linea"] == 2000

def test_tarjeta_oh_premium():
    resultado = evaluar_tc_cliente(edad = 30, ingresos = 7500)
    assert resultado["califica"] is True
    assert resultado["categoria"] == "Tarjeta OH Premium"

def test_tarjeta_caso_intermedio():
    resultado = evaluar_tc_cliente(edad = 21, ingresos = 10000)
    assert resultado["califica"] is True
    assert resultado["categoria"] == "Tarjeta OH"