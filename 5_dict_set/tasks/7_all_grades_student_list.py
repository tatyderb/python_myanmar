import json
with open('all_exams.json') as fin:
    data = json.load(fin)

grades = {}
for course in data:
    for student, score in data[course].items():
        if student not in grades:
            grades[student] = {}
        grades[student][course] = score
    
print(json.dumps(grades, indent=4))
