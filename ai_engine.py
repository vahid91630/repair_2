import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_and_repair(code: str) -> dict:
    prompt = f"""
کد پایتون زیر را تحلیل کن:
- اگر خطایی دارد، توضیح بده چه خطایی.
- نسخه‌ی بهتر و اصلاح‌شده آن را بده.

کد:
{code}

پاسخ:
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "تو یک تعمیرکار حرفه‌ای پایتون هستی."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=800
        )

        answer = response['choices'][0]['message']['content']
        return {
            "full_response": answer
        }

    except Exception as e:
        return {
            "error": str(e)
        }
