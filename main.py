import time
from modules.replit_checker import get_replit_code
from modules.ai_engine import analyze_and_repair
from modules.dashboard import log_to_dashboard

CHECK_INTERVAL = 1

def run_repair_cycle():
    print("🤖 ربات تعمیرکار هوشمند فعال شد...")

    while True:
        print("🔍 در حال بررسی کد ربات رپلیت...")
        code = get_replit_code()

        if not code:
            print("⚠️ کدی یافت نشد یا اتصال به رپلیت ناموفق بود.")
        else:
            result = analyze_and_repair(code)
            log_to_dashboard(result)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    run_repair_cycle()
