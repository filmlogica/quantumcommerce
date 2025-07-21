import schedule
import time

def post_promo():
    print("🚀 Promo content posted to Twitter / Reddit / Discord (simulated)...")

schedule.every().day.at("09:00").do(post_promo)
schedule.every().day.at("17:00").do(post_promo)

if __name__ == "__main__":
    print("🕒 Promotion scheduler running...")
    while True:
        schedule.run_pending()
        time.sleep(60)
