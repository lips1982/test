# -*- coding: utf-8 -*-
#TESTTTTT

import datetime
import time
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesSinginSpotify import Acciones
from threading import Thread, Barrier

password='!asdf2021'
hilos=5
start=time.time()
start1=time.time()

def accountsSpotify():

    id=[]
    email =[]
    

    db=MongoDB(hilos)
    db.iniciarDB()
    for elem in (db.findby1("accountmanager","acc_estado",1)):
        email.append(elem["email"])
        id.append(elem["_id"])
    
    for elemid in id:
        db.updateOne("accountmanager",elemid,"creacionlistasentrenamiento",2)
        #db.insertOne("statusconexion",{"_id":elemid, "statusloging":"Conexion Exitosa","ultimaconexion":str(datetime.datetime.now().strftime("%H-%M-%S")),"horasactivo":0}) 
        db.updateOne3("statusconexion",elemid, "statusloging","TOPSECRET","ultimaconexion",str(datetime.datetime.now().strftime("%H-%M-%S")),"horasactivo",0) 
        
    db.cerrarConexion()
    return email, id

users, id= accountsSpotify()
print (len(users))
    
def iniciarSpotify(barrier,id,start):

    
    driver = BaseConexion().conexionChrome()
    #driver = BaseConexion().conexionChromeHeadless()

    acciones = Acciones(driver)
    try:
        acciones.ingresarSpotify()
    except:
        driver.refresh()
        acciones.ingresarSpotify()

    db=MongoDB()

    contadortime=180
    endtime= time.time()
    while endtime-start<contadortime:
        time.sleep(178)
        endtime=time.time()
        contadortime+=180
        print(endtime-start,contadortime)
        db.iniciarDB()
        db.updateOne("statusconexion",id,"horasactivo",endtime-start)
        db.cerrarConexion()
        if endtime-start>3440:
            db.iniciarDB()
            print(endtime-start,contadortime)
            db.updateOne("statusconexion",id,"horasactivo",endtime-start)
            db.cerrarConexion()
            break

        
    print (f"Account {i} lista de reproduccion de entrenamiento creada ok")
    # 


barrier = Barrier(len(users))
hiloscerrados = 0
threads = []
for i in range(len(users)):
    i = Thread(target=iniciarSpotify, args=(barrier,id[i],start))
    i.start()
    threads.append(i)

for i in threads:
	i.join()
 
#iniciarSpotify()


