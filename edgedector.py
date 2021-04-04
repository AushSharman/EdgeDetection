import pyautogui
from PIL import Image
import numpy as np

sobel_X = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
sobel_Y = np.matrix([[-1,-2,-1],[0,0,0],[1,2,1]])


#screenshot = pyautogui.screenshot("screenshot.png")
screenshot = Image.open("C:\\Users\\ayush\\Documents\\Python\\LearningPytohn\\EdgeDection\\Images\\eyes.jpg", "r")
image = screenshot.transpose(method=Image.FLIP_LEFT_RIGHT)

image = image.convert("L")     #Converting from RGB to Greyscale
pixel_data = image.load()   #Accessing pixels of the image

width,height = image.size   #Width and Height of the image

stop = 10000  
w = (width-1) % stop          # Get our own width dimensions (smaller makes edge detection shorter)
h = (height-1) % stop
print(f"Width:{width}\nHeight:{height}")

new_image = Image.new("L",(width,height),color=0)
new_data = new_image.load()

#loop through the entire picture 
for x in range(1,w-1):
    for y in range(1,h-1):
        top = [pixel_data[x+i,y-1] for i in range(-1,2,1)]
        middle = [pixel_data[x+i,y] for i in range(-1,2,1)]
        bottom = [pixel_data[x+i,y+1] for i in range(-1,2,1)]
        
        input_matrix = np.matrix([top,middle,bottom])
        
        product_X = (input_matrix[0,:]*sobel_X[:,0]) + (input_matrix[1,:]*sobel_X[:,1]) + (input_matrix[2,:]*sobel_X[:,2])
        #product_Y = abs(int(input_matrix[0,:]*sobel_Y[:,0]) + (input_matrix[1,:]*sobel_Y[:,1]) + (input_matrix[2,:]*sobel_Y[:,2]))

        new_data[x,y] = abs(int(product_X))
        #new_data[x,y] = abs(int(product_Y))

new_image.save("Edge.png")
new_image.show()

print(new_image.size)

#TODO: Addition of the Y axis too
#TODO: 