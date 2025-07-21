import subprocess
from jinja2 import Environment, FileSystemLoader

# Step 1: Load prompt from the new file
with open("/home/roymnel/Documents/QuantumCommerce/prompts/safepayment.txt", "r") as f:
    prompt = f.read()

# Step 2: Send to Mistral (via Ollama)
response = subprocess.run(
    ["ollama", "run", "mistral", prompt],
    capture_output=True,
    text=True
)

content = response.stdout

# Step 3: Format the response into clean HTML paragraphs (no titles)
formatted_content = ''.join(
    f"<p>{line.strip()}</p>" 
    for line in content.split('\n') if line.strip()
)

# Step 4: Load the Kindle-style template (assumes Bulma in use)
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('page.html')  # Your Bulma layout here
html = template.render(content=formatted_content)

# Step 5: Save the final HTML into the served directory
with open("/home/roymnel/Documents/QuantumCommerce/pages/safepayment.html", "w") as f:
    f.write(html)
