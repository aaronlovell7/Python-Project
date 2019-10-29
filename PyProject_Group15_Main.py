#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	
Assignment Information
	Assignment:     Py4_PA Task 2
	Author:         Heath Aaron Lovell, hlovell@purdue.edu
	Team ID:        003-15 (e.g. 001-14 for section 1 team 14)
	
Contributor:    N/A [repeat for each]
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
import cv2
import os.path # checking that the file exists
import PyProject_Group15_Rotation as rot
import PyProject_Group15_Smoothing as smooth
import PyProject_Group15_Grayscale as gray

inputImageFName = str(input("Enter image file name to edit: "))

while os.path.exists(inputImageFName) == False:
    print("Incorrect file name or type. Please enter a correct one:")
    inputImageFName = str(input())

def initial():
    inputImage=cv2.imread(inputImageFName)
    
    print ("What filter would you like to add?:")
    print ("1-Grayscale")
    print ("2-Mirror image")
    print ("3-Rotate image")
    print ("4-Smooth image")
    inputChoice=int(input("Enter option desired: "))
    while inputChoice != 1 and inputChoice != 2 and inputChoice != 3 and inputChoice != 4:
        print("Invalid input choice. Please enter a correct input: ")
        inputChoice = int(input())
    if inputChoice == 1:
        gray.grayscale(inputImage)
    elif inputChoice == 2:
        rot.rotate(inputImageFName, 'mirror')
    elif inputChoice == 3:
        angle = str(input("Enter what angle you want to rotate the image: "))
        while angle != '90' and angle != '180' and angle != '270':
            angle = str(input("Wrong angle entered. Please enter the correct angle:"))
        rot.rotate(inputImageFName, angle)
    elif inputChoice == 4:
        smooth.smoothImage(inputImage, inputImageFName)
    
    
initial()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''






