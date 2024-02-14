Description:

This Python script utilizes the `socket` module to perform a port scanning operation on a specified IP address. Port scanning is a common technique used to identify open ports on a target system, which can be crucial for network security assessments or troubleshooting purposes.

The `scan_port` function is defined to handle the scanning process for a single port. It takes two parameters: `ip`, which represents the target IP address, and `port`, which denotes the port number to be scanned. Inside the function, a TCP socket is created using `socket.socket`, and the `connect_ex` method is employed to attempt a connection to the specified IP address and port. The result is checked, and if it equals `0`, it indicates that the port is open, and a corresponding message is printed. Otherwise, a message indicating a closed port is printed. Any encountered errors during the connection attempt are caught and displayed.

The script prompts the user to input the target IP address interactively. It then defines a range of ports to scan, from `start_port` to `end_port`, inclusive, and iterates over this range. For each port, the `scan_port` function is called, and if the port is determined to be open, its number is appended to the `open_ports` list.

After scanning all the ports, the script writes the list of open ports to a file named "open_ports.txt" using a `with` statement and a file-writing loop. Finally, it prints out the list of open ports along with a message indicating that the results have been saved to the file.

This script provides a basic yet functional implementation of port scanning in Python, allowing users to quickly identify open ports on a specified IP address within a given range. However, it's important to note that port scanning should only be performed on systems/networks where you have proper authorization to do so, as unauthorized scanning can be considered illegal and unethical.
