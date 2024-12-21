## Simple Cobots Pipeline Framework
This project demonstrates an easy to use hybrid cognitive architecture for "cobotics". 

--- a fancy name for a small project. The ultimate goal is a system that uses an LLM as the driver of natural language understanding, and picks _plans_ or _action_. Below are examples (there is only one so far). Ideally, this pipeline is a framework for highly interactive cobots (collaborative robot).


### Servo LLM
This directory is the codebase for a configuration with a RaspberryPi and a servo motor. This minimal demonstration suggets how extendable the system is.

In order to have access to the pins on the RaspberryPi AND use the python virtual environment, run
```
sudo path/to/venv/bin/python servo_llm/servo_example.py
```
Then in the input field type messages, and have it respond with text and motor movements.
