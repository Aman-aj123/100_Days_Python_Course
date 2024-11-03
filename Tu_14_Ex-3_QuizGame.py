# Quiz  using python


# Lists of many questions with their answers
questions = [
    {
        "question": "Which is the highest mountain peak in the world?",
        "answer": "Mount Everest"
    },
    {
        "question": "Which is the longest river in the world?",
        "answer": "The Ganga"
    },
    {
        "question": "What is the largest ocean in the world?",
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "question": "Who invented the light bulb?",
        "answer": "Thomas Edison"
    },
    {
        "question": "What is the smallest country in the world?",
        "answer": "Vatican City"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "answer": "Oxygen"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "answer": "William Shakespeare"
    }
]

correctAns = 0
wrongAns = 0
leaveAns = 0

for c in questions :
   ask = input(c["question"])  
   if(ask.lower() == c["answer"].lower()) : 
       correctAns = correctAns + 1
   elif(ask == "") :
     leaveAns = leaveAns + 1
   else : 
       wrongAns = wrongAns + 1


print(f"You have given '{correctAns}' correct answers out of '{len(questions)}' ")
print(f"Correct Ans : {correctAns}\n Wrong Ans : {wrongAns} \n Leave Ans : {leaveAns}")