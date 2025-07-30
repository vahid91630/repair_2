def get_replit_code():
    try:
        with open("replit_sample_code.py", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""
