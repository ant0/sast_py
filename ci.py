import subprocess

API_KEY='password123'
PASSWORD='catchme'
DB_PASSWORD='db-pass'

ip = input("Enter the IP: ")
output = subprocess.check_output(f"ping {ip}", shell=True, encoding='UTF-8')
print(output)

if 'output' in locals():
  print(API_KEY)
  print(PASSWORD)
  prin(DB_PASSWORD)
