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
% hist(w)

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
% A(:) puts all elements of A into a single vector (A was a matrix)
% C = [A B] concatenates matrices A and B together (side by side)
% C = [A; B] concatenates matrices A and B together (A on top of B)

% A .* B is element-wise multiplication of two matrices
% A .^ 2
% 1 ./ v (v is a vector) does 1 / each element of v but the dot isn't needed for some others?
% for example v + 1 adds 1 to all elements in v
% v < 2 returns a vector of 1s and 0s (T and F) where that condition is true
% find(v < 2) returns the indices where the condition is true
% max(A, [], 1) takes the column-wise maximums in A (1 says it's the column, 2 would be row)
% sum(A, 1) sums the columns and sum(A, 2) does the rows
% A .* eye(9) (if A is a 9x9 matrix) returns just the diagonal values, so can be used for diag sums
% the opposite diagonal would be A.*flipud(eye(9))
% pinv(A) is the inverse of A (stands for pseudo-inverse)

% Plotting J(theta) (the cost function) can show gradient descent is converging
% plot(x, y) is basic plot
% hold on will plot next command on the same plot
% plot(x, y2, 'r') will plot another line in red following the hold on
% xlabel('time')
% ylabel('value')
% legend('y1','y2')
% title('my plot')
% print -dpng 'myPlot.png' will save as a png
% figure(1); plot(x,y); will plot in one window, while subsequent 'figure's will plot in other windows
% subplot(1, 2, 1) will split the window into two plots, and the final 1 allows you to access the first one
% axis command changes the axis
% clf clears a figure
% imagesc(A) plots the matrix as a plot of colors
% imagesc(A), colorbar, colormap gray; will include the colorbar of colors, and is in grey
% 'comma-chaining' allows you to do multiple commands separated by a comma

v = zeros(10,1)
for i=1:10,
 v(i) = 2^i;
end;
v

i = 1;
while i <= 5,
 v(i) = 100;
 i = i+1;
end;
v

i = 1;
while true,
 v(i) = 999;
 i = i+1;
 if i == 6,
  break;
 end;
end;
v

v(1) = 2;
if v(1) == 1,
 disp('The value is one');
elseif v(1) == 2,
 disp('The value is 2');
 else
 disp('The value is not one or two.');
end;

squareThisNumber(5)
[a,b] = squareAndCubeThisNumber(5)
%using 'addpath' gives Octave multiple directories to search for the files


X = [1 1; 1 2; 1 3;]
y = [1; 2; 3]
theta = [0; 1];

j = costFunctionJ(X, y, theta)

theta = [0; 0];
j = costFunctionJ(X, y, theta)

% Vectorization

% This language is 1-indexed

% Instead of doing a for loop to iterate over two vectors and do calculations
% you can use the language's native linear algebra routines
% For example, theta transpose * x instead of prediction += theta[j] * x[j]
