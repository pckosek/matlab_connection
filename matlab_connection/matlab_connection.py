import numpy as np
import matlab.engine
import os

# --------------------------------------------------- #
# MATLAB CONNECTION CLASS
# --------------------------------------------------- #
class matlab_connection:

  def __init__(self, session_name):
    self.session_name = session_name
    self.eng = matlab.engine.connect_matlab(session_name)

  def put_var(self, var_name, values) :
    self.eng.workspace[var_name] = matlab.double( np.asarray(values).tolist() ) 

  def get_var(self, var_name) :
    return np.asarray( self.eng.workspace[var_name] )

  def move_to_cwd(self) :
    f = self.eng.cd(os.getcwd())

  def run_script(self, script_name) :
    f = self.eng.from_python(script_name)

  def run_function(self, fcn_name, data) :
    f = self.eng.from_python(script_name)

  def should_stop(self) :
    return self.eng.should_stop()