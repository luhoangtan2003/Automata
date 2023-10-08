class NFA:  # Định nghĩa một lớp có tên là NFA
    def __init__(self, Transitions, Start_State, Accept_States):  # Khởi tạo lớp với Transitions, Start_State và Accept_States
        self.Transitions = Transitions  # Gán Transitions cho thể hiện
        self.Start_State = Start_State  # Gán Start_State cho thể hiện
        self.Accept_States = Accept_States  # Gán Accept_States cho thể hiện

    def Move(self, States, Symbol):  # Định nghĩa một phương thức để di chuyển từ một trạng thái sang trạng thái khác
        New_States = set()  # Tạo một tập hợp rỗng cho New_States
        for State in States:  # Đối với mỗi State trong States
            if (State, Symbol) in self.Transitions:  # Nếu bộ (State, Symbol) có trong Transitions
                New_States.update(self.Transitions[State,Symbol])  # Cập nhật New_States với các chuyển đổi tương ứng
        return New_States  # Trả về New_States

    def Accept(self, Input_String):  # Định nghĩa một phương thức để kiểm tra xem một chuỗi đầu vào có được NFA chấp nhận hay không
        Current_States = {self.Start_State}  # Đặt trạng thái hiện tại là Start_State
        for Symbol in Input_String:  # Đối với mỗi Symbol trong Input_String
            Current_States = self.Move(Current_States,Symbol)  # Cập nhật Current_States bằng cách di chuyển từ trạng thái hiện tại sang các trạng thái mới dựa trên Symbol
        return any(State in self.Accept_States for State in Current_States)  # Trả về True nếu bất kỳ trạng thái hiện tại nào nằm trong Accept_States, ngược lại trả về False

Transitions = {  # Định nghĩa các quy tắc chuyển đổi cho NFA
    ('Q0', '0'): {'Q0', 'Q3'},
    ('Q0', '1'): {'Q0', 'Q1'},
    ('Q1', '0'): set(),
    ('Q1', '1'): {'Q2'},
    ('Q2', '0'): {'Q2'},
    ('Q2', '1'): {'Q2'},
    ('Q3', '0'): {'Q4'},
    ('Q3', '1'): set(),
    ('Q4', '0'): {'Q4'},
    ('Q4', '1'): {'Q4'},
}

Start_State = 'Q0'  # Định nghĩa trạng thái bắt đầu của NFA

Accept_States = {'Q2','Q4'}  # Định nghĩa các trạng thái chấp nhận của NFA

A = NFA(Transitions,Start_State,Accept_States)  # Tạo một thể hiện của NFA với Transitions, Start_State và Accept_States

Input_String = '0000011101'  # Định nghĩa một chuỗi đầu vào

print("Chuỗi {0} có được chấp nhận không?:".format(Input_String),A.Accept(Input_String))  # In ra xem chuỗi đầu vào có được NFA chấp nhận hay không