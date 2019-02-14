function a_out = function_from_python(a_in,varargin)

if nargin>1
	a_out = feval(a_in,varargin{:});
else
	a_out = feval(a_in);
end