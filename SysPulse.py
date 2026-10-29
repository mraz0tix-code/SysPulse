#!/usr/bin/env python
import subprocess
import os
import webbrowser
import shutil
import time

def NetPulse_Main():
    while True:
        clear_screen()
        print("=" * 40)
        print("               NetPulse")
        print("=" * 40)
        print("1. Check the internet connection's menu")
        print("2. Check the ports menu")
        print("3. Nmap usage mode (nmap)")
        print("4. Exit NetPulse")
        
        print("\n5. Open mraz0tix's site")

        main_choice = input("\nSelect a menu option (1-4): > ")
         
        if main_choice == "1":
            Internet_menu()
        elif main_choice == "2":
            Ports_menu()
        elif main_choice == "3":
            nmap_mode()
        elif main_choice == "4":
            print("\n[+] Bye Bye!")
            break
        
        elif main_choice == "5":
            Site()
        
        else:
            print("\nSysPulse >> [!] Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def Internet_menu():       
    while True:
        clear_screen()
        print("=" * 40)
        print("              Internet Menu")
        print("=" * 40)
        print("1. Run ping test (8.8.8.8)")
        print("2. Ping custom website or IP")  
        print("3. Back to main menu")

        choice_internet = input("\nSelect a menu option (1-3): > ")  

        if choice_internet == "1":
            Internet_check_default()  
        elif choice_internet == "2":
            Internet_check_custom()   
        elif choice_internet == "3":
            break
        else:
            print("\nSysPulse >> [!] Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def Internet_check_default():
    print("\nSysPulse >> [+] Okay! Already checking connection...")
    time.sleep(0.5)
    try:
        subprocess.run(["kitty", "--hold", "ping", "-c", "3", "8.8.8.8"], check=True)
        print("SysPulse >> [+] Internet connection checked successfully!")
    except FileNotFoundError:
        print("\nSysPulse >> [!] Error: 'kitty' terminal is not installed.")
    input("\nSysPulse >> Press Enter to continue...")

def Internet_check_custom():
    target = input("\nSysPulse >> Enter website or IP to ping (e.g., google.com): > ")
    if target: 
        print(f"\nSysPulse >> [+] Pinging {target}...")
        time.sleep(0.5)
        try:
            subprocess.run(["kitty", "--hold", "ping", "-c", "4", target], check=True)
            print("\nSysPulse >> [+] Ping completed successfully!")
        except FileNotFoundError:
            print("\nSysPulse >> [!] Error: 'kitty' terminal is not installed.")
    else:
        print("\nSysPulse >> [!] Error: Empty target.")
    input("\nSysPulse >> Press Enter to continue...")

def Ports_menu():
    while True:
        clear_screen()
        print("=" * 40)
        print("             Menu for ports")
        print("=" * 40)
        print("1. Check your open ports (ss)")
        print("2. Back to main menu")

        main_choice_ports = input("\nSelect a menu option (1-2): > ")
        
        if main_choice_ports == "1":
            print("\nSysPulse >> [+] Okay! Already checking ports...")
            time.sleep(0.5)
            try:
                subprocess.run(["kitty", "--hold", "ss", "-tuln"], check=True)
                print("SysPulse >> [+] Ports checked successfully!")
            except FileNotFoundError:
                print("\nSysPulse >> [!] Error: 'kitty' terminal is not installed.")
            input("\nSysPulse >> Press Enter to continue...")
        elif main_choice_ports == "2":
            break
        else:
            print("\nSysPulse >> [!] Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def nmap_mode():
    while True:
        clear_screen()
        print("=" * 40)
        print("           Nmap mode-menu")
        print("=" * 40)
        print("1. View your subnet (Scan custom target)")
        print("2. Back to main menu")

        nmap_choice = input("\nSelect a menu option (1-2): > ")

        if nmap_choice == "1":
            subnet = input("\nEnter target subnet (Default: 192.168.1.0/24): > ")
            if not subnet:
                subnet = "192.168.1.0/24"

            print(f"\nSysPulse >> [+] Okay, checking subnet {subnet} via Nmap...")
            
            cmd = ["kitty", "--hold", "sudo", "nmap", "-sS", "-sV", "-O", subnet]
            
            try:
                subprocess.run(cmd, check=True)
            except FileNotFoundError:
                print("\nSysPulse >> [!] Error: 'kitty' terminal emulator or 'nmap' is not installed.")
                input("\nSysPulse >> Press Enter to continue...")
            except subprocess.CalledProcessError:
                print("\nSysPulse >> [!] Scan was interrupted or failed (maybe wrong sudo password?).")
                input("\nSysPulse >> Press Enter to continue...")
                
        elif nmap_choice == "2":
            break
        else:
            print("\nSysPulse >> [!] Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def clear_screen():
    os.system("clear || cls")

def Site():
    print("SysPulse >> Okay!")
    webbrowser.open("https://mraz0tix-code.github.io/")

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
        print("\nSysPulse >> [ERROR] Enter only numbers, not individual digits!")
        input("\nSysPulse >> Press Enter to continue...")
        return

    print("=" * 40, "      Calculator_V1")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    
    if b == 0:
        print("SysPulse >> 0 / 0 == ERROR!") 
    else:
        print(f"a / b = {a / b}")

    print("=" * 40, "       Calculator_V1")
    input("\nSysPulse >> Press Enter to return to Main Menu...")

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
        print("2. Exit to Toolbox Menu")
        print("=" * 40)
        
        Internet_choice = input("Select a menu option (1-2): ")

        if Internet_choice == "1":
            print("\nSysPulse >> Checking connection...")
            subprocess.run(["kitty", "--hold", "ping", "-c", "3", "8.8.8.8"])
            input("\nSysPulse >> Press Enter to continue...")
        elif Internet_choice == "2":
            print("SysPulse >> Okay exit the Internet main")
            break
        else:
            print("\nSysPulse >> Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def Kernel():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          Uname Main")
        print("=" * 40)
        print("1. Uname (Kernel)")
        print("2. Exit to Toolbox Menu")
        print("=" * 40)

        Kernel_choice = input("Select a menu option (1-2): ")

        if Kernel_choice == "1":
            print("\nSysPulse >> Kernel Information:")
            subprocess.run(["uname", "-a"])
            input("\nSysPulse >> Press Enter to continue...")
        elif Kernel_choice == "2":
            print("SysPulse >> Okay exit the Uname main")
            break
        else:
            print("\nSysPulse >> Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def Network_ports():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          Network and ports Main")
        print("=" * 40)
        print("1. Check the ports")
        print("2. Exit to Main Menu")
        print("=" * 40)

        Network_ports_choice = input("Select a menu option (1-2): ")

        if Network_ports_choice == "1":
            print("\nSysPulse >> Listening ports in the system:")
            subprocess.run(["ss", "-tuln"])
            input("\nSysPulse >> Press Enter to continue...")
        elif Network_ports_choice == "2":
            print("SysPulse >> Okay exit the Network and ports main")
            break
        else:
            print("\nSysPulse >> Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def Fastfetch():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          fastfetch Main")
        print("=" * 40)
        print("1. Run fastfetch")
        print("2. Exit to Main Menu")
        print("=" * 40)

        fastfetch_choice = input("Select a menu option (1-2): ")

        if fastfetch_choice == "1":
            try:
                subprocess.run(["kitty", "--hold", "fastfetch"])
            except FileNotFoundError:
                print("\nSysPulse >> Error: 'fastfetch' is not installed on your system.")
            input("\nSysPulse >> Press Enter to continue...")
        elif fastfetch_choice == "2":
            print("SysPulse >> Okay exit the fastfetch main")
            break
        else:
            print("\nSysPulse >> Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def Disk_info():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          Disk Main")
        print("=" * 40)
        print("1. Check your disk")
        print("2. Exit to Main Menu")
        print("=" * 40)

        disk_choice = input("Select a menu option (1-2): ")

        if disk_choice == "1":
            print("\n=== DISK STORAGE ANALYSIS ===")
            print(get_disk_progress_bar("/"))
            input("\nPress Enter to continue...")
        elif disk_choice == "2":
            print("SysPulse >> Okay exit the disk main")
            break
        else:
            print("\nSysPulse >> Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def htop():
    while True: 
        os.system("clear || cls")
        print("=" * 40)
        print("          htop Main")
        print("=" * 40)
        print("1. Run htop")
        print("2. Exit to Main Menu")
        print("=" * 40)

        htop_choice = input("Select a menu option (1-2): ")

        if htop_choice == "1":
            print("\nSysPulse >> Running htop...")
            subprocess.run(["kitty", "--hold", "htop"])
            input("\nSysPulse >> Press Enter to continue...")
        elif htop_choice == "2":
            print("SysPulse >> Okay exit the htop main")
            break
        else:
            print("\nSysPulse >> Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def Reboot():
    print("\nSysPulse >> [WARNING] Rebooting system")
    time.sleep(1)
    subprocess.run(["kitty", "--hold", "sudo", "reboot"])

def shutdown():
    print("\nSysPulse >> [WARNING] Shutdown system...")
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
            print("\nSysPulse >> Returning to main menu...")
            break
        else:
            print("\nSysPulse >> Invalid choice inside Toolbox. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def Main_Menu():
    while True:
        os.system("clear || cls")
        print("=" * 40)
        print("               Main Menu")
        print("=" * 40)
        print("1. Toolbox (by mraz0tix)")
        print("2. Open my site (mraz0tix-code.github.io)")
        print("3. Run Calculator")
        print("4. Run NetPulse")
        print("0. Exit the program")
        print("=" * 40)
        main_choice = input("Select a menu option (0-4): ")

        if main_choice == "1":
            Run_Toolbox()
        elif main_choice == "2":
            print("\nSysPulse >> Opening mraz0tix's awesome website...")
            Site()
            input("\nSysPulse >> Press Enter to continue...")
        elif main_choice == "3":
            Calculator()
        elif main_choice == "4":
            NetPulse_Main()
        elif main_choice == "0":
            print("\nSysPulse >> Okay! Goodbye!")
            os.system("clear || cls")
            break
        else:
            print("\nSysPulse >> Invalid choice in main menu. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

if __name__ == "__main__":
    Main_Menu()
