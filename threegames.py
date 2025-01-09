import time

def program1():
    print('Welcome to Triangle Builder!')
    time.sleep(2)
    value = input("How tall would you like your triangle to be? Please enter an integer only.")
    height = int(value)
    num = 1
    right_side_copy = 0
    spaces = height
    for i in range(height):
        for x in range(spaces):
            print(" ", end="")
        for x in range(num):
            print("*", end="")
        for x in range(right_side_copy):
            print("*", end="")
        print("")
        right_side_copy += 1
        num += 1
        spaces -= 1
        if num > height:
            break
        
def program2():
    print('Welcome to Dot Runner!')
    time.sleep(2)
    print('How to Play: Once "GO!" appears, repeatedly enter the word "run" as input to reach the finish line!')
    time.sleep(4)

    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!")

    start = time.time()
    steps = 0
    finish_line = 10
    print("*")
    while (steps != finish_line):
        step_forward = input()
        if step_forward == "run":
            steps += 1
            for i in range(steps):
                print(" ", end="")
            print("*")
            for i in range(finish_line):
                print(" ", end="")
            print("|")
    end = time.time()
    print(f"Congratulations! You finished the race in {end-start} seconds!")
    time.sleep(2)

def program3():
    print("Welcome to ChatGPT 0.1!")
    time.sleep(2)
    prompt = input("Please enter a prompt or 'e' to exit.")
    while (prompt != "e"):
        print("I'm sorry, I do not understand.")
        time.sleep(2)
        prompt = input("Please enter another prompt or 'e' to exit ChatGPT 0.01.")
    print("User has exited ChatGPT 0.01.")
    
program = input("Welcome! This program contains three mini applications. Please enter 1, 2, or 3 as input to run one of the three applications. Otherwise, enter 'e' to exit.")

while (program != "e"):
    if program == "1":
        program1()
    elif program == "2":
        program2()
    elif program == "3":
        program3()
    else:
        print("Invalid input.")

    time.sleep(1)
    program = input("If you would like to run another program, please enter an integer from 1 to 3. Otherwise, enter 'e' to exit.")

print("Goodbye!")
    
