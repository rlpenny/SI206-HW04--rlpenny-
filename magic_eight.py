import random

def question():
    s = input("What is your question?")
    return(s)

ans = ["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely",
"Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now",
"Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]

def answers():
    return random.choice(ans)


def check_question(s):
    if s[-1] == "?":
        return answers()
    else:
        print("I’m sorry, I can only answer questions")
        questions()

question()
