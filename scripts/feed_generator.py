import feedparser
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("../templates"))

FEEDS = [
    "https://example.com/rss/news.xml",
    "https://example.com/rss/scamshield.xml"
]

def collect_feed_entries():
    entries = []
    for url in FEEDS:
        feed = feedparser.parse(url)
        entries.extend(feed.entries[:5])  # Limit to top 5 per feed
    return entries

def render_feed(entries, output_file):
    template = env.get_template("daily_update.html")
    combined_content = "\n".join([f"<h2>{e.title}</h2><p>{e.summary}</p>" for e in entries])
    html = template.render(content=combined_content, last_updated="Dynamic Feed")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    entries = collect_feed_entries()
    render_feed(entries, "../pages/dynamic_affiliate_feed.html")
    print("✅ Feed generated.")
