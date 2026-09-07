import json
print("==QUIZ APP 🧑‍🎓==")

def load_quiz():
    try:
        with open("quiz.json", "r") as file:
            quiz = json.load(file)
            # return quiz 
    except (json.JSONDecodeError, FileNotFoundError):
        quiz = [] 
    return quiz 
    
quiz = load_quiz()

def save_quiz():
    with open("quiz.json", "w")as file:
        json.dump(quiz, file, indent=4)

def add_questions():
    while True:
        ques = input("Enter your question: ")
        opt = [input("Enter option a: "),
                input("Enter option b: "),
                input("Enter option c: "),
                input("Enter option d: ")]
        while True:
            uncheck_ans = input("Enter Your answer between options a - d: ").strip().lower()
            if uncheck_ans == "a" or uncheck_ans =="b" or uncheck_ans == "c" or uncheck_ans == "d":
                ans = uncheck_ans
                break 
            else:
                print("Enter answer between a - d")
                continue 
        
        add_question = {"Question": ques,
                        "Options": opt,
                        "Answer": ans}
        quiz.append(add_question)
        save_quiz()
        print("Question added successfully")
        print("add more question?")
        print("1) yes")
        print("2) no")
        while True:
            try:
                add_more = int(input("Enter your choice: "))
            except ValueError:
                print("Enter a valid choice between 1-2")
                continue
            if add_more == 1:
                break      
            elif add_more == 2:
                break 
            else:
                print("choose between 1 and 2")
                continue 
        if add_more == 2:
            break
                   
def delete_quiz():
    quiz.clear()
    save_quiz()
    print("quiz deleted successfully")
            
def run_quiz():
    score = 0
    if quiz == []:
        print("first Add a Quiz, there is no Quiz in memory")
    else:
        print("--You are doing Quiz--")
        for question in quiz:
            print(question["Question"])
            for items in question["Options"]:
                print(items)
            while True:
                answer = input("Enter answer between a - d: ").strip().lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    break  
                else:
                    print("Enter valid answer between a - d")
                    continue 
            if answer == question["Answer"]:
                print("anwer is correct")
                score += 1 
            
            else:
                print("answer is wrong")
        print("Quiz has ended") 
        print(f"You Scored {score}/{len(quiz)}")    
        
while True:
    print("Choose Task ?")
    print("1 = Run quiz")
    print("2 = Quiz settings")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter number between 1 - 2")
        continue
        
    if choice == 1:
        run_quiz()
        
    elif choice == 2:
        while True:
            print("--SETTINGS--")
            print("-------------")
            print("1. Add Questions")
            print("2. Delete Quiz")
            try:
                choice = int(input("Enter Your choice between 1 - 2 : "))
            except ValueError:
                print("Enter a valid input between 1 - 2")
                continue
            if choice == 1:
                add_questions()
                break 
            elif choice == 2:
                delete_quiz()
                break 
            else:
                print("Enter a valid choice between 1 - 2")
                continue  
    else:
        print("Enter a valid number between 1 - 2")
        continue     
        
    break 