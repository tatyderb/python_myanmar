import json
with open('grades.json') as fin:
    data = json.load(fin)

grades = {}
for student, score in data.items():
    grades[score] = grades.get(score, 0) + 1
    
print(json.dumps(grades, indent=4))
