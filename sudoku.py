class sudoku:
    """SUDOKU SOLVER
    
    Version 1.1
    Created by John Murray
    Date: 9 Dec 15
    Github user: Scripturbator
    Text Editor: Pythonista iOS (Pyhon 2.7)
    
    1.0 Notes
    ---------
    
        -First time playing with classes (super fun!)
        -Figured out that best way to solve is to find out what 'could'
         go in to a cell (by mistake if we're being honest here). If the board
         is correct, you will always find at least one cell with only one
         possible value. You then set it to that value and iterate over the
         entire board again and find another single value cell. 
        -Haven't done a lot of testing so let me know if theres issues
        -I included a sample puzzle to test the class directly. 
    
    1.1 Notes
    ---------
    
        -Prettied up code
        -Removed stat finding code. It was helpful in the learning process
         but ultimately clogs up the code, making it hard to follow. 
        -I should also note that I did this without researching anything but
         coding. It took a while but was a gratifying experience to use
         scripting as a method of problem solving. 
        -Show board before and after solving
    
    Process
    -------
    
    -First I split up the board by section:
        
        -------------
        | 1 | 2 | 3 |
        -------------
        | 4 | 5 | 6 |
        -------------
        | 7 | 8 | 9 |
        -------------      
        
    -Then within each section, by cell:
        -------------------
        | 123 | 123 | 123 |
        | 456 | 456 | 456 |
        | 789 | 789 | 789 |
        -------------------
        | 123 | 123 | 123 |
        | 456 | 456 | 456 |
        | 789 | 789 | 789 |
        -------------------
        | 123 | 123 | 123 |
        | 456 | 456 | 456 |
        | 789 | 789 | 789 |
        -------------------
        
        This became the main class variable as a dictionary of dictionaries. 
        
        sections{cells{value}}
        
        In retrospect, it made it more complicated.  I should have started with
        just row/col.
    
    -Next create row and column class variables:
        
        rows{column{value}}
        
                    Column:
                123   456   789 
              -------------------
        Row 1:| 123 | 456 | 789 |
        Row 2:| 123 | 456 | 789 |
        Row 3:| 123 | 456 | 789 |
              -------------------
        Row 4:| 123 | 456 | 789 |
        Row 5:| 123 | 456 | 789 |
        Row 6:| 123 | 456 | 789 |
              -------------------
        Row 7:| 123 | 456 | 789 |
        Row 8:| 123 | 456 | 789 |
        Row 9:| 123 | 456 | 789 |
              -------------------
        
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
    
    """
 
    def __init__(self):
        'Identify class variables and create blank suduko board'

        # Populate blank sudoku sheet
        sections = {}
        for x in range(1,10):
            section = x
            cells = {}
            for y in range(1,10):
                cell = y
                cells[y] = " "
            sections[section] = cells

        # Set class variables
        self.sections = sections
        self.__fillRowsAndCols()
        self.width = 3
        self.iterations = 0
        self.__findMaybes()     

    def __fillRowsAndCols(self):
        'populate row and column dictionaries with section data'
        sections = self.sections
        
        # Create blank rows and colums then populate
        rows = {}
        cols = {}
        for grp in [rows,cols]:
            for x in range(1,10):
                grp[x] = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
        
        # Fill with actual values
        for row in range(1,10):
            for col in range(1,10):
                section, cell = self.__getSectAndCell(row, col)
                val = sections[section][cell]
                rows[row][col] = val
                cols[col][row] = val
        
        # Reset attribures
        self.rows = rows
        self.cols = cols
    
    def __findMaybes(self):
        """Find out possible locations for values and adjust column width as 
        needed for larger entries. 
        """
        
        rows = self.rows
        cols = self.cols
        sections = self.sections
        nums = range(1,10)
        maybes = {}
        most_vals = 1
        
        # Look at each value
        for row in sorted(rows):
            maybes[row] = {}
            for col in sorted(rows[row]):
                val = rows[row][col]
                
                # If no value, determine possible values
                if val == " ":
                    no_val = []
                    section = self.__getSectAndCell(row, col)[0]                 
                    
                    # Check what values are available
                    for n in nums:
                        row_vals = n in rows[row].values()
                        col_vals = n in cols[col].values()
                        sec_vals = n in sections[section].values()
                        if not(row_vals or col_vals or sec_vals):
                            no_val.append(n)
                    
                    # Expand printing column width to allow for all values
                    if no_val:
                        maybes[row][col] = no_val
                        if len(no_val) > most_vals:
                            most_vals = len(no_val)
        
        # Add 2 to column width to give space between values
        self.width = most_vals + 2
        
        # Set class variable
        self.maybes = maybes
      
    def setVal(self, c1):
        """With a single or array of 3-digit integers representing 
        row/column/value, update board and attempt solution
        """
        sections = self.__updateBoard(rtn_vals = True)[0]
        
        if isinstance(c1, int):
            set_list = [c1]
        else:
            set_list = c1
        
        for item in set_list:
            r, c, val = str(item)           
            section, cell = self.__getSectAndCell(int(r), int(c))
            sections[section][cell] = int(val)

        self.__updateBoard(sections)
        
        # If first iteration, print board
        if not self.iterations:
            print ("Initial entry:")
            print(self)
        
        self.__attemptSolve()

    def __updateBoard(self, sections = "", rtn_vals = False):
        """Update sudoku values with new board given"""
        if sections:
            self.sections = sections
            self.__fillRowsAndCols()
            self.__findMaybes() 
        
        if rtn_vals:
            return self.sections, self.rows, self.cols, self.maybes
 
    def __attemptSolve(self):
        'Attempt to solve. Iterate until no values derived then print'
        
        maybes = self.__updateBoard(rtn_vals = True)[3]
        for row in maybes:
            for col in maybes[row]:
                if len(maybes[row][col]) == 1:
                    self.iterations += 1
                    vals_str = map(str, [row, col, maybes[row][col][0]])
                    val = int("".join(vals_str))
                    self.setVal(val)
                    return
        self.iterations = 0
        
        print("Solution")
        print(self)             
         
    def __getSectAndCell(self,x,y):
        """
        Identify section and position when given row,col coords for board
        
        Ex (x = 6, y = 8): 
        sec_row_dex[6] + sec_col_dex[8] = 6
        cell_row_dex[6] + cell_col_dex[8] = 8
        
        In other words, the cell at coordinates 6,8 is in section 6, 
        position 8
        """
        
        sri = {1:1, 2:1, 3:1, 4:4, 5:4, 6:4, 7:7, 8:7, 9:7}
        sci = {1:0, 2:0, 3:0, 4:1, 5:1, 6:1, 7:2, 8:2, 9:2}
        cri = {1:1, 2:4, 3:7, 4:1, 5:4, 6:7, 7:1, 8:4, 9:7}
        cci = {1:0, 2:1, 3:2, 4:0, 5:1, 6:2, 7:0, 8:1, 9:2}
        return [(sri[x] + sci[y]), (cri[x] + cci[y])]
    
    def __ctrTxt(self, in_text):
        'Center text within a defined string character width'
        
        width = self.width
        txt_len = len(in_text)
        empty_spc = width - txt_len
        if not empty_spc % 2 == 0:
            l_marg = (empty_spc - 1) / 2
            r_marg = l_marg + 1
        else: 
            l_marg = empty_spc / 2
            r_marg = l_marg
        rtn_text = ((" " * l_marg) + in_text + (" " * r_marg))
        return rtn_text
        
    def __str__(self):
        'Display board'
        width = self.width
        rows = self.rows
        maybes = self.maybes
        dash_row = (("|" + "-" * (3 * width)) * 3) + "|\n"
        mid_row =  (("|" + " " * (3 * width)) * 3) + "|\n"
        top_row = ("-" * ((width * 9) + 4)) + "\n"
        row_print = top_row
        for row in sorted(rows):
            # Ex: rows[row]={1: 1, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 1, 8: 2, 9: 3}
            cols = rows[row]
            row_print += "|"
            for col in sorted(cols):
                val = str(cols[col])
                if val == " ":
                    val = "(" + "".join(map(str, maybes[row][col])) + ")"
                if col % 3 == 0:
                    row_print += self.__ctrTxt(str(val)) + "|"
                    if col == 9:
                        if row % 3 == 0:
                            if row == 9:
                                row_print += "\n" + top_row
                            else:
                                row_print += "\n" + dash_row
                        else:
                            row_print += "\n" + mid_row
                else:
                    row_print += self.__ctrTxt(str(val))
        return row_print
      
# Test class
testme = sudoku()

# Cant't be solved logically
print ("This can't be solved:")
set_vals = [119, 147, 153, 185, 212, 248, 266, 277, 284, 344, 437, 452, 476, 488, 499, 616, 651, 694, 765, 817, 849, 925, 978, 997]

testme.setVal(set_vals)

# Re-test class
testme = sudoku()

# Can be solved
print ("This can be solved:")
set_vals = [119, 147, 153, 185, 212, 235, 248, 266, 277, 284, 331, 344, 437, 452, 476, 488, 499, 616, 651, 694, 765, 817, 849, 873, 925, 978, 997]

testme.setVal(set_vals)
