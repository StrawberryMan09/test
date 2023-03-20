image Alex angry C = "Alex angry C.png"        #connect name and image(from image file)
image Alex angry O = "Alex angry O.png"
image Alex disappointed C = "Alex disappoint C.png"
image Alex disappointed O = "Alex disappointed O.png"
image Alex happy O = "Alex happy O.png"
image Alex interested O = "Alex interested O.png"
image Alex nervous blush C = "Alex nervous blush C.png"
image Alex sad C = "Alex sad C.png"
image Alex shocked blush O = "Alex shocked blush O.png"
image Alex suprised C = "Alex suprised C.png"

# Declare characters
define a = Character("Alex")     #give name define

#Game starts 
label start:
    
    scene bg room with vpunch           #bg w/animation
    show Alex shocked blush O               #add sprite
    
    a "{b}S-S-Senpi!!{/b}"                        #text
    a "W-w-w-what are {b}you{/b} doing here!?!?!"
    
    show Alex nervous blush C

    menu:         #list player options
        "I live here?":      #option 1
            show Alex shocked blush O
            a "o-oh! what a coincidence!"        #reaction 1
            show Alex nervous blush C 
            a "."
            a ".."
            a "..."
            a "...."
            jump help
             

        "I hate you.":      #option 2
            show Alex angry O 
            a "o-oh um...."        #reaction 2
            a "awkward.."
            show Alex angry C
            a "."
            a ".."
            show Alex suprised C 
            a "..."
            a "...."
            jump help
            
        "I love you":         #option 3
            show Alex shocked blush O
            a "s-senpi!?!"     #reaction 3
            show Alex disappointed O 
            a "That's fucking weird."
            a "I'm going home. creep."
            hide Alex with moveoutright
            return

label help:
    show Alex happy O 
    a "A-anyway! I'm here as you requested! what did you want from me??"
    show Alex nervous blush C

    menu:
        "Be Friends":
            show Alex interested O 
            a "OH!"
            a "um"
            a "No <3"
            show Alex suprised C with moveoutright
            return 

        "Study":
            show Alex interested O 
            a "Study what?" 
            show Alex suprised C 

            menu: 
                "Your Mom":
                    show Alex disappointed C 
                    hide Alex with moveoutright
                    return

                "School work":
                    show Alex happy O 
                    a "Oh Okay!"
                    show Alex suprised C 
                    
                    menu: 
                        "Study":
                            scene bg books
                            show Alex suprised C 
                            "The next day you both failed the test at school"
                            show Alex disappointed C 
                            "You never saw them again"
                            hide Alex disappointed C with Dissolve(1.0)
                            return

                        "Kiss them":
                            show Alex shocked blush O
                            a "s-senpi!?!"     #reaction 3
                            show Alex disappointed O 
                            a "That's fucking weird."
                            a "I'm going home. creep."
                            hide Alex with moveoutright
                            return

                "You":
                    show Alex shocked blush O
                    a "s-senpi!?!"     #reaction 3
                    show Alex disappointed O 
                    a "That's fucking weird."
                    a "I'm going home. creep."
                    hide Alex with moveoutright
                    return

        "Make Love":
            show Alex shocked blush O
            a "s-senpi!?!"     #reaction 3
            show Alex disappointed O 
            a "That's fucking weird."
            a "I'm going home. creep."
            hide Alex with moveoutright
            return


return       #end(return to start screen)