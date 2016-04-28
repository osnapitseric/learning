
def break_time():
    print("Eric and Lena drive back to home sweet home. They open the and then")
    print("1. Austin feverishly greets us!")
    print("2. All the furniture in the house looks to be missing!")
    door = input("> ")
    if door != int:
        print("learn how to type a number!")
        break_time()
    elif door == "1":
        print("We take him for a walk and snuggle with him for the rest of the day")
    elif door == "2":
        print("But that's fine because Eric's family decided to upgrade our entire interior!")
    else:
        break_time()

def honeymoon():
    print("Where should they go?")
    print("1. Europe")
    print("2. Asia")
    print("3. Russia")
    honeymoon = input("> ")
    if door == str():
        print("Select a number")
    elif honeymoon == "1":
        print("wow such great time!")
    elif honeymoon == "2":
        print("we're gaining 30lbs from eating")
    elif honeymoon == "3":
        print("brrr toooo cold")
    else:
        print("suggest somewhere else then")

def baby():
    print("""
        Take a good look at it
        Look at it now
        Might be the last time you'll
        Have a go round
        I'll let you touch it if you'd
        Like to go down
        I'll let you go further
        If you take the southern route
        Don't go too fast
        Don't go too slow
        You've got to let your body flow
        I like 'em attentive
        And I like 'em in control

        Baby it's yours
        All yours
        If you want it tonight
        I'll give you the red light special
        All through the night
        Baby it's yours
        All yours
        If you want it tonight
        Just come through my door
        Take off my clothes
        And turn on the red light

        I know that you want me I can
        See it in your eyes
        You might as well be honest 'cause the
        Body never lies
        Tell me your secrets and I'll
        I'll tell you mine
        I'm feelin' quite sexy
        And I want you for tonight
        If I move too fast just let me know
        'Cause it means you move too slow
        I like some excitement
        And I like a man that goes

        Baby it's yours
        All yours
        If you want it tonight
        I'll give you the red light special
        All through the night
        Baby it's yours
        All yours
        If you want it tonight
        Just come through my door
        Take off my clothes
        And turn on the red light

        If you want me
        Let me know it
        I'll make time but
        You've got to show it
        If you need me
        I want to see
        But don't mistake me
        I don't want you down on your knees
        I need someone a real man
        I need someone who understands
        I'm a woman a real woman
        I know just what I want
        I know just who I am
        """)

def end():
    print("Are you old enough to see this? How old are you?")
    math = int(input("> "))
    if math == str():
        print("Select a number")
    elif math in range(32,40):
        print("8====D (::)")
        print("hehehe")
    else:
        print("there's nothing to see. Goodbye!")


print("Eric and Lena get married on August 27 2016. What should they do after their wedding day?")
print("1. Take a break and relax from the chaos.")
print("2. Honeymoon!")
print("3. Baby making mode")
decide = input("> ")

if decide == "1":
    break_time()
elif decide == "2":
    honeymoon()
elif decide == "3":
    baby()
else:
    end()

