#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	creates function that smooths an image using 5x5

Assignment Information
	Assignment:     Python Project
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
#Imports libraries needed for this function
import cv2
from PIL import Image


def smoothImage(image, imageFName):         #define smoothImage function with arguments of image and imageFName
    height, width = image.shape[:2]         #sets width and height to the width and height of the image
    smoothedImage = cv2.imread(imageFName)  #initialize smoothed image
    
    for y in range(0, width-2):             #For loop, iterates through each column
        for x in range(0, height-2):        #For loop, iterates through each row
            totalAvg = 0                    #Initiates totalAvg variable
            
            #x = 0
            px1 = image[x-2][y-2]           #0/0
            px2 = image[x-2][y-1]           #0/1
            px3 = image[x-2][y]             #0/2
            px4 = image[x-2][y+1]           #0/3
            px5 = image[x-2][y+2]           #0/4
            
            #x = 1
            px6 = image[x-1][y-2]           #1/0
            px7 = image[x-1][y-1]           #1/1
            px8 = image[x-1][y]             #1/2
            px9 = image[x-1][y+1]           #1/3
            px10 = image[x-1][y+2]          #1/4
            
            #x = 2
            px11 = image[x][y-2]            #2/0
            px12 = image[x][y-1]            #2/1
            px13 = image[x][y]              #2/2
            px14 = image[x][y+1]            #2/3
            px15 = image[x][y+2]            #2/4
            
            #x = 3
            px16 = image[x+1][y-2]          #3/0
            px17 = image[x+1][y-1]          #3/1
            px18 = image[x+1][y]            #3/2
            px19 = image[x+1][y+1]          #3/3
            px20 = image[x+1][y+2]          #3/4
            
            #x = 4
            px21 = image[x+2][y-2]          #4/0
            px22 = image[x+2][y-1]          #4/1
            px23 = image[x+2][y]            #4/2
            px24 = image[x+2][y+1]          #4/3
            px25 = image[x+2][y+1]          #4/4
            
            #creates array of all pixels for each 5x5
            pixels = [px1,px2,px3,px4,px5,
                      px6,px7,px8,px9,px10,
                      px11,px12,px13,px14,px15,
                      px16,px17,px18,px19,px20,
                      px21,px22,px23,px24,px25]
            
            #calculates the average of the 9 pixels in the current 5x5
            for i in range(25):
                totalAvg = totalAvg + pixels[i]/25 

            #sets the [2,2] pixel in the 5x5 (the middle pixel) to the average previously calculated
            smoothedImage[x][y] = totalAvg

    outputImage = Image.fromarray(smoothedImage)    #creates outputImage
    #outputImage.save('Group15_Output.jpg')
    #outputImage.show()
    return outputImage

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''