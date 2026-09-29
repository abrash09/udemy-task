student_scores = [80, 60, 50, 65, 75, 55]

def sum_score_above_average(p_student_scores):
    count = 0
    total = 0
    
    for num in p_student_scores:
        total += num
        count += 1
        average = total / count
        avg = 0
    for num in p_student_scores:
        if num > average:
            avg += num
    return avg

print(sum_score_above_average(student_scores))