import json
with open('grades.json') as fin:
    data = json.load(fin)

grades = {}
for student, score in data.items():
    d = grades.get(score, [])
    d.append(student)
    grades[score] = d
    
print(json.dumps(grades, indent=4))
