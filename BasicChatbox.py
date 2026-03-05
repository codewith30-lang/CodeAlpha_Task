import random
from datetime import datetime 
import pyjokes 

replies = ["Hi!", "Hello!", "Hey! what's up?", "hey! How are you?"]
print(random.choice(replies))

while True:
    user = input("You: ")
    
    if user == "fine" or user =="good" or user == "great" or user == "I am fine" :
        print("Thats great to hear!")
        
    elif "how are you" in user:
        print("doing well, thanks for asking!")
        
    elif user == "thank you":
        print("You're welcome")
    
    elif user == "bye":
        print("bye, see you next time!")
        break
    
    elif user == "hey" or user == "hi" or user == "hello":
        print("how are you!")
        
    elif "time" in user :
        print(datetime.now())
        
    elif "date" in user:
        print(datetime.now())
    
    elif "joke" in user:
        print(pyjokes.get_joke())
        if "not funny" in user:
            print("ok")
    
    elif "yes" in user:
        print("anything else?")
    
    elif "no" in user:
        print("bye")
        break
    
    else:
        print("I don't understand!")
        break 

