import os
import requests
import datetime

# Configs (from GitHub Secrets)
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TARGET_DATES = os.getenv("TARGET_DATES", "2025-11-23").split(",")

# You’ll need to inspect Eurostar Snap’s site for a real API endpoint
# Below is a placeholder check simulating result availability
def check_snap_availability(date):
    # TODO: Replace this with real logic after inspecting snap.eurostar.com
    # For example, use requests.get("https://snap.eurostar.com/api/availability?...date=...")
    # Return True if tickets available, else False
    print(f"Checking Eurostar Snap for {date}")
    return False  # change to True when you detect availability

def send_discord_message(msg):
    if not WEBHOOK_URL:
        print("No Discord webhook URL configured")
        return
    requests.post(WEBHOOK_URL, json={"content": msg})

def main():
    found = []
    for date in TARGET_DATES:
        if check_snap_availability(date.strip()):
            found.append(date.strip())

    if found:
        msg = "⚡ Eurostar SNAP available for: " + ", ".join(found)
    else:
        msg = f"No SNAP tickets found ({datetime.datetime.now().isoformat(timespec='minutes')})"

    send_discord_message(msg)
    print(msg)

if __name__ == "__main__":
    main()
