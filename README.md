# FlowScan

TCP port scanner. Multi-threaded, fast, with colored output.

## Run

```bash
python flowscan.py
```

## Requirements

- Python 3.x
- No external libs

## Features

- scans all 65535 TCP ports
- 500 threads
- open ports — green, closed — red
- summary at the end

## Example

```
Scanning 127.0.0.1 (1-65535)...
  [+] 135 OPEN
  [-] 136 CLOSED
  ...
[+] Open ports   : 12
[-] Closed ports : 65523
```
