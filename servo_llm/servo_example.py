#!usr/bin/python3

import os
from time import sleep
from openai import OpenAI
from gpiozero import Servo

servo = Servo(17)

client = OpenAI()
unified_library_truncs = ["sleep", "servo.min", "print", "servo.max"]
unified_library = ["sleep(seconds)", "servo.min()", "servo.max()", "print(text)"]

while True:
        prompt = input("Message for Servo:\n") + "\n Respond with some of these function calls \n" + str(unified_library) + "."
        completion = client.chat.completions.create(
          model="gpt-4o",
          messages=[
            {"role": "system", "content": "Pretend you control a servo motor."},
            {"role": "user", "content": prompt}
          ]
        )
        text = completion.choices[0].message.content
        print(text)
        print("\n\n")
        # Actualizing
        words = text.replace(",","").replace("\n", " ").split(' ')
        executions = []
        for w in words:
                print("Word: " + w, end="")
                index = w.find("(")
                if index != -1:
                        w_trunc = w[:index]
                        if w_trunc in unified_library_truncs:
                                print(" = hit!")
                                executions.append(w)
                        else:
                                print(" = miss!")
                                pass # just another word
                else:
                        print(" = not a function!")
        print("\n\n")
        #print("(Executions:)\n" + str(executions))
        for x in executions:
                try:
                        print("Executing " + x)
                        exec(x)
                        print("(Executed " + x + ")")
                except Exception as e:
                        
                        print(e)
                        print("(Ignoring: " + x + "...)")
