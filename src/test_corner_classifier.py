import pickle
import cv2
import CVAnalysis 

if __name__ == "__main__":

	#=====[ Step 1: load in an image	]=====
	image = cv2.imread ('../data/p1/5.jpg')

	#=====[ Step 2: get corners, descriptors	]=====
	hc = CVAnalysis.get_harris_corners (image)
	# sd = CVAnalysis.get_sift_descriptors (image, hc)

	# pickle.dump(sd, open('test.sd', 'w'))
	# sd = pickle.load (open('test.sd', 'r'))

	#=====[ Step 3: load in classifier, predict	]=====
	# clf = pickle.load (open('../data/classifiers/corner_classifier.clf', 'r'))
	# print clf.predict (sd)
	# predictions = clf.predict (sd)
	# pickle.dump (predictions, open('test_predictions.pkl','w'))
	predictions = pickle.load (open('test_predictions.pkl', 'r'))