def display_urinals(urinals):
    # Display the urinal list with 'O' for occupied and 'X' for empty
    print("".join("O" if occupied else "X" for occupied in urinals))

def find_next_urinal(urinals):
    # Find the urinal with the maximum distance to the nearest occupied urinal
    max_distance = -1
    chosen_urinal = -1

    for i in range(len(urinals)):
        if urinals[i]:  # Skip if the urinal is occupied
            continue

        # Calculate the minimum distance to the nearest occupied urinal
        distance = min(
            (j - i) if urinals[j] and j > i else (i - j)
            for j in range(len(urinals))
            if urinals[j]
        )

        # Choose this urinal if the distance is the largest we've seen
        if distance > max_distance:
            max_distance = distance
            chosen_urinal = i

    return chosen_urinal

def simulate_bathroom_usage(n):
    urinals = [False] * n  # Initialize all urinals as empty

    if n > 0:
        # First person enters and occupies the last urinal
        urinals[-1] = True
        display_urinals(urinals)

    if n > 1:
        # Second person enters and occupies the first urinal
        urinals[0] = True
        display_urinals(urinals)

    for person in range(2, n):
        # Find the next optimal urinal for maximum spacing
        next_urinal = find_next_urinal(urinals)
        if next_urinal != -1:
            urinals[next_urinal] = True
        display_urinals(urinals)

# Example usage
n = 10  # Number of urinals and people
simulate_bathroom_usage(n)
