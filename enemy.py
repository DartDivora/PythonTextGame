


lvl = 1
hp = 10 * lvl
att = 2 * lvl
defense = 3 * lvl




while True:
    user_input1 = input("Would you like to see this enemy\'s stats?\n:")
    if user_input1 == "yes" or "Yes" or "y":
        user_input2 = input("""Okay which stats?
Level
Health Points
Attack
Defense
All
Exit
:""")
        
        if user_input2 == "Exit" or "exit":
            print("dumb")
        elif user_input2 == "Level" or "level":
            print("Level: " + str(lvl))
        elif user_input2 == "Health Points" or "health points":
            print("Health Points: " + str(hp))
        elif user_input2 == "Attack" or "attack":
            print("Attack: " + str(att))
        elif user_input2 == "Defense" or "defense":
            print("Defense: " + str(defense))
        elif user_input2 == "All" or "all":
            print("All stats.")
        else:
            print("wtf")


    elif user_input1 == "no" or "No":
        print("That's cool man.")
        break

    else:
        print("Try again.")
            
        



     
      

    
           

    

   
   

    
    
    



      
    





