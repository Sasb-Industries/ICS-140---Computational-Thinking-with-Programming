def main():
    print("This program will collect your answers for a multiple choice test.  All answers will be A - D.")
    student_answers = collect_student_answers()
    score = check_answers(student_answers)
    print(score)


def collect_student_answers():
    student_answers = []
    valid_answers = ["A","B","C","D"]
    for i in range(10):
        answer = input(f"What is your answer for question #{i+1}?").upper()
        while answer not in valid_answers:
            answer = input(f"Invalid Input.  What is your answer for question #{i+1}?").upper()
        student_answers.append(answer)
    print(f"Your answers where : {student_answers}")
    return student_answers

def check_answers(answer):
    answer_key = ["A", "C","D","B","B","D","B","A","C","A"]
    print(f"The correct answers are : {answer_key}")
    number_correct = 0
    for i in range(len(answer)):
        if answer[i] == answer_key[i]:
            number_correct = number_correct + 1
    return (f"Your score is {number_correct}/{len(answer)} !")

main()