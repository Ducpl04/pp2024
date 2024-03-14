import numpy as np
import math

class information:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
    def describe(self):
        print(f"\nID: {self.ID}")
        print (f"Name: {self.name}")

class students(information):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.arr_mark = np.array([],'f')
        self.arr_credit = np.array([], 'i')
    def date_of_birth(self, DoB):
        self.DoB = DoB
    def describe(self):
        super().describe()
        print(f"DoB: {self.DoB}")
    def set_mark_function(self, mark, credits):
        self.arr_mark = np.append(self.arr_mark , mark)
        self.arr_credit = np.append(self.arr_credit , credits)
    def calculate_gpa(self):
        weighted_sum = self.arr_credit * self.arr_mark
        gpa = np.sum(weighted_sum) / np.sum(self.arr_credit)    
       #return round(gpa,1)     idk why mr.son ask me to use floor() function but okay
        return math.floor(gpa)

class courses(information):
    def __init__(self, ID, name, credit):
        super().__init__(ID, name)
        self.credit = credit
    def describe(self):
        super().describe()
        print(f"Credits: {self.credit}")