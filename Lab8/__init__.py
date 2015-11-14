__author__ = 'ChrisPOConnell'
'''
Assignment 7 (or 8 depending on where you're looking)
__init__.py
'''

# A test that presents fragments of The Gettysburg Address for acceptance
# (Practice with the queue data structure)

# GLOBAL VARIABLES AND CONSTANTS
# resulting_text = the old(fragment_choice) elements selected by user
# AND fragment_choice = elements not yet chosen

resulting_text = ""  # text resulting from choices
fragments_remaining = [
        "a new nation,\n",
        "and dedicated to the proposition that all men are created equal.\n",
        "Four score and seven years ago our fathers brought forth on this continent ",
        "can long endure.\n",
        "Now we are engaged in a great civil war, ",
        "that we should do this. ",
        "\nWe have come to dedicate a portion of that field, ",
        "conceived in liberty, ",
        "testing whether that nation,\n",
        "for those who here gave their lives ",
        "We are met on a great battlefield of that war. ",
        "that that nation might live. ",
        "\nIt is altogether fitting and proper ",
        "as a final resting place\n",
        "or any nation so conceived and so dedicated, "]

FRONT_INDEX = 0  # name for front index of the queue

def offer_front_fragment():
    '''
    Postcondition 1: "Select " + <the front element of fragment_choice> +
    " next (press 'n' for no)?: " is on monitor
    Postcondition 2: returns character that user pressed
    '''
    print("Select '" + fragments_remaining[FRONT_INDEX] + "' next (press 'n' for no)?: ")
    return input()


def describe_test_to_user():
    print("\nBY ACCEPTING OR REJECTING THE FRAGMENTS PRESENTED, RECONSTRUCT THE FIRST PART\n"
          " OF LINCOLN'S GETTYSBURG ADDRESS. (REJECTED FRAGMENTS REAPPEAR LATER UNTIL ACCEPTED).\n")
          
def offer_and_process_front_fragment():
    '''
    Precondition: fragment_choice has at least one element

    Postcondition 1:
    (1) The user selected old(fragment_choice)[FRONT_INDEX]
    AND it is at the end of resulting_text AND absent from fragment_choice
    --OR--
    (2) The user did not select it and it is at the end (not front) of fragment_choice

    Postcondition 2: resulting_text is on the monitor
    '''
    # Fulfillment of Postcondition 2:
    global resulting_text, fragments_remaining

    fragment_selected_q = offer_front_fragment()
    # Fulfillment of Postcondition 1:
    # Fulfillment of Part(1) of Postcondition 1:
    if fragment_selected_q != 'n':  # not "no"
        dequeue_results = de_queue(resulting_text, fragments_remaining)
        fragments_remaining = dequeue_results[1]
        resulting_text = str(dequeue_results[0])
    else: #is "no"
        # Fulfillment of Part(2) of Postcondition 1:
        move_from_front_to_back(fragments_remaining)

    # Fulfillment of Postconditions 1-2:
    print("Your answer so far: " + resulting_text + "\n")

    #DEBUG
    #print("Length of fragments_remaining:" + str(len(fragments_remaining)))

def move_from_front_to_back(a_list):
    front_value = a_list.pop(FRONT_INDEX)
    a_list.append(front_value)
    return a_list

    #DEBUGGING CODE
    #print("First a_list: " + a_list[0])
    #i = len(a_list) - 1
    #print("Second a_list: " + a_list[i])
    #print("id of a_list is " + str(id(a_list)))
    #print("id of new_list is " + str(id(new_list)))

def de_queue(a_text, a_list):
    # Returns (0) a_list[FRONT_INDEX] + a_text AND
    # (1) a_list with a_list[FRONT_INDEX] removed
    # for "Returns (0) (the first return)"
    front_element = a_list[FRONT_INDEX]
    new_text = a_text + str(front_element)
    # for "Returns (1) (the second return)"
    new_list = a_list  # (rather than try to manipulate parameters)
    new_list.remove(front_element)
    return new_text, new_list

def run_test():
    describe_test_to_user()
    while len(fragments_remaining) > 0:
        offer_and_process_front_fragment()

# EXECUTION

run_test()
