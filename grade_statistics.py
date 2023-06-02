#Enter student exam score(0-20) and exercise score(0-100) separated by a space
#Hit enter on an empty input to run stastistical anaylsis on class results

#Retrieves all exam and exercise scores 
def input_scores():
    exam_scores = []
    exercise_scores = []
    while True:
        grade_input = input("Exam points and exercises completed:")
        if grade_input == "":
            break
        grade_split = grade_input.split()
        exam_scores.append(int(grade_split[0]))
        exercise_scores.append(int(grade_split[1]))
    
    exercise_scores_converted = exercise_score_converter(exercise_scores)
    return exam_scores, exercise_scores_converted

#converts exercise score 
def exercise_score_converter(exercise_scores : list):
    exercise_score_conv = []
    for score in exercise_scores:
        converted_score = score // 10
        exercise_score_conv.append(converted_score)
    return exercise_score_conv

#calculates grades 
def grade_calculator(exam_scores : list,exercise_scores_converted : list):
    grade_list = []
    for i in range(len(exam_scores)):
        exam = exam_scores[i]
        exercises = exercise_scores_converted[i]
        points = exam + exercises
        if exam < 10 or points <= 14:
            grade_list.append(0)
        elif points <= 17:
            grade_list.append(1)
        elif points <= 20:
            grade_list.append(2)
        elif points <= 23:
            grade_list.append(3)
        elif points <= 27:
            grade_list.append(4)
        elif points <= 30:
            grade_list.append(5)
    return grade_list

def statistical_analysis(grade_list: list,exam_scores : list,exercise_scores_converted: list):
    print("Statistics:")
    print(f"Points average: {(sum(exam_scores)+sum(exercise_scores_converted))/len(exam_scores):.1f}")
    pass_count = 0
    for grade in grade_list:
        if grade != 0:
            pass_count+=1

    print(f"Pass percentage: {pass_count/len(exam_scores)*100:.1f} ")
    print("Grade distribution:")
    print(f"5: {grade_list.count(5) * '*'}")
    print(f"4: {grade_list.count(4) * '*'}")
    print(f"3: {grade_list.count(3) * '*'}")
    print(f"2: {grade_list.count(2) * '*'}")
    print(f"1: {grade_list.count(1) * '*'}")
    print(f"0: {grade_list.count(0) * '*'}")

def main():
    exam_scores, exercise_score_converted = input_scores()
    grade_list = grade_calculator(exam_scores, exercise_score_converted)
    statistical_analysis(grade_list,exam_scores,exercise_score_converted)
main()
 

