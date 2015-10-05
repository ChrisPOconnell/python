__author__ = 'MET'

import random

# Constants
SOURCE_FILE = 'knowlass_1_annotated_source.txt'
SEPARATOR = '@'

# Contents of SOURCE_FILE are on the console --AND--
# content_list = list of fragments in SOURCE_FILE, separated by SEPARATOR

def part1():
    #intent: Read and print the file.
    #precondition: file must exist
    fileR = open(SOURCE_FILE)
    content_of_file = fileR.read()
    print('Entire file: ---------------------------')
    print(content_of_file)
    print('-----------------------------------------')
    content_list = content_of_file.split(SEPARATOR)
    return(content_list)
    #Postcondition: file contents is returned.
# (1) reordered_fragment_indices is a re-ordering of 0, 1, ..., content_list.length - 1
# AND (2) the elements of content_list, are on the console in this order

# Part (1)

def part2(content_list):
    #Intent: creates randomized index
    #precondition, content_list must be generated and passed in.
    reordered_fragment_indices = list(range(len(content_list)))  # *
    print("Here's the reorderded_fragment_indices: ",reordered_fragment_indices)
    random.shuffle(reordered_fragment_indices)
    return(reordered_fragment_indices)
    #Postcondition: index

# Part (2)
def part3(content_list,reordered_fragment_indices):
    #Intent: shuffle and display
    #Precondition: Content_list must be created and index must be generated
    #and randomized.
    print()
    for i in range(len(content_list)):
        current_index = reordered_fragment_indices[i]
        print(str(current_index) + '.' + content_list[current_index])

# * e.g., list(range(3)) means [0, 1, 2]

out_contentlist=part1()
out_randomshuffle=part2(out_contentlist)
part3(out_contentlist,out_randomshuffle)