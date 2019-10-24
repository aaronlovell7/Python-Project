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
from PyProject_Group15_Smoothing import smoothImage as smooth

inputImageFName = "graytestreal2.jpg" #input("Enter the name of the image you want to filter: ")
image = cv2.imread(inputImageFName) #import image


outputImage = smooth(image, inputImageFName)
outputImage.save('OutputImage.jpg')
outputImage.show()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''