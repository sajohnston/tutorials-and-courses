1 ~= 2 % not
% ; suppresses output
a = pi;
disp(a) % displays the values
disp(sprintf('2 decimals: %0.2f', a))

A = [1 2; 3 4; 5 6]

V = [1; 2; 3]
V2 = 1:0.1:2
V2'

C = 2*ones(2,3)

w = rand(3,3)
wnorm = randn(1, 3)

w = -6 + sqrt(10)*(randn(1,10000));
hist(w)

eye(4) % 4x4 'eye'dentity matrix

% 'help' function name


size(A)
size(A,1)
length(A)

% load('filename') or load filename
% who shows variables
% whos gives a detailed view of the variables
whos
% clear variablename or clear (no variable name would clear all)
% save hello.mat v would save the variable v into a file called hello.mat
% save hello.txt v -ascii would save it in a text file in ascii format
% A(row, column)
% A([1 3], :) means to get the 1st and 3rd row, all columns
% A(:,2) = [10; 11; 12] assigns the 10-12 column vector to the second column
