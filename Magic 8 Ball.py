import random

ball = random.randint(1, 9)

Question = input("Question? ")
Answer = ""

if ball == 9:
    Answer = "Yes - definitely." 
elif ball == 8:
    Answer = "It is decidedly so."
elif ball == 7:
    Answer = "Without a doubt."
elif ball == 6:
    Answer = "Reply hazy, try again."
elif ball == 5:
    Answer = "Ask again later."
elif ball == 4:
    Answer = "Better not tell you now."
elif ball == 3:
    Answer = "My source say no."
elif ball == 2:
    Answer = "Outlook not so good."
elif ball == 1:
    Answer = "Very doubtful"

print("Question: ", Question)
print("Answer:   ", Answer)