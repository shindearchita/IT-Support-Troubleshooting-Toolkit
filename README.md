# IT Support Troubleshooting Toolkit

A Python-based command-line toolkit designed to assist IT Support technicians with common first-level system and network troubleshooting tasks.

The toolkit automates basic diagnostic checks, provides system and network information, performs connectivity tests, monitors system resources, and generates timestamped diagnostic reports.

---

## 📌 Project Overview

IT Support technicians often perform repetitive diagnostic checks when troubleshooting user issues, such as checking IP configuration, testing network connectivity, verifying DNS resolution, and checking system resource usage.

This project brings several of these first-level troubleshooting tasks together into a single command-line application.

The goal of the project is to make basic diagnostics faster, more organized, and easier to document.

---

## ✨ Features

### 🖥️ System Information

Displays important information about the computer, including:

* Computer name
* Operating system
* OS version
* System architecture
* Processor information

### 🌐 Network Information

Displays network configuration using Windows networking utilities.

* Hostname
* IP address
* Detailed `ipconfig` information

### 📡 Internet Connectivity Test

Tests internet connectivity by sending ICMP ping requests to Google's public DNS server.

* Connectivity status
* Ping response results
* PASS/FAIL indication

### 🔍 DNS Lookup

Resolves a domain name into its corresponding IP address.

Example:

```text
google.com → IP Address
```

This can help identify basic DNS resolution problems.

### 📶 Ping Test

Allows the user to test connectivity to a specific:

* IP address
* Hostname
* Domain

The tool displays the ping results and provides a PASS/FAIL status.

### ⚙️ System Resource Monitoring

Displays current system resource utilization:

* CPU usage
* RAM usage
* Disk usage

### 📄 Diagnostic Report Generation

Generates a timestamped IT Support diagnostic report containing:

* System information
* Network information
* Internet connectivity status
* CPU usage
* RAM usage
* Disk usage

Reports are automatically stored in the `reports` directory.

### 📂 Open Latest Report

Allows the user to open the most recently generated diagnostic report directly from the application.

---

## 🛠️ Technologies Used

| Technology    | Purpose                                   |
| ------------- | ----------------------------------------- |
| Python 3      | Application development                   |
| `psutil`      | CPU, RAM and disk monitoring              |
| `socket`      | Hostname, IP and DNS operations           |
| `subprocess`  | Executing Windows networking commands     |
| `platform`    | Operating system and hardware information |
| `datetime`    | Timestamping diagnostic reports           |
| File Handling | Creating and storing support reports      |

---

## 📋 Requirements

* Windows 10 or Windows 11
* Python 3.x
* `psutil` Python package

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Navigate to the project directory

```bash
cd IT_Support_Troubleshooting_Toolkit
```

### 3. Install the required dependency

```bash
python -m pip install psutil
```

### 4. Run the application

```bash
python main.py
```

---

## 🖥️ Application Menu

When the application starts, the following menu is displayed:

```text
========================================
     IT SUPPORT TROUBLESHOOTING TOOL
========================================
1. System Information
2. Network Information
3. Test Internet Connectivity
4. DNS Lookup
5. Ping a Host
6. Check CPU, RAM & Disk Usage
7. Generate Support Report
8. Open Latest Support Report
9. Exit
========================================
```

---

## 🔧 Example Use Case

### Scenario: User Cannot Access the Internet

An IT Support technician can use the toolkit to perform initial diagnostics:

**Step 1 — Network Information**

Check the system's IP configuration.

**Step 2 — Internet Connectivity**

Test whether the machine can reach an external IP address.

**Step 3 — DNS Lookup**

Check whether domain names can be resolved.

**Step 4 — Ping Test**

Test connectivity to a specific host or IP address.

**Step 5 — Resource Monitoring**

Check whether high CPU, RAM, or disk utilization may be affecting the system.

**Step 6 — Generate Report**

Create a diagnostic report that can be reviewed or shared for further troubleshooting.

---

## 📁 Project Structure

```text
IT_Support_Troubleshooting_Toolkit/
│
├── main.py
├── README.md
├── reports/
│   └── support_report_YYYYMMDD_HHMMSS.txt
│
└── requirements.txt
```

---

## 🎯 Learning Objectives

This project was developed to strengthen practical knowledge of:

* IT Support troubleshooting
* Windows system administration concepts
* Networking fundamentals
* DNS and connectivity troubleshooting
* Python scripting
* System resource monitoring
* Command-line utilities
* Basic automation
* Technical documentation

---

## 🔮 Future Enhancements

Possible future improvements include:

* Graphical User Interface (GUI)
* Network adapter health checks
* Automatic detection of default gateway
* TCP port connectivity testing
* Windows service status monitoring
* Event Viewer log collection
* Automated troubleshooting recommendations
* Export reports to HTML or PDF
* Logging and ticket integration
* Remote diagnostic capabilities

---

## ⚠️ Disclaimer

This project is intended for educational and IT Support troubleshooting purposes.

Some features rely on Windows-specific commands and therefore may not work as expected on Linux or macOS systems.

---

## 👩‍💻 Author

**Archita Shinde**

IT Support | Networking | Cybersecurity

---

## ⭐ Project Highlights

* Automated first-level IT diagnostics
* Network connectivity and DNS troubleshooting
* System resource monitoring
* Timestamped diagnostic reporting
* Windows-focused support utilities
* Designed with practical IT Support scenarios in mind
