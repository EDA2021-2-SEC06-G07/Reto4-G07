"""
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
    print("1- ")
    print("3- ");


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


def req3(city_origin, city_destination):
    origin = map.get(catalog["airports"], city_origin)['IATA'];
    destination = map.get(catalog['airports'], city_destination)['IATA'];
    path = controller.req3(catalog, origin, destination);
    print(path);


def req5(aeropuerto):
    info= controller.req5(catalog,aeropuerto)
    i= iter.newIterator(info)
    while(iter.hasNext(i)):
        airport = iter.next(i)
        print(airport['Name'])
    

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
        elif int(inputs[0]) == 5:
            aeropuerto = str(input('Agregue el aeropuerto: '))
            req5(aeropuerto)
        else:
            running = False 
