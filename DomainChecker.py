import socket
import os

def domain_checker(domain_name):
    try:
        # DNS
        socket.gethostbyname(domain_name)
        return f"\033[91m{domain_name} Registered.\033[0m"  # Red
    except socket.gaierror:
        return f"\033[92m{domain_name} Receivable!\033[0m"  # Green renk

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_terminal()
        print("\033[96m--- Domain Checker ---\033[0m")  
        domain_name = input("Enter a Domain Addres : ")

        if domain_name.lower() == 'q':
            break

        result = domain_checker(domain_name)
        print(result)

        input("\nPress Enter to continue... ")

if __name__ == "__main__":
    main()

# Created by TPàshà
# https://github.com/TPashaxrd