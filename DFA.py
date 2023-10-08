def Simulate_DFA(Input_String, Move, Start_State, Accept_States):  # Định nghĩa một hàm mô phỏng DFA với chuỗi đầu vào, hàm chuyển, trạng thái bắt đầu và tập trạng thái chấp nhận
    # Khởi tạo trạng thái hiện tại là trạng thái bắt đầu
    Current_State = Start_State

    # Duyệt qua từng ký tự trong chuỗi đầu vào
    for Char in Input_String:
        # Cập nhật trạng thái hiện tại dựa trên hàm chuyển và ký tự hiện tại
        Current_State = Move[(Current_State, Char)]

    # Kiểm tra xem trạng thái cuối cùng có thuộc tập trạng thái chấp nhận hay không
    if Current_State in Accept_States:
        print("Chuỗi '{0}' được chấp nhận".format(Input_String))
    else:
        print("Không chấp nhận chuỗi '{0}'".format(Input_String))

# Định nghĩa hàm chuyển và tập trạng thái chấp nhận
Move = {('Q0', '0'): 'Q2',
        ('Q0', '1'): 'Q1',
        ('Q1', '0'): 'Q3',
        ('Q1', '1'): 'Q0',
        ('Q2', '0'): 'Q0',
        ('Q2', '1'): 'Q3',
        ('Q3', '0'): 'Q1',
        ('Q3', '1'): 'Q2',}

Start_State = 'Q0'  # Định nghĩa trạng thái bắt đầu của DFA

Accept_States = ['Q0']  # Định nghĩa tập trạng thái chấp nhận của DFA

# Chuỗi đầu vào
Input_String = "01110010"

# Gọi hàm mô phỏng DFA
Simulate_DFA(Input_String, Move, Start_State, Accept_States)