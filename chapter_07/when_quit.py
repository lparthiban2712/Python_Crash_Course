message = input("Tell me something, and I will repeat it back to you (type 'quit' to end the program): ")
while message.lower() != 'quit':
    print(message)
    message = input("Tell me something else (type 'quit' to end the program): ")