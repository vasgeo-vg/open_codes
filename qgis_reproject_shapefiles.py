import os
import processing
from qgis.core import *
from qgis.utils import iface
from PyQt5.QtCore import QVariant

def list_files(path, tipo):
    list = []
    for root, directory, files in os.walk(path):
        for file in files:
            if file.endswith(tipo):
                list.append(file)
    return list

def criar_pasta(path):
    if not os.path.exists(path + 'reproject'):
        os.makedirs(path + 'reproject')

def reproject(path, epsg):
    criar_pasta(path)
    for shape in list_files(path,'.shp'):
        inpath = path + shape
        outpath = path + '/reproject/' + str(epsg) + '_' + shape
        processing.run("native:reprojectlayer", 
                        {'INPUT':inpath,
                        'TARGET_CRS':QgsCoordinateReferenceSystem(f'EPSG:{epsg}'),
                        'OUTPUT':outpath})
    return

path = 'C:/Users/Name/Desktop/Shapefiles/'
reproject(path, 5880)