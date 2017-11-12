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

image bg cat = im.Scale("cat.jpg", 1280, 720)
image bg xgames = im.Scale("xgames.jpg", 1280, 720)
image bg shelter = "shelter.jpg"
image bg park = "park.jpg"
image bg table = "table.jpg"
image bg room = "room.jpg"
image bg rd_radflip = im.Scale("radflip.png", 1280, 720)
image bg bird ="bird.jpg"
image bg orange = im.Scale("orange.jpg", 1280, 720)

define y = DynamicCharacter("player_name", who_color="00bfff")
define sl = Character("Shelter Lady", who_color="ffbae8")
define s = DynamicCharacter("skater_name", who_color="88ff00")
define e = Character("Everyone")
define a = Character("Announcer", who_color="e04366")

label start:
    $ skater_name = "Skater"
    scene bg orange with fade
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="You"
    play music "chipper.mp3"
    
    scene bg room 
    with fade

    "Today is the day."
    "Today is the day your dog is coming home!"
    "You remember going to the shelter a few weeks ago..."

    scene bg shelter
    with fade

    y "I'm so excited to see all these dogs!"
    show shelterlady 
    sl "Let's go then!"
    hide shelterlady

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
    "The next dog seems to be shy. He has a lot of bulk on him and seems to turn away when you try to look at his eyes."
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
    play music "Pookatori and Friends.mp3"
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
    play sound "rdbark.mp3"
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
    play music "chipper.mp3"
    show rd happy
    "The park is lively with all of the skateboarders and dogs. There's a group of skaters to the right."
    "%(dog_name)s pant excitedly at them."
    show rd happy:
        xalign 0.0
        linear 0.3 xpos 0.6
    show skater at right behind rd
    s "Hey dude!"
    s "That's a rad dog you've got there!"
    y "I know and I love them." 
    s "My name's Cal by the way. I really love dogs."
    $ skater_name = "Cal"
    y "Me too! I'm %(player_name)s. Hey can you help me try teaching him to skate?"
    s "Yeah! Of course! Let's try to get him the board."
    hide skater
    hide rd happy
    jump xgames

label xgames:
    scene black 
    with fade
    centered "{b}a few years later..."
    scene bg xgames
    play music "Pookatori and Friends.mp3"
    "The audience cheers."
    play sound "cheer.mp3"
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

label fdog: 
    y "The beautiful dog!"
    play music "Ranz des Vaches.mp3"
    $ dog_name = renpy.input("What is the dog's name?")
    $ dog_name = dog_name.strip()
    if dog_name == "":
        $ dog_name="Fashion Dog"
    show fd neutral
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
    play sound "fdbark.mp3"
    y "It's time for your regular walk!"
    "Where to?"
    menu:
        "The park":
            jump fdpark

label fdpark:
    scene bg park
    play music "Ranz des Vaches.mp3"
    show fd neutral
    play sound "fdbark.mp3"
    "The park is lively with all of the skateboarders and dogs. There's a group of skaters to the right."
    "%(dog_name)s is runnning around wildly. Her majestic, horse-like gait attracts the eyes of surronding park-goers."
    show skater at right
    s "You have a beautiful dog!"
    y "I know and I love them." 
    hide skater
    "She looks so at peace running in the open."
    "Maybe she really should be a model..."
    jump magazine

label magazine:
    scene black with fade
    centered "{b}a few years later..."
    scene bg table with fade
    show vogue with dissolve
    play music "Ranz des Vaches.mp3"
    "Your precious %(dog_name)s has become the icon of the modeling world. With their dashing looks and free spirit, they've captured the hearts of everyone."
    "Including yours."
    scene black with fade
    centered "{b}Fashion Dog Ending"
    return

label pdog:
    y "The sad dog!"
    play music "saddogtheme.mp3"
    $ dog_name = renpy.input("What is the dog's name?")
    $ dog_name = dog_name.strip()
    if dog_name == "":
        $ dog_name="Good Dog"
    "You hear aggressive borking from the living room."
    y "?"
    show pd down
    y "Hm?"
    y "What the!"
    y "%(dog_name)s!"

    show bg bird
    hide pd down
    "You try to walk closer, but %(dog_name)s shivers and backs away further"
    y "Hmm...."

    scene bg shelter
    with fade
    play music "saddogtheme.mp3"
    show shelterlady

    y "Hey... my dog is acting pretty abnormally..."
    sl "Did %(dog_name)s pee on the couch?"
    y "No...."
    sl "Did %(dog_name)s chew up the pillows?"
    y "Yes, bu.."
    sl "Oh, don't worry about it, that's just puppies teething!"
    y "Uh... but he also borked a bird down!"
    sl "Oh... that... %(dog_name)s was a stray."
    sl "Of his 13 siblings, he was the only one that survived..."
    sl "Strays can often act aggressive or fearful."
    sl "You can divert his attention by giving him chew toys or walking him in the park!"
    y "...."
    sl "If %(dog_name)s is still acting aggressive, you can bring %(dog_name)s back to me."
    y "Ok...."

    scene bg room
    with fade
    play music "saddogtheme.mp3"
    show pd down
    "You're back with your angsty pupper, what do you do?"
    menu:
        "Give chew toy":
            y "Here, take Mr.Hot Dog."
            show pd happytoy

        "Take a walk in the park!":
            y "Yay!"


    scene bg park
    with fade
    play music "saddogtheme.mp3"
    "As you take a walk in the combination dog and skate park with %(dog_name)s, looking at his little butt plodding on the grass."
    "You realize that the our conversations with other messengers have led to a redefining of pseudo-mystical consciousness."
    "Reality has always been bursting with seekers whose third eyes are nurtured by beauty. We are in the midst "
    "of a pranic awakening of conscious living that will align us with the quantum matrix itself."
    "In other words, you don't want to bid farewell to %(dog_name)s, this is a relationship worth fostering."

    scene bg room
    with fade
    play music "saddogtheme.mp3"
    show pd down
    y "I am glad to be by your side, my pawsome furry friend. I am sorry life hasn't treated you better,"
    y "but I believe life will be better with the two of us working together."
    play sound "pdbark.mp3"
    y "You deserve love and I will do whatever it takes to make you feel at home again. You'll belong like a"
    y "warm chocolate chip cookie to a glass of milk."

    scene black with fade
    scene bg room
    with fade
    play music "chipper.mp3"
    y "*yawnnnnn* hello world()"
    y "???"
    "You see a tiny bump in the bed..."
    "You take off the blanket to discover ..."
    show pd happy

    y "%(dog_name)s!"

    menu:
        "Kiss your doggo":
            play sound "kiss.mp3"
            "You smooch %(dog_name)s like a suburban mom with Chihuahua."

        "hug":
            "You hug %(dog_name)s like a babushka hugs her grandson."

    "%(dog_name)s attacks with the most irresistable snuggle in the world!"
    y "I love life and I love you my doggo!"
    scene black with fade
    centered "{b}Good Dog Ending"
    return



label cat:
    "I wanted a cat!"
    "Yep. That's when I decided that cats were for me."
    scene bg cat
    y "God, I love cats."
    scene black with fade
    centered "{b}Cat Ending"
    return
