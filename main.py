import os
import shutil
import subprocess

while True:
    # Get user input
    user_input = input("$ ")

    # Exit the terminal if the user enters "exit"
    if user_input == "exit":
        break

    # Execute the user's command
    try:
        if user_input.startswith("cd"):
            # Change directory
            path = user_input.split()[1]
            os.chdir(path)
        elif user_input.startswith("ls"):
            # List directory contents
            print(os.listdir("."))
        elif user_input.startswith("cp"):
            # Copy file
            source = user_input.split()[1]
            destination = user_input.split()[2]
            shutil.copyfile(source, destination)
        elif user_input.startswith("mv"):
            # Move or rename file
            source = user_input.split()[1]
            destination = user_input.split()[2]
            shutil.move(source, destination)
        elif user_input.startswith("rm"):
            # Remove file
            file_path = user_input.split()[1]
            os.remove(file_path)
        elif user_input.startswith("mkdir"):
            # Create directory
            dir_path = user_input.split()[1]
            os.mkdir(dir_path)
        elif user_input.startswith("rmdir"):
            # Remove directory
            dir_path = user_input.split()[1]
            os.rmdir(dir_path)
        elif user_input.startswith("del"):
            # Remove file or directory
            path = user_input.split()[1]
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        elif user_input.startswith("ps"):
            # List running processes
            subprocess.call(["ps", "aux"])
        else:
            # Execute system command
            result = os.system(user_input)
            print(result)
    except Exception as e:
        print(e)
