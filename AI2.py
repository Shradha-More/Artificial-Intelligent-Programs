# Graph Coloring using Constraint Satisfaction
def promising(state, color):
    for neighbor in neighbors.get(state, []):
        if colors_of_states.get(neighbor) == color:
            return False
    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

# Driver Code
states = input("Enter the states separated by space: ").split()
colors = input("Enter the colors separated by space: ").split()

neighbors = {}
for state in states:
    neighbor_states = input(f"Enter the neighbors of {state} separated by space: ").split()
    neighbors[state] = neighbor_states

colors_of_states = {}
for state in states:
    colors_of_states[state] = get_color_for_state(state)

print("Coloring of the states:")
print(colors_of_states)
