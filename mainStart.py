# -*- coding: utf-8 -*-
#TESTTTTT

import datetime
import time
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesSinginSpotify import Acciones
from threading import Thread, Barrier


hilos=1
#hilos

db=MongoDB()
db.iniciarDB()
KEY_ACCESS="REEMPLAZARKEY_ACCESS"
accname="REEMPLAZARACCNAME"
try:                                                #{ {d1:v1},{d2:v2},{}}
    db.insertOne('neverinstall_loging_log',{"KEY_ACCESS":KEY_ACCESS,"accname":accname,"datalog":str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))}) 
except:
    pass
db.cerrarConexion()

 
#iniciarSpotify()


