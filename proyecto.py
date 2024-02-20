class curp:
    def __init__(self):
        self.states = [0, 1, 2, 3, 4]
        self.final_states = [1, 2, 3, 4]
        self.alphabet = ['V', 'E', 'J', 'V', 'v', 'e', 'j', 'v']
        self.transition_table = {
            (0, 'V'): 1, (0, 'v'): 1,
            (1, 'E'): 2, (1, 'e'): 2,
            (2, 'J'): 3, (2, 'j'): 3,
            (3, 'V'): 4, (3, 'v'): 4
        }
        self.current_state = 0

    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) not in self.transition_table:
            self.current_state = None
        else:
            self.current_state = self.transition_table[(self.current_state, input_value)]

    def in_accept_state(self):
        return self.current_state in self.final_states

    def go_to_initial_state(self):
        self.current_state = 0

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            if self.current_state is None:
                return False
        return self.in_accept_state()

dfa = curp()

user_input = input("Inserte las 4 letras: ")

is_valid = dfa.run_with_input_list(user_input)

if is_valid:
    print(f"La Curp '{user_input}' es correcto.")
else:
    print(f"La Curp '{user_input}' es incorrecta.")
    
# Mis 4 iniciales  ->  VEJV/vejv 