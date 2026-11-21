#!/usr/bin/env python
import subprocess
import os
import webbrowser
import shutil
import time

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, BarColumn, TextColumn
    console = Console()
    RICH = True
except ImportError:
    RICH = False


def animate(text="Working", seconds=1.0):
    if RICH:
        with console.status(f"[bold cyan]{text}...", spinner="dots"):
            time.sleep(seconds)
    else:
        print(f"{text}...")
        time.sleep(seconds)


def banner(title):
    if not RICH:
        return
    console.print(Panel.fit(f"[bold magenta]{title}[/]\n[dim]by mraz0tix![/]", border_style="cyan"))
    with Progress(TextColumn("[cyan]Loading"), BarColumn(bar_width=30), transient=True) as progress:
        task = progress.add_task("", total=30)
        for _ in range(30):
            progress.advance(task)
            time.sleep(0.03)


def gui(title, actions):
    try:
        import queue
        import threading
        import tkinter as tk
        from tkinter import scrolledtext
    except ImportError:
        print("\n[!] tkinter is not installed (install python-tk).")
        input("\nPress Enter to continue...")
        return

    try:
        root = tk.Tk()
    except tk.TclError:
        print("\n[!] No graphical display available.")
        input("\nPress Enter to continue...")
        return

    root.title(f"{title} by mraz0tix")
    root.geometry("700x480")
    root.configure(bg="#1e1e2e")

    side = tk.Frame(root, bg="#1e1e2e")
    side.pack(side="left", fill="y", padx=8, pady=8)

    out = scrolledtext.ScrolledText(
        root, bg="#11111b", fg="#a6e3a1", insertbackground="white",
        font=("monospace", 10), state="disabled"
    )
    out.pack(side="right", fill="both", expand=True, padx=8, pady=8)

    results = queue.Queue()

    def show(text):
        out.configure(state="normal")
        out.delete("1.0", "end")
        out.insert("end", text)
        out.configure(state="disabled")

    def worker(cmd):
        try:
            done = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            results.put(done.stdout + done.stderr)
        except FileNotFoundError:
            results.put(f"{cmd[0]} isn't installed!")
        except subprocess.TimeoutExpired:
            results.put("Timed out.")

    def poll():
        try:
            while True:
                show(results.get_nowait())
        except queue.Empty:
            pass
        root.after(100, poll)

    def click(action):
        result = action() if callable(action) else action
        if isinstance(result, list):
            show("Running: " + " ".join(result) + " ...")
            threading.Thread(target=worker, args=(result,), daemon=True).start()
        elif result:
            show(result)

    show(f"{title} by mraz0tix\n\nChoose an action on the left.")
    for label, action in actions:
        tk.Button(side, text=label, width=22, command=lambda a=action: click(a)).pack(pady=3)
    tk.Button(side, text="Close", width=22, command=root.destroy).pack(pady=3)

    poll()
    root.mainloop()


def gui_site():
    webbrowser.open("https://mraz0tix-code.github.io/")
    return "Opening mraz0tix's site in your browser..."


def disk_animation(path="/"):
    total, used, free = shutil.disk_usage(path)
    percent = (used / total) * 100
    if RICH:
        with Progress(TextColumn("[bold]{task.description}"), BarColumn(bar_width=30), TextColumn("{task.percentage:>5.1f}%")) as progress:
            task = progress.add_task(f"[{path}]", total=100)
            for step in range(int(percent) + 1):
                progress.update(task, completed=min(step, percent))
                time.sleep(0.02)
            progress.update(task, completed=percent)
        console.print(f"Free: {free / (1024 ** 3):.1f} GB of {total / (1024 ** 3):.1f} GB")
    else:
        print(get_disk_progress_bar(path))


def gui_calculator():
    from tkinter import simpledialog
    a = simpledialog.askfloat("Calculator", "a = ?")
    b = simpledialog.askfloat("Calculator", "b = ?")
    if a is None or b is None:
        return "Cancelled."
    lines = [f"a + b = {a + b}", f"a - b = {a - b}", f"a * b = {a * b}"]
    lines.append("a / b = ERROR! (b = 0)" if b == 0 else f"a / b = {a / b}")
    return "\n".join(lines)


