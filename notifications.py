# parameter to call is the text that we want to yell
# a colon starts the body of a function

def yell(text):
    text = text.upper()
    num_of_char = len(text)
    shout = text + "!" * (num_of_char // 6)
    print(shout)

yell("You are doing great!")
yell("Remember, to always ask for help when you need it!")
yell("Use the treehouse community to answer questions!")