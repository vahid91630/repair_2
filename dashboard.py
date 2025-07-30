from datetime import datetime

def log_to_dashboard(data: dict):
    with open("logs/repair_log.txt", "a", encoding="utf-8") as log:
        log.write(f"\n\n🕒 {datetime.now()}\n")
        if 'error' in data:
            log.write("❌ خطا:\n")
            log.write(data['error'] + "\n")
        else:
            log.write("✅ نتیجه تحلیل:\n")
            log.write(data['full_response'] + "\n")
