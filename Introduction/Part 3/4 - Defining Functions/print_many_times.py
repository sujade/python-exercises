#Please write a function named print_many_times(text, times), which takes a string and an integer as arguments.

def print_many_times(text, times):
    if times > 0:
        print(text)
        print_many_times(text, times - 1)