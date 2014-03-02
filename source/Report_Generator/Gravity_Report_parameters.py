def Report_parameters(Gravity_object):
    S = r'''

\section{Parameters}

The following parameters are used in this run, \\

Field proparties:
\begin{verbatim}
  Geometry  = ''' + Gravity_object.Geometry_type_name + r'''
  Cosmological constant  = ''' + str(Gravity_object.Cosmological_cosntant) + r'''
  '''
    if Gravity_object.field.Horizon:
	S3 = r'''
	Radius of Horizon ''' + str(Gravity_object.field.Horizon_r) + r'''
'''
    else: S3 = r''' '''

    S4 = r'''
  Potential = ''' + Gravity_object.Potential_type_name + r'''
\end{verbatim}

Initial Conditions:
\begin{verbatim}
  Initial Condition = ''' + Gravity_object.Initial_Condition_type_name + r'''
  '''
    if Gravity_object.Initial_Condition_type_name == 'Gaussian':
	S1 = r'''
	Initial epsilon = ''' + str(Gravity_object.initial_eps) + r'''
	Initial sigma = ''' + str(Gravity_object.initial_sigma) + r'''
'''

    else: S1 = r''' '''

    S2 = r'''
\end{verbatim}

Numerical method:
\begin{verbatim}
  Solver = ''' + Gravity_object.Solver_type_name + r'''
  Grid size = ''' + str(Gravity_object.Grid_size) + r'''
\end{verbatim}

Ending conditions:
\begin{verbatim}
  Horizon condition (A_min) = ''' + str(Gravity_object.A_min) + r'''
  Maximum number of iteration = ''' + str(Gravity_object.Max_interation) + r'''
\end{verbatim}

'''
    return S+S3+S4+S1+S2
