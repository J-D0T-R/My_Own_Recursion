###   James Rutley   ###
###   Start Date: 09/29/2021   ###
###   End Date: 10/1/2021   ###

###   My Own Recursion   ###

# Variables #
#starting number
n = 1
#end number
n2 = 0

# Functions #

# This recursive function counts down from n1 until it reaches n2.
def counting_down(n, n2):
    if n == n2:
        print(f"{n2}!")
        
    else:
        print(f"{n}")
        counting_down(n - 1, n2)

# This recursive function counts up from n1 until it reaches n2
def counting_up(n, n2):
    #exit clause: the function has done its job
    if n == n2:
        print(f"{n2}!")
    #recalling the function
    else:
        print(f"{n}")
        counting_up(n + 1, n2)

# Main code #

# while loop so they don't have to run the code over if they want to use it more than once.
while True:
    try:
        #setting the value of the starting number
        n = int(input("What number do you want to start from? "))
        #now the ending number
        n2 = int(input("What number are you trying to reach? "))
        
        # if they want to count up 
        if n < n2:
            counting_up(n, n2)
            pass
        
        # if they want to count down
        else:
            counting_down(n, n2)
            pass
     
     # basic anti-crash precaution, if they input a letter when it asks for an integer
     # runs again instead of crashing.
    except ValueError:
        print("That isn't a number.")
      
    # they can choose to quit or go again.
    count_again = input("Want to pick another number? (Y/N) ")
    
    # they go again
    if "Y" in str(count_again) or "y" in str(count_again):
        continue
     
    # they quit
    else:
        print("See you later!")
        break
                