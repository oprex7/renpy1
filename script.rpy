# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default Brad = Character('Brad', color="#E03B8B")


# The game starts here.

label start:
    $ refuse_drink = False
    $ drank_tea = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show hythe_range with fade

    show man1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    Brad "Welcome to Hythe Ranges"

    # test branching
menu:
     "What should I do?"

     "Go to the outside targets":
         "I start walking, but i feel im doing something wrong."

     "Follow the path":
         $ drank_tea = True
         "I start walking and enjoy the view."

     "Walk infront while flag is up":
         $ refuse_drink = True
         jump ending
  

label after_menu:

     scene hythe_range_2 with fade

     show man1

     "its getting near the end of visiting time, what should i do?."

     show soldier 1 at right

menu:

    "steal a gun.":
        "you got shot dead, womp womp'"
        
    "Go right.":
        "You chose the wrong direction you got shot bcos u didnt see the flag"

    "ask for a ciggerette and leave." if drank_tea:
        "Everyone loves you, gg'"

    
label ending:

    if refuse_drink:
        "You walked infront and got shot - Bye"
    else:
        "The end."
return