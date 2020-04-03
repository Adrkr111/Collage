# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:32:59 2020

@author: Aindril_kar(ADR_7)
"""

import random
import os
from PIL import Image
import numpy as np
fl=os.listdir(r"D:\collarge")#getting the images
path="D:\collarge" #storing the path
k=1
while(k<=5):    #simulating to create more replicas incase you have less images
    fl+=fl
    #fl.remove(np.random.choice(fl))
    k+=1
k=1
while(k<=92):
    #fl+=fl
    fl.remove(np.random.choice(fl))
    k+=1
random.shuffle(fl)  #shuffling the images
nim=Image.new("RGBA",(3200,3200))  #creating a new image of given size
nim.show()
c=0
for i in range(0,3200,64):        #Creating the collage
    for j in range(0,3200,64):
        im=Image.open(path+"\\"+fl[c])
        im=im.resize((64,64))
        nim.paste(im,(j,i))
        c+=1

n=Image.open(r"D:\collarge\IMG_20190317_094236.jpg")  #getting the final image to be formed
n=n.resize((3200,3200))
n=n.convert("RGBA")
n3=Image.blend(nim,n,.59999) #creating the final image
n3.show()
n3=n3.convert("RGB")
n3.save(r"D:\main\output1.jpg")  #saving it.