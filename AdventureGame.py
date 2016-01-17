# Text-based adventure game created by Elaine
import math
import time
import random 

def Pause(lines):
    for line, pause in lines:
        print(line)
        time.sleep(pause)
        
def Ask(question):
    ans = input(question + "[y/n]: ")
    return ans.upper() in ["Y", "YES"]

inventory = []

def StartRoom():
    global inventory 
    Pause([("~~~~~~Welcome to the Chamber of Secrets~~~~~~", 2),
           ("You are in a hall there is a sword on the floor.", 2)])
    if Ask("would you take it?"):
        inventory.append("sword")
        print(inventory)
        time.sleep(1)
    else:
        Pause([("you leave the sword on the floor.", 2)])
    print
    PreWar()
    
def PreWar():
    Pause([("you proceed to the next room.", 2),
           ("Suddenly, you feel something dangerous is approaching...", 2)])
    
    if Ask("Would you run away?"):
        Pause([("you try to run back to the hall...", 2),
               ("but something won't let you...", 2),
               ("there is a freaking BASILISK!!!", 3)])
    else:
        Pause([("you look around and see a BASILISK!", 3)])
        
    if Ask("would you fight?"):
        print
        Combat()
    else:
        Pause([("you are killed by the basilisk.", 2),
               ("your body is left in the cold chamber FOREVER...", 3)])
        complete = 0
        return complete 
        
def Combat():
    global inventory
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if inventory != []:
        Pause([("you have a sword.", 3),
        ("you quickly jab the basilisk in it's eye and gain an advantage.",3),
        ("~~~~~~~~~~~~~~~~~~~~~~~~~~~FIGHTING~~~~~~~~~~~~~~~~~~~~~~~~~~~", 3),
        ("YOU MUST JUMP ABOVE 5 TO KILL THE BASILISK.", 3),
        ("AND IF THE BASILISK HITS HIGHER THAN YOU, YOU WILL DIE.", 3),
        ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",3)])
        hp = int(random.randint(3, 10))
        ba = int(random.randint(5,8))
    else:
        Pause([("you do not have any weapon.", 3),
               ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",3),
               ("~~~~~~~~~~~~~~~~~~~~~~~~~~~FIGHTING~~~~~~~~~~~~~~~~~~~~~~~~~~~", 3),
               ("YOU MUST JUMP ABOVE 5 TO KILL THE BASILISK.", 3),
               ("AND IF THE BASILISK HITS HIGHER THAN YOU, YOU WILL DIE.", 3),
               ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 3)])
        hp = int(random.randint(1, 8))
        ba = int(random.randint(1,5))
    Pause([("you hit a " + "{0}".format(hp), 2),
          ("the basilisk hits a " + "{0}".format(ba), 2)])
    if ba > hp:
        Pause([("The basilisk has dealt more damage than you!",1),
               ("you are dead...", 2)])
        complete = 0
        return complete 
    elif hp < 5:
        print ("You didn't do enough damage to kill the basilisk, but you" 
        " manage to escape!")
        complete = 1
        return complete 
    else:
        print ("You killed the basilisk!")
        complete = 1
        return complete 

def game():
    global inventory
    complete = StartRoom()
    while True:
        if Ask("Do you want to play it again?"):
            game()
        break
        
game()
   
    

        
        
        
            
            
        
              
              
              
    
    

    
    
    
    
    
    
    