def Create_data(Grav_obj):
	print "\n\ncreating datalog\n\n"
	f = open('datalog.txt', 'w')
	
	f.write('Field properties\n')
	f.write('\tGeometry: %s \n' %(Grav_obj.Geometry_type_name))
	f.write('\tCosmological constant = %f \n' %(Grav_obj.Cosmological_cosntant))

	if Grav_obj.field.Horizon:
		f.write('\nHorizon Conditions\n')
		f.write('\tTime of horizon = %.12f seconds \n' %(Grav_obj.field.time))
		f.write('\tRadius of Horizon = %.12f \n' %(Grav_obj.field.Horizon_r))
		
	f.write('\nPotential Conditions\n')
	f.write('\tPotential = %s \n' %(Grav_obj.Potential_type_name))

	f.write('\nInitial Conditions\n')
	f.write('\tInitial Conditional = %s \n' %(Grav_obj.Initial_Condition_type_name))
	
	if Grav_obj.Initial_Condition_type_name == 'Gaussian':
		f.write('\tInitial epsilon = %.12f \n' %(Grav_obj.initial_eps))
		f.write('\tInitial sigma = %.12f \n' %(Grav_obj.initial_sigma))

	f.write('\nNumerical Method\n')
	f.write('\tSolver : %s \n' %(Grav_obj.Solver_type_name))
	f.write('\tGrid Size: %f \n' %(Grav_obj.Grid_size))

	f.write('\nEnding Conditions\n')
	f.write('\tHorizon Condition: %.12f \n' %(Grav_obj.A_min))
	f.write('\tMax iterations: %f \n' %(Grav_obj.Max_interation))
	f.close
	
	if Grav_obj.pbs_arr:
		f2 = open('times%3f'%(float(pbID)), 'w')
		f3 = open('eps%3f'%(float(pbID)), 'w')
		f4 = open('radius%3f'%(float(pbID)), 'w')
		if Grav_obj.field.Horizon:
			f2.write('%3f \n'%(float(pbID)))
			f2.write('%.12f\n' %( Grav_obj.field.time))	
		
			f3.write('%3f \n'%(float(pbID)))
			f3.write('%.12f\n' %(Grav_obj.initial_eps))
	
			f4.write('%3f \n'%(float(pbID)))
			f4.write('%.12f\n' %(float(Grav_obj.field.Horizon_r)))
		f2.close
		f3.close
		f4.close
#	if Grav_obj.output.Power_Spectrum_status:
#		if Grav_obj.pbs_arr:
#			f5 = open('pspectrum%3f'(float(pbID)), 'w')
#		else:
#			f5 = open('pspectrum', 'w')
#		f5.write('r\t\tn\n')
#		for i in range(Grav_obj.output.Power_Spectrum_points):
#			f5.write('%12f\t'%(Grav_obj.field.r[i]))
#			f5.write('%12f\n'%(Grav_obj.field.Power_Spec_n[i]))
#		f5.close

def Pspec_data(Grav_obj):
	if Grav_obj.output.Power_Spectrum_status:
		if Grav_obj.pbs_arr:
			f5 = open('pspectrum%3f'(float(pbID)), 'w')
		else:
			f5 = open('pspectrum', 'w')
		f5.write('r\t\tn\n')
		for i in range(Grav_obj.output.Power_Spectrum_points):
			f5.write('%12f\t'%(Grav_obj.field.r[i]))
			f5.write('%12f\n'%(Grav_obj.field.Power_Spec_n[i]))
		f5.close
