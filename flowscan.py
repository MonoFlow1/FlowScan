# -*- coding: utf-8 -*-
import socket
import threading
import sys

NUM_THREADS = 500
MAX_PORT = 65535
CONN_TIMEOUT = 0.0001

OK_COLOR = '\033[92m'
BAD_COLOR = '\033[91m'
NO_COLOR = '\033[0m'

open_ports_list = []
closed_count_val = 0
checked_count_val = 0
data_lock = threading.Lock()

def fetch_my_ip():
    my_ip = "127.0.0.1"
    try:
        tmp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tmp_sock.settimeout(0.5)
        tmp_sock.connect(("8.8.8.8", 80))
        my_ip = tmp_sock.getsockname()[0]
        tmp_sock.close()
    except:
        pass
    return my_ip

def check_port_range(target_host, range_start, range_stop):
    global checked_count_val, closed_count_val
    
    current = range_start
    while current < range_stop:
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.settimeout(CONN_TIMEOUT)
        
        connect_result = test_socket.connect_ex((target_host, current))
        
        data_lock.acquire()
        try:
            if connect_result == 0:
                open_ports_list.append(current)
                print(OK_COLOR + "  [+] " + str(current) + " OPEN" + NO_COLOR)
            else:
                closed_count_val = closed_count_val + 1
                print(BAD_COLOR + "  [-] " + str(current) + " CLOSED" + NO_COLOR)
            checked_count_val = checked_count_val + 1
        finally:
            data_lock.release()
        
        test_socket.close()
        current = current + 1

def run_scanner():
    my_addr = fetch_my_ip()

    print("=" * 40)
    print("FlowScan")
    print("=" * 40)
    print("Your local IP: " + str(my_addr))
    print("=" * 40)

    target_addr = input("Target IP: ")
    if target_addr == "" or target_addr is None:
        print("No target specified, exiting...")
        sys.exit(0)

    per_thread = MAX_PORT // NUM_THREADS

    print("\nScanning " + str(target_addr) + " (1-" + str(MAX_PORT) + ")...\n")

    thread_list = []
    for idx in range(NUM_THREADS):
        start_port = idx * per_thread + 1
        if idx < NUM_THREADS - 1:
            end_port = (idx + 1) * per_thread + 1
        else:
            end_port = MAX_PORT + 1
        
        worker = threading.Thread(
            target=check_port_range,
            args=(target_addr, start_port, end_port)
        )
        worker.daemon = True
        worker.start()
        thread_list.append(worker)

    for worker_thread in thread_list:
        worker_thread.join()

    print("\n" + "=" * 40)
    print("Scan complete")
    print("=" * 40)
    print("Total scanned : " + str(checked_count_val))
    print(OK_COLOR + "Open ports   : " + str(len(open_ports_list)) + NO_COLOR)
    print(BAD_COLOR + "Closed ports : " + str(closed_count_val) + NO_COLOR)

    if len(open_ports_list) > 0:
        print("\n" + OK_COLOR + "Open ports list:" + NO_COLOR)
        sorted_ports = sorted(open_ports_list)
        for port_num in sorted_ports:
            print(OK_COLOR + "  [+] " + str(port_num) + NO_COLOR)
    else:
        print("\n" + BAD_COLOR + "No open ports found." + NO_COLOR)

    print("=" * 40)
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    run_scanner()