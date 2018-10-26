import numpy as np
import cv2
from PIL import ImageGrab as ig
import pyautogui

total = 255*40*40


def predict(im):

	gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

	image = cv2.resize(255-gray_im, (40, 40))
	cv2.imwrite('gray_image.png',image)



	on_pixel = image.sum() 
	percentage = (on_pixel/ total) * 100

	if percentage < 80:
		return percentage
	else:
		return 100 - percentage


	print(percentage)





while(True):
	screen = ig.grab(bbox=(390,180,525,275))
	prediction = predict(np.array(screen))
	if prediction > 5:
		pyautogui.keyDown("space")
		pyautogui.keyUp("space")
		print("{} Jump".format(prediction))



