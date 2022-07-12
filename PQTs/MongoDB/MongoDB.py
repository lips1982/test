# -*- coding: utf-8 -*-

import pymongo

from PQTs.Utilizar import UrlDB, accountsDB

class MongoDB:
    
    def __init__(self,hilos=1):
        self.hilos=hilos
        self.UrlDB = UrlDB
        self.Client = None
        self.DB = None
        self.accountsDB=accountsDB

    def iniciarDB(self):
        self.Client = pymongo.MongoClient(self.UrlDB)
        self.DB = self.Client[self.accountsDB]


    def insertOne(self,coleccion,dato):
        self.DB[coleccion].insert_one(dato)

    def insertMany(self,coleccion,dato):
        self.DB[coleccion].insert_many(dato)

    def findby1(self,coleccion,clave, valor):
        return list(self.DB[coleccion].find({clave:valor}).limit(self.hilos))

    def findby2(self,coleccion,clave1, valor1,clave2,valor2):
        return list(self.DB[coleccion].find({clave1:valor1},{clave2:valor2}).limit(self.hilos))


    def updateOne1(self,coleccion,id,clavevalor):
        self.DB[coleccion].update_one({"_id":id},{"$set":{clavevalor}})

    def updateOne(self,coleccion,id,clave,valor):
        self.DB[coleccion].update_one({"_id":id},{"$set":{clave:valor}})

    def updateOne3(self,coleccion,id,clave1,valor1,clave2,valor2,clave3,valor3):
        self.DB[coleccion].update_one({"_id":id},{"$set":{clave1:valor1,clave2:valor2,clave3:valor3}})

    def cerrarConexion(self,):
        self.Client.close()