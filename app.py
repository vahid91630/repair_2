from flask import Flask

app = Flask(__name__)

@app.route("/")
def health_check():
    return "✅ ربات تعمیرکار آنلاین آماده‌ست."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
