from django.db import models

def get_message(answers, gender):
    total = sum(answers)
    message = ""

    if total <= 17:
        if gender == 1:
            message = "1.1"
        else:
            message = "1.0"
    elif 18 <= total <= 26:
        if gender == 1:
            message = "2.1"
        else:
            message = "2.0"
    elif 27 <= total <= 30:
        if gender == 1:
            message = "3.1"
        else:
            message = "3.0"
    elif total > 31:
        if gender == 1:
            message = "4.1"
        else:
            message = "4.0"

    return {"total_score": total, "interpretation": message}
