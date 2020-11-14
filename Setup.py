class board:
    

    class home:

        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    class robot:
          
        def __init__(self,fuel,clean_V,x,y,start_x, start_y):
            self.fuel = fuel
            self.clean_V = clean_V
            self.max_fuel = fuel
            self.max_clean_V = clean_V
            self.x=x
            self.y=y
            self.base = home(start_x,start_y)
            
              
        def set_fuel(self,fuel):
            self.fuel = fuel
      
        def set_clean_V(self,clean_V):
            self.clean_V = clean_V

        def restock(self,fuel,clean_V):
            self.set_fuel(fuel)
            self.set_clean_V(clean_V)
          
      
    def __init__(self):
        self.num_robot=0
        self.width=0
        self.height=0
        self.tile[n][m]=0
        self.robot[x]=robot()

    def boardSetup(self):

        size = []

        gameStats = []

        with open(TESTDOC) as file:

            gameStats = file.readline()
            
            size = file.readline()

            size.split()

            gameBoard = []

            #read in entire matrix

            for line in file:

                gameBoard.append(line.split())

            #convert to a numpy array for possible transpose

            temp = np.array(gameBoard)

            #change matrix if its not how we want it to be

            if(size[0]>size[2]):

                newGameBoard = temp.transpose()

                masterBoard = newGameBoard

            #if matrix is the way we want, we keep it

            else:

                masterBoard = temp

            
            x=0
            y=0
            x_max = int(size[0])
            y_max = int(size[1])
            self.width = x_max
            self.tile[x_max-1][y_max-1]
            while x < x_max:
                while y < y_max:
                    self.tile[x][y]=int(masterBoard[x][y])
                    y += 1
                x += 1
                y = 0



    def move_up(self,robot_choice):
        if self.robot[robot_choice].y < self.height:
            self.robot[robot_choice].y = self.robot[robot_choice].y + 1
        else:
            return
    def move_down(self,robot_choice):
        if self.robot[robot_choice].y >= 0:
            self.robot[robot_choice].y = self.robot[robot_choice].y - 1
        else:
            return

    def move_left(self,robot_choice):
        if self.robot[robot_choice].x > 0:
            self.robot[robot_choice].x = self.robot[robot_choice].x - 1
        else:
            return
    def move_right(self,robot_choice):
        if self.robot[robot_choice].x < self.width:
            self.robot[robot_choice].x = self.robot[robot_choice].x + 1
        else:
            return
    def print_clean(self,robot_choice, clean_value):
        print('["robot #' , robot_choice , '"] , "clean" , ' , clean_value , ' ] \n')
        
    def clean(self,robot_choice):
        if self.tile[self.robot[robot_choice].x][self.robot[robot_choice].y] < self.robot[robot_choice].clean_V:
            save = self.tile[self.robot[robot_choice].x][self.robot[robot_choice].y]
            self.tile[self.robot[robot_choice].x][self.robot[robot_choice].y] = 0
            self.robot[robot_choice].clean_V -= save
            print_clean(robot_choice, save)
        else:
            save = self.robot[robot_choice].clean_V
            self.robot[robot_choice].clean_V = 0
            self.tile[self.robot[robot_choice].x][self.robot[robot_choice].y] = self.tile[self.robot[robot_choice].x][self.robot[robot_choice].y] - save
            print_clean(robot_choice, save)
    
    def total_contaminant(self):
        count_x = 0
        count_y = 0
        x_max = self.width
        y_max = self.height
        total = 0
        while count_x < x_max:
            while count_y <= y_max:
                total += self.tile[count_x][count_y]
                count_y += 1
            count_y = 0
            count_x += 1
        return total
