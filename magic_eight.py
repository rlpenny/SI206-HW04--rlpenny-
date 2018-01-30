import random

<<<<<<< HEAD
=======
def question():
    s = input("What is your question?")

    while s[-1] == "?":
        return(answers())
    else:
        print("I’m sorry, I can only answer questions")
        question()



>>>>>>> refs/remotes/origin/master
ans = ["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely",
"Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now",
"Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]

def question():
    s = input("What is your question?")
    print (check_question())
    return answers()


def answers():
<<<<<<< HEAD
    print (random.choice(ans))

def check_question():
    s = question()
    while s[-1] == "?":
        return "I’m sorry, I can only answer questions"

    else:
        return answers()

=======
    print(random.choice(ans))
>>>>>>> refs/remotes/origin/master

question()
