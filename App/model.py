"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map
from DISClib.ADT import orderedmap as tree
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import linkedlistiterator as iter
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import graph;
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo
def add_airport(catalog, airport):
    graph.insertVertex(catalog["routes"], airport["IATA"]);
    map.put(catalog["airports"], airport["IATA"], airport);


def add_route(catalog, route):
    graph.addEdge(catalog["routes"], route["Departure"], route["Destination"], route["distance_km"]);


def add_city(catalog, city):
    map.put(catalog["cities"],city["city_ascii"],city);


# Funciones para creacion de datos
def init_catalog():
    catalog = {
        "routes": None,
        "airports": None,
        "cities": None
    };
    catalog["routes"] = graph.newGraph(datastructure="ADJ_LIST", directed=True);
    catalog["cities"] = map.newMap(maptype="PROBING");
    catalog["airports"] = map.newMap(maptype="PROBING");
    return catalog;

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

# Compare functions

def cmp_airport_size(degree1, degree2):
    res = 1;
    if(degree1 < degree2):
        res = -1;
    elif(degree1 == degree2):
        res = 0;
    
    return res;

# Requerimientos
def req1(catalog):
    airports = tree.newMap(omaptype='RBT', comparefunction=cmp_airport_size);
    airportlist = map.valueSet(catalog['airports']);
    
    i = iter.newIterator(airportlist);
    while(iter.hasNext(i)):
        airport = iter.next(i);
        degree = graph.degree(catalog['routes'], airport['IATA']);
        tree.put(airports,degree,airport);

    return airports;



def req3():
    pass
