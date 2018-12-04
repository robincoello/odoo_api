# -*- coding: iso-8859-15 -*-
import os

def create(file, content):
    file = open(file, "w")    
    file.write(content)
    file.close()

