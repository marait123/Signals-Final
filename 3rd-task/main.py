import cv2
import utils
# part A: done read the image and display each of its components
image = cv2.imread('image1.bmp')
utils.imgDisplay('OriginalImage', image)
imgRedComponent = utils.getImageComponent('red', image)
utils.imgDisplay("red",imgRedComponent)
imgBlueComponent = utils.getImageComponent('blue', image)
utils.imgDisplay("blue",imgBlueComponent)
imgGreenComponent = utils.getImageComponent('green', image)
utils.imgDisplay("green",imgGreenComponent)
