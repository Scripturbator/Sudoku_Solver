SUDOKU SOLVER
=============

Version 1.1
Created by John Murray
Date: 9 Dec 15
Github user: Scripturbator
Text Editor: Pythonista iOS (Pyhon 2.7)

1.0 Notes
---------

* First time playing with classes (super fun!)  
* Figured out that best way to solve is to find out what 'could' go in to a cell (by mistake if we're being honest here). If the board is correct, you will always find at least one cell with only one possible value. You then set it to that value and iterate over the entire board again and find another single value cell.  
* Haven't done a lot of testing so let me know if there's issues.  
* I included a sample puzzle to test the class directly.  
  
1.1 Notes
---------

* Prettied up code  
* Removed stat finding code. It was helpful in the learning process but ultimately clogs up the code, making it hard to follow.  
* I should also note that I did this without researching anything but coding. It took a while but was a gratifying experience to use scripting as a method of problem solving.  
* Show board before and after solving  
* Learned Markup to create readme file

Process
-------
1. First I split up the board by section:  

**1**|**2**|**3**
:---:|:---:|:---:
**4**|**5**|**6**
**7**|**8**|**9**  
2.  Then within each section, by cell:  

**1  2  3**<br>**4  5  6**<br>**7  8  9**|**1  2  3**<br>**4  5  6**<br>**7  8  9**|**1  2  3**<br>**4  5  6**<br>**7  8  9**
:---:|:---:|:---:
**1  2  3**<br>**4  5  6**<br>**7  8  9**|**1  2  3**<br>**4  5  6**<br>**7  8  9**|**1  2  3**<br>**4  5  6**<br>**7  8  9**
**1  2  3**<br>**4  5  6**<br>**7  8  9**|**1  2  3**<br>**4  5  6**<br>**7  8  9**|**1  2  3**<br>**4  5  6**<br>**7  8  9**  
  
This became the main class variable as a dictionary of dictionaries. 
```(python)
sections = {cells{value}}
```
In retrospect, it made it more complicated.  I should have started with just row/col.  
  
3.  Next create row and column class variables:  

|**Columns->**|**1  2  3**|**4  5  6**|**7  8  9**|
|---:|:---:|:---:|:---:|
|**Row 1**<br>**Row 2**<br>**Row 3**|**1  2  3**<br>**1  2  3**<br>**1  2  3**|**4  5  6**<br>**4  5  6**<br>**4  5  6**|**7  8  9**<br>**7  8  9**<br>**7  8  9**|
|**Row 4**<br>**Row 5**<br>**Row 6**|**1  2  3**<br>**1  2  3**<br>**1  2  3**|**4  5  6**<br>**4  5  6**<br>**4  5  6**|**7  8  9**<br>**7  8  9**<br>**7  8  9**|
|**Row 7**<br>**Row 8**<br>**Row 9**|**1  2  3**<br>**1  2  3**<br>**1  2  3**|**4  5  6**<br>**4  5  6**<br>**4  5  6**|**7  8  9**<br>**7  8  9**<br>**7  8  9**|  

  rows{column{value}}
  columns{row{value}}
  
              Column:
          123   456   789 
        -------------------
  Row 1:| 111 | 111 | 111 |
  Row 2:| 222 | 222 | 222 |
  Row 3:| 333 | 333 | 333 |
        -------------------
  Row 4:| 444 | 444 | 444 |
  Row 5:| 555 | 555 | 555 |
  Row 6:| 666 | 666 | 666 |
        -------------------
  Row 7:| 777 | 777 | 777 |
  Row 8:| 888 | 888 | 888 |
  Row 9:| 999 | 999 | 999 |
        -------------------

-Once a user enters the board values, the class finds the cells that are
empty, and figures what the values 'could' be based on the sudoku rules. 

-Next find out which empty cell has only one 'possible' value and reset the
board to include that value

-Iterate finding the solveable cells until none can be found. 

-Print the board, showing the solved and non-solved cells (if any) with
the possible values. 
  
How to use
----------

-Set a variable to the sudoku class
  
  from sudoku_solver import sudoku
  
  myBoard = sudoku()

-Enter cell values as a 3-digit integer representing: 
  row (1-9:top to bottom), 
  column (1-9:left to right), 
  value (1-9)

They can be inserted one at a time or as a list.
  
  # Call class
  from sudoku_solver import sudoku
  
  # Make blank board
  myBoard = sudoku()  
  
  # Set known values on board one at a time to see progress
  myBoard.setVal(119) #Set (row-1, col 1) to 9
  myBoard.setVal(147) #Set (1, 4) to 7
  myBoard.setVal(153) #Set (1, 5) to 3
  ...
  
  *OR*
  
  # Enter all values and view solution
  set_vals = [119, 147, 153, 185, 212, 235, 248, 266, 277, 284, 331, \
              344, 437, 452, 476, 488, 499, 616, 651, 694, 765, 817, \
              849, 873, 925, 978, 997]
  
  # Set values
  myBoard.setVal(set_vals)

If it is logically possible to extrapolate the values, the class will 
do so. It will print what solution it came up with. 

OUTPUT:

  -------------------------------
  | 9  4  6 | 7  3  1 | 2  5  8 |
  |         |         |         |
  | 2  3  5 | 8  9  6 | 7  4  1 |
  |         |         |         |
  | 8  7  1 | 4  5  2 | 9  6  3 |
  |---------|---------|---------|
  | 3  1  7 | 5  2  4 | 6  8  9 |
  |         |         |         |
  | 5  9  4 | 6  8  7 | 1  3  2 |
  |         |         |         |
  | 6  2  8 | 3  1  9 | 5  7  4 |
  |---------|---------|---------|
  | 1  8  3 | 2  7  5 | 4  9  6 |
  |         |         |         |
  | 7  6  2 | 9  4  8 | 3  1  5 |
  |         |         |         |
  | 4  5  9 | 1  6  3 | 8  2  7 |
  -------------------------------

It will also show possible values if the board isn't logically solveable.

This example shows what happens when we take three values from the 
previous one. 

  # Call class
  from sudoku_solver import sudoku
  
  # Make blank board
  myBoard = sudoku()
  
  # Enter all values and view solution
  set_vals = [119, 147, 153, 185, 212, 248, 266, 277, 284, 344, \
              437, 452, 476, 488, 499, 616, 651, 694, 765, 817, \
              849, 925, 978, 997]
  
  # Set values
  myBoard.setVal(set_vals)

OUTPUT:

  -------------------------------------------------------------------------------------
  |    9     (1468)   (1468)  |    7        3      (12)   |  (12)       5     (1268)  |
  |                           |                           |                           |
  |    2      (13)     (135)  |    8      (59)       6    |    7        4      (13)   |
  |                           |                           |                           |
  | (1358)   (13678)  (13568) |    4      (59)     (129)  | (1239)   (12369)  (12368) |
  |---------------------------|---------------------------|---------------------------|
  | (1345)    (134)      7    |  (35)       2      (34)   |    6        8        9    |
  |                           |                           |                           |
  | (13458) (123489) (1234589)|  (356)  (456789)  (34789) | (1235)   (1237)   (1235)  |
  |                           |                           |                           |
  |    6     (2389)   (23589) |  (35)       1     (3789)  |  (235)    (237)      4    |
  |---------------------------|---------------------------|---------------------------|
  | (1348)  (1234689)(1234689)| (1236)   (4678)      5    | (12349)  (12369)  (1236)  |
  |                           |                           |                           |
  |    7    (123468) (123468) |    9      (468)   (12348) | (12345)  (1236)   (12356) |
  |                           |                           |                           |
  |  (134)      5    (123469) | (1236)    (46)    (1234)  |    8     (12369)     7    |
  -------------------------------------------------------------------------------------   
  
You can also use this to make your own sudoku challenges from scratch! 

Just enter one value at a time until it's solved, then copy the values on 
to a blank board for your friends to solve. Be a Sudoku maker! 

Dream: Obtained

