from fastapi import FastAPI, HTTPException
import random
import csv

app = FastAPI()
CSV_FILE = "ips.csv"

def load_ips():
    with open(CSV_FILE, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]
    
def save_ips(ips):
    with open(CSV_FILE, "w") as f:
        for ip in ips:
            f.write(ip + "\n")

@app.get("/get-ip")

def get_ip():
    ips = load_ips()

    if not ips:
        raise HTTPException(status_code=404, detail="no more ips")
    
    chosen_ip = random.choice(ips)
    ips.remove(chosen_ip)
    save_ips(ips)

    return chosen_ip
