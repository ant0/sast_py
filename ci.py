import subprocess

API_KEY='password123'
PASSWORD='catchme'

ip = input("Enter the IP: ")
output = subprocess.check_output(f"ping {ip}", shell=True, encoding='UTF-8')
print(output)
