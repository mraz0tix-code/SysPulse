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
            print("\nFastSysPulse >> [+] Bye Bye!")
            break
        
        elif main_choice == "5":
            Site()
        
        else:
            print("\nFastSysPulse >> [!] Invalid choice. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

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
            print("\nFastSysPulse >> [!] Invalid choice. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

def Internet_check_default():
    print("\nFastSysPulse >> [+] Okay! Already checking connection...")
    try:
        subprocess.run(["ping", "-c", "3", "8.8.8.8"], check=True)
        print("FastSysPulse >> [+] Internet connection checked successfully!")
    except FileNotFoundError:
        print("\nFastSysPulse >> [!] Error: 'kitty' terminal is not installed.")
    input("\nFastSysPulse >> Press Enter to continue...")

def Internet_check_custom():
    target = input("\nFastSysPulse >> Enter website or IP to ping (e.g., google.com): > ")
    if target: 
        print(f"\nFastSysPulse >> [+] Pinging {target}...")
        try:
            subprocess.run(["ping", "-c", "4", target], check=True)
            print("\nFastSysPulse >> [+] Ping completed successfully!")
        except FileNotFoundError:
            print("\nFastSysPulse >> [!] Error: 'kitty' terminal is not installed.")
    else:
        print("\nFastSysPulse >> [!] Error: Empty target.")
    input("\nFastSysPulse >> Press Enter to continue...")

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
            print("\nFastSysPulse >> [+] Okay! Already checking ports...")
            time.sleep(0.5)
            try:
                subprocess.run(["ss", "-tuln"], check=True)
                print("FastSysPulse >> [+] Ports checked successfully!")
            except FileNotFoundError:
                print("\nFastSysPulse >> [!] Error: 'kitty' terminal is not installed.")
            input("\nFastSysPulse >> Press Enter to continue...")
        elif main_choice_ports == "2":
            break
        else:
            print("\nFastSysPulse >> [!] Invalid choice. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

def nmap_mode():
    while True:
        clear_screen()
        print("=" * 40)
        print("           Nmap mode-menu")
        print("=" * 40)
        print("1. View your subnet (Scan custom target)")
        print("2. Back to main menu")

        nmap_choice = input("\nFastSysPulse >> Select a menu option (1-2): > ")

        if nmap_choice == "1":
            subnet = input("\nFastSysPulse >> Enter target subnet (Default: 192.168.1.0/24): > ")
            if not subnet:
                subnet = "192.168.1.0/24"

            print(f"\nFastSysPulse >> [+] Okay, checking subnet {subnet} via Nmap...")
            
            cmd = ["sudo", "nmap", "-sS", "-sV", "-O", subnet]
            
            try:
                subprocess.run(cmd, check=True)
            except FileNotFoundError:
                print("\nFastSysPulse >> [!] Error: 'kitty' terminal emulator or 'nmap' is not installed.")
                input("\nFastSysPulse >> Press Enter to continue...")
            except subprocess.CalledProcessError:
                print("\nFastSysPulse >> [!] Scan was interrupted or failed (maybe wrong sudo password?).")
                input("\nFastSysPulse >> Press Enter to continue...")
                
        elif nmap_choice == "2":
            break
        else:
            print("\n[!] Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

def clear_screen():
    os.system("clear || cls")

def Site():
    webbrowser.open("https://mraz0tix-code.github.io/")

def Calculator():
    clear_screen()
    print("=" * 40)
    print("             Calculator_V1")
    print("=" * 40)
    input("\nFastSysPulse >> Please click the button enter!")

    clear_screen()
    print("=" * 40, "      Calculator_V1")

    try:
        a = float(input("a = ?: "))
        b = float(input("b = ?: "))
    except ValueError:
        print("\nFastSysPulse >> [ERROR] Вводи строго числа, а не буквы!")
        input("\nFastSysPulse >> Press Enter to continue...")
        return

    print("=" * 40, "      Calculator_V1")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    
    if b == 0:
        print("FastSysPulse >> 0 / 0 == ERROR!") 
    else:
        print(f"a / b = {a / b}")

    print("=" * 40, "       Calculator_V1")
    input("\nFastSysPulse >> Press Enter to return to Main Menu...")

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
        clear_screen()
        print("=" * 40)
        print("          Internet Main")
        print("=" * 40)
        print("1. Internet (Ping)")
        print("2. Exit to Toolbox Menu")
        print("=" * 40)
        
        Internet_choice = input("Select a menu option (1-2): ")

        if Internet_choice == "1":
            print("\nFastSysPulse >> Checking connection...")
            subprocess.run(["ping", "-c", "3", "8.8.8.8"])
            input("\nFastSysPulse >> Press Enter to continue...")
        elif Internet_choice == "2":
            print("FastSysPulse >> Okay exit the Internet main")
            break
        else:
            print("\nFastSysPulse >> Invalid choice. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

def Kernel():
    while True: 
        clear_screen()
        print("=" * 40)
        print("          Uname Main")
        print("=" * 40)
        print("1. Uname (Kernel)")
        print("2. Exit to Toolbox Menu")
        print("=" * 40)

        Kernel_choice = input("Select a menu option (1-2): ")

        if Kernel_choice == "1":
            print("\nFastSysPulse >> Kernel Information:")
            subprocess.run(["uname", "-a"])
            input("\nFastSysPulse >> Press Enter to continue...")
        elif Kernel_choice == "2":
            print("FastSysPulse >> Okay exit the Uname main")
            break
        else:
            print("\nFastSysPulse >> Invalid choice. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

def Network_ports():
    while True: 
        clear_screen()
        print("=" * 40)
        print("          Network and ports Main")
        print("=" * 40)
        print("1. Check the ports")
        print("2. Exit to Main Menu")
        print("=" * 40)

        Network_ports_choice = input("Select a menu option (1-2): ")

        if Network_ports_choice == "1":
            print("\nFastSysPulse >> Listening ports in the system:")
            subprocess.run(["ss", "-tuln"])
            input("\nFastSysPulse >> Press Enter to continue...")
        elif Network_ports_choice == "2":
            print("FastSysPulse >> Okay exit the Network and ports main")
            break
        else:
            print("\nFastSysPulse >> Invalid choice. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

def Fastfetch():
    while True: 
        clear_screen()
        print("=" * 40)
        print("          fastfetch Main")
        print("=" * 40)
        print("1. Run fastfetch")
        print("2. Exit to Main Menu")
        print("=" * 40)

        fastfetch_choice = input("Select a menu option (1-2): ")

        if fastfetch_choice == "1":
            try:
                subprocess.run(["fastfetch"])
            except FileNotFoundError:
                print("\nFastSysPulse >> Error: 'fastfetch' is not installed on your system.")
            input("\nFastSysPulse >> Press Enter to continue...")
        elif fastfetch_choice == "2":
            print("FastSysPulse >> Okay exit the fastfetch main")
            break
        else:
            print("\nFastSysPulse >> Invalid choice. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

def Disk_info():
    while True: 
        clear_screen()
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
            print("FastSysPulse >> Okay exit the disk main")
            break
        else:
            print("\nFastSysPulse >> Invalid choice. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

def htop():
    while True: 
        clear_screen()
        print("=" * 40)
        print("          htop Main")
        print("=" * 40)
        print("1. Run htop")
        print("2. Exit to Main Menu")
        print("=" * 40)

        htop_choice = input("Select a menu option (1-2): ")

        if htop_choice == "1":
            print("\nFastSysPulse >> Running htop...")
            subprocess.run(["htop"])
            input("\nFastSysPulse >> Press Enter to continue...")
        elif htop_choice == "2":
            print("FastSysPulse >> Okay exit the htop main")
            break
        else:
            print("\nFastSysPulse >> Invalid choice. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

def Reboot():
    print("\nFastSysPulse >> [WARNING] Rebooting system")
    subprocess.run(["sudo", "reboot"])

def shutdown():
    print("\nFastSysPulse >> [WARNING] Shutdown system...")
    subprocess.run(["sudo", "poweroff"])

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
            print("\nFastSysPulse >> Returning to main menu...")
            break
        else:
            print("\nFastSysPulse >> Invalid choice inside Toolbox. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

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
            print("\nFastSysPulse >> Opening mraz0tix's awesome website...")
            Site()
            input("\nFastSysPulse >> Press Enter to continue...")
        elif main_choice == "3":
            Calculator()
        elif main_choice == "4":
            NetPulse_Main()
        elif main_choice == "0":
            print("\nFastSysPulse >> Okay! Goodbye!")
            os.system("clear || cls")
            break
        else:
            print("\nFastSysPulse >> Invalid choice in main menu. Please try again.")
            input("\nFastSysPulse >> Press Enter to continue...")

if __name__ == "__main__":
    Main_Menu()
