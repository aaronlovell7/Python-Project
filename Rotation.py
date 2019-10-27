import numpy as np
import cv2


image = cv2.imread('Sample.jpg') #read the image's matrix


def rotate(matrix):  #create a function which allows user to rotate the image
    
    x=(input('Select the angle to rotate: (90 ,180 ,270 ,or mirror)\n')) #prompt the user to input the rotation angle              
    if x ==('mirror'): #if the input is 'mirror'
        matrix=matrix[::-1]  #reverse the matrix order
        for i in range(len(matrix)):    #the length of the matrix, the rows
            for j in range(i):   #the columns
               matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j] #swapping the values
               matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j] #swapping the values one more time because we are flipping it
               
        matrix=matrix[::-1] #reverse one more time because we had just flipped the image, but havent mirrored it
    
        for i in range(len(matrix)):
            for j in range(i):
               matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]  #turn the image 90 degrees
            
        matrix=matrix[::-1]

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] #turn the image another 90 degrees 
    if x==('90'):
        matrix=matrix[::-1]
        for i in range(len(matrix)):  #if we are rotating the image 90 degrees, run this for loop one time.
            for j in range(i):
               matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]
    if x==('180'):
        matrix=matrix[::-1]
        for i in range(len(matrix)):   #if we are rotating the image 180 degrees, run this for loop two times.
            for j in range(i):
               matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]
        matrix=matrix[::-1]
    
        for i in range(len(matrix)):
            for j in range(i):
               matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] 
               
    if x==('270'):
        matrix=matrix[::-1]
        for i in range(len(matrix)): #if we are rotating the image 270 degrees, run this for loop three times.
            for j in range(i):
               matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]
        matrix=matrix[::-1]
    
        for i in range(len(matrix)):
            for j in range(i):
               matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] 
        matrix=matrix[::-1]
        for i in range(len(matrix)):
            for j in range(i):
               matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]
               
    else:
        print("Please enter a valid input!")
    
           
    return matrix

io=image.tolist()  #turn the matrix intolists
t=(rotate(io)) #rotate the image by using the function we had created
    
x=np.uint8(t) #change the list into uint8 type

#plt.imsave('Sample_copy2.jpg',x)
cv2.imwrite('Output.jpg', x) #save the image
outimage=cv2.imread('Output.jpg') #read the rotated image
cv2.imshow('rotation_output', outimage) #output and show the rotated image
cv2.waitKey(0)
cv2.destroyAllWindows()

