import hashlib

def cloak_link(product_url, affiliate_id):
    tag = hashlib.sha256(affiliate_id.encode()).hexdigest()[:8]
    return f"{product_url}?ref={tag}"

if __name__ == "__main__":
    product = "https://quantumcommerce.ga/products/scamshield"
    aff_id = "affiliate_xyz"
    print("🔗 Cloaked Link:", cloak_link(product, aff_id))
