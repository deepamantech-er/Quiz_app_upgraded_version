import json
import random
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
        try:
            last_ques = quiz[-1]
            ques_no = last_ques["Ques.no"] + 1
        except IndexError:
            ques_no = 1
        print("Quesno",ques_no)
        ques = input("Enter your question: ")
        opt =  {"a":input("Enter option a: "),
                "b":input("Enter option b: "),
                "c":input("Enter option c: "),
                "d":input("Enter option d: ")}
        while True:
            uncheck_ans = input("Enter Your answer between options a - d: ").strip().lower()
            if uncheck_ans == "a" or uncheck_ans =="b" or uncheck_ans == "c" or uncheck_ans == "d":
                ans = uncheck_ans
                break 
            else:
                print("Enter answer between a - d")
                continue 
        
        add_question = {"Ques.no" : ques_no,
                        "Question": ques,
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
    if not quiz:
        print("first Add a Quiz, there is no Quiz in memory")
    else:
        print("--You are doing Quiz--")
        for question in quiz:
            print(question["Ques.no"] ,end=") ")
            print(question["Question"])
            for keys, values in question["Options"].items():
                print(keys, end=") ")
                print(values)
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
        
def random_quiz_run():
    Quesno = 1
    score = 0
    used_questions = []
    if not quiz:
        print("first Add a Quiz, there is no Quiz in memory")
    else:
        print("--You are doing random quiz--")
        while True:
            try:
                random_question_for_use = [question for question in quiz if question not in used_questions]
                random_question = random.choice(random_question_for_use)
            except IndexError:
                print("Quiz has completed")
                break 
            print(f"Ques.no {Quesno}")
            Quesno += 1 
            print(random_question["Question"])
            for keys, values in random_question["Options"].items():
                print(keys, end=") ")
                print(values)
            used_questions.append(random_question)
            while True:
                answer = input("Enter answer between a - d: ")
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    break 
                else:
                    print("Enter a valid answer between a - d")
                    continue 
            if answer == random_question["Answer"]:
                print("answer is correct")
                score += 1
                continue
            else:
                print("answer is wrong")
                continue 
        print(f"Your score is {score}/{len(quiz)}")
        
def edit_question():
    while True:
        try:
            choice = int(input("Enter Question no which you want to edit: "))
        except ValueError:
            print("Enter a valid choice")
            continue 
        for question in quiz:
            if choice == question["Ques.no"]:
                print(question["Question"])
                for keys, values in question["Options"].items():
                    print(keys, end=") ")
                    print(values)
                print(f"Answer is {question["Answer"]}")
                question["Question"] = input("Enter updated Question: ")
                question["Options"] = {"a":input("Enter option a: "),
                                       "b":input("Enter option b: "),
                                       "c":input("Enter option c: "),
                                       "d":input("Enter option d: ")}
                while True:
                    modified_answer = input("Enter Your answer between options a - d: ").strip().lower()
                    if modified_answer == "a" or modified_answer == "b" or  modified_answer == "c" or modified_answer == "d":
                        question["Answer"] = modified_answer 
                        save_quiz()
                        print("Question edited successfully")
                        return  
                    else:
                        print("Enter a valid answer between a-d")
                        continue 
        else:
            print("Enter a valid Question no") 
            
while True:
    print("Choose Task ?")
    print("1 = Run quiz")
    print("2 = Run Random quiz")
    print("3 = Quiz settings")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter number between 1 - 2")
        continue
        
    if choice == 1:
        run_quiz()
        
    elif choice == 2:
        random_quiz_run()
        
    elif choice == 3:
        while True:
            print("--SETTINGS--")
            print("-------------")
            print("1. Add Questions")
            print("2. Edit Question")
            print("3. Delete Quiz")
            try:
                choice = int(input("Enter Your choice between 1 - 3 : "))
            except ValueError:
                print("Enter a valid input between 1 - 2")
                continue          
            if choice == 1:
                add_questions()
                break 
            elif choice == 2:
                edit_question()
                break 
            elif choice == 3:
                delete_quiz()
                break 
            else:
                print("Enter a valid choice between 1 - 2")
                continue  
    else:
        print("Enter a valid number between 1 - 2")
        continue     
        
    break 