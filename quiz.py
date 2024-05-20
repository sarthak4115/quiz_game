
name=input("Enter your name : ")
print()
print(f"Welcome to KBC {name}!")
q1=[
  "What is the capital of australia?",
  "a. Sydney",
  "b. Melbourne",
  "c. Canberra",
  "d. Brisbane",
  3
]
q2=[
  "In which year did the titanic sink?",
  "a. 1912",
  "b. 1920",
  "c. 1905",
  "d. 1931",
  1
]
q3=[
  "Who wrote the play \"Romeo and juliet\"?",
  "a. William Shakespeare",
  "b. Charles Dickens",
  "c. Jane Austen",
  "d. Mark Twain",
  1
]
q4=[
  "Which planet is known as the \"Red plaet\"?",
  "a. Venus",
  "b. Mars",
  "c. Jupiter",
  "d. Saturn",
  2
]
q5=[
  "What is the currency of Japan?",
  "a. Won",
  "b. Yen",
  "c. Ringgit",
  "d. Baht",
  2
]
q6=[
  "Who painted the Mona Lisa?",
  "a. Vincent van Gogh",
  "b. Pablo Picasso",
  "c. Leonardo da Vinci",
  "d. Michelangelo",
  3
]
q7=[
  "Which ocean is largest on earth?",
  "a. Atlantic Ocean",
  "b. Indian Ocean",
  "c. Southern Ocean",
  "d. Pacific Ocean",
  4
]
q8=[
  "What is the largest mamal on earth?",
  "a. Elephant",
  "b. Giraffe",
  "c. Blue Whale",
  "d. Gorilla",
  3
]
q9=[
  "In which country did the olympic games originate?",
  "a. Greece",
  "b. Italy",
  "c. Egypt",
  "d. China",
  1
]
q10=[
  "What is the world's longest river?",
  "a. Nile",
  "b. Amazon",
  "c. Yangtze",
  "d. Mississippi",
  1
]
q11=[
  "Who is known as the \"the father of computer science\"?",
  "a. Alan Turing",
  "b. Bill Gates",
  "c. Steve Jobs",
  "d. Mark Zuckerberg",
  1
]
q12=[
  "Which country is famous for its tulip fields and windmills?",
  "a. France",
  "b. Netherlands",
  "c. Switzerland",
  "d. Belgium",
  2
]
q13=[
  "What is the largest largest desert in the world?",
  "a. Sahara Desert",
  "b. Gobi Desert",
  "c. Arabian Desert",
  "d. Antarcica",
  1
]
q14=[
  "Who wrote the novel \"1984\"?",
  "a. George Orwell",
  "b. J.K. Rowling",
  "c. Ernest Hemingway",
  "d. F.Scott Fitzgerland",
  1
]
q15=[
  "Which element has the chemical symbol 'Au'?",
  "a. Oxygen",
  "b. Gold",
  "c. Iron",
  "d. Silver",
  2
]
q16=[
  "In which year did the United States declare its independence?",
  "a. 1776",
  "b. 1789",
  "c. 1800",
  "d. 1754",
  1
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,0]
print()
money=0
a=input("Press Enter to continue :")
ques=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16]
print()
for i in range(0,len(ques)):
  print(f"Question for Rs. {levels[i]}")
  print()
  print(ques[i][0])
  print(ques[i][1])
  print(ques[i][2])
  print(ques[i][3])
  print(ques[i][4])
  print()
  ans=int(input("Enter your answer (1-4) or 0 to quit :"))
  print()
  if ans==0:
    money=levels[i-1]
    print()
    print(f"you have won Rs. {money}")
    break
  if ans==ques[i][-1]:
    print(f"Correct answer, you have won Rs. {levels[i]}")
    print()
    a=input("Press Enter to continue : ")
    print()
    print()
  else:
    print()
    print("Wrong answer!")
    print(f"You have won Rs. {levels[i-1]}")
    break
print()
print("Thank you for playing KBC! ")
