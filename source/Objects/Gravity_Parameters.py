import sys
from numpy                        import linspace, pi
from Utilities                    import read_data_string, read_data_float, read_data_int
from Gravity_Dictionary           import *
from Condition_Change		  import Change_eps

class Gravity_obj:

      from Gravity_Output_Properties    import Output_parameters
      from Gravity_Field_Properties     import Field_parameters
      
      field  = Field_parameters()
      output = Output_parameters()

      def __init__(self):

         #Geometry Properties
         self.Geometry_type_name     = read_data_string(tag_name='Geometry_type',file_name='parameters/parameters.xml')
         self.Cosmological_cosntant  = read_data_float(tag_name='Cosmological_constant',file_name='parameters/parameters.xml')

         #Field Properties
         self.Potential_type_name    = read_data_string(tag_name = 'Potential',file_name = 'parameters/parameters.xml')
         self.Potential_func         = Gravity_Dictionary["Potential"][self.Potential_type_name][0]
         self.Potential_dfunc        = Gravity_Dictionary["Potential"][self.Potential_type_name][1]
         
         #Initial Condition
	 #reads in the name of the initial condition
         self.Initial_Condition_type_name  = read_data_string(tag_name = 'Initial_Condition_Method',file_name = 'parameters/parameters.xml')
	 #matches the name of the initial condition to the stuff in the Gravity dictionary

         try:
	         self.Initial_Condition_type = Gravity_Dictionary["Initial_Condition"][self.Initial_Condition_type_name]
	 except KeyError:
		print 'ERROR: Initial Condition name is wrong'
		sys.exit(1)
         #Numerical Method Setup
         self.Solver_type_name       = read_data_string(tag_name = 'Solver_type',file_name = 'parameters/parameters.xml')
         self.Grid_size              = read_data_int(tag_name = 'Grid_size',file_name = 'parameters/parameters.xml')

         #Ending Conditions
         self.Max_interation         = read_data_int(tag_name = 'i_max',file_name = 'parameters/parameters.xml')
         #Horizon Condition
         self.A_min                  = read_data_float(tag_name = 'A_min',file_name = 'parameters/parameters.xml')

	#sets the initial conditions for generating end data
	 if self.Initial_Condition_type_name =='Gaussian':
		self.initial_eps		= read_data_float(tag_name = 'epsilon' , file_name = 'parameters/Initial_Condition/Gaussian.xml')
		self.initial_sigma		= read_data_float(tag_name = 'sigma' , file_name = 'parameters/Initial_Condition/Gaussian.xml')
		self.initial_eps = Change_eps(self.initial_eps)

	#Initial Condition Setup
         if (self.Initial_Condition_type != Initial_Condition_Input_File):
            self.field.r = linspace(0.0,pi/2.0,self.Grid_size+1)
            (self.field.phi , self.field.Phi , self.field.Pi) = self.Initial_Condition_type(self.field.r)
         else:
            (self.field.r , self.field.phi , self.field.Phi , self.field.Pi) = self.Initial_Condition_type()

         print "The Gravity Object is initialized susseccfully."

