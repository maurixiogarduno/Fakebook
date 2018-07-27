#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import unicodedata
from random import choice, randint

mujer = ["Sofía","Camila","Valentina","Isabella","Valeria","Daniela","Mariana",
"Sara","Victoria","Gabriela","Ximena","Andrea","Natalia","Mía","Martina",
"Lucía","Samantha","María","María Fernanda","Nicole","Alejandra","Paula",
"Emily","María José","Fernanda","Luciana","Ana Sofía","Melanie","Regina",
"Catalina","Ashley","Renata","Agustina","Abril","Emma","Emilia","Jazmín",
"Juanita","Briana","Vanessa","Antonia","Laura","Antonella","Luna","Carla",
"Allison","Monserrat","Paulin","Isabel","Juliana","Valerie","Florencia",
"Adriana","Naomí","Amanda","Ariana","Morena","Natalie","Constanza","Lola",
"Zoe","Carolina","Micaela","Julia","Claudia","Paola","Alexa","Elena","Isidora",
"Rebeca","Josefina","Abigail","Julieta","Melissa","Michelle","Alba",
"María Camila","Angela","Delfina","Aitana","Stephanie","Fátima","Manuela",
"Alexandra","Paloma","Candela","Clara","Laura Sofía","Diana","Ana María",
"Guadalupe","Bárbara","Bianca","Miranda","Sabrina","Pilar","Ana María","Marta",
"Ana","Génesis"]

hombre = ["Santiago","Sebastián","Diego","Nicolás","Samuel","Alejandro",
"Daniel","Mateo","Ángel","Matías","Gabriel","Tomás","David","Emiliano","Andrés",
"Joaquín","Carlos","Alexander","Adrián","Lucas","Benjamín","Leonardo","Rodrigo",
"Felipe","Francisco","Pablo","Martín","Fernando","Isaac","Manuel","Juan Pablo",
"Emmanuel","Emilio","Vicente","Eduardo","Juan","Javier","Jorge","Aarón","José",
"Erick","Luis","Cristian","Ignacio","Christopher","Jesús","Kevin","Juan José",
"Agustín","Juan David","Simón","Joshua","Maximiliano","Miguel Ángel",
"Juan Sebastián","Bruno","Iván","Gael","Miguel","Thiago","Jerónimo","Hugo",
"Ricardo","Antonio","Ian","Anthony","Pedro","Rafael","Jonathan","Esteban",
"Juan Manuel","Julián","Mauricio","Oscar","Santino","Axel","Sergio","Guillermo",
"Matthew","Valentín","Bautista","Álvaro","Dylan","Marco","Mauro","Luciano",
"Mario","César","Cristóbal","Luca","Iker","Gonzalo","Roberto","Valentino",
"Facundo","Patricio","Diego Alejandro","Josué","Franco"]

apellido = ["García","González","Rodríguez""Fernández","López","Martínez",
"Sánchez","Pérez","Gómez","Martin","Jiménez","Ruiz","Hernández","Diaz","Moreno",
"Muñoz","Álvarez","Romero","Alonso","Gutiérrez","Navarro","Torres","Domínguez",
"Vázquez","Ramos","Gil","Ramírez","Serrano","Blanco","Molina","Morales",
"Suarez","Ortega","Delgado","Castro","Ortiz","Rubio","Marín","Sanz","Núñez",
"Iglesias","Medina","Garrido","Cortes","Castillo","Santos","Lozano",
"Guerrero","Cano","Prieto","Méndez","Cruz","Calvo","Gallego","Vidal","León",
"Márquez","Herrera","Peña","Flores","Cabrera","Campos","Vega","Fuentes",
"Carrasco","Diez","Caballero","Reyes","Nieto","Aguilar","Pascual","Santana",
"Herrero","Lorenzo","Montero","Hidalgo","Giménez","Ibáñez","Ferrer","Duran",
"Santiago","Benítez","Mora","Vicente","Vargas","Arias","Carmona","Crespo",
"Román","Pastor","Soto","Sáez","Velasco","Moya","Soler","Parra","Esteban",
"Bravo","Gallardo","Rojas"]

# Genero
sex = choice(["Hombre","Mujer"])

if sex == "Hombre":
    nombre = hombre

if sex == "Mujer":
    nombre = mujer

# Nombre y Apellido
ramdom_nombre = choice(nombre)
ramdom_apellido = choice(apellido)

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s.decode()
# Limpia tildes del nombre
ramdom_nombre = ramdom_nombre.decode('utf-8')
ramdom_nombre = elimina_tildes(ramdom_nombre)
# Limpia tildes del apellido
ramdom_apellido = ramdom_apellido.decode('utf-8')
ramdom_apellido = elimina_tildes(ramdom_apellido)

# Email
e_longitud = 8
e_valores = "0123456789abcdefghijklmnopqrstuvwxyz-_."
e_ramdom = ""
e_ramdom = e_ramdom.join([choice(e_valores) for i in range(e_longitud)])
email = (ramdom_apellido.lower() + e_ramdom + '@gmail.com')

# Contraseña
longitud = 18
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
ramdom_pw = ""
ramdom_pw = ramdom_pw.join([choice(valores) for i in range(longitud)])

# Fecha de nacimiento
year = str(randint(1985, 2000))
month = str(randint(1, 12))
day = str(randint(1, 28))
birth_date = (day + '/' + month + '/' + year)

# Imprimir en pantalla
print('Nombre = ' + ramdom_nombre + ' ' + ramdom_apellido)
print('Email = ' + email)
print('Contraseña = ' + ramdom_pw)
print('Fecha de nacimiento = ' + birth_date)
print('Genero = ' + sex)

# Guardar Datos en fakebook.txt
file = open("fakebook.txt","r+")
file.read()
file.write('\n' + '----------------------------------------------------')
file.write('\n' + 'Nombre = ' + ramdom_nombre + ' ' + ramdom_apellido)
file.write('\n' + 'Email = ' + email)
file.write('\n' + 'Contraseña = ' + ramdom_pw)
file.write('\n' + 'Fecha de nacimiento = ' + birth_date)
file.write('\n' + 'Genero = ' + sex)
file.close()
