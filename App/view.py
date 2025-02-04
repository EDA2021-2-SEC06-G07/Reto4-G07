﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from typing import Collection
import config as cf
import sys
import controller
import timer
from DISClib.ADT import list as lt
from DISClib.ADT import map
from DISClib.ADT import orderedmap as tree
from DISClib.DataStructures import linkedlistiterator as iter
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Aeropuerto i sus conscciones")
    print('2- Encontrar clústeres de tráfico aéreo');
    print("3- Como llegar rde una ciudad a otra");
    print('4- Utilizar las millas de viajero');
    print('5- Cuantificar el efecto de un aeropuerto cerrado');
    print('7- speed test');
    print('8- exit');


def load():
    catalog = controller.load();
    return catalog


catalog = None


def req1():
    airports = controller.req1(catalog);

    airports_list = tree.valueSet(airports);
    degree_list = tree.keySet(airports);

    i = iter.newIterator(airports_list);
    j = iter.newIterator(degree_list);
    while(iter.hasNext(i)):
        airport = iter.next(i);
        degree = iter.next(j);
        IATA = airport['IATA'];
        name = airport['Name'];
        city = airport['City'];
        country = airport['Country'];
        print(f"Airport {name} in city {city} in {country} with the IATA {IATA}");
        print(f"Has {degree} amount of connections.\n");


def req2(aeropuerto1, aeropuerto2):
    respuesta = controller.req2(catalog,aeropuerto1,aeropuerto2)
    
    if respuesta is True:
        print('los dos aeropuertos SON fuertemente conectados.')
    if respuesta is False:
        print('Los dos aeropuertos NO son fuertemente conectados')
    print('--------------------------------------------------')


def req3(origin, destination):
    path = controller.req3(catalog, origin, destination);

    total_distance = 0;
    i = iter.newIterator(path);
    while iter.hasNext(i):
        current = iter.next(i);
        airportA = map.get(catalog['airports'],current['vertexA'])['value']['Name'];
        airportB = map.get(catalog['airports'],current['vertexB'])['value']['Name'];
        distance = current['weight'];

        print(f"{airportA} to {airportB} has {distance}km");
        total_distance += distance;

    print(f"The total distance you will travel is: {total_distance}");
    

def req4(aeropuerto, millas):
    respuesta = controller.req4(catalog, aeropuerto, millas)
    print('Los aeropuertos en la rama son: ')
    print('')
    i= iter.newIterator(respuesta)
    while(iter.hasNext(i)):
        airport = iter.next(i)
        print('IATA: '+airport['IATA'])
        print('Nombre: '+airport['Name'])
        print('Nombre: '+airport['City'])
        print('Nombre: '+airport['Country'])
        print('')
        

def req5(aeropuerto):
    info = controller.req5(catalog,aeropuerto)
    
    print('Los aeropuertos afectados son: ')
    print('')
    i= iter.newIterator(info)
    while(iter.hasNext(i)):
        airport = iter.next(i)
        print('IATA: '+airport['IATA'])
        print('Nombre: '+airport['Name'])
        print('Nombre: '+airport['City'])
        print('Nombre: '+airport['Country'])
        print('')
    

def test_req2():
    req2('LED', 'RTP');


def test_req3():
    req3('St. Petersburg', 'Lisbon');


def test_req4():
    req4('LIS', 19850.0);


def test_req5():
    req5('DXB');



"""
Menu principal
"""
if __name__ == "__main__":
    running = True
    while running:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 0:
            print("Cargando información de los archivos ....")
            catalog = load()

            size_airports = map.size(catalog["airports"]);
            size_cities = map.size(catalog["cities"]);
            print(f"{size_airports} airports where added");
            print(f"{size_cities} cities were added");
        elif int(inputs[0]) == 1:
            req1();
        elif int(inputs[0]) == 2:
            aeropuerto1 = str(input('Agregue el primer aeropuerto: '))
            aeropuerto2 = str(input('Agregue el segundo aeropuerto: '))
            req2(aeropuerto1, aeropuerto2)
        elif int(inputs[0]) == 3:
            origin = input("Ciudad de origen:");
            destination = input("Ciudad de destino:");
            req3(origin, destination);
        elif int(inputs[0]) == 4:
            aeropuerto= input('Agregue el aeropuerto:')
            millas= float(input('Escribe las millas: '))
            req4(aeropuerto, millas)
        elif int(inputs[0]) == 5:
            aeropuerto = str(input('Agregue el aeropuerto: '))
            req5(aeropuerto)
        elif int(inputs[0]) == 7:
            stop_watch = timer.Timer()
            catalog = load()

            time1 = stop_watch.time_function(req1)
            time2 = stop_watch.time_function(test_req2)
            time3 = stop_watch.time_function(test_req3)
            time4 = stop_watch.time_function(test_req4)
            time5 = stop_watch.time_function(test_req5)

            print('\n\n')
            print("time req1: " + str(time1) + 's')
            print("time req2: " + str(time2) + 's')
            print("time req3: " + str(time3) + 's')
            print("time req4: " + str(time4) + 's')
            print("time req5: " + str(time5) + 's')
        else:
            running = False 
