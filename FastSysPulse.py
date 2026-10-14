#!/usr/bin/env python
import subprocess
import os
import webbrowser
import shutil
import time

def get_disk_progress_bar(path="/"):
    total, used, free = shutil.disk_usage(path)
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)
    percent = (used / total) * 100
    
    bar_length = 20
    filled_length = int(round((bar_length * percent) / 100))
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    return f"[{path}]: {bar} {percent:.1f}% [Free: {free_gb:.1f} GB of {total_gb:.1f} GB]"

def Toolbox():
    while True:
        os.system("clear || cls")

        print("=" * 40)
        print("          Toolbox by mraz0tix!")
        print("=" * 40)
        print("1. Check Internet Connection (Ping Google)")
        print("2. Show System Information (Uname)")
        print("3. Show Active Network Ports (ss)")
        print("4. Run Fastfetch (fastfetch)")
        print("5. Disk info ")
        print("6. Run htop (htop) ")
        print("7. Reboot system (sudo reboot)")
        print("8. Shutdown system (sudo power off)")
        print("0. Exit to Main Menu")
        print("=" * 40)

        sub_choice = input("Select a menu option (0-8): ")

        if sub_choice == "1":
            print("\nChecking connection...")
            subprocess.run(["ping", "-c", "3", "8.8.8.8"])
            input("\nPress Enter to continue...")

        elif sub_choice == "2":
            print("\nKernel Information:")
            subprocess.run(["uname", "-a"])
            input("\nPress Enter to continue...")

        elif sub_choice == "3":
            print("\nListening ports in the system:")
            subprocess.run(["ss", "-tuln"])
            input("\nPress Enter to continue...")

        elif sub_choice == "4":
            try:
                subprocess.run(["fastfetch"])
            except FileNotFoundError:
                print("\nError: 'fastfetch' is not installed on your system.")
            input("\nPress Enter to continue...")

        elif sub_choice == "5":
            print("\n=== DISK STORAGE ANALYSIS ===")
            print(get_disk_progress_bar("/"))
            input("\nPress Enter to continue...")

        elif sub_choice == "6":    
            print("\nRunning htop...")
            subprocess.run(["htop"])
            input("\nPress Enter to continue...")

        elif sub_choice == "7":
            print("Rebooting system")
            subprocess.run(["sudo", "reboot"])

        elif sub_choice == "8":
            print("Shutdown system")
            time.sleep(1)
            subprocess.run(["sudo", "poweroff"])

        elif sub_choice == "0":
            print("\nReturning to main menu...")
            break

        else:
            print("\nInvalid choice inside Toolbox. Please try again.")
            input("\nPress Enter to continue...")

def Main_Menu():
    while True:
        os.system("clear || cls")
    
        print("=" * 40)
        print("               Main Menu")
        print("=" * 40)
        print("1. Toolbox (by mraz0tix)")
        print("2. Open my site (mraz0tix-code.github.io)")
        print("3. Exit the program")
        print("=" * 40)
        main_choice = input("Select a menu option (1-3): ")

        if main_choice == "1":
            Toolbox()

        elif main_choice == "2":
            print("\nOpening mraz0tix's awesome website...")
            webbrowser.open("https://mraz0tix-code.github.io/")
            input("\nPress Enter to continue...")   

        elif main_choice == "3":
            print("\nOkay! Goodbye!")
            os.system("clear || cls")
            break

        else:
            print("\nInvalid choice in main menu. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    Main_Menu()
