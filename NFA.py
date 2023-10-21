import copy

class NFA:
    def __init__(self, Transitions, Start_State, Accept_States, Input_String):
        self.Transitions = Transitions
        self.Start_State = Start_State
        self.Accept_States = Accept_States
        self.Input_String = Input_String

    def Move(self, States, Symbol):
        New_States = set()
        for State in States:
            if (State, Symbol) in self.Transitions:
                New_States.update(self.Transitions[State,Symbol])
        return New_States

    def Accept(self):
        Current_States = {self.Start_State}
        for Symbol in self.Input_String:
            Prev_States = copy.deepcopy(Current_States)
            Current_States = self.Move(Current_States,Symbol)
            Print_Move(Prev_States, Current_States, Symbol)
        return any(State in self.Accept_States for State in Current_States)

def Print_Move(Prev, Curent, Symbol):
    print("({:<10},{}) => {:>10}".format(''.join(Prev),Symbol,''.join(Curent)))

def Read_Data():
    with open("NFA.txt",'r') as File:
        Lines = File.readlines()
        for Item in Lines:
            Line = Item.split()
            if Line[2] != '0':
                Transitions[Line[0],Line[1]] = set(Line[2:])
            else:
                Transitions[Line[0],Line[1]] = set()

Transitions = dict()
Start_State = 'Q0'
Accept_States = {'Q2','Q4'}

while True:
    Input_String = input("Nhập vào chuỗi nhị phân:")
    Valid = 0
    for Item in Input_String:
        if Item in ('0','1'):
            Valid += 1
    if Valid == len(Input_String):
        break

Read_Data()
A = NFA(Transitions,Start_State,Accept_States,Input_String)
Result =  A.Accept()

if Result:
    print("Chuỗi '{0}' được chấp nhận".format(Input_String))
else:
    print("Chuỗi '{0}' không hợp lệ".format(Input_String))