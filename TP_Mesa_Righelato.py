# -*- coding: utf-8 -*-
import csv

#Actividad n° 1
def obtenerCategoriaVehiculos (matriz):
  cat_cobrada = []
  for fila in matriz:
    categ = fila[2]
    while categ not in cat_cobrada:
      cat_cobrada.append(categ)
  return cat_cobrada

def obtenerPeaje (matriz):
  id_peaje = []
  for fila in matriz:
    peaje = fila[3]
    while peaje not in id_peaje:
      id_peaje.append(peaje)
  return id_peaje

#Actividad n° 2

def obtenerRegistroVehiculo (matriz, categoria):
  registrosV = []
  for fila in matriz:
    if categoria == fila[2]:
      registrosV.append(fila)
  return registrosV

#Actividad n° 3

def obtenerRegistroFecha (matriz, fecha):
  registrosFecha = []
  for fila in matriz:
    lista_fecha = fila[0].split("/")
    dia= int(lista_fecha[0])
    if dia == fecha:
      registrosFecha.append(fila)
  return registrosFecha

#Actividad n° 4

def obtenerCantidadTotal(matriz, fecha, encabezado, sentido):
    lista_por_hh = [[0]*(len(encabezado)+1) for i in range(24)]
    c = 0
    for fila in lista_por_hh:
        fila[0] = c
        c += 1
    lista_por_hh.insert(0,["Horas"] + encabezado)
    for fila in matriz:
        filaPeaje = fila[3]
        filaFecha = fila[0]
        filaSentido = fila[5]
        filaHH = int(fila[1])
        filaPasos= round(float(fila[-1]))
        if filaFecha == fecha and filaSentido == sentido and filaPeaje in encabezado:
            index_hora = filaHH + 1
            index_peaje = encabezado.index(filaPeaje) + 1
            lista_por_hh[index_hora][index_peaje] += filaPasos
    return lista_por_hh

#Actividad n° 5

def obtenerCol(matriz,f):
    col = -1
    categoria = f[1]
    sentido = f[2]
    cantCol = len(matriz[0])
    for i in range(1,cantCol):
        if matriz[0][i] == categoria:
            if sentido == "Centro":
                col = i
            else:
                col = i+1
            break
    return col

def crearMatrizArchi (matriz, listacategoria,id_peaje,fecha5):
     c = 0
     cantCat=0
     listacategorianueva=[]
     for i in listacategoria:
         cantCat+=1
     for i in listacategoria:
         listacategorianueva.append(i)
         listacategorianueva.append("")
     matriz_cat= [[0]*(len(listacategorianueva)+1) for i in range(24)]
     for fila in matriz_cat:
         fila[0] = c
         c += 1
     matriz_cat.insert(0,["Categorias:"] + listacategorianueva)
     matriz_cat.insert(1, ["Horas"]+(["Centro","Provincia"]*cantCat))
     filasxidpeajexfecha = [fila for fila in matriz if fila[3] == id_peaje and fila[0] == fecha5]
     datos_agrupados = []
     for fila in filasxidpeajexfecha:
         pasos = round(float(fila[7]))
         categoria = fila[2]
         sentido = fila[5]
         hora = fila[1]
         grupo_existe = False
         for f in datos_agrupados:
             if f[1] == categoria and f[2] == sentido and f[0]==hora:
                 f[3] += pasos  
                 grupo_existe = True
                 break
         if not grupo_existe:
             datos_agrupados.append([hora,categoria, sentido, pasos])
         for fila in datos_agrupados:
             col_CatxSentido = obtenerCol(matriz_cat,fila)
             hora = int(fila[0])
             fila_hora = hora+2
             matriz_cat[fila_hora][col_CatxSentido] = fila[3]
     return matriz_cat

matriz=[]
with open ("C:/Users/Freedomware/Downloads/Trabajo Práctico - Peajes-20230627/Transito Febrero 2023.csv", "r", encoding="UTF-8") as archi:
  todo= csv.reader(archi, delimiter=";")
  encabezado=next(todo)
  for fila in todo:
    fila = fila[:-2]
    if 'Total general' in fila:
      break
    matriz.append(fila)

#Actividad n° 1

listadoCategoria= obtenerCategoriaVehiculos(matriz)
listadoPeaje= obtenerPeaje(matriz)
print("Para la actividad número 1 \n")

print("El listado de las categorías de vehiculos registrados es: ")
for categoria in listadoCategoria:
    print(categoria)

