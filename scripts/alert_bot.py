def trigger_alert(event_type):
    alerts = {
        "milestone": "🎉 You hit a milestone! Commission boosted!",
        "spike": "📈 Sales spike detected! Time to double down.",
        "new_promo": "🧨 New promo launched! Share and earn."
    }
    print(alerts.get(event_type, "🚨 Unknown alert type."))

if __name__ == "__main__":
    trigger_alert("milestone")
    trigger_alert("new_promo")
