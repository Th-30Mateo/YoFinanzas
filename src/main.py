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
eq = "="*30

def ver_gastos():
    hay_gasto = False
    for item in transacciones:
        if item["tipo"] == "gasto":
            if not hay_gasto:
                print(f"\n----- Gasto encontrado -----\n"
                      f"{eq}")
                hay_gasto = True
            print(f"Identificador: {item['id']}\n"
                f"Gasto: {item['categoria']}\n"
                f"Monto y fecha: {item['monto']} {item['fecha']}\n"
                f"Descripcion: {item['descripcion']}\n"
                f"{eq}\n")
    if not hay_gasto:
        print("No hay gastos registrados.\n")
    input("\nPresione ENTER para volver al menu principal...")

def ver_ingresos():
    hay_ingreso = False
    for item in transacciones:
        if item["tipo"] == "ingreso":
            if not hay_ingreso:
                print("\n----- Ingresos encontrados -----\n"
                      f"{eq}")
                hay_ingreso = True
            print(f"Identificador: {item['id']}\n"
                  f"Ingreso: {item['categoria']}\n"
                  f"Monto y fecha: {item['monto']} {item['fecha']}\n"
                  f"Descripcion: {item['descripcion']}\n"
                  f"{eq}\n")
    if not hay_ingreso:
        print("No hay ingresos registrados\n")
    input("\nPresione ENTER para volver al menu principal...")
