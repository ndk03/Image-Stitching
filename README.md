# Image-Stitching and RANSAC
The goal of this task is to stitch two images of overlap into one image.To this end, you need to find feature points of interest in one image, and then find the corresponding ones in another image. After this, you can simply stitch the two images by aligning the matched feature points.

Ransac algorithm is used to  fit a line to the given points, and output the names of inlier points and outlier points for the line.
