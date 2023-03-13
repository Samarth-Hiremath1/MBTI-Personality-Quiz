import os
import time

#Function sets up Homepage for program.
def homePage():
  os.system("clear")
  print("Hello and Welcome to the MBTI test!")
  print("An MBTI test measures your preferences on the Myers and Briggs' four dimensions of personality type.")
  print("")
  print("Press 1 and click enter if you want to learn more about an MBIT test!")
  print("                              OR")
  print("Press 2 and click enter if you want to take an MBTI test for yourself!")
  print("")
  where = int(input("Enter Number Here: "))
  if(where == 1):
    info()
  else:
    quiz()

#Function dislpayś info about MBTI test.
def info():
  os.system("clear")
  print("The Myers–Briggs Type Indicator is an introspective self-report questionnaire based on the personality theory created by Isabel Myers and Katharine Briggs indicating differing psychological preferences in how people perceive the world and make decisions. The test attempts to assign four categories: introversion or extraversion, sensing or intuition, thinking or feeling, judging or perceiving (descriptions of each can be found below). About 2 million people take it annually, at the behest of corporate HR departments, colleges, and even government agencies.") 

  print("\nThere are 16 possible personality options created using combinations of the following factors:")
  print("Extroversion(E) or Introversion(I): Signifies the source and direction of a person’s energy expression")
  print("An extravert’s source and direction of energy expression is mainly in the external world, while an introvert has a source of energy mainly in their own internal world.")

  print("\nSensing(S) or Intuition(N): Represents the method by which someone perceives information")
  print("Sensing means that a person mainly believes information he or she receives directly from the external world. Intuition means that a person believes mainly information he or she receives from the internal or imaginative world.")

  print("\nThinking(T) or Feeling(F): Represents how a person processes information")
  print("Thinking means that a person makes a decision mainly through logic. Feeling means that, as a rule, he or she makes a decision based on emotion, i.e. based on what they feel they should do.")

  print("\n Judging(J) or Perceiving(P): Reflects how a person implements the information he or she has processed")
  print("Judging means that a person organizes all of his life events and, as a rule, sticks to his plans. Perceiving means that he or she is inclined to improvise and explore alternative options.")

  print("\nIt is important to note that this test is not meant to be used as a fundamental aspect of a person's identity, but rather a fun quiz to find out your results using a sample MBTI test.")
  print("")
  pquiz = int(input("Enter any number once you are ready to take the MBTI test yourself!"))
  if (pquiz > -100000000):
    os.system("clear")
    print("Welcome to thep personality quiz. After reading the question, choose a number between 1 - 4 and click enter to submit your answer.")
    nextp = int(input("Enter a number when you are ready to continue."))
    if(nextp > -100000000):
      quiz()

#Function loops through questions list to display quesetions and take in input as answers
def quiz():
  global pquizq
  global pquiza
  count = 0
  os.system("clear")
  for outer_array in range(0, 4):
    for inner_questions in range(0, 3):
      os.system("clear")
      print(pquizq[outer_array][inner_questions])
      print("1. Strongly Agree")
      print("2. Agree")
      print("3. Disagree")
      print("4. Strongly Disagree")
      count += 1
      if(count != 13):
        choice = int(input("Select a number between 1 - 4 based on your option choice: "))
        newVal(choice)
        pquiza[outer_array].append(choice)
  if(results(pquiza) == True):
    print("\nEnter 1 to return to the Homepage")
    print("                 OR")
    print("Enter 2 to learn some more about the MBTI Personality Test")
    home = int(input("Enter Number Here: "))
    if(home == 1):
      homePage()
    else:
      info()

def newVal(choice):
  if(choice > 4 or choice < 1):
      while(choice > 4 or choice < 1):
        choice = int(input("Error! Enter another number BETWEEN 1 - 4 based on your option choice: "))
  else:
    print("Perfect!")  
    time.sleep(2)

  if(choice <=2):
    choice = 1 
  else:
    choice = -1
  return choice


#This function determines the final results of the quiz.
def results(ans):
  global personality
  
  os.system("clear")
  print("Your personality is: ")
  print("")

  #The following loops goes through answers provided by user to determine a personality.
  for j in range(0, 4):
    res = sum(ans[j])
    if(res > 0 and j == 0):
      personality.append("E") 
      print("You mainly fall in the category of Extroversion.  An extravert’s source and direction of energy expression is mainly in the external world.")
      print("")

    elif(res < 0 and j == 0):
      personality.append("I")
      print("You mainly fall in the category of Introversion An introvert has a source of energy mainly in their own internal world.")
      print("")

    elif(res > 0 and j == 1):
      personality.append("N")
      print("You mainly fall in the category of Intuition. Intuition means that a person believes mainly information he or she receives from the internal or imaginative world.")
      print("")

    elif(res < 0 and j == 1):
      personality.append("S")
      print("You mainly fall in the category of Sensing. Sensing means that a person mainly believes information he or she receives directly from the external world.")
      print("")
      
    elif(res > 0 and j == 2):
      personality.append("F")
      print("You mainly fall in the cateogory of Feeling. Feeling means that, as a rule, he or she makes a decision based on emotion, i.e. based on what they feel they should do.")
      print("")

    elif(res < 0 and j == 2):
      personality.append("T")
      print("You mainly fall in the category of Thinking. Thinking means that a person makes a decision mainly through logic.")
      print("")

    elif(res > 0 and j == 3):
      personality.append("J")
      print("You mainly fall in the cateogory of Judging. Judging means that a person organizes all of their life events and, as a rule, sticks to their plans.")
      print("")
      
    else:
      personality.append("P")
      print("You mainly fall in the category of perceiving. Perceiving means that he or she is inclined to improvise and explore alternative options.")
      print("")

  print("Your Personality Is: ")
  print(*personality)

#Returning True indicates the quiz is over and results are printed.
  return True

#List that stores all the questions.
pquizq = [["Do you enjoy being the center of attention","You enjoy having a wide circle of acquaintances", "You would rather socialize at a party than stay at home and read a book"], ["You tend to rely on your experience rather than on theoretical alternatives","When solving a problem you would rather follow a familiar approach than seek a new one","You are more inclined to experiment than to follow familiar approaches"],["Your decisions are based more on the feeling of a moment than on the thorough planning", "You are easily affected by strong emotions","You frequently and easily express your feelings and emotions"],["You take pleasure in putting things in order", "You are almost always on time to where you need to be", "You easily perceive various ways in which events could develop"]]

pquiza = [[], [], [], []]
personality =["Empty list"]

homePage()
