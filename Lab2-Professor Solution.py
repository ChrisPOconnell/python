__author__ = 'chris'
def get_min(an_array):
    # Precondition: len(an_array) > 0
    # Postcondition 1: min = an_array(index_of_max)
    # Postcondition 2: min >= an_array(best_index) for all 0 <= best_index < an_array.len
    # Postcondition 3: max >= an_array(best_index) for all 0 <= best_index < an_array.len

    # Objective 1: = Postcondition 1 --AND--
    # Objective 2: min <= an_array(best_index) for all 0 <= best_index < upper_index

    upper_index = 0
    best_index = upper_index # Objective 2
    min = an_array[best_index] # Objective 1

    # Objective 3: upper_index = len(an_array) - 1

    while upper_index < len(an_array) - 1:
        # Terminates because upper_index is bounded and increases on every iteration
        upper_index += 1 # perturb towards termination
        # Restore Objectives 1 and 2:
        if an_array[upper_index] < min:
            best_index = upper_index
            min = an_array[best_index]

    return min

# TESTING

def test_get_min():
    print("get_min([102345, 102343] should equal 102343: "
            + str(get_min([102345, 102343])))

test_get_min()
