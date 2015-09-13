#an_array = 102345,102343
#print(an_array)

def get_min(an_array): #4
    upper_index = 0 #19
    best_index = upper_index #25
    min = an_array[best_index] #10
    print(min) #DEBUG CODE
    print(len(an_array)) #DEBUG CODE
    while upper_index < len(an_array): #21 HAD TO REMOVE -1 FROM THIS LINE
         print("Entering while loop") #DEBUG
         if an_array[upper_index] < min:
             print("entering IF loop", upper_index)
             best_index = upper_index #25
             min = an_array[best_index] #10
         upper_index += 1 # 11 perturb towards termination #11
    return min #9

print("get_min([102345, 102343] should equal 102343: " #16
+ str(get_min([102345, 102343]))) #26
