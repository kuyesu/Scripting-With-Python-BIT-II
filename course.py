# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:47:13 2022

@author: Tyrah
"""
import math

def  Area_of_circle():
   print("calculating the area of a circle")
   radius= float(input("Enter the radius of a circle"))
   print(radius)
   Area_of_circle=math.pi*radius**2
   print(Area_of_circle)

   cal()
  
  
def  Area_of_rectangle():
      print("calculating the area of a rectangle")
      length=int(input("Enter the value of the length"))
      Width=int(input("Enter the value of the width"))
      Area_of_rectangle=length*Width
      print(Area_of_rectangle)
   
   
def Volume_of_box():
      print("calculating the volume of a box")
      length=int(input("Enter the value of the length"))
      Width=int(input("Enter the value of the width"))
      height=int(input("Enter the value of the height"))
      Volume_of_box =length*Width*height
      print( Volume_of_box)
   
   
def  Volume_of_sphere():
      print("calculating the volume of sphere")
      radius= float(input("Enter the radius of a circle"))
      Volume_of_sphere=(4/3)*math.pi*radius*radius*radius
      print(Volume_of_sphere)
   

def cal():
      print ("******WELOCOME TO A GEOMETRY SOLVER!*******")
      
      #if choice1=="R"or choice1="r":
      print ("Press any key to continue")
      choice1=input()
      print("Lets  get started:")
      print("1)Area of a circle")
      print("2)Area of a rectangle")
      print("3)Volume of a box")
      print("4)Volume of a sphere")
      print("x) Exit")
      selection = (input("Please select an option:\n"))
      if int(selection)==1:
         Area_of_circle()
      elif selection==2:
         Area_of_rectangle()
      elif selection==3:
         Volume_of_box()
      elif selection==4:
         Volume_of_sphere()
      elif selection == "x":
         exit()
      else:
            print("Invalid option")  


cal()
