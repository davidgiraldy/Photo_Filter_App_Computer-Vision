import cv2
import numpy as np

def null(*args):
    pass

# Source Kernel : https://towardsdatascience.com/basics-of-kernels-and-convolutions-with-opencv-c15311ab8f55

identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
box_kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.float32)/9.0
outline_kernel = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]])
gaussian_kernel1 = cv2.getGaussianKernel(3, 0)
gaussian_kernel2 = cv2.getGaussianKernel(5, 0)
sobel_kernel = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
kernels = [identity_kernel, box_kernel, sharpen_kernel, gaussian_kernel1, gaussian_kernel2, outline_kernel, sobel_kernel]

# Read Image yang mau di edit
input_image = cv2.imread('Dataset/yurina.jpg')
invert_image = cv2.bitwise_not(input_image)
gray_convert = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Membuat Window (User Interface)
cv2.namedWindow('Slider')
cv2.resizeWindow('Slider', 800, 150)
cv2.namedWindow('Image', cv2.WINDOW_FREERATIO)

# Mengatur Window Image untuk mengikuti ukuran foto
h,w,_ = input_image.shape
if(w > 1000 and h > 1000):
    h = int(h*30/100)
    w = int(w*30/100)
# print(h,w)
cv2.resizeWindow('Image', w, h)

# trackBarName, windowName, startValue, maxValue, onChange (event handle)
cv2.createTrackbar('Contrast', 'Slider', 500, 1000, null)
cv2.createTrackbar('Brightness', 'Slider', 500, 1000, null)
cv2.createTrackbar('Filter', 'Slider', 0, len(kernels)-1, null) #update nilai max dari filter
cv2.createTrackbar('Color', 'Slider', 0, 2, null)

count = 1
while True :
    # TODO : getTrackbarPos take int from slider
    grayscale = cv2.getTrackbarPos('Color','Slider')
    contrast = cv2.getTrackbarPos('Contrast', 'Slider')
    brightness = cv2.getTrackbarPos('Brightness', 'Slider')
    kernel_idx = cv2.getTrackbarPos('Filter', 'Slider')
    
    # TODO : apply the filters from kernels list
    color = cv2.filter2D(input_image, -1, kernels[kernel_idx])
    gray = cv2.filter2D(gray_convert, -1, kernels[kernel_idx])
    invert = cv2.filter2D(invert_image, -1, kernels[kernel_idx])
    
    # TODO : apply the brightness and contrast from slider value
    color = cv2.addWeighted(color, contrast/500, (input_image), 0, brightness//10 - 50)
    gray = cv2.addWeighted(gray, contrast/500, (gray_convert), 0, brightness//10 - 50)
    invert = cv2.addWeighted(invert_image, contrast/10, (invert_image), 0, brightness//10 - 50)
    
    # function to save the current edit and to end windows
    key  = cv2.waitKey(100)
    if key == ord('q'):
        break
    elif key == ord('s'):
        # Save image
        if grayscale == 0:
            cv2.imwrite('Output Data/edited_{}.png'.format(count), color)
        elif grayscale == 1:
            cv2.imwrite('Output Data/edited_{}.png'.format(count), gray)
        else:
            cv2.imwrite('Output Data/edited_{}.png'.format(count), invert)
        count += 1

    # plot the image
    if grayscale == 0:
        cv2.imshow('Image', color)
    elif grayscale == 1:
        cv2.imshow('Image', gray)
    else:
        cv2.imshow('Image', invert)

cv2.destroyAllWindows()
