# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image rd neutral = "rd_neutral.png"
image rd happy = "rd_happy.png"
image rd xgames = "rd_xgames.png"
image fd neutral = "fd_neutral.png"
image fd living = "fd_living.png"
image pd happy = "pd_happy.png"
image pd down = "pd_sad.png"
image pd happytoy = "pd_happytoy.png"
image shelterlady concerned = "shelterlady_concerned.png"
image shelterlady = "shelterlady.png"
image skater xgames = "skater_xgames.png"
image skater = "skater.png"
image vogue = "vogue.png"
image bg table = "table.jpg"
image bg room = "room.jpg"
image bg rd_radflip = "radflip.png"

define y = Character("You")
define sl = Character("Shelter Lady")
define s = Character("Skater")
define e = Character("Everyone")
define a = Character("Announcer")
# The game starts here.

label start:
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="You"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #play music "chipper.ogg"
    
    scene bg room 
    with fade

    "Today is the day."
    "Today is the day your dog is coming home!"
    "You remember going to the shelter a few weeks ago to take a look."

    scene bg shelter
    with fade

    "Oh man, all these dogs are the bee's knees."

    show rd neutral 
    "This one is some kind of border collie mix. His tongue is lolling out of his mouth happily."
    "Is he trying to wink?"
    "Are those...?"
    "Sunglasses...?"
    "How are those staying up? He doesn't have ears down there?"
    hide rd neutral
    
    show shelterlady
    sl "Oh yes, he loves those sunglasses. We can never get them away from him. Isn't that adorable?"

    menu:
        "Hell yeah.":
            y "Hell yeah."

        "...":
            y "...Okay."

    sl "Well anyway take a look at these other dogs."

    hide shelterlady
    
    show pd down
    "The next dog is a little shyer. He has a lot of bulk on him and seems to turn away when you try to look at his eyes."
    "He lays down facing away from you and you can see a large gash across his right rear."

    sl "He came from a rough place. He's getting a lot better now. If you're interested in adopting him, keep in mind that you'll have to be very patient."
    sl "Here's the last one."
    hide pd down
    show fd neutral

    "What. THIS IS A BEAUTIFUL DOG."
    "SHE'S BEAUTY, SHE'S GRACE. SHE'S MISS UNITED STATES."

    sl "A little awestruck I see? Yes, she's very beautiful."
    sl "Borzois are a very popular breed among celebrities and as show dogs."
    sl "Our sweet baby here has been having trouble getting adopted because of her excercise needs. She needs to be walked and let loose to run everyday."

    hide fd neutral

    scene bg room
    with fade

    "In my heart I knew which dog I wanted. I wanted..."
    menu:
        "the rad dog!":
            jump rdog
        "the sad dog!":
            jump pdog
        "the beautiful dog!":
            jump fdog
        "a cat!":
            jump cat

label rdog:
    #play music "rad.ogg"
    "The rad dog!"
    $ dog_name = renpy.input("What is the dog's name?")
    $ dog_name = dog_name.strip()
    if dog_name == "":
        $ dog_name="Rad Dog"
    show rd neutral
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
        "Yes":
            "You pet him."
        "Yes":
            "You pet him."
        "Yes":
            "You pet him."
        "Yes":
            "You pet him."
    hide rd neutral
    show rd happy
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
    show rd_happy
    "The park is lively with all of the skateboarders and dogs. There's a group of skaters to the right."
    "%(dog_name)s pant excitedly at them."
    show skater
    s "Hey dude!"
    s "That's a rad dog you've got there!"
    y "I know and I love them." 
    s "My name's Cal by the way. I really love dogs."
    y "Me too! I'm %(player_name)s. Hey can you help me try teaching him to skate?"
    s "Yeah! Of course! Let's try to get him the board."
    hide skater
    jump xgames

label xgames:
    scene black 
    with fade
    centered "{b}a few years later..."
    scene bg stadium 
    "The audience cheers."
    #play audience cheering
    a "WELCOME TO THE 69TH X-GAMES!!!!"
    a "THIS IS THE ONE AND ONLY, THE BEST, THE BADDEST, THE RADDEST"
    a "YOUR FAVORITE DOG"
    a "%(dog_name)s!!!!!"
    show rd xgames at left
    show skater xgames at right
    s "Haha! I can't believe we made it! This is rad!"
    scene bg rd_radflip with fade
    e "Yee-Haw!!!"
    scene black with fade
    centered "{b}RAD Ending"
    return 

label pdog:
    return

label fdog: 
    y "The beautiful dog!"
    $ dog_name = renpy.input("What is the dog's name?")
    $ dog_name = dog_name.strip()
    if dog_name == "":
        $ dog_name="Fashion Dog"
    "You go to pat them, but are intimidated by their gaze."
    y "...so...elegant!"
    "They sniffed at you and nosed your hand"
    "Pet?"
    menu:
        "Yes":
            "You pet them."
        "Yes":
            "You pet them."
        "Yes":
            "You pet them."
        "Yes":
            "You pet them."
    #dog "*bark*"
    y "It's time for your regular walk!"
    "Where to?"
    menu:
        "The park":
            jump fdpark

label fdpark:
    scene bg park
    #insert rd_happy
    #play bark
    "The park is lively with all of the skateboarders and dogs. There's a group of skaters to the right."
    "%(dog_name)s pant excitedly at them."
    show skater
    s "Hey dude!"
    s "That's a rad dog you've got there!"
    y "I know and I love them." 
    s "My name's Cal by the way. I really love dogs."
    y "Me too! I'm %(player_name)s. Hey can you help me try teaching him to skate?"
    s "Yeah! Of course! Let's try to get him the board."
    hide skater
    jump xgames



label cat:
    "I wanted a cat!"
    "Yep. That's when I decided that cats were for me."
    scene bg cat
    y "God, I love cats."
    scene black with fade
    centered "{b}Cat Ending"

    return
