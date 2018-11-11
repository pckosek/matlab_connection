# matlab_connection

### this package is designed to streamline reading from and writing data to MATLAB from python

### _Purpose_:<br>
The matlab.engine library from Mathworks is impressive in that it allows python to connect to a MATLAB session, but can become a little long winded when interacting with numpy and calling functions.
<br><br>
The **matlab_connection** module contains a class that allows get and put variables, as well as call functions and run m-files in a straightforward, extensible manner.

### _Features_:<br>
- get matlab variables into python
- put python variables into MATLAB
- run an script (not as a function) from python
- call a MATLAB function from python