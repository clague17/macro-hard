This folder contains two challenges from the msft3c competition I recently attended.
Side note: Since this was a Microsoft coding games event, our team decided on a "cool" name, MacroHard as our team name.


1. Matrix Transpose:
	This problem was worth 1 point, and does exactly what it sounds like, takes a matrix and produces its transpose. The only bit of 	 work I had to do with this problem was read from a file and parse the format into a list of lists, which I then used as input into 	    a Transpose function that did the heavy lifting. After that, I parsed it back into the format required for the output and the 	  challenge was complete.

2. Cylinder ship:
	This problem was worth 2 points and was actually interesting. The premise was, a company is trying to ship 'special edition' 		cylindrical boxes and the challenge is to decide if/how many rectangular prism box(es) and/or triangular prism box(es) fit(s) 		within the given cylindrical box. The input is a file, of the form:

	2;
	61,3,104;
	64,3,109;

	The first line delineates how many boxes a company is trying to ship in total, in this case 2, which matches to the lines of the 	 file. 
	For each line, index 0 corresponds to the radius of the cylindrical box that the company is considering. 
	Index 1 denotes whether the box they are trying to fit is rectangular or triangular: 3 = triangular prism, 4 = rectangular prism
	Index 2 denotes the side length of the base of the respective prism. 

	**NOTE** For this challenge, cylindrical boxes were of fixed height 13 inches, while the other boxes were of fixed height 12 		inches. Further, the base of the rectangular prism was a square, and the base of the triangular prism was an equilateral triangle. 

	The difficulty with this problem was once again parsing the data into a readable format and then deciding the actual number of 		boxes, which I run out of time for.

