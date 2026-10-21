#Quiz Game:

Questions = ['1. Which element has the chemical symbol Au?',
             '2. What is the longest river in the world?',
             '3. Total Number of bones in body?',
             '4. What is the capital of France?',
             '5. What is the smallest bone in the human body?']

Correct_Answers = ['Gold',
           'Nile',
           '206',
           'Paris',
           'Stapes']

point = 0



for question, answer in zip (Questions,Correct_Answers):
    print(question)
    Player_Answer = (input('Enter the Correct Answer:'))
    
    if Player_Answer.lower() == answer.lower():
        
        print('Correct Answer!!!')
        point = point + 1
        
    else:
        print(f'Wrong Answer! Correct is {answer}')
    print()

print(f"Score: {point}/5")


            
