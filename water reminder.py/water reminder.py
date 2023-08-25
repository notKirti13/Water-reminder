import time
from plyer import notification

def water_reminder(interval, total_reminders):
    for _ in range(total_reminders):
        notification_title = "Stay Hydrated!"
        notification_message = "It's time to drink water."

        notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=10  # The notification will disappear after 10 seconds.
        )

        time.sleep(interval * 60)  # Convert interval to minutes and wait

if __name__ == "__main__":
    interval_minutes = 30  # Remind every 30 minutes
    total_reminders = 8    # Total reminders for the day

    water_reminder(interval_minutes, total_reminders)
