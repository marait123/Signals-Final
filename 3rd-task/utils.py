from scipy.fft import dct
import cv2
import numpy as np

RGB = {'blue': 0, 'green': 1, 'red': 2}


def getImageComponent(compName, imageMat):
    """
    @summary: returns the image with all other components set to zero except the one needed
    """
    b = imageMat.copy()
    # set green and red channels to 0
    for i in range(3):
        if (i == RGB[compName.lower()]):
            continue
        b[:, :, i] = 0
    return b


def imgDisplay(imageName, imageMat):
    cv2.imshow(imageName, imageMat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# A function that calculates the dct transform of a given matrix
def blockDct(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

# A function that compresses images
def compress(image, m):
    # Extract the number of columns and rows from the dimensions of the image
    rows, cols, = image.shape[0:2]

    # Calculating the dimensions of the new array and initialzing it
    newrows = rows / 8 * m
    newcols = cols / 8 * m
    newImage = np.zeros((int(newrows), int(newcols), 3))

    # Changing range of values from 0-255 to (-128)-127
    image = image.astype('int16') - 128

    # Calculating DCT for the image in place
    # we calculate the DCT by slicing an 8x8 matrix and calculate its DCT matrix
    for i in range(0, rows, 8):
        for j in range(0, cols, 8):
            for k in range(3):
                image[i:i+8, j:j+8, k] = blockDct(image[i:i+8, j:j+8, k])

  # Slicing the top left mxm matrix from each block
    for i in range(0, int(rows/8)):
        for j in range(0, int(cols/8)):
            for k in range(3):
                newy = i*m
                newx = j*m
                oldx = j*8
                oldy = i*8
                newImage[newy:newy+m, newx:newx+m,
                         k] = image[oldy:oldy+m, oldx:oldx+m, k]
    return newImage

