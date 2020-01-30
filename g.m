function [pos] = g(i,j)
jmax=4;

pos=j+jmax*(i-1);

end



%Each entry of the constraint matrices A and Aeq corresponds to an entry of x 
%(and y, and other varibales that may be added as this formulation is extended)
%In order to keep track of this correspondence, we order the y variables as follows:

%variable    position
%y_11          1
%y_12          2
%...          ...
%y_1s          s
%y_21         s+1
%y_22         s+2
%...          ...
%y_2s         2s
%y_31         2s+1
%...          ...
%y_rs         r*s

%where r,s are the maximum values of each index.

%Given an ordered pair (i,j), the function g returns the position 
%of y_{ij} according to the ordering above


