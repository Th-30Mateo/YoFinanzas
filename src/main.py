categoria_gastos = ["comida", "transporte", "combustible", "varios", "salarios pagados"]
categoria_ingresos = ["ventas", "donaciones", "servicios", "retiro de inversiones", "sueldo"]

identificador = 0
transacciones = [
    {
        "id" : 0,
        "categoria" : "categoria",
        "tipo" : "tipo",
        "monto" : 0,
        "descripcion" : "descripcion",
        "fecha" : "fecha"
    },
]


def ver_gastos():
    hay_gasto = False
    eq = "="*30
    for items in transacciones:
        if items["tipo"] == "gasto":
            if not hay_gasto:
                print(f"----- Gasto encontrado -----\n")
                hay_gasto = True
            print(f"Identificador: {items['id']}\n"
                f"Gasto: {items['categoria']}\n"
                f"Monto y fecha: {items['monto']} {items['fecha']}\n"
                f"Descripcion: {items['descripcion']}\n")
    if not hay_gasto:
        print("No hay gastos registrados.")

def modificar_monto_gasto():

    gasto = transacciones["tipo"]
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
