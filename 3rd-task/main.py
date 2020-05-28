import cv2
import utils
import numpy as np

# part A: done read the image and display each of its components
image = cv2.imread('image1.bmp')

utils.imgDisplay('OriginalImage', image)
imgRedComponent = utils.getImageComponent('red', image)
utils.imgDisplay("red", imgRedComponent)
cv2.imwrite("red-component.jpg", imgRedComponent)

imgBlueComponent = utils.getImageComponent('blue', image)
utils.imgDisplay("blue", imgBlueComponent)
cv2.imwrite("blue-component.jpg", imgBlueComponent)

imgGreenComponent = utils.getImageComponent('green', image)
utils.imgDisplay("green", imgGreenComponent)
cv2.imwrite("green-component.jpg", imgGreenComponent)


for m in [1,2,3,4]:
  # Compress the image
  compressedImage = utils.compress(image, m)

  np.save('image1.npy', image)
  np.save('decompressedm{}.npy'.format(m), compressedImage)

  decompressedImage = utils.decompress(compressedImage, m)
  cv2.imwrite('decompressedm{}.bmp'.format(m), decompressedImage)

  utils.imgDisplay('OriginalImage', decompressedImage)
  imgRedComponent = utils.getImageComponent('red', decompressedImage)
  utils.imgDisplay("red", imgRedComponent)
  imgBlueComponent = utils.getImageComponent('blue', decompressedImage)
  utils.imgDisplay("blue", imgBlueComponent)
  imgGreenComponent = utils.getImageComponent('green', decompressedImage)
  utils.imgDisplay("green", imgGreenComponent)

  #find and show the psnr
  psnr = 255 ** 2
  psnr = psnr / (np.square(np.subtract(image, decompressedImage)).mean())
  psnr = 10 * np.log10(psnr)
  print("at m="+str(m)+" PSNR="+str(psnr))
