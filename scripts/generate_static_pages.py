# File: scripts/generate_static_pages.py

import os
import sys
from jinja2 import Environment, FileSystemLoader

# Allow imports relative to project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

env = Environment(loader=FileSystemLoader("templates"))

STATIC_PRODUCTS = {
    "hwp_explainer": "hwp_explainer.txt",
    "safepayment": "safepayment.txt",
    "parody_power": "parody_power.txt",
    "quantumlaunch": "quantumlaunch.txt",
    "mememasterclass": "mememasterclass.txt",
    "gospel_core": "gospel_core.txt",
    "shiftshield": "shiftshield.txt",
    "cult_explainer": "cult_explainer.txt",
    "buildflow_clarity": "buildflow_clarity.txt",
    "lessonboost": "lessonboost.txt",
    "oneclickapp": "oneclickapp.txt",
    "passiveincomestarter": "passiveincomestarter.txt"
}

def run_mistral(prompt):
    # Replace this with actual call to Ollama or local Mistral instance
    return f"[Mistral Response] {prompt}"

def load_prompt(filename):
    path = os.path.join("prompts", filename)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return f.read()
    return ""

def render_page(product_id, content):
    template = env.get_template("daily_update.html")
    rendered = template.render(content=content, last_updated="")
    output_path = os.path.join("pages", f"{product_id}.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)
    print(f"📦 Static page created: {product_id}.html")

def generate_all():
    for product_id, prompt_file in STATIC_PRODUCTS.items():
        prompt = load_prompt(prompt_file)
        content = run_mistral(prompt)
        render_page(product_id, content)

if __name__ == "__main__":
    generate_all()
