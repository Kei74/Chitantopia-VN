# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Loopy")
define mc = Character("MC")
define mom = Character("mom")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene intro-house

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    mc "Bye, Sis! Bye Mom! I'll let you know when I get to RVDS!"

    mom "Do you have everything with you? Want me to pack you a lunch for the journey?"

    mc "No Mom, I'll be fine!"

    mom "Did you pack your underwear? Do you have your card? Things are very different in RVDS, you know! The people can be very rude and-"

    mc "Mom, I sad I'll be fine! I'll ask you if I need any help with anything!"

    show loopy flashback 
    
    l "You better reply to my texts every day, Onii-chan! Or else I'll come over and kick your butt!"

    "I knelt down and pat my sister's head. She may be small, but she certainly packed a punch. I saw myself missing her a lot, and despite the harrassment she gave me, I knew that she would miss me too."

    mc "I'll get you a souvenir when I come back to visit you. You better behave and listen to mom! Or I'll be the one kicking you!"

    "Loopy grinned as I stood back up, but I could see that she was fighting back tears."
    "She would never forgive me if I saw her cry, so I took the chance to finally leave my family behind and start a new life."

    scene black
    with dissolve

    "That was almost 4 years ago."

    "My sister is 18 now, Chitantopia has closed its borders, and my life is at a dead end."

    scene RVDS

    "After moving to RVDS, I managed to find work as a journalist reviewing anime."

    "But ever since the leader went into hiding, the entire nation went into decline, and soon the company I wrote for went under."

    "With my job gone and rampant crime ravaging the streets, I decided to finally return to my homeland."

    scene Train

    "As I made my way back to Chitantopia, I realised how difficult this entire decision would be."

    "First of all, contact with my sister completely ceased 2 years after I left."

    "It was all over the news: 'Military Coup Overthrows Queen of Chitantopia'."

    "After that, the borders were closed and restricted to Chitantopians only, and all contact with the outside world was cut off."

    "I still held my passport, so getting back in shouldn't be a problem."

    "Still, reading that article in the news naturally made me worried about my family and friends back home, but I figured that they would be able to handle everything on their own. "

    "My sister wasn't a girl to be messed with, after all!"

    # This ends the game.

    return
