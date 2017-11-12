# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define sl = Character("Shelter Lady")
define s = Character("Skater")
define e = Character("Everyone")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #play music "chipper.ogg"
    
    scene bg room 
    with fade

    "Today is the day."
    "Today is the day your dog is coming home!"
    "You remember going to the shelter a few weeks ago to take a look."

    #scene bg shelter
    #with fade
    "Oh man, all these dogs are the bee's knees."

    #show rd_neutral 
    "This one is some kind of border collie mix. His tongue is lolling out of his mouth happily."
    "Is he trying to wink?"
    "Are those...?"
    "Sunglasses...?"
    "How are those staying up? He doesn't have ears down there?"


    #hide rd_neutral
    #show shelterlady
    sl "Oh yes, he loves those sunglasses. We can never get them away from him. Isn't that adorable?"

    menu:
        "Hell yeah.":
            y "Hell yeah."

        "...":
            y "...Okay."

    sl "Well anyway take a look at these other dogs."

    #hide shelterlady
    #show pd_down
    "The next dog is a little shyer. He has a lot of bulk on him and seems to turn away when you try to look at his eyes."
    "He lays down facing away from you and you can see a large gash across his right rear."

    sl "He came from a rough place. He's getting a lot better now. If you're interested in adopting him, keep in mind that you'll have to be very patient."
    sl "Here's the last one."
    #hide pd_down
    #show fd_neutral

    "What. THIS IS A BEAUTIFUL DOG."
    "SHE'S BEAUTY, SHE'S GRACE. SHE'S MISS UNITED STATES."

    sl "A little awestruck I see? Yes, she's very beautiful."
    sl "Borzois are a very popular breed among celebrities and as show dogs."
    sl "Our sweet baby here has been having trouble getting adopted because of her excercise needs. She needs to be walked and let loose to run everyday."

    #hide fd_neutral"

    scene bg room
    with fade

    "In my heart I knew which dog I wanted. I wanted..."
    menu:
        "the rad dog!":
            jump rdog
        "the sad dog!":
            return
        "the beautiful dog!":
            jump bdog
        "a cat!":
            jump cat

label rdog:
    #play music "rad.ogg"
    "The rad dog!"
    $ dog_name = renpy.input("What is the dog's name?")
    $ dog_name = dog_name.strip()
    if dog_name == "":
        $ dog_name="Rad Dog"
    define dog = Character(dog_name)
    #show rd_neutral
    y "Oh my god. Hello, %(dog_name)s! You are so rad."
    "You begin to pat him."
    "He flips over to his belly."
    y "So soft... so cool..."
    "%(dog_name)s walks over to your skateboard and paws at it."
    y "Do you want to use it?"
    "You lay the skateboard on the ground and %(dog_name)s steps onto it."
    y "Jesus. How can he get any cooler?"
    #play sound effect "bark"
    "Are you going to pet him?"
    menu:
        "yes":
            "you pet him."
        "yes":
            "you pet him."
        "yes":
            "you pet him."
        "yes":
            "you pet him."
    #hide rd_neutral
    #show rd_happy
    "%(dog_name)s seems happy."
    y "Oh! It's almost time for a walk."
    menu:
        "Go to the park.":
            "Well the only park in town is a combination skate park, dog park, people park anyways."
            jump rdpark
        "Go to skatepark":
            "Well the only park in town is a combination skate park, dog park, people park anyways."
            jump rdpark
        "Go to X-games":
            jump xgames

label rdpark: 
    scene bg park
    #insert rd_happy
    "*bark*"
    "RD sees the skateborders and pants excitedly"
    s "Hey dude!"
    s "That's a rad dog you've got there!"
    y "I know and I love them. Hey can you help me try teaching him to skate?"
    s "Yeah! Of course! Let's try to get him the board."

label xgames:
    "/The audience is cheering/"
    scene bg stadium 
    "WELCOME TO THE 69TH X-GAMES!!!!"
    "THIS IS THE ONE AND ONLY, THE BEST, THE BADDEST, THE RADDEST"
    "YOUR FAVORITE DOG"
    dog_name + "!!!!!"
    # image rd_neutral
    # image skater 
    s "Haha! I can't believe we made it! This is rad!"
    rd "*bark bark*"
    #rd splash screen insert
    e "Yee-Haw!!!"
    scene black with fade
    centered "{b}RD Ending"
    #rad dog ending
    return 

label fdog: #THIS IS UNFINISHED AND UNTESTED 
    "...so...elegant!"
    "They sniffed at you and nosed your hand"
    "Pet?"
    menu:
        "yes":
            "you pet them"
        "yes":
            "you pet them"
        "yes":
            "you pet them"
        "yes":
            "you pet them"
    $ dog_name = renpy.input("What is the dog's name?")
    $ dog_name = dog_name.strip()
    if dog_name == "":
        $ dog_name="Fashion Dog"
    define dog = Character(dog_name)
    dog "*bark*"
    # time forward
    "Walk!"
    "Where to?"
    menu:
        "The park"
# WARNING... UNFINISHED AND UNTESTED!



label cat:
    "I wanted a cat!"
    "Yep. That's when I decided that cats were for me."
    scene bg cat
    y "God, I love cats."
    scene black with fade
    centered "{b}Cat Ending"

    return
