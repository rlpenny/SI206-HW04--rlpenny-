def question():
    s = input("What is your question?")
    return(s)


def check_question(s):
    if s[-1] == "?":
        answers()
    else:
        print("I’m sorry, I can only answer questions")
        questions()

question()
