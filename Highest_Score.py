exam_scores = [85, 96, 78, 388, 95, 73, 89, 191, 576, 84]
# total_exam_score = sum(exam_scores)
# max_score = max(exam_scores)
# min_score = min(exam_scores)
# print(max_score)
# print(total_exam_score)
# print(min_score)

sum = 0
for score in exam_scores:
    sum += score

print("The sum of the list is" ,sum)

max_exam_score = 0

for  score in exam_scores:
    if(score > max_exam_score):
        max_exam_score = score

print("The maximum score in te list is", max_exam_score)

min_exam_score = exam_scores[0]

for score in exam_scores:
    if(score < min_exam_score):
        min_exam_score  = score

print("The minimum score is" ,min_exam_score)
