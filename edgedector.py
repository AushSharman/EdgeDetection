import pyautogui
import PIL
import numpy as np

screen_cap = pyautogui.screenshot("screenshot.png")

flip = screen_cap.transpose(method=PIL.Image.FLIP_TOP_BOTTOM)

pixel_data = flip.load() # Loads the image into a list variable we can change.

width,height = flip.size    #Size of the image in pixels taken from PIL

print(f"W: {width}\nH: {height}")



sobel_X = np.matrix([[1,0,-1],[2,0,-2],[1,0,-1]])
sobel_Y = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])

flip = flip.convert("L")    #RGB to GreyScale

for x in range(1,width,1):
    for y in range(1,height,1):
        top = [pixel_data[x+i, y-1] for i in range(-1, 2, 1)]   # Creates a list of the 3 pixels above left middle and right of the pixel the loop is on.
        mid = [pixel_data[x+i, y] for i in range(-1, 2, 1)]     #                   "            beside                 "
        bot = [pixel_data[x+i, y+1] for i in range(-1, 2, 1)]   #                   "            below                  "

#        pixel_matrix = np.matrix([top, mid, bot])               # Create a numpy matrix with these 3 lists.
        print(top,mid,bot)
        break
    break



#flip.save("flipped_with_red.png")