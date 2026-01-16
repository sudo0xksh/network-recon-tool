import subprocess
import sys

print("=========================================")
print("Welcome to Network Recon Tool\n")

if len(sys.argv) < 2:
    print("Usage: python main.py <target.com>/<targets.txt>")
    sys.exit()

input_value = sys.argv[1]

if input_value.endswith(".txt"):
    file = open(input_value, "r")
    targets = file.readlines()
    file.close()
else:
    targets = [input_value]

for target in targets:
    target = target.strip()

    if (
        target.startswith("http://") or
        target.startswith("https://") or
        "." in target
    ):
        pass  # valid target → continue processing
    else:
        print("Invalid target:", target, "\n")
        continue
    
    print("Pinging:", target)
    ping = subprocess.run(["ping", target])

    if ping.returncode != 0:
        print("Ping failed for:", target, "\n")
        continue

    print("\nRunning nslookup:", target)
    nslookup = subprocess.run(["nslookup", target])
    if nslookup.returncode != 0:
        print("nslookup failed for:", target, "\n")
        continue

    print("\nRunning tracert:", target)
    tracert = subprocess.run(["tracert", target])
    if tracert.returncode != 0:
        print("tracert failed for:", target, "\n")
        continue

    print("\nRunning NMAP:", target)
    nmap = subprocess.run(["nmap", target])

    if nmap.returncode != 0:
        print("NMAP failed for:", target, "\n")
        continue

print("=========================================")
print("Thanks for using Network Recon Tool")
print("Developed by sudo_0xksh")
sys.exit()