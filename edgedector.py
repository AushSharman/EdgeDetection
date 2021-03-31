import pyautogui
import PIL

screen_cap = pyautogui.screenshot("screenshot.png")

flip = screen_cap.transpose(method=PIL.Image.FLIP_TOP_BOTTOM)

pixel_data = flip.load()

width,height = flip.size

print(f"W: {width}\nH: {height}")