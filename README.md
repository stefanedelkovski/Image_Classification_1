# Image_Classification_1

## CNN Image Quality Classifier

### Overview

As a first solution to the Image Quality Classification problem, I provide you with a Machine Learning
approach, specifically in the domain of Computer Vision. This method uses a Laplacian filter in order to 
detect edges. As a return, we obtain a sharpness value for each image. Based on the mean between the maximum and 
the minimum sharpness value between two categories, two thresholds are generated. These thresholds serve as 
a delimiter, whether the image falls into one category or another. 


### Usage

If the thresholds are already saved, skip step number **2**.

1. Install the necessary requirements

`pip install -r requirements.txt`

2. Run the *define_thresholds.py* script to generate the thresholds for predictions

`python training.py`

3. Pass an image to the *classify_image.py* script, which outputs a category

`python classify_image.py --image 'PATH/TO/IMAGE'`

### Additional info

One simple explanation why this method works, is that all the categories have specific sharpness value distribution.

1. The mean of the sharpness value in the 'bad' images is **~1.90**

2. The mean of the sharpness value in the 'average' images is **~5.94**

3. The mean of the sharpness value in the 'bad' images is **~500.98**

Normal distribution as shown in the images:

![Figure_1](https://user-images.githubusercontent.com/74499280/142888810-e383c4c2-9b8d-4b15-9669-4a8d4b1b2649.png)
![Figure_2](https://user-images.githubusercontent.com/74499280/142889562-4e7a0472-7e23-44a3-a5c6-aafc8fda8f6d.png)
![Figure_3](https://user-images.githubusercontent.com/74499280/142889609-43ce5d41-1a57-44a7-94b0-f1668672ad2c.png)

If we compare the values from the X axis from these distributions, we can clearly conclude that there's a quality 
gap between the qualities of the photos. Simply by placing a threshold between the categories is sufficient to classify
image as bad, average or good. 
