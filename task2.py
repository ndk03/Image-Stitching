import cv2
import numpy as np
import random 

def solution(left_img, right_img):
	"""
	:param left_img:
	:param right_img:
	:return: you need to return the result image which is stitched by left_img and right_img
	"""
	img_ = right_img
	img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)
	img = left_img
	img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	sift = cv2.xfeatures2d.SIFT_create()
	p1, res1 = sift.detectAndCompute(img1,None)
	p2, res2 = sift.detectAndCompute(img2,None)

	bf = cv2.BFMatcher()
	matches = bf.knnMatch(res1,res2, k=3)
	perfect = []
	for m in matches:
		if m[0].distance < 0.5*m[1].distance:
			perfect.append(m)
			matches = np.asarray(perfect)
	if len(matches[:,0]) >= 4:
		src = np.float32([ p1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
		dst = np.float32([ p2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
		H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
	else:
		raise AssertionError("Can’t find enough keypoints.")
	dst = cv2.warpPerspective(img_,H,(img.shape[1] + img_.shape[1], img.shape[0]))
	dst[0:img.shape[0], 0:img.shape[1]] = img
	return dst
	
if __name__ == "__main__":
    left_img = cv2.imread('left.jpg')
    right_img = cv2.imread('right.jpg')
    result_image = solution(left_img, right_img)
    cv2.imwrite('results/task2_result.jpg',result_image)


