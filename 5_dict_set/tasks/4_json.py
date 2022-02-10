import json
data = [
                        {
                                "name": "Alexey Ivanov",
                                "courses" : [
                                        {
                                                "title": "mathematics",
                                                "grades": [8, 9, 9, 6]
                                        }, 
                                        {
                                                "title": "physics",
                                                "grades": [5, 7]
                                        }, 
                                ]
                        },
                        {
                                "name": "Jhon Smith",
                                "courses" : [
                                        {
                                                "title": "russian language",
                                                "grades": [8, 9, 9, 6]
                                        }
                                ]
                        }

]
print(data)
print(json.dumps(data))
print(json.dumps(data, indent=4))
