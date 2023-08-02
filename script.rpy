# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Loopy")
define mc = Character("MC")
define mom = Character("mom")
define bcdude Character("Border Control Dude")
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

    "I knelt down and pat my sister's head. She may be small, but she certainly packed a punch.{w}\nI saw myself missing her a lot, and despite the harrassment she gave me, I knew that she would miss me too."

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

    scene Border

    "After an hour long train ride, I found myself standing in front of Border Control."

    "I double checked the station I was on."

    "This is Chitantopia, right?..."

    "Why did it look like this? Did it really change this drastically after only 4 years?"

    scene Border_Control

    "I walked up to the man checking the passports. Nobody else was around, and it looked like I was the only person checking in the entire day."

    bcdude "Papers please."

    mc "Sure, here."

    "I handed over my passport."

    bcdude "You a journalist, huh?"

    mc "Ex-journalist. I left the company."

    "The man in the booth stared me down.{w} I wasn't surprised.{w} An isolated country like Chitantopia wouldn't take too kindly to people who's careers were to snoop around."

    bcdude "You recognise this guy?"

    "I look at the photo he gave me. Of course I recognised him, he was the world's most wanted terrorist,{w} Welkin."

    "Of course, I wasn't going to tell him that."

    mc "Never seen him before."

    bcdude "Alright. Entry into Chitantopia approved,{w} cause no trouble."

    "He stamped my passport and handed it back to be."

    bcdude "Look into the camera."

    "I looked into the camera facing me, and waited for it to take a photo."

    "After a blinding flash, I turned back to the man in the booth."

    bcdude "Welcome home. We will be keeping an eye on you."

    "I nodded at the man and picked up my suitcase, looking over at the distant skyscrapers, which definitely weren't there 4 years ago."

    scene Border

    "I took out my phone, but it looked like the internet was blocked. Thankfully, the map still worked."

    "I walked over to the nearest bus stop by the border and waited for the next bus to arrive."

    "I guess the first step is to see Loopy again..."

    # This ends the game.

    return
