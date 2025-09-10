# 3. Install an external module and use it to perform an operation of your interest.
# We Install """pyttsx3""" module using pip.

import pyttsx3
engine = pyttsx3.init()
# engine.say("I will speak this text")
engine.say("HELLO My Name is DHIRENDRA JHA")
engine.runAndWait()