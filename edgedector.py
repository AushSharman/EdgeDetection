import pyautogui
import PIL
import numpy as np

sobel_X = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
sobel_Y = np.matrix([[-1,-2,-1],[0,0,0],[1,2,1]])


screenshot = pyautogui.screenshot("screenshot.png")
image = screenshot.transpose(method=PIL.Image.FLIP_LEFT_RIGHT)

image = image.convert("L")     #Converting from RGB to Greyscale
pixel_data = image.load()   #Accessing pixels of the image

width,height = image.size   #Width and Height of the image

print(f"Width:{width}\nHeight:{height}")

new_image = PIL.Image.new("L",(width,height),color=0)
new_data = new_image.load()

#loop through the entire picture 
for x in range(1,width-1):
    for y in range(1,height-1):
        top = [pixel_data[x+i,y-1] for i in range(-1,2,1)]
        middle = [pixel_data[x+i,y] for i in range(-1,2,1)]
        bottom = [pixel_data[x+i,y+1] for i in range(-1,2,1)]
        
        input_matrix = np.matrix([top,middle,bottom])
        product = (input_matrix[0,:]*sobel_X[:,0]) + (input_matrix[1,:]*sobel_X[:,1]) + (input_matrix[2,:]*sobel_X[:,2])

        new_data[x,y] = (abs(int(product)))

image.save("pic.png")
new_image.save("Edge.png")
new_image.show()