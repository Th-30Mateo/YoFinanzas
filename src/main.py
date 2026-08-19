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



print("="*30)
print(f"---Bienvenido a YoFinanzas---")
print("="*30)
print(" ")
print("¿Que desea hacer?\n")
print(" -1- para menu principal.\n -2- para salir.\n" )
opcion = input(str("Ingrese una opcion para continuar:  ")).strip().lower()
if opcion == "2":
    print("=="*10)
    print("Saliendo...")
    print("=="*10)
while opcion == "1":
    print("="*20)
    menu = print("---Menu principal---\n -1- Modificar gastos. \n -2- Modificar ingresos \n"
    "-3- Ver gastos. \n -4- Ver ingresos. \n " )
    op_menu = input(str("Seleccione una opcion para continuar."))
    match op_menu:
        case "1":
            while True:
                op_mod_gas = input(str("Seleccione una opcion para continuar: ")).strip()
                print("---"*20)
                print("-1- mostrar todos los gastos\n -2- seleccionar gasto por id \n"
                " -3- seleccionar gasto por tipo\n -4- salir")
                print("---"*20)
                if op_mod_gas == "1":
                    print(f"---Gastos totales---")
                    mostrar_gastos()


def modificar_monto_gasto(tipo, monto):

    gasto = gastos["tipo"]
    gasto["monto"] = monto
    print("Acutalizacion de monto final:")
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
