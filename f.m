function [pos] = f(i,j,k,l)
imax=8;
jmax=4;
kmax=9;
lmax=2;

pos=l+lmax*(k-1)+lmax*kmax*(j-1)+jmax*kmax*lmax*(i-1);

end

%Each entry of the constraint matrices A and Aeq corresponds to an entry of x 
%(and y, and other varibales that may be added as this formulation is extended)
%In order to keep track of this correspondence, we order the x variables as follows:

%variable    position
%x_1111       1
%x_1112       2
%...         ...
%x_111s       s
%x_1121      s+1
%x_1122      s+2
%...         ...
%x_112s      2s
%x_1131      2s+1
%...         ...
%x_pqrs      p*q*r*s

%where p,q,r,s are the maximum values of each index.

%Given an ordered quadruple (i,j,k,l), the function f returns the position 
%of x_{ijkl} according to the ordering above


