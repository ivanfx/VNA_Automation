import pyvisa 
rm = pyvisa.ResourceManager()
print("---Buscando instrumentos conectados--")

#Lista todo lo que encuentre 
equipos = rm.list_resources()

if len(equipos) == 0:
    print("No encontre nada")
else:
    for equipo in equipos:
            print(f"Encontrado: {equipo}")

