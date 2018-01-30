import random

def question():
    s = input("What is your question?")
    return(s)

<<<<<<< HEAD
ans = ["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely",
"Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now",
"Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]

def answers():
    return random.choice(ans)
>>>>>>> add_questions
=======

def check_question(s):
    if s[-1] == "?":
        answers()
    else:
        print("I’m sorry, I can only answer questions")
        questions()

question()
>>>>>>> fec9b8823a65f920ff0b58026df592ace95b99af
