from scipy.fft import dct, idct
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

# A function that calculates inverse dct of a matrix
def blockIdct(block):
  return idct(idct(block.T, norm='ortho').T, norm='ortho')

# A function that compresses images
def compress(image, m):
    # Extract the number of columns and rows from the dimensions of the image
    rows, cols, = image.shape[0:2]

    # Calculating the dimensions of the new array and initialzing it
    newrows = rows / 8 * m
    newcols = cols / 8 * m
    compressed = np.zeros((int(newrows), int(newcols), 3), dtype=np.float16)

    # Changing range of values from 0-255 to (-128)-127
    image = image.astype('int16') - 128

    # Calculating DCT for the image
    # we calculate the DCT by slicing an 8x8 matrix and calculate its DCT matrix
    # and then slicing the top left mxm matrix from each block
    for i in range(0, int(rows/8)):
        for j in range(0, int(cols/8)):
            for k in range(3):

                # Calculating the indices on the compressed image
                newy = i*m
                newx = j*m

                # calculating the indices on the original image
                oldx = j*8
                oldy = i*8
                
                # Calculating the dct
                sliced = blockDct(image[oldy:oldy+8, oldx:oldx+8, k])
                
                # Slicing the top left mxm matrix
                sliced = sliced[0:m, 0:m]

                # Assiging the new dct values to the new image
                compressed[newy:newy+m, newx:newx+m, k] = sliced

                  

    return compressed



def decompress(compressed, m):
  rows, cols, = compressed.shape[0:2]
  originalRows = rows / m * 8
  originalCols = cols / m * 8

  original = np.zeros((int(originalRows), int(originalCols), 3), dtype=np.uint8)

  for i in range(0, int(rows/m)):
    for j in range(0, int(cols/m)):
      for k in range(3):
        comx = j * m
        comy = i * m

        orgx = j * 8
        orgy = i * 8

        retrieve = np.zeros((8,8))
        retrieve[0:m,0:m] = compressed[comy:comy+m, comx:comx+m, k]
        retrieve = blockIdct(retrieve) + 128
        retrieve = retrieve.clip(min=0, max=255)
        original[orgy:orgy+8, orgx:orgx+8, k] = retrieve
        

  return original

