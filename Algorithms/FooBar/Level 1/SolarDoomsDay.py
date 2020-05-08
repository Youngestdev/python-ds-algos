from math import sqrt


def solution(area):
    # Your code here
    temp_area = area
    store = []

    while area > 0:
        square_of_area = sqrt(temp_area)

        # Let's check if it's a perfect square
        if square_of_area == int(square_of_area):
            # If the number is a perfect square, add it to the array.
            store.append(temp_area)
            # Deduct this value from the area
            area -= temp_area
            # Set the temp_area again to continue the cycle of loops
            temp_area = area
            # Continue looping!
            continue
        # Decrease the temp_area by 1 if the area passed isn't a perfect square
        temp_area -= 1
    # Return the list of perfect squares.
    return store
