import os
import subprocess

def main():
    """Automatically downloads and installs python modules in a given text file"""

    #open main import file
    file_in = open('imports.txt', 'r')

    #Upgrades pip
    update_pip = 'pip install --upgrade pip'
    subprocess.call(update_pip, shell=True)
    
    # Loops through file installing all imports
    for line in file_in:
        
        import_string = str(line.strip('\n'))
        command = 'pip install ' + import_string
        subprocess.call(command, shell=True)

    os.system('pause')
        


if __name__ == "__main__":
    main()