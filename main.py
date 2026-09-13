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

def validation_of_answer():
    option_list = ["a", "b", "c", "d"]
    while True:
        answer = input("Enter your answer between a - d: ").strip().lower()
        if answer in option_list:
            return answer
        else:
            print("Enter a valid answer between a - d")
            
def Question_show(question):
    print(question["Question"])
    for keys, values in question["Options"].items():
        print(keys, end=") ")
        print(values)
        
def verification_of_answer(answer, question, initial_score):
    if answer == question["Answer"]:
        print("Answer is correct")
        initial_score += 1
    else:
        print("Answer is wrong")
    return initial_score 

def input_question():
    question = input("Enter your question: ")
    options = {"a":input("Enter option a: "),
                "b":input("Enter option b: "),
                "c":input("Enter option c: "),
                "d":input("Enter option d: ")} 
    return question, options 

def marks_card(score, quiz):
    total_questions = len(quiz)
    percentage = (score/total_questions)*100
    print(f"You scored {score}/{total_questions}, percentage achieved {percentage:.0f}%") 

def add_questions():
    while True: 
        try:
            last_ques = quiz[-1]
            ques_no = last_ques["Ques.no"] + 1
        except IndexError:
            ques_no = 1
        print("Quesno",ques_no)
        question, option = input_question()
        answer = validation_of_answer()
        
        add_question = {"Ques.no" : ques_no,
                        "Question": question,
                        "Options": option,
                        "Answer": answer}
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
         
def edit_question():
    while True:
        try:
            choice = int(input("Enter Question no which you want to edit: "))
        except ValueError:
            print("Enter a valid choice")
            continue 
        for question in quiz:
            if choice == question["Ques.no"]:
                Question_show(question)
                print(f'Answer is {question["Answer"]}')
                print("edit question now....")
                ques, opt = input_question()
                question["Question"] = ques 
                question["Options"] = opt
                answer = validation_of_answer()
                question["Answer"] = answer 
                save_quiz()
                print("Question edited successfully")
                return  
        else:
            print("Enter a valid Question no") 
                   
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
            Question_show(question)
            answer = validation_of_answer()
            score = verification_of_answer(answer, question, score)
        print("Quiz has ended") 
        marks_card(score, quiz)   
        
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
            Question_show(random_question)
            used_questions.append(random_question)
            answer = validation_of_answer()
            score = verification_of_answer(answer, random_question, score)
        marks_card(score, quiz)
            
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