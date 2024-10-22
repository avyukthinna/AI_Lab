def print_board(state):
    n = len(state)
    board = [['.' for _ in range(n)] for _ in range(n)]
    for col, row in enumerate(state):
        board[row][col] = 'Q'  
    for row in board:
        print(' '.join(row))
    print()  

def calculate_cost(state):
    cost = 0
    n = len(state)
   
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost

def generate_neighbors(state):
    neighbors = []
    n = len(state)
    
    for col in range(n):
        for row in range(n):
            if state[col] != row:  
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)
    
    return neighbors

def hill_climbing_4_queens(initial_state):
    n = 4  
    
    current_state = initial_state
    current_cost = calculate_cost(current_state)
    
    print(f"Initial state: {current_state}, Cost: {current_cost}")
    print_board(current_state)
    
    steps = 0

    while current_cost != 0:
        steps += 1
       
        neighbors = generate_neighbors(current_state)
        neighbor_costs = [calculate_cost(neighbor) for neighbor in neighbors]
    
        min_cost = min(neighbor_costs)
        best_neighbor = neighbors[neighbor_costs.index(min_cost)]
        
        print(f"Step {steps}: Best neighbor: {best_neighbor}, Cost: {min_cost}")
        print_board(best_neighbor)
    
        if min_cost < current_cost:
            current_state = best_neighbor
            current_cost = min_cost
        else:
            print("Stuck at local maximum.")
            break
    
    if current_cost == 0:
        print("Solution found:")
        print_board(current_state)
    else:
        print("No solution found. Stuck at a local maximum.")

def get_user_input():
    print("Enter the initial positions of the queens on the board (0-based index for each column):")
    initial_state = []
    for col in range(4):
        row = int(input(f"Enter row position for column {col+1}: "))
        initial_state.append(row)
    return initial_state

def main():
    confirm = input("Run Hill Climbing for the 4-Queens problem? (yes/no): ").strip().lower()
    if confirm == 'yes':
        initial_state = get_user_input()  
        hill_climbing_4_queens(initial_state)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()