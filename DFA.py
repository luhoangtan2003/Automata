def DFA(Input_String, Move, Start_State, Accept_States):

    Current_State = Start_State

    print("Thứ tự chuyển đổi trạng thái:")

    for Char in Input_String:

        Prev_State = Current_State

        Current_State = Move[Current_State, Char]

        Print_Move(Prev_State, Current_State, Char)

    if Current_State in Accept_States:
        print("Chuỗi '{0}' được chấp nhận".format(Input_String))
    else:
        print("Không chấp nhận chuỗi '{0}'".format(Input_String))

def Print_Move(Prev_State, Curent_State, Char):
    print("({0},{1}) => {2}".format(Prev_State,Char,Curent_State))

def Read_Data():
    with open("DFA.txt",'r') as File:
        Lines = File.readlines()
        for Item in Lines:
            Line = Item.split()
            Move[Line[0],Line[1]] = Line[2]


Move = dict()

Start = 'Q0'

Accept = ['Q0']

Read_Data()

while True:
    Input_String = input("Nhập vào chuỗi nhị phân:")
    Valid = 0
    for Item in Input_String:
        if Item in ('0','1'):
            Valid += 1
    if Valid == len(Input_String):
        break

DFA(Input_String, Move, Start, Accept)