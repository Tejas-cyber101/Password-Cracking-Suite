An automated cross-platform security toolkit for auditing password strength and credential resilience. Features include dictionary generation, hash extraction (Linux/Windows), and mathematical entropy analysis# Password Cracking & Credential Attack Suite

## 1. Project Overview
This project is a practical toolkit designed for **password policy testing** and **credential security assessment**[cite: 4]. [cite_start]It provides an ethical environment to understand how credentials are stored, how they are attacked, and how to reinforce authentication[cite: 7, 8].

## 2. Key Features
* [cite_start]**Dictionary Generator**: Creates custom wordlists with mutation rules (leet-speak, casing, number padding)[cite: 33, 34].
* [cite_start]**Hash Extraction**: Extracts `/etc/shadow` entries on Linux and exports SAM/SYSTEM hives on Windows using `reg.exe`[cite: 36, 37, 60].
* [cite_start]**Brute-Force Simulator**: Tests password robustness via dictionary attack simulations[cite: 39, 40].
* [cite_start]**Strength Analyzer**: Estimates password entropy and complexity[cite: 44, 46].
* [cite_start]**Audit Reporting**: Generates a summary of vulnerabilities and risk severity[cite: 49, 50].

## 3. Workflow Architecture
[cite_start]The suite follows a 6-step workflow [cite: 76-87]:
1. **User Input**
2. **Dictionary Generation**
3. **Hash Extraction**
4. **Attack Simulation**
5. **Strength Analysis**
6. **Report Generation**



## 4. Setup & Usage
### Prerequisites
- Python 3.x
- Administrative/Root privileges (Required for Hash Extraction)

### Installation
```bash
pip install -r requirements.txt

RUNNING THE TOOL
LINUX :- sudo python3 main_suite.py
WINDOWS :- 1> Open PowerShell/CMD as Administrator.
           2> Run: python main_suite.py


### 📊 Project Summary Table
| File | Documentation Goal | Source |
| :--- | :--- | :--- |
| `main_suite.py` | Working toolkit (simulation only) | [cite: 122] |
| `README.md` | Project documentation (Description/Scope/Workflow) | [cite: 121] |
| `requirements.txt` | Tooling & Modules used | [cite: 57] |

**Would you like me to help you create a PowerPoint (PPT) outline for your final presentation as mentioned in Source 125?**

