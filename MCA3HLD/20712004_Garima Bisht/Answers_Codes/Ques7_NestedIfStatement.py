score = int(input("\nEnter your score"))

if(score <=100 and score >= 90): 
  print("Outstanding")
elif(score < 90 and score >= 80):
  print("Excellent")
elif(score < 80 and score >= 70):
  print("VeryGood")
elif(score < 70 and score >= 60):
  print("Good")
elif(score < 60 and score > 50):
  print("Fair")
elif(score == 50):
  print("Dont loose hope work hard , All the best for next time")
elif(score < 50 and score >= 0):
  print("Dont loose hope work hard , All the best for next time")
else:
  print("Enter a valid score between 0 and 100")