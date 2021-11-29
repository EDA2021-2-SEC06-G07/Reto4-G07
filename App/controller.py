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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def load():
    catalog = model.init_catalog();

    airport_file = cf.file_dir + "/Data/Skylines/airports_full.csv";
    route_file = cf.file_dir + "/Data/Skylines/routes_full.csv";
    cities_file = cf.file_dir + "/Data/Skylines/worldcities.csv";

    airport_data = csv.DictReader(open(airport_file, encoding="utf-8"));
    route_data = csv.DictReader(open(route_file, encoding="utf-8"));
    cities_data = csv.DictReader(open(cities_file, encoding="utf-8"));

    for city in cities_data:
        model.add_city(catalog, city);

    for airport in airport_data:
        model.add_airport(catalog, airport);

    for route in route_data:
        model.add_route(catalog, route);

    return catalog;


# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

# Requirements
def req1(catalog):
    return model.req1(catalog);