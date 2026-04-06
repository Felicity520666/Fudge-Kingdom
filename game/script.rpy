# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Ophelie", color="#FFE6BF")
define a = Character("Abigail", color="#00FF80")

transform smallright:
    zoom 0.7  # scale down to 40% of original size
    xalign 1.0  # right edge
    yalign 1.0  # bottom edge
transform smallleft:
    zoom 0.7
    xalign -0.7
    yalign 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   
    scene sleep with fade
    play sound "snoring-71560.mp3" volume 8.5
    pause 3.0

    scene dream with fade
    pause 3.0

    play sound "magic-03-278824.mp3"
    scene appear with dissolve
    pause 0.5
    play music "cute-mood-151368.mp3"
    pause 3.0
    scene hi with fade
    a "Hello girl!"
    show scared at smallleft with dissolve
    play sound "fear.mp3" volume 8.5
    o "Ah! Who, I mean, WHAT are you?!"
    a "Hey, don't panic, you're not crazy."
    o "I'm not crazy?! I'm taking to fudges!"
    play sound "girl-laugh-149491.mp3" volume 3.5
    a "Haha.. Oh don't worry, we're not the odd ones here--you are!"
    o "What do you even mean?!"
    a "Well, you see, this is the fudge kindom. Everyone here is a fudge."
    o "HEY! Excuse me?! I'm not a fudge!"
    o "Excactly! So in our eyes, you are the weird one here!"
    a "But we know you adore fudge!"
    a "So, the thing is, you are here because you are the human who loves fudge the most!"
    a "And we are truly touched by your love for fudge."
    a "So after a discussion, we decided to invite you to our kingdom to visit us!"
    show believe at smallleft with dissolve
    o "Okay, thanks a lot then..."
    o "Although it still sounds unbelievable."
    o "But I honestly do love fudge a lot."
    a "Yep! we know that!"
    a "So we plan to give you a whole bunch of fudge as a gift after the tour!"
    show yes at smallleft
    play sound "wow-thatx27s-amazing-girl-229854.mp3" volume 5.9
    o "Wow, that's amazing!"
    o "So sweet of you guys!"
    show glad at smallleft with dissolve
    o "Thank you so much... um, your name please?"
    a "Oh glad you asked that! I am Abigail, your tour guide! And you?"
    o "I'm Ophelie. Nice meeting you Abigail!"
    a "You too Ophelie! So in our kingdom, there are many ethnic groups of fudges."
    a "I am from the mint fudge group--you're favourite flavour!"
    hide glad
    show yes at smallleft with fade
    o "Oh yeah! Definitely! Mint fudge is so good!"
    a "Haha, thank you so much, my mint family will be so happy to hear that!"
    a "Anyway, let me show you around our fudge kingdom!"
    o "Okay! I'm actually really excited!"
    a "Great! Next stop, Peanut Butter Fudge Townlet!"
    play music "footsteps-on-the-nature-trail-419017.mp3"
    scene peanut
    pause 1.5
    play music "village-music-village-background-music-no-copyright-song-217565.mp3"
    show wow at smallleft with fade
    a "Here we are Ophelie!"
    show yes at smallright
    o "Wow! This place smells strongly of peanut butter!"
    play sound "girl-laugh-149491.mp3" volume 3.5
    hide wow
    show happy at smallleft
    a "Haha! Of course! This is the Peanut Butter Fudge Townlet -- every citizen here is peanut butter fudge!"
    o "Wow, amazing! peanut Butter fudge is such a rich, creamy, sweet & salty confection!"
    a "Haha, you know so much about it Abigail! You can almost take my tour guide job!"
    a "So yes, peanut butter fudge is famous for it's dense, melt-in-your-mouth texture, balancing sugary sweetness with nutty peanut butter flavor."
    o "Mmm... Yeah! I also know that thet are often enhanced with vanilla and butter for depth, and can range from simple 4-ingredient version to more complex recipes with chocolate or crunchy additions, providing a satisfying smooth, not gritty, treat perfect for gifting or snacking!"
    a "Oh yeah, perfect for gifting! You will get peanut butter fudge if you can anwser this question."
    o "Yes yes yes! I want peanut butter fudge! What question? I'm ready for the challenge!"
    a "Okay, so you said that there is a simple 4-ingredient version, what are the 4 ingredients?"
    o "Ha! Easy peasy! You can make easy 4-ingredient peanut butter fudge using either a cooked sugar/mailk method or a no-cook butter/sugar method."
    a "Oh you even know that! So, talk about the cooked sugar/milk method first! What are the 4 ingredients?"
    o "As the name suggests, sugar and milk are in it. The others are the crucial peanut butter and the facinating vanilla!"
    a "And for the no-cook butter/sugar method?"
    o "Butter, peanut butter, powdered sugar, and vanilla."
    a "Great job! You really are the ultimate fudge lover!"
    a "You will get a whole box of peanut butter fudge after the tour!"
    o "Thank you! Let's go to the next stop! I'm so excited!"
    play music "footsteps-on-the-nature-trail-419017.mp3"
    scene mint
    pause 1.5
    play music "garden-fairytale-368607.mp3"
    show yes at smallleft with fade
    o "Ahhhhh! My favourite! Is this your hometown Abigail?"
    show happy at smallright with fade
    a "Of course! Welcome to our Mint Fudge Garden!"
    hide yes
    show glad at smallleft with fade
    o "Ahhhhh! You don't even need to introduce it! I know everything about mint fudge!"
    play sound "girl-laugh-149491.mp3" volume 3.5
    a "Haha! I'm so happy to hear that!"
    hide happy
    show yeah at smallright with dissolve
    a "Feeling confident? Here are some questions for you..."
    o "And if I answer correctly I get mint fudge?"
    a "Absolutely! As much as you want!"
    hide glad
    show confident at smallleft with fade
    o "Og my god! Bring it on!"
    a "Okay, first question, what is the flavour?"
    o "A balance of sweet chocolate and cool peppermint or spearmint, sometimes with vanilla notes."
    a "Texture?"
    o "Smooth, soft, and creamy, with variations like a crisp chocolate coating or crunchy cookie pieces."
    a "Appearance?"
    o "Often two-toned, which are green and brown. Sometimes with colorful toppings or a glossy chocolate glaze."
    a "What about ingredients?"
    o "That's easy! Mint fudge are typically made with sugar, butter, milk/cream, chocolate/cocoa, and mint flavoring, like extract or candy."
    a "Wow! Super! Last question is on the variations."
    o "You think it's hard for me? Mint fudge is my favourite! I know all about it!"
    o "Mint fudge can be layered, swirled, loaded with Andes mints, or incororate crushed Thin Mints cookies for added crunch."
    a "Incredible! You know us so well!"
    a "So you got the questions all correct! Yes, mint fudge is often described as a decadent, refreshing, and nostalgic candy that captures the essence of a mint chocolate bar, offering a cooling sensation alongside rich sweetness."
    o "Cool! I can't wait to get my fudge after the tour!"
    o "Where are we going next?"
    hide yeah
    show wow with fade
    a "Actually, I want to ask you that question!"
    a "Where would you prefer to go next?"
    hide wow
    menu:
        "Maple Fudge Burgh":
            a "Great choice! My best friend is a maple fudge!"
            o "Awesome! Oh I love maple fudge so much! Let's go!"
            play music "footsteps-on-the-nature-trail-419017.mp3" 
            jump maple
        "Easter Fudge Park":
            o "Easter fudge! I love easter!"
            a "Excellent! Let's go then!"
            play music "footsteps-on-the-nature-trail-419017.mp3"
            jump easter

    label maple:
        scene road with fade
        play music "maple-chimes-245404.mp3"
        pause 2.0
        show happy at smallright with dissolve
        a "We're almost there Ophelie..."
        pause 2.5
        play sound "magic-03-278824.mp3"
        jump home


    label easter:
        scene road with fade
        play music "spring-easter-day-music-319084.mp3"
        pause 2.0
        show happy at smallright with dissolve
        a "We're almost there Ophelie..."
        pause 2.5
        play sound "magic-03-278824.mp3"
        jump home

    label home:
        play music "relax-piano-171605.mp3"
        scene sleep with fade
        pause 0.5
        scene open
        pause 0.3
        scene sleep
        pause 0.3
        scene open
        pause 0.3
        scene sleep
        pause 0.3
        scene open
        pause 0.3
        play sound "yawning-6096.mp3" volume 4.5
        scene yawn
        o "Oh... no... was it all a dream?"
        scene think with fade
        o "If that sweet fudge kingdom was just a dream, that means..."
        scene bu with fade
        o "I can't get those yummy fudges I was promised..."
        scene think with fade
        o "And I'm not the biggest fudge lover after all..."
        scene bu with dissolve
        o "No!!!!"
        scene buy with fade
        o "Wait... I can buy fudge myself!"
        stop music fadeout 1.5
        play sound "openmindaudio-podcast-outro-stinger-short-clean-end-cue-469091.mp3"
        o "Yes! I'm leaving right away!"

        
    return
