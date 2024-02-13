for i in range(12):

    if( i == 6 or i == 4):
        print("Iteration skipped")
        continue       #It just skips that iteration and runs the loop again

    if( i == 11):
        break       #Quite obvious, it just breaks the loop and exits,

    print("5 X", i, "=", 5*(i))

print("Exited the loop")