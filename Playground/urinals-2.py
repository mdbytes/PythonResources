def urinal_problem(n):
    # Initialize a list of urinals (0 means empty, 1 means occupied).
    urinals = [0] * n
    
    # Place the first person in the last spot
    urinals[-1] = 1
    print(f"After 1st person: {urinals}")
    
    # Place the second person in the first spot
    urinals[0] = 1
    print(f"After 2nd person: {urinals}")
    
    # Place subsequent persons
    for person in range(3, n + 1):
        max_distance = -1
        best_spot = -1
        
        # Check all empty urinals and calculate the minimum distance to the nearest occupied urinal
        for i in range(n):
            if urinals[i] == 0:  # Only consider empty spots
                # Find the distance to the nearest occupied urinal
                left_distance = float('inf') if i == 0 else next((j for j in range(i-1, -1, -1) if urinals[j] == 1), -1)
                right_distance = float('inf') if i == n - 1 else next((j for j in range(i+1, n) if urinals[j] == 1), n)
                
                # Calculate the distance to the nearest occupied spot
                min_distance = min(i - left_distance if left_distance != -1 else float('inf'),
                                   right_distance - i if right_distance != n else float('inf'))
                
                # Update if this spot maximizes the minimum distance
                if min_distance > max_distance:
                    max_distance = min_distance
                    best_spot = i
                # In case of tie (same distance), prefer the more centered spot
                elif min_distance == max_distance and i < best_spot:
                    best_spot = i
        
        # Place the person at the best spot found
        urinals[best_spot] = 1
        print(f"After {person}th person: {urinals}")
    
    return urinals

# Test the function with an example
n = 10  # Number of urinals
final_urinals = urinal_problem(n)
