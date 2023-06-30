# 3D-reconstruction

This project demonstrates a pipeline for 3D reconstruction using a series of images. The pipeline is integrated into a Flask application that allows users to upload the images and obtain a 3D reconstruction as an OBJ file.

For the setup, there are two options 
1. Perform camera calibration using a calibration pattern or known geometry to estimate the camera parameters. This step is crucial for accurate reconstruction.
2. Take the images and use a feature extraction algorithm such as SIFT to extract features. 

## Pipeline Steps

## 1. Image Acquisition
Capture a series of images from different viewpoints. Ensure sufficient coverage and overlap between the images to facilitate accurate reconstruction.

## 2. Feature Extraction
Detect and extract distinctive features from the images. Use feature extraction algorithms like SIFT, SURF, or ORB to identify key points or regions.

### Scale Invariant Feature Transform(SIFT)

Transforms image data into scale-invariant coordinates relative to local features.

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

### Finding keypoints
The Laplacian of Gaussian (LoG) approximations are derived from the DoG images. The LoG is obtained by calculating the Laplacian operator on the DoG images. The Laplacian operator is a filter used to enhance edges and other features in an image.

The significance of using the DoG and LoG approximations is that they provide scale invariance, meaning they can detect and describe image features regardless of their size or scale<br>
One pixel in an image is compared with its 8 neighbors as well as 9 pixels in the next scale and 9 pixels in previous scales. This way, a total of 26 checks are made. If it is a local extrema, it is a potential keypoint. It basically means that keypoint is best represented in that scale.
![image](https://github.com/kaburia/3D-reconstruction/assets/88529649/a9398a9b-4f6c-460c-878d-47b45421c7b9)



- Keypoint Localization: Accurately locating the feature keypoints

The keypoints generated, some of them lie along an edge, or they don't have enough contrast making them not very useful as features.<br>
Harris corner detector: A corner detection operator used to extract corners and infer features of an image.
For those with low contrast, to adjust their intensities.
A Taylor Series expansion of scale space to get a more accurate location of extrema, and if the intensity at the extrema is less than a threshold value it is rejected.
DoG has a higher response for edges hence the need for a Hessian matrix to compute the principal curvature (2x2 matrix)


- Orientation Assignment: Assigning orientation to keypoints

With the stable keypoints, the next thing is to assign an orientation to each keypoint to make it rotation invariance.
The scale at which the keypoint is detected is the same scale as of the blurred image.<br>
A neighbourhood is taken around the keypoint location depending on the scale and the gradient magnitude and direction is calculated in that region.
  
- Keypoint descriptor: Describing the keypoints as a high dimensional vector
- Keypoint Matching

## 3. Feature Matching
Match corresponding features across the images to establish correspondences. This step helps determine the camera poses and the 3D structure of the object.

### RANSAC Algorithm
The RAndom SAmple Consensus Algorithm is an iterative algorithm which will be used to estimate the parameters of a statistical model from a set of observed data which contains outliers. This is an outlier detection method



### . Structure from Motion (SfM)
Apply structure from motion techniques to estimate camera poses and the 3D structure of the object based on the feature correspondences. Libraries like OpenCV or VisualSFM can assist with SfM.

### 6. Dense Reconstruction
Utilize the estimated camera poses and the feature correspondences to perform dense reconstruction, estimating the depth or 3D position for each pixel in the images. Algorithms like Multi-View Stereo (MVS) or depth estimation from stereo matching can be used for this step.

### 7. Mesh Reconstruction
Generate a mesh representation of the 3D object from the dense reconstruction results. This step involves surface reconstruction algorithms like Poisson reconstruction or marching cubes.