def tool_actions():
    return [
        ("Ping 8.8.8.8", ["ping", "-c", "3", "8.8.8.8"]),
        ("Kernel (uname)", ["uname", "-a"]),
        ("Open ports (ss)", ["ss", "-tuln"]),
        ("Disks (lsblk)", ["lsblk", "-f"]),
        ("Disk usage", lambda: get_disk_progress_bar("/")),
        ("Fastfetch", ["fastfetch"]),
        ("Calculator", gui_calculator),
        ("Open my site", gui_site),
    ]


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

        main_choice = input("\nSelect a menu option (1-5): > ")
         
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
        print("0. Connect via ssh (Security Shell)")

        choice_internet = input("\nSelect a menu option (0-3): > ")  

        if choice_internet == "1":
            Internet_check_default()  
        elif choice_internet == "2":
            Internet_check_custom()   
        elif choice_internet == "3":
            break
        elif choice_internet == "0":
            conection_via_ssh()
        else:
            print("\nSysPulse >> [!] Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def conection_via_ssh():
    while True:
        clear_screen()
        print("=" * 40)
        print("              SSH Conection menu")
        print("=" * 40)
        print("1. Connect with ip adress")
        print("2. Back to main menu")  

        choice_internet = input("\nSelect a menu option (1-2): > ")  
   
        if choice_internet == "1":
            SSH_conection()   
        elif choice_internet == "2":
            break
        else:
            print("\nSysPulse >> [!] Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def SSH_conection():
    name = input("\nEnter username on system > ")
    target = input("\nEnter IP of server > ")
    if target:
        animate("Working")
        try:
            subprocess.run(["kitty", "--hold", "ssh", f"{name}@{target}"], check=True)
        except FileNotFoundError:
            print("\nSysPulse >> [!] Error: 'kitty' terminal is not installed.")
    else:
        print("\nSysPulse >> [!] Error: Empty ip or username.")
    input("\nSysPulse >> Press Enter to continue...")

def Internet_check_default():
    print("\nSysPulse >> [+] Okay! Already checking connection...")
    animate("Working")
    try:
        subprocess.run(["kitty", "--hold", "ping", "-c", "3", "8.8.8.8"], check=True)
        print("[+] Internet connection checked successfully!")
    except FileNotFoundError:
        print("\nSysPulse >> [!] Error: 'kitty' terminal is not installed.")
    input("\nSysPulse >> Press Enter to continue...")

def Internet_check_custom():
    target = input("\nEnter website or IP to ping (e.g., google.com): > ")
    if target: 
        print(f"\nSysPulse >> [+] Pinging {target}...")
        animate("Working")
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
            animate("Working")
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
        print("0. Back to main menu")

        nmap_choice = input("\nSelect a menu option (0-1): > ")

        if nmap_choice == "1":
            subnet = input("\nEnter target subnet (Default: 192.168.1.0/24): > ")
            if not subnet:
                subnet = "192.168.1.0/24"

            print(f"\n[+] Okay, checking subnet {subnet} via Nmap...")
            
            cmd = ["kitty", "--hold", "sudo", "nmap", "-sS", "-sV", "-O", subnet]
            
            try:
                subprocess.run(cmd, check=True)
            except FileNotFoundError:
                print("\nSysPulse >> [!] Error: 'kitty' terminal emulator or 'nmap' is not installed.")
                input("\nNSysPulse >> Press Enter to continue...")
            except subprocess.CalledProcessError:
                print("\nSysPulse >> [!] Scan was interrupted or failed (maybe wrong sudo password?).")
                input("\nSysPulse >> Press Enter to continue...")
                
        elif nmap_choice == "0":
            break
        else:
            print("\nSysPulse >> [!] Invalid choice. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

def Site():
    print("SysPulse >> Okay!")
    webbrowser.open("https://mraz0tix-code.github.io/")
    input("\nSysPulse >> Press Enter to continue...")
    clear_screen()

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
            disk_animation("/")
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
    animate("Please wait")
    subprocess.run(["kitty", "--hold", "sudo", "reboot"])

def shutdown():
    print("\nSysPulse >> [WARNING] Shutdown system...")
    animate("Please wait")
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
        print("5. Open GUI window")
        print("0. Exit the program")
        print("=" * 40)
        main_choice = input("Select a menu option (0-5): ")

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
        elif main_choice == "5":
            gui("SysPulse", tool_actions())
        elif main_choice == "0":
            print("\nSysPulse >> Okay! Goodbye!")
            os.system("clear || cls")
            break
        else:
            print("\nSysPulse >> Invalid choice in main menu. Please try again.")
            input("\nSysPulse >> Press Enter to continue...")

if __name__ == "__main__":
    banner("SysPulse")
    Main_Menu()
