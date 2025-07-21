def make_local_page(city, affiliate):
    filename = f"../pages/{city.lower()}_{affiliate}.html"
    html = f"""
    <html><head><title>{city} Deals by {affiliate}</title></head>
    <body>
        <h1>{city}'s Top Picks from {affiliate}</h1>
        <p>Explore ScamShield, ShiftShield, and TripSignal curated for local interest.</p>
    </body></html>
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"📍 Local SEO page generated: {filename}")

if __name__ == "__main__":
    make_local_page("Atlanta", "affiliate_xyz")
