function a_out = script_from_python(a_in,varargin)

evalin('base',a_in)

% PYTHON REALLY WANTS US TO RETURN SOMETHING HERE!!
a_out = true;