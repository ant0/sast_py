import subprocess

ip = input("Enter the IP: ")
output = subprocess.check_output(f"ping {ip}", shell=True, encoding='UTF-8')
print(output)
