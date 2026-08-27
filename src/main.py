tipos_gastos = ["comida", "transporte", "combustible", "varios", "salarios pagados"]
tipos_ingresos = ["ventas", "donaciones", "servicios", "retiro de inversiones", "sueldo"]

id_transacciones = 0
transacciones = {id_transacciones :
    {
        "tipo" : "tipo",
        "categoria" : "categoria",
        "monto" : 0,
        "descripcion" : "descripcion",
        "fecha" : "fecha"
    },
}




def modificar_monto_gasto(tipo, monto):

    gasto = gastos["tipo"]
    gasto["monto"] = monto
    print("Actualizacion de monto final:")
    print("="*20)
    print(f"Monto de {gasto["categoria"]} modificado = {gasto["monto"]}")
    print("-"*30)

def agregar_gastos(categoria, monto, fecha):
    gasto = {
    "tipo" : "gasto",
    "categoria" : categoria, 
    "monto" : monto,
    "fecha" : fecha
    }
    if len(transacciones) == 0:
        id_nueva = 1

    else:
        max_id = max(transacciones.keys())
        id_nueva = max_id + 1
    return mostrar_gasto(id_gasto)

def mostrar_gasto(id_gasto):
    if id_gasto in transacciones:
        gasto = transacciones[id_gasto]
        print("----- Gasto encontrado ------")
        print()
        for clave, valor in gasto.items():
            print(f"{clave}: {valor}")
            print()
            print("-"*30)
    else:
        print("Gasto no encontrado!")
        print("Volviendo al menu anterior...")
        print("="*30)




def mostrar_gastos():
    hay_gastos = False
    for id_dic, datos in transacciones.items():
        if datos["tipo"] == "gasto":
            hay_gastos = True
            print(f"ID de la transaccion: {id_dic}")
            for clave, valor in datos.items():
                print(clave, valor)
                print("-"*20)

    if not hay_gastos:
        print("Aun no ha registrado gastos!!")
