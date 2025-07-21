# File: scripts/update_pages.py

import sys, os, json
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from jinja2 import Environment, FileSystemLoader
from models import call_model

env = Environment(loader=FileSystemLoader("templates"))

DAILY_PRODUCTS = {
    "sermon_connect": "sermon_connect.txt",
    "harvestlogic": "harvestlogic.txt",
    "shopsignal": "shopsignal.txt",
    "buildflow_suite": "buildflow_suite.txt",
    "scamshield_daily": "scamshield_daily.txt",
    "powerpulse": "powerpulse.txt",
    "dealcloser": "dealcloser.txt",
    "leanops": "leanops.txt",
    "tripsignal": "tripsignal.txt",
    "drivescan": "drivescan.txt",
    "remote_jobs": "remote_jobs.txt",
    "paycheck_tracker": "paycheck_tracker.txt",
    "cult_watch": "cult_watch.txt",
    "hwpupdates": "hwpupdates.txt",
    "quantumaffiliates": "quantumaffiliates.txt"
}

def load_prompt(filename):
    path = os.path.join("prompts", filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def write_json(product_id, content, ad):
    data = {
        "product_id": product_id,
        "content": content,
        "ad": ad,
        "last_updated": datetime.utcnow().isoformat()
    }
    output_path = os.path.join("data", f"{product_id}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"🧠 JSON saved: {output_path}")

def update_all():
    for product_id, prompt_file in DAILY_PRODUCTS.items():
        prompt = load_prompt(prompt_file)
        ad_file = prompt_file.replace(".txt", "_ad.txt")
        ad = load_prompt(ad_file)
        content = call_model("mistral", prompt)
        write_json(product_id, content, ad)

if __name__ == "__main__":
    update_all()
