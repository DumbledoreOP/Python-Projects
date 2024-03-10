print("Welcome to my Computer Quiz.")

playing = input("Do you want to play the quiz game? ")

if(playing.lower() != "yes"):
    quit()

print("Okay! Let's Play the game :)")

score = 0

answer =  input("What does CPU stand for? ")

if(answer.lower() == "central processing unit"):
    print("Congratulations! Your answer is Correct!")
    score+=1

else:
    print("Alas! It looks like you are incorrect!")

answer =  input("What does GPU stand for? ")

if(answer.lower() == "graphics processing unit"):
    print("Congratulations! Your answer is Correct!")
    score+=1

else:
    print("Alas! It looks like you are incorrect!")

answer =  input("What does RAM stand for? ")

if(answer.lower() == "random access memory"):
    print("Congratulations! Your answer is Correct!")
    score+=1

else:
    print("Alas! It looks like you are incorrect!")

answer =  input("Whjat does PSU stand for? ")

if(answer.lower() == "power supply unit"):
    print("Congratulations! Your answer is Correct!")
    score+=1

else:
    print("Alas! It looks like you are incorrect!")


print(f"You have got {score} questions correct.")

print(f"Your result in this quiz is {(score*100)/4}%")