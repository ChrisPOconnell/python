__author__ = 'chris'
__author__ = 'chris'
from eight_queensattempt2.obstruction_tests import obstructed_above

BOARD_SIZE = 8


def get_stable_configurations():
    row_index = 0
    stable_configurations = \
        [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0], \
         [4, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0, 0, 0], [6, 0, 0, 0, 0, 0, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0]]
    #temp_stable_configurations = stable_configurations.copy()  # for changes
    while row_index < BOARD_SIZE - 1:  # termination fulfills subgoal 3 (see Note 1 below)
        #print("-------entering for WHILE LOOP.  Configuration index = ","Row Index = ",row_index)
        temp_stable_configurations = stable_configurations.copy()  # for changes
        row_index = row_index + 1  # termination is obvious
        for configuration_index in range(len(stable_configurations)):
            #print("-------entering for configuration index loop.  Configuration index = ",configuration_index,"Row Index = ",row_index)
            configuration = stable_configurations[configuration_index]  # shorthand
            temp_stable_configurations.remove(configuration)  # (may replace)
            #print("Configuration:",configuration)
            #temporary_configuration = configuration.copy()  # redefined
            for column_index in range(BOARD_SIZE):
                temporary_configuration = configuration.copy()

                #temporary_configuration[row_index]=column_index
                #configuration = stable_configurations[configuration_index]  # shorthand
                #print("-------entering for COLUMN_INDEX index loop.  Stable Configurations = ", len(stable_configurations),"Configuration index = ",configuration_index,"Row Index = ",row_index," Column Index = ",column_index)
                #print(obstructed_above(row_index,column_index,configuration))
                if not obstructed_above(row_index, column_index, configuration):
                    #print("first - temporary_configuration: ",temporary_configuration)
                    #temporary_configuration[row_index] = column_index
                    #print("Second - temporary_configuration: ",temporary_configuration)
                    temporary_configuration[row_index]=column_index
                    temp_stable_configurations.append(temporary_configuration)
        stable_configurations=temp_stable_configurations.copy()


    #OK
    stable_configurations = temp_stable_configurations.copy()  # restore #(at the end?)
    #OK
    return stable_configurations

# TEST
print("------- TEST of get_stable_configurations() -------")
stable_configurations = get_stable_configurations()
print("\nNumber of solutions: " + str(len(stable_configurations)) + "\n")
print(stable_configurations)
