import os

""" list Directory content
A simple program that lists any directory content
it makes use of Absolute and relative path.
and handles error efficiently.
"""

print("press ctr/command D to exit prompt")
try:
    while True:
        path = input("Please enter directory Path (absolute or relative) to view the output: ")
        expand_path = os.path.expanduser(path)
        # check if the path exists and also a tilde so we expand
        if os.path.exists(expand_path):
            # check if path exit and is a directory
            if os.path.isdir(expand_path):
                content = os.listdir(expand_path)
                # Display Non-hidden file
                for cnt in content:
                    if not cnt.startswith("."):
                        print(cnt)
            else:
                print("Error: The provided path is a file not a directory")
        else:
            print("No such Directory")
        
except (EOFError, KeyboardInterrupt):
    print("\nGood bye!")
