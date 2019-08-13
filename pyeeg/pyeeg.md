#### [ pyeeg ][1]

### DFA
- Detrended Fluctuation Analysis
1. First integrate x into a new series y = [y(1),…, y(N)](), where y(k)=∑ki=1(xi−x⎯⎯) and x⎯⎯ is the average of x 1, x 2,…, x N.

2. The integrated series is then sliced into boxes of equal length n. In each box of length n, a least-squares line is fit to the data, representing the trend in that box. The y coordinate of the straight line segments is denoted by y n(k).

3. The root-mean-square fluctuation of the integrated series is calculated by F(n)=(1/N)∑Nk=1[y(k)−yn(k)]()√, where the part y(k) − y n(k) is called detrending.
	- What does it mean to Detrend Data?
		-  

4. The fluctuation can be defined as the slope of the line relating log  F(n) to log  n.

### Hjorth

### Hurst

### Spectral Entropy

### PFD
- Petrosian Fractal Dimension 
	￼￼	1. Computing first-order-diff 
	- X = [x(1),x(2),……,x(n-1),x(n)]()
		- Y = [x(2)-x(1), x(3)-x(2), x(4)-x(3),…, x(n)-x(n-1)]()
			\2. 
- What is Fractal Dimension?
	- ratio providing a statistical index of complexity comparing how detail in a pattern changes


[1]:	pyeeg
