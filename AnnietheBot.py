#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Introduce the user to the conversation.

print("Hi, I'm Annie the bot. What's your name?")

name = input("type your name here >> ")

print("Nice to meet you, " + name + ".")
print("One last thing, can you please enter your email?")

email = input("type your email here >> ")

print("OK, got it. Your EMAIL is : " + email+  ". Thank you! Have a nice day! ;)")
print("Oh sorry, can I get your name again? I have awful memory...")

name = input("type you name here >> ")

if name == "Anna" or name == "Anne" or name == "Ann" or name == "Anni":
    print("oooo! that's similar to my name...so pretty :)")
elif name == "Annie":
    print("Ooooh!!! We have the same name, didn't realize it at first!")
else:
    print("hmmm, that's an odd name. Never heard it before. It's ok. Let's keep talking!")

print("I'll be honest-- I'm a rather lonely robot but it really is a pleasure speaking with you, " + name + ".")

answer= input("Can I ask you a rather personal question, " + name + " ?"
              " type your answer here >> ")
while answer != "yes" and answer != "Yes" and answer != "No" and answer != "no":       
    answer= input("Can I ask you a rather personal question, " + name + " ?"
              " type your answer here >> ")
    #if answer == "yes" or answer == "Yes" or answer == "No" or answer == "no":
       # break
        
#***********************
# THE BOT ANALYZES THE CONDITION FROM HERE
#***********************
        
if answer == "yes" or answer == "Yes":    
    answer2 = input("Do you find me amusing?")
    if answer2 == "yes" or answer == "Yes":
        print("I find you amusing too! After all, humans are super interesting! :)")
    elif answer2 == "no" or answer2 == "No":
        print("No worries, I don't find you amusing either...")
    else:
        print("Please answer with a 'yes' or a 'no'. Thanks a bunch")
        answer2 = input("Do you find me amusing?")
        # Create a while loop until the user answers 'yes' or 'no'
        while answer2 != "yes" and answer2 != "Yes" and answer2 != "No" and answer2 != "no":
            answer2 = input("Do you find me amusing?")
        
            
elif answer == "no" or answer == "No":    
    print("Sorry, I'm asking the question anyway! Too bad! :)")   
    answer2 = input("Do you find me amusing?")  
    while answer2 != "yes" and answer != "Yes" and answer2 != "No" and answer2 != "no":       
        answer2 = input("Do you find me amusing," + name + " ?" 
                  " type your answer here >> ")
       
        
#********* END **************






# In[ ]:




