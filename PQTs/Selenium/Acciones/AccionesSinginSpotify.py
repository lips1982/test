# -*- coding: utf-8 -*-

from os import access
import random
import time
from PQTs.Selenium.Base import BaseAcciones

from PQTs.Utilizar import urlSpotifysinginUS

from selenium.common import exceptions
from selenium.webdriver.common.by import By

class Acciones(BaseAcciones):

    def ingresarSpotify(self):
        self.ir('https://www.youtube.com/watch?v=SUuvxZGU73Q&list=PLFAs0FYFvieEFaVejGEf_0SYHEyOonzCy')

    
