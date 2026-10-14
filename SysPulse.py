#!/usr/bin/env python
import subprocess
import os
import webbrowser
import shutil
import time

def Calculator():
    os.system("clear || cls")
    print("=" * 40)
    print("             Calculator_V1")
    print("=" * 40)
    input("\nPlease click the button enter!")

    os.system("clear || cls")
    print("=" * 40, "      Calculator_V1")

    try:
        a = float(input("a = ?: "))
        b = float(input("b = ?: "))
    except ValueError:
        print("\n[ERROR] Вводи строго числа, а не буквы!")
        input("\nPress Enter to continue...")
        return

    print("=" * 40, "      Calculator_V1")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    
    if b == 0:
        print("0 / 0 == ERROR!") 
    else:
        print(f"a / b = {a / b}")

    print("=" * 40, "       Calculator_V1")
    input("\nPress Enter to return to Main Menu...")

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

def Internet():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          Internet Main")
        print("=" * 40)
        print("1. Internet (Ping)")
        print("0. Exit to Toolbox Menu")
        print("=" * 40)
        
        Internet_choice = input("Select a menu option (0-1): ")

        if Internet_choice == "1":
            print("\nChecking connection...")
            subprocess.run(["kitty", "--hold", "ping", "-c", "3", "8.8.8.8"])
            input("\nPress Enter to continue...")
        elif Internet_choice == "0":
            print("Okay exit the Internet main")
            break

def Kernel():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          Uname Main")
        print("=" * 40)
        print("1. Uname (Kernel)")
        print("0. Exit to Toolbox Menu")
        print("=" * 40)

        Kernel_choice = input("Select a menu option (0-1): ")

        if Kernel_choice == "1":
            print("\nKernel Information:")
            subprocess.run(["uname", "-a"])
            input("\nPress Enter to continue...")
        elif Kernel_choice == "0":
            print("Okay exit the Uname main")
            break

def Network_ports():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          Network and ports Main")
        print("=" * 40)
        print("1. Check the ports")
        print("0. Exit to Toolbox Menu")
        print("=" * 40)

        Network_ports_choice = input("Select a menu option (0-1): ")

        if Network_ports_choice == "1":
            print("\nListening ports in the system:")
            subprocess.run(["ss", "-tuln"])
            input("\nPress Enter to continue...")
        elif Network_ports_choice == "0":
            print("Okay exit the Network and ports main")
            break

def Fastfetch():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          fastfetch Main")
        print("=" * 40)
        print("1. Run fastfetch")
        print("0. Exit to Toolbox Menu")
        print("=" * 40)

        fastfetch_choice = input("Select a menu option (0-1): ")

        if fastfetch_choice == "1":
            try:
                subprocess.run(["kitty", "--hold", "fastfetch"])
            except FileNotFoundError:
                print("\nError: 'fastfetch' is not installed.")
            input("\nPress Enter to continue...")
        elif fastfetch_choice == "0":
            print("Okay exit the fastfetch main")
            break

def Disk_info():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          Disk Main")
        print("=" * 40)
        print("1. Check your disk")
        print("0. Exit to Toolbox Menu")
        print("=" * 40)

        disk_choice = input("Select a menu option (0-1): ")

        if disk_choice == "1":
            print("\n=== DISK STORAGE ANALYSIS ===")
            print(get_disk_progress_bar("/"))
            input("\nPress Enter to continue...")
        elif disk_choice == "0":
            print("Okay exit the disk main")
            break

def htop():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          htop Main")
        print("=" * 40)
        print("1. Run htop")
        print("0. Exit to Toolbox Menu")
        print("=" * 40)

        htop_choice = input("Select a menu option (0-1): ")

        if htop_choice == "1":
            print("\nRunning htop...")
            subprocess.run(["kitty", "--hold", "htop"])
            input("\nPress Enter to continue...")
        elif htop_choice == "0":
            print("Okay exit the htop main")
            break

def Reboot():
    print("\n[WARNING] Rebooting system")
    time.sleep(1)
    subprocess.run(["kitty", "--hold", "sudo", "reboot"])

def shutdown():
    print("\n[WARNING] Shutdown system...")
    time.sleep(1)
    subprocess.run(["kitty", "--hold", "sudo", "poweroff"])

def Run_Toolbox():
    while True:
        os.system("clear || cls")
        print("=" * 40)
        print("          Toolbox by mraz0tix!")
        print("=" * 40)
        print("1. Internet (Ping) SubMenu")
        print("2. Show System Information (Uname) SubMenu")
        print("3. Show Active Network Ports (ss) SubMenu")
        print("4. Run Fastfetch (fastfetch) SubMenu")
        print("5. Disk info SubMenu")
        print("6. Run htop (htop) SubMenu")
        print("7. Reboot system (sudo reboot)")
        print("8. Shutdown system (sudo power off)")
        print("0. Exit to Main Menu")
        print("=" * 40)

        sub_choice = input("Select a menu option (0-8): ")

        if sub_choice == "1":
            Internet()
        elif sub_choice == "2":
            Kernel()
        elif sub_choice == "3":
            Network_ports()
        elif sub_choice == "4":
            Fastfetch()
        elif sub_choice == "5":
            Disk_info()
        elif sub_choice == "6":    
            htop()
        elif sub_choice == "7":
            Reboot()
        elif sub_choice == "8":
            shutdown()
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
        print("3. Run Calculator")
        print("0. Exit the program")
        print("=" * 40)
        main_choice = input("Select a menu option (0-3): ")

        if main_choice == "1":
            Run_Toolbox()
        elif main_choice == "2":
            print("\nOpening mraz0tix's awesome website...")
            webbrowser.open("https://mraz0tix-code.github.io/")
            input("\nPress Enter to continue...")
        elif main_choice == "3":
            Calculator()
        elif main_choice == "0":
            print("\nOkay! Goodbye!")
            os.system("clear || cls")
            break
        else:
            print("\nInvalid choice in main menu. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    Main_Menu()
