import os

def ping_script(ping_list):
    for each_address in ping_list:
        file_write = open("ping_output","a")
        hostname = each_address
        response = os.system("ping -c 1 -w 1 " + hostname)
        if response == 0:
          file_write.write(f"{hostname} is online\n")
        else:
          file_write.write(f"{hostname} is offline\n")
        
ping_list = []
list_of_lists = []
#creates an empty array for successful devices, failed devices which will be used for reporting
#list_of_lists will be used for the file for loop results

if os.path.exists("ping_output"):
  os.remove("ping_output")
  print("Previous result log file has been removed by the Python file tool")
else:
  print("log file does not exisit")   

print("a - ping 1 IP")
print("b - ping a list of IP's")
print("c - ping a subnet")
ping_selection = input("Select an option: ")

if ping_selection == "a":
  selected_ip = input("What is the IP address? i.e. 192.168.0.1 ")
  ping_list = [selected_ip]
  ping_script(ping_list)
elif ping_selection == "b":
  a_file = open("list_file.txt", "r")
  for line in a_file:
    line_list = line.split()
    ping_script(line_list)
  a_file.close()
  #opens a file with the name logs in read only mode
  #loop through the file, line by line
  #line.strip removes the leading and ending charachter. In this case it would be the empty space
  #appends the naked word to the empty array
  #closes the file
elif ping_selection == "c":
  import ipaddress
  # Prompt the user to input a network address
  net_addr = input("Enter a network address in CIDR format(ex.192.168.1.0/24): ")
  # Create the network
  ip_net = ipaddress.ip_network(net_addr)
  # Get all hosts on that network
  all_hosts = list(ip_net.hosts())
  ping_script(str(all_hosts))
