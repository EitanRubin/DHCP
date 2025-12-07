import csv

with open("ips.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    r = [n for n in range(0, 256)]
    for x in r:
        writer.writerows([[f'10.0.1.{x}']])