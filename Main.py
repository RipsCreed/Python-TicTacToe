import random
class TicTacToe():
    table = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    place = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    def __init__(self):
        self.printTable("O")   
    def printTable(self, sign):
        print(f"""     A   B   C
    -----------
1 ┆  {self.table[0]} │ {self.table[1]} │ {self.table[2]} 
  ┆ ───┼───┼───
2 ┆  {self.table[3]} │ {self.table[4]} │ {self.table[5]} 
  ┆ ───┼───┼───
3 ┆  {self.table[6]} │ {self.table[7]} │ {self.table[8]}
""")     
        if (sign == "X"):
            self.control("X")
        elif (sign == "O"):
            self.control("O")   
    def control(self, next):
        if (self.table[0] == self.table[1] == self.table[2] == self.table[3] == self.table[4] == self.table[5] == self.table[6] == self.table[7] == self.table[8] != " "):
            print("Draw!")       
        elif (self.table[0] == self.table[1] == self.table[2] == "X") or (self.table[0] == self.table[1] == self.table[2] == "O"):
            if (self.table[0] == "X"):
                print("X wins")
            else:
                print("O wins")             
        elif (self.table[3] == self.table[4] == self.table[5] == "X") or (self.table[3] == self.table[4] == self.table[5] == "O"):
            if (self.table[3] == "X"):
                print("X wins")
            else:
                print("O wins")
        elif (self.table[6] == self.table[7] == self.table[8] == "X") or (self.table[6] == self.table[7] == self.table[8] == "O"):
            if (self.table[6] == "X"):
                print("X wins")
            else:
                print("O wins")           
        elif (self.table[0] == self.table[3] == self.table[6] == "X") or (self.table[0] == self.table[3] == self.table[6] == "O"):
            if (self.table[0] == "X"):
                print("X wins")
            else:
                print("O wins")          
        elif (self.table[1] == self.table[4] == self.table[7] == "X") or (self.table[1] == self.table[4] == self.table[7] == "O"):
            if (self.table[1] == "X"):
                print("X wins")
            else:
                print("O wins")         
        elif (self.table[2] == self.table[5] == self.table[8] == "X") or (self.table[2] == self.table[5] == self.table[8] == "O"):
            if (self.table[2] == "X"):
                print("X wins")
            else:
                print("O wins")         
        elif (self.table[0] == self.table[4] == self.table[8] == "X") or (self.table[0] == self.table[4] == self.table[8] == "O"):
            if (self.table[0] == "X"):
                print("X wins")
            else:
                print("O wins")
        elif (self.table[2] == self.table[4] == self.table[6] == "X") or (self.table[2] == self.table[4] == self.table[6] == "O"):
            if (self.table[2] == "X"):
                print("X wins")
            else:
                print("O wins")
        else:
            if (next == "X"):
                self.computerInput()
            elif (next == "O"):
                self.userInput()
    def putSymbols(self, result, value):
        self.value = str(value)
        if (result == "a1") or (result == "A1"):
            if (self.table[0] != "X") or (self.table != "O"):
                self.table[0] = self.value
                self.printTable(self.value)
            else:
                self.putSymbols
        elif(result == "a2") or (result == "A2"):
            self.table[3] = self.value
            self.printTable(self.value)
        elif(result == "a3") or (result == "A3"):
            self.table[6] = self.value
            self.printTable(self.value)
        elif(result == "b1") or (result == "B1"):
            self.table[1] = self.value
            self.printTable(self.value)
        elif(result == "b2") or (result == "B2"):
            self.table[4] = self.value
            self.printTable(self.value)
        elif(result == "b3") or (result == "B3"):
            self.table[7] = self.value
            self.printTable(self.value)
        elif(result == "c1") or (result == "C1"):
            self.table[2] = self.value
            self.printTable(self.value)
        elif(result == "c2") or (result == "C2"):
            self.table[5] = self.value
            self.printTable(self.value)
        elif(result == "c3") or (result == "C3"):
            self.table[8] = self.value
            self.printTable(self.value)
        else:
            print("Wrong Place! Try Again.")
            self.putSymbols()
    def userInput(self):
        self.user_input = input("X's Move  :")
        self.putSymbols(self.user_input, "X")
    def computerInput(self):
        self.computer_input = input("O's Move  :")
        self.putSymbols(self.computer_input, "O")
TicTacToe()