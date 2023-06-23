# 3D-reconstruction

This project demonstrates a pipeline for 3D reconstruction using a series of images. The pipeline is integrated into a Flask application that allows users to upload the images and obtain a 3D reconstruction as an OBJ file.

## Pipeline Steps

## 1. Image Acquisition
Capture a series of images from different viewpoints. Ensure sufficient coverage and overlap between the images to facilitate accurate reconstruction.

## 2. Feature Extraction
Detect and extract distinctive features from the images. Use feature extraction algorithms like SIFT, SURF, or ORB to identify key points or regions.

### Scale Invariant Feature Transform(SIFT)

- Scale-space peak selection: Potential Location for finding features.<br>

The scale space of an image is a function L(x,y,σ) that is produced from the convolution of a Gaussian kernel(Blurring) at different scales with the input image. Scale space is separated into octaves and the number of octaves and scale depends on the size of the original image. So we generate several octaves of the original image. Each octave’s image size is half the previous one.

### Blurring

Images are progressively blurred using the Gaussian Blur operator. The convolution of the Gaussian operator and the image.
Gaussian Blur has a particular expression applied to each pixel

### Difference of Gaussians
Used to find out interesting keypoints in the image

The Difference of Gaussians (DoG) is a method used for image processing and feature detection. It involves subtracting an image convolved with a Gaussian of a wider standard deviation from the image convolved with a Gaussian of a narrower standard deviation.<be>
The DoG function is defined as:

Γ_σ₁,σ₂ = I * G_σ₁ - I * G_σ₂

Where:
- Γ_σ₁,σ₂: DoG function obtained by subtracting two convolutions
- I: Input image
- *: Convolution operation
- G_σ₁: Gaussian function with standard deviation σ₁
- G_σ₂: Gaussian function with standard deviation σ₂

This form indicates that the DoG is obtained by convolving the image with the difference between two Gaussian functions.

The DoG helps enhance certain features by emphasizing the differences between scales in the image.

- Keypoint Localization: Accurately locating the feature keypoints
- Orientation Assignment: Assigning orientation to keypoints
- Keypoint descriptor: Describing the keypoints as a high dimensional vector
- Keypoint Matching

## 3. Feature Matching
Match corresponding features across the images to establish correspondences. This step helps determine the camera poses and the 3D structure of the object.

### 4. Camera Calibration
Perform camera calibration using a calibration pattern or known geometry to estimate the camera parameters. This step is crucial for accurate reconstruction. OpenCV provides functions for camera calibration.

### 5. Structure from Motion (SfM)
Apply structure from motion techniques to estimate camera poses and the 3D structure of the object based on the feature correspondences. Libraries like OpenCV or VisualSFM can assist with SfM.

### 6. Dense Reconstruction
Utilize the estimated camera poses and the feature correspondences to perform dense reconstruction, estimating the depth or 3D position for each pixel in the images. Algorithms like Multi-View Stereo (MVS) or depth estimation from stereo matching can be used for this step.

### 7. Mesh Reconstruction
Generate a mesh representation of the 3D object from the dense reconstruction results. This step involves surface reconstruction algorithms like Poisson reconstruction or marching cubes.



