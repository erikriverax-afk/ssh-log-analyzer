counts = {}
with open("auth.log") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            spot = parts.index("from")
            ip = parts [spot + 1]
            counts [ip] = counts.get(ip, 0) + 1

for ip in counts:
    print(ip, "failed", counts[ip], "times")

with open("auth.log") as file:
    for line in file:
        if "Accepted password" in line:
            parts = line.split()
            ip = parts[parts.index("from") + 1]
            if counts.get(ip, 0) >=5:
                print("ALERT: possible break-in from", ip)