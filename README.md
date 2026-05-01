# FlowScan

![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A fast, multi-threaded TCP port scanner written in Python. Built for learning network fundamentals and security research on authorized systems.

---

## Screenshots

**Scan in progress**

![work](work.png)

**Scan complete**

![end](end.png)

---

## Quick Start

```bash
python flowscan.py


Requirements
	•	Python 3.x
	•	No external dependencies — standard library only (socket, threading, sys)

Features
	•	Scans all 65,535 TCP ports
	•	500 concurrent threads for fast results
	•	Color-coded output — green for open, red for closed
	•	Displays your local IP automatically
	•	Summary report at the end

Example Output

========================================
FlowScan
========================================
Your local IP: 192.168.1.18
========================================
Target IP: 127.0.0.1

Scanning 127.0.0.1 (1-65535)...

  [+] 135 OPEN
  [+] 443 OPEN
  ...

========================================
Scan complete
========================================
Total scanned : 65535
Open ports    : 12
Closed ports  : 65523

Open ports list:
  [+] 135
  [+] 443
========================================


Notes
Only use on systems you own or have explicit permission to scan.

Author
Made by MonoFlow1 — open to feedback and contributions.

.​​​​​​​​​​​​​
