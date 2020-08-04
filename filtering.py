from skimage.exposure import rescale_intensity
import numpy as np
import cv2 as cv
# import argparse

im = cv.imread('pokemon1.jpg')
b, g, r = cv.split(im)
gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)




# Kernel masks declarations
vsob_k = np.array(([1, 0, -1], [2, 0, -2], [1, 0, -1]), dtype='int')
hsob_k = np.array(([1, 2, 1], [0, 0, 0], [-1, -2, -1]), dtype='int')
hpf1_k = np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), dtype='int')
hpf2_k = np.array(([1, -2, 1], [-2, 5, -2], [1, -2, 1]), dtype='int')
lpf1_k = np.ones([3, 3], dtype='float') * (1.0/(3.0*3.0))
lpf2_k = np.ones([5, 5], dtype='float') * (1.0/(5.0*5.0))
gauss_k = np.array(([1, 2, 1], [2, 4, 2], [1, 2, 1]), dtype='int')


# Bank of kernels used to filtering - dictionary
kernels = {'hpf1': hpf1_k,
           'hpf2': hpf2_k,
           'lpf1': lpf1_k,
           'lpf2': lpf2_k,
           'sobelx': hsob_k,
           'sobely': vsob_k,
           'gauss': gauss_k,
           }


# Function that will convolute image with kernel.
# The function is supposed to operate on 2 dimensional arrays, so we probably should operate on grayscale but...
# Look at the explanation of filtering process mentioned in line 52.
def convolution(image, kernel):
    (im_h, im_w) = image.shape[:2]      # Take the spatial dimensions of image
    (ke_h, ke_w) = kernel.shape[:2]     # Take the spatial dimensions of kernel
    padding = (ke_w - 1) // 2           # Set padding according to kernels dimensions
    image = cv.copyMakeBorder(image, padding, padding, padding, padding, cv.BORDER_REPLICATE)  # Add padding borders
    output = np.zeros((im_h, im_w), dtype='float32')    # Declare and initiate output as array filled with 0s
    for y in np.arange(padding, im_h + padding):        # Here we go across whole image "sliding" the kernel
        for x in np.arange(padding, im_w + padding):    # through it to calculate new values
            roi = image[y - padding:y + padding + 1, x - padding:x + padding + 1]   # Extract region of interest
            k = (roi * kernel).sum()                    # Perform convolutions between img and kernel
            output[y - padding, x - padding] = k        # Save conv product as output excluding paddings
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype('uint8')             # Rescale output values to 8 bit values
    return output


# The whole trick is that in the line 7 we split our 3-dimensional array (width,height,rgb)
# to 3 2-dimensional arrays containing color chromas!
# Next, below we will filter each of those chromas patterns and merge them to obtain filtering an image in color.
def rgb_conv(blue, green, red, kernel):
    b1 = convolution(blue, kernel)
    g1 = convolution(green, kernel)
    r1 = convolution(red, kernel)
    return cv.merge((b1, g1, r1))


convout = rgb_conv(b, g, r, kernels['sobely'])
cvout = cv.filter2D(im, -1, kernels['sobely'])
cv.imshow('Original', im)
cv.imshow("Convolution function", convout)
cv.imshow("Filter2D openCV", cvout)
cv.waitKey(0)
cv.destroyAllWindows()





