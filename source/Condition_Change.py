from Utilities 			import read_data_float
import os

def Change_eps(ieps):
	try:
		pID = os.environ['PBS_ARRAYID']
		num_points = read_data_float(tag_name='Number_of_points' , file_name='parameters/Initial_Condition/Gaussian.xml')
		end_eps = read_data_float(tag_name='Final_epsilon' ,file_name='parameters/Initial_Condition/Gaussian.xml')
		print 'success with reading in number of points = %f eeps = %f' %(num_points, end_eps)
		return ieps + (float(pID)-1)*((end_eps-ieps)/num_points)

	except KeyError:
		print("not a PBS array")
		return ieps

def Change_sigma(isigma):
	return isigma + (float(pID)-1)/(0.9/100)
