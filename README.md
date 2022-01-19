## Photo Filter App using OpenCV
Photo Filter Application is Simple Application for filtering photo such as :
1. Contrast
2. Brightness
3. Filter
4. Color Scaling  


**Contrast**  
Adjust slider to right side to increase contrast and left side to decrease contrast  


**Brigthness**\
Slide to right side to increase brightness and left side to decrease brightness  


**Filter**  
Filter has many effect to apply :
> *Filter = 0* -> Identity Kernel, which mean the original photo\
> *Filter = 1* -> Smooth, make photo more smooth\
> *Filter = 2* -> Sharpen, make photo more sharp\
> *Filter = 3* -> Gaussian Kernel with kSize = 3 with Sigma = 0 (Blur)\
> *Filter = 4* -> Gaussian Kernel with kSize = 5 with Sigma = 0 (More Blur)\
> *Filter = 5* -> Outline, make photo to highlight the outline\
> *Filter = 6* -> Make photo more highlight the outline


**Color Scaling**\
This setting is to turn Photo color into :
> *Color = 0* -> Keep the photo in RGB Color\
*Color = 1* -> Turn photo into Grayscale\
*Color = 2* -> Turn photo into Inverted Color


