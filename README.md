# Image Search Using Clarifai

**Problem Statement:** Take around 2K images of wedding parties from the internet. Build a  text-based search engine using tags over those images. The tags for each image can be obtained using the Clarifai API.

**Prerequisites :**


pip install clarifai==2.0.9

You can get the id and secret from https://developer.clarifai.com and config them for client's use by

$ clarifai config

CLARIFAI_APP_ID: []: ************************************

CLARIFAI_APP_SECRET: []: ************************************


**Note:**
The prototype python script was tested for a single image but works as intended. 


**Description:
**

The script  intelligently distinguishes between an image url or a local directory of images that was passed to it as a command line argument. It then sends the images to Clarifai API one by one and records the response. The scripts iterates through the response and saves  the image location and the tags from the processed image into a sqlite database which can be easily queried.




**Usage :** python s1.py [pass a url/ local file / directory ]
