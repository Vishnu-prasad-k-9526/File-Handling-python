import random
import os
def load_questions(filename="questions.txt"):
    questions= []
    try:
        with open (filename, 'r') as file:
            for line in file:
                parts= line.strip().split('|')
                if len (parts)==2:
                    question = parts [0] .strip()
                    answer = parts [1].strip().lower()
                    questions.append({"question":question,"answer":answer})
        if not questions:
            print(f"warning: NO question  found in '{filename}'please ensure the file is correctly formatted.")
    except FileNotFoundError:
        print(f"Error:The file '{filename}' was not found. please create with it questions")
        return []
    return questions

def run_quiz(questions):
    if not questions:
        print("cannot start the quiz: NO questions not avaliable")
        return
    
    score=0
    random.shuffle(questions)
    for i,q_data in enumerate(questions):
        print(f"\nQuestion{i+1}: {q_data['question']}")
        user_answer = input("your answer:"). strip()

        if user_answer.lower() == q_data['answer'].lower():
            print("correct!")
            score +=1
        else:
            print(f"incorrect .THE correct answer was:{q_data['answer']}")
    print(f"\n Quiz finished ! you scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    base_dir=os.path.dirname(os.path.abspath(__file__))
    quiz_file=os.path.join(base_dir,"question.txt")
    all_questions= load_questions(quiz_file)
    run_quiz(all_questions)