print("\nEl listado de los puestos de peajes es:" )
for peaje in listadoPeaje:
    print(peaje)

#Actividad n° 2

print("\nPara la actividad número 2 \n")
print("El listado de las categorías de vehiculos registrados es: ")

for categoria in listadoCategoria:
    print(categoria)

while True:
    categoria2=input("\nIngrese una categoria de vehiculo (Si desea cancelar ingrese 0): ")
    if categoria2 == "0":
        print("Usted canceló el programa.")
        break
    elif categoria2 in listadoCategoria:
        print("\nLos registros correspondientes a esa categoría son: ")
        listaRegistro= obtenerRegistroVehiculo(matriz, categoria2)
        for lista in listaRegistro:
            print(lista)
        break
    else:
        print("\nEsa categoría no se encuentra en el listado. Intente nuevamente.\n")
        continue
    
#Actividad n° 3

listaDia = []

for fila in matriz:
    lista_fecha = fila[0].split("/")
    listaDia.append(int(lista_fecha[0]))
    
print("\nPara la actividad número 3 \n")

while True:
    fecha3=input("\nIngrese un día de febrero del año 2023 (Si desea cancelar ingrese 0): ")
    if fecha3 == "0":
        print("Usted canceló el programa.")
        break
    if not fecha3.isdigit():
        print("\nEl contenido ingresado no es valido. Intente nuevamente.")
        continue
    fecha_int = int(fecha3)
    if fecha_int in listaDia:
        listadoRegistros= obtenerRegistroFecha(matriz, fecha_int)
        print("\nEl listado de registros del día ", fecha3, " es: ")
        for lista in listadoRegistros:
            print(lista)
        break
    
#Actividad n° 4

filaFechas = [fila[0] for fila in matriz]
filaSentidos = [fila[5] for fila in matriz]

print("\nPara la actividad número 4 \n")

while True:
    fecha4=input("Ingrese una fecha de febrero en formato d/m/aaaa (Si desea cancelar ingrese 0): ")
    if fecha4 == "0" :
        print("Usted canceló el programa.")
        break
    if fecha4 not in filaFechas:
        print("\nEl contenido ingresado no es valido. Intente nuevamente.")
        continue
    sentido= input("Ingrese el sentido Centro/Provincia (Si desea cancelar ingrese 0): ")
    if sentido == "0":
        print("Usted canceló el programa.")
        break
    if sentido not in filaSentidos:
        print("\nEl contenido ingresado no es valido. Intente nuevamente.")
        continue
    if fecha4 in filaFechas and sentido in filaSentidos:
        tabla= obtenerCantidadTotal(matriz, fecha4, obtenerPeaje(matriz), sentido)
        print("\nLa tabla para la fecha ", fecha4, "y sentido ", sentido, "es: ")
        for lista in tabla:
            print(lista)
        break
    break

#Actividad n° 5

print("\nPara la actividad número 5 \n")
print("Los ID del peaje son los siguientes: ", listadoPeaje)


filaID= [fila[3] for fila in matriz]
listacategoria=obtenerCategoriaVehiculos(matriz)

while True:
    id_peaje = input("Ingrese el ID del peaje(Si desea cancelar ingrese 0): ")
    if id_peaje == "0":
        print("Usted canceló el programa.")
        break
    fecha5 = input("Ingrese la fecha (dd/mm/aaaa)(Si desea cancelar ingrese 0): ")
    if fecha5 == "0":
        print("Usted canceló el programa.")
        break
    if id_peaje in filaID and fecha5 in filaFechas:
        print("\nLa información para la fecha ", fecha5, "e ID ", id_peaje, " esta cargada en el archivo: FlujoVehicular_ddmmaaaa_CodPeaje.csv")
        break
    else:
        print("\nEl contenido ingresado no es valido. Intente nuevamente.")
        continue
    break
     
encabezadoPeaje = ["Pasos de vehiculos para el peaje:","","",id_peaje]
encabezadoFecha = ["Fecha:",fecha5]
matrizFinalRta5= crearMatrizArchi (matriz, listacategoria,id_peaje,fecha5)

with open("FlujoVehicular_ddmmaaaa_CodPeaje.csv", "w", encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv, delimiter=";",lineterminator="\n")
    escritor_csv.writerow(encabezadoPeaje)
    escritor_csv.writerow(encabezadoFecha)
    for fila in matrizFinalRta5:
        escritor_csv.writerow(fila)  
    
