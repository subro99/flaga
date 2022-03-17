import random

def quiz_generator(quest_ans):
    keys_list = list(quest_ans)
    values_list = list(quest_ans.values())
    quiz_1 = random.sample(keys_list, 5)
    d_quiz_1 = {}
    correct_answers = {}
    for question in quiz_1:
        correct_answer = quest_ans.get(question)
        correct_answers.update({question: correct_answer})
        wrong_answers = random.sample(values_list, 3)
        wrong_answers.append(correct_answer)
        answers = wrong_answers
        random.shuffle(answers)
        d_quiz_1.update({question: answers})
    return d_quiz_1, correct_answers

capitals = {'Alabama': 'Montgomery',
            'Alaska': 'Juneau',
            'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock',
            'California': 'Sacramento',
            'Colorado': 'Denver',
            'Connecticut': 'Hartford',
            'Delaware': 'Dover',
            'Florida': 'Tallahassee',
            'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu',
            'Idaho': 'Boise',
            'Illinois': 'Springfield',
            'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines',
            'Kansas': 'Topeka',
            'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta',
            'Maryland': 'Annapolis',
            'Massachusetts': 'Boston',
            'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City',
            'Montana': 'Helena',
            'Nebraska': 'Lincoln',
            'Nevada': 'Carson City',
            'New Hampshire': 'Concord',
            'New Jersey': 'Trenton',
            'NewMexico': 'Santa Fe',
            'New York': 'Albany',
            'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck',
            'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence',
            'South Carolina': 'Columbia',
            'South Dakota': 'Pierre',
            'Tennessee': 'Nashville',
            'Texas': 'Austin',
            'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier',
            'Virginia': 'Richmond',
            'Washington': 'Olympia',
            'West Virginia': 'Charleston',
            'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'
            }
a,b=quiz_generator(capitals)
print(a)
print(b)
