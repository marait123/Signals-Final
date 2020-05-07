import cv2
RGB = {'blue': 0, 'green':1, 'red':2}

def getImageComponent(compName, imageMat):
    """
    @summary: returns the image with all other components set to zero except the one needed
    """
    b = imageMat.copy()
    # set green and red channels to 0
    for i in range(3):
        if (i == RGB[compName.lower()]):
            continue
        b[:,:,i] = 0    
    return b
    
def imgDisplay(imageName, imageMat):
    cv2.imshow(imageName,imageMat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()