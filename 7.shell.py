import subprocess
import sys
import os

def execute_command(command):
    """Execute a single shell command with optional redirection and pipe."""
    # Handle piping and redirection
    if '|' in command:
        parts = command.split('|')
        processes = []

        # Create the pipeline of processes
        for part in parts:
            cmd = part.strip().split()
            processes.append(subprocess.Popen(cmd, stdout=subprocess.PIPE))
        
        # Connect pipes
        for i in range(len(processes) - 1):
            processes[i].stdout = processes[i + 1].stdin

        # Wait for the last process to finish
        processes[-1].wait()
    
    else:
        # Handle I/O redirection (either input or output)
        if '>' in command:
            cmd, output_file = command.split('>', 1)
            cmd = cmd.strip().split()
            output_file = output_file.strip()
            with open(output_file, 'w') as outfile:
                subprocess.run(cmd, stdout=outfile, shell=True)
        elif '<' in command:
            cmd, input_file = command.split('<', 1)
            cmd = cmd.strip().split()
            input_file = input_file.strip()

            # Check if the input file exists before proceeding
            if os.path.exists(input_file):
                with open(input_file, 'r') as infile:
                    subprocess.run(cmd, stdin=infile, shell=True)
            else:
                print(f"Error: File '{input_file}' not found.")
                return
        else:
            # Handle special case for Windows - ls -> dir
            cmd = command.strip().split()

            # Replace 'ls' with 'dir' for Windows
            if cmd[0] == 'ls':
                cmd[0] = 'dir'
            
            subprocess.run(cmd, shell=True)

def main():
    while True:
        # Display prompt
        user_input = input("Shell> ")

        # Exit shell if user types "exit"
        if user_input.lower() == "exit":
            print("Exiting shell...")
            break

        # Execute the command
        execute_command(user_input)

if __name__ == "__main__":
    main()
