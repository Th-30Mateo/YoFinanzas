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