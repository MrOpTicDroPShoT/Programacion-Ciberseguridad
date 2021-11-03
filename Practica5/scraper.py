#!/usr/bin/python3
import requests, re, shutil, sys, openpyxl
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
import os

def scrapNoticias():
    f = open("../txt/noticias.txt", "r")
    a = (f.readlines())
    lineaN = (a[-1]).strip("\n")
    url1 = requests.get(lineaN).text
    soup1 = BeautifulSoup(url1, "lxml")
    news = (soup1.find_all("h3", class_="teaser__title"))
    file = open("../txt/Texto de las noticias.txt", "w")
    for i in range (3):
        print(news[i].text)
        file.write(news[i].text + os.linesep)
    file.close()


def makeDir():
    if os.path.isdir("../txt") is not True:
        os.mkdir("../txt")
        print("SE HA CREADO LA CARPETA \"txt\"")
    else:
        print("TODAS LAS CARPETAS EXISTEN")

#Imprimir todos los archivos en la carpeta txt.
def printDir():
        for archivo in os.listdir("../txt"):
            if archivo.endswith(".txt"):
                print(archivo)

DIR_TXT = "../txt/"
def create():
    f=open("../txt/noticias.txt","w")
    f.write("https://onefootball.com/es/equipo/monterrey-1648"+"\n")
    f.close()
def edit(name, notas):
    ''' Abre un archivo elegido y le agrega al mismo líneas de código. '''
    archivo = open(DIR_TXT+name+".txt", 'a')
    archivo.write("\n"+notas)
    archivo.close()

def read(name):
    ''' Lee un archivo e imprime las líneas que contiene '''
    archivo = open(DIR_TXT+name+".txt",'r')
    print(archivo.readlines()[-1])
    archivo.close()



makeDir()
printDir()
create()
scrapNoticias()
