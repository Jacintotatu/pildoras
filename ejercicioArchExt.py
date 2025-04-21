from io import *

agendaClientes = open("clientes.txt", "r", encoding="utf-8")

listaClientes = agendaClientes.readlines()

agendaClientes.close()

archivoClientes = []

for cliente in listaClientes:
    listaClientes = cliente.split(";")
    listado = f"Código Artículo: {listaClientes[0]} Nombre: {listaClientes[1]}\
Dirección: {listaClientes[2]} Población: {listaClientes[3]} Tfno.: {listaClientes[4]}\
Responsable: {listaClientes[5]}."
    archivoClientes.append(listado)

print(archivoClientes)

for cliente in archivoClientes:
    print(cliente)