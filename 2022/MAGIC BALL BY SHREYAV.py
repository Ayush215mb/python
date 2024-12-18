import random

print("\n\n\n\n                                                          Welcome to Magic 8 Ball  ")
print("             __________________________________________________________________________________________________________________________________")
print()

Ans = ["it is certainly", "it is decidedly so", "without a doubt ", "yes - definitely ", "you may rely on it ", "as i see it...yes ", "most likely", "outlook good", "yes", "signs point to yes ", "reply hazy,try again ", "ask again later ", "better not tell you now ", "cannot predict ", "please ask again ", "don't count on it ", "my reply is no ", "my sources say no", "outlook not so good ", "very doubtful"]

while True:

   name = input(" Enter your name :  ")
   print()
   print("Hii " + name+" !!")
   print()
   input("What is your question for the magic 8 ball ?  ")

   choice = random.randint(1, 20)

   Answer = Ans[choice]
   print()
   print(".............................................................................................................................")
   print()
   
   print("                                                     Magic 8 ball :  ", Answer)
   print("\n*******************************************************************************************************************************************")
   print("*******************************************************************************************************************************************\n\n\n\n")
print()

