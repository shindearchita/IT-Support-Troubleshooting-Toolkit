import platform
import socket
import subprocess
import psutil
import os
from datetime import datetime


# --------------------------------------------------
# 1. SYSTEM INFORMATION
# --------------------------------------------------

def show_system_info():
    print("\n========== SYSTEM INFORMATION ==========")

    print(f"Computer Name   : {socket.gethostname()}")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version      : {platform.version()}")
    print(f"Architecture    : {platform.machine()}")
    print(f"Processor       : {platform.processor()}")


# --------------------------------------------------
# 2. NETWORK INFORMATION
# --------------------------------------------------

def show_network_info():
    print("\n========== NETWORK INFORMATION ==========")

    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.error:
        ip_address = "Unable to determine"

    print(f"Computer Name : {hostname}")
    print(f"IP Address    : {ip_address}")

    print("\nDetailed Network Configuration:")
    subprocess.run("ipconfig", shell=True)


# --------------------------------------------------
# 3. INTERNET CONNECTIVITY TEST
# --------------------------------------------------

def test_internet():
    print("\n========== INTERNET CONNECTIVITY ==========")
    print("Testing internet connection...")

    result = subprocess.run(
        ["ping", "-n", "4", "8.8.8.8"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("\nStatus: PASS - Internet connectivity is available.")
    else:
        print("\nStatus: FAIL - Internet connectivity could not be verified.")

    print("\nPing Results:")
    print(result.stdout)


# --------------------------------------------------
# 4. DNS LOOKUP
# --------------------------------------------------

def dns_lookup():
    print("\n========== DNS LOOKUP ==========")

    domain = input("Enter domain name (example: google.com): ")

    try:
        ip_address = socket.gethostbyname(domain)

        print(f"\nDomain     : {domain}")
        print(f"IP Address : {ip_address}")
        print("DNS Status : PASS")

    except socket.gaierror:
        print("\nDNS Status : FAIL - Domain could not be resolved.")


# --------------------------------------------------
# 5. PING TEST
# --------------------------------------------------

def ping_host():
    print("\n========== PING TEST ==========")

    host = input("Enter IP address or hostname: ")

    result = subprocess.run(
        ["ping", "-n", "4", host],
        capture_output=True,
        text=True
    )

    print("\nPing Results:")
    print(result.stdout)

    if result.returncode == 0:
        print("Ping Status: PASS")
    else:
        print("Ping Status: FAIL")


# --------------------------------------------------
# 6. CPU, RAM AND DISK USAGE
# --------------------------------------------------

def show_resource_usage():
    print("\n========== SYSTEM RESOURCE USAGE ==========")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    print(f"CPU Usage      : {cpu}%")
    print(f"RAM Usage      : {memory.percent}%")
    print(f"Disk Usage C:  : {disk.percent}%")


# --------------------------------------------------
# 7. GENERATE SUPPORT REPORT
# --------------------------------------------------

def generate_report():
    print("\n========== GENERATING SUPPORT REPORT ==========")

    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.error:
        ip_address = "Unable to determine"

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    internet_result = subprocess.run(
        ["ping", "-n", "2", "8.8.8.8"],
        capture_output=True,
        text=True
    )

    if internet_result.returncode == 0:
        internet_status = "PASS - Internet connectivity available"
    else:
        internet_status = "FAIL - Internet connectivity unavailable"

    report = f"""
========================================
       IT SUPPORT DIAGNOSTIC REPORT
========================================

Generated        : {report_time}

SYSTEM INFORMATION
----------------------------------------
Computer Name    : {hostname}
Operating System : {platform.system()}
OS Version       : {platform.version()}
Architecture     : {platform.machine()}
Processor        : {platform.processor()}

NETWORK INFORMATION
----------------------------------------
IP Address       : {ip_address}
Internet Status  : {internet_status}

SYSTEM RESOURCE USAGE
----------------------------------------
CPU Usage        : {cpu}%
RAM Usage        : {memory.percent}%
Disk Usage (C:)  : {disk.percent}%

========================================
             END OF REPORT
========================================
"""

    project_folder = os.path.dirname(os.path.abspath(__file__))
    reports_folder = os.path.join(project_folder, "reports")

    os.makedirs(reports_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.join(
        reports_folder,
        f"support_report_{timestamp}.txt"
    )

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    print("\n========================================")
    print("       REPORT GENERATED SUCCESSFULLY")
    print("========================================")
    print(f"\nSaved at:\n{filename}")


# --------------------------------------------------
# 8. OPEN LATEST REPORT
# --------------------------------------------------

def open_latest_report():

    project_folder = os.path.dirname(os.path.abspath(__file__))
    reports_folder = os.path.join(project_folder, "reports")

    if not os.path.exists(reports_folder):
        print("\nNo reports folder found.")
        print("Generate a report first.")
        return

    reports = [
        file for file in os.listdir(reports_folder)
        if file.startswith("support_report_") and file.endswith(".txt")
    ]

    if not reports:
        print("\nNo support reports found.")
        print("Please generate a report first.")
        return

    reports.sort(
        key=lambda file: os.path.getmtime(
            os.path.join(reports_folder, file)
        ),
        reverse=True
    )

    latest_report = os.path.join(
        reports_folder,
        reports[0]
    )

    print(f"\nOpening report:")
    print(latest_report)

    try:
        os.startfile(latest_report)
        print("\nReport opened successfully.")
    except Exception as error:
        print("\nUnable to open the report automatically.")
        print(f"Error: {error}")


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main():

    while True:

        print("\n")
        print("========================================")
        print("     IT SUPPORT TROUBLESHOOTING TOOL")
        print("========================================")
        print("1. System Information")
        print("2. Network Information")
        print("3. Test Internet Connectivity")
        print("4. DNS Lookup")
        print("5. Ping a Host")
        print("6. Check CPU, RAM & Disk Usage")
        print("7. Generate Support Report")
        print("8. Open Latest Support Report")
        print("9. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_system_info()

        elif choice == "2":
            show_network_info()

        elif choice == "3":
            test_internet()

        elif choice == "4":
            dns_lookup()

        elif choice == "5":
            ping_host()

        elif choice == "6":
            show_resource_usage()

        elif choice == "7":
            generate_report()

        elif choice == "8":
            open_latest_report()

        elif choice == "9":
            print("\nThank you for using the IT Support Troubleshooting Toolkit!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice.")
            print("Please enter a number between 1 and 9.")


# --------------------------------------------------
# START PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    main()