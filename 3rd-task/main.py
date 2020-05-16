import cv2
import utils
import numpy as np

# part A: done read the image and display each of its components
image = cv2.imread('image1.bmp')

# Get the value of m from the user
while True:
  m = input('Please enter the value of m (a value from 1 to 4)\n')
  if m in ['1','2','3','4']:
    break

m = int(m)
# Compress the image
compressedImage = utils.compress(image, m)

np.save('image1.npy', image)
np.save('decompressedm{}.npy'.format(m), compressedImage)

decompressedImage = utils.decompress(compressedImage, m)
cv2.imwrite('decompressedm{}.bmp'.format(m), decompressedImage)

utils.imgDisplay('OriginalImage', image)
imgRedComponent = utils.getImageComponent('red', image)
utils.imgDisplay("red",imgRedComponent)
imgBlueComponent = utils.getImageComponent('blue', image)
utils.imgDisplay("blue",imgBlueComponent)
imgGreenComponent = utils.getImageComponent('green', image)
utils.imgDisplay("green",imgGreenComponent)
