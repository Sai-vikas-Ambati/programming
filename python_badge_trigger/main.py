#!/usr/bin/env python3
"""
main.py
A lightweight utility that demonstrates Python coding activity.
Purpose: helps trigger the YOLO Octocat badge on GitHub.
"""

import datetime
import platform
import random

def generate_message():
    quotes = [
        "Code is poetry written in logic.",
        "Automation is the  oxygen of productivity.",
        "Every line you write shapes tomorrow’s tech.",
        "Stay consistent — greatness compounds.",
    ]
    today = datetime.date.today().strftime("%B %d, %Y")
    system = platform.system()
    return f"[{today}] Running on {system}. Random Thought: {random.choice(quotes)}"

if __name__ == "__main__":
    print(generate_message())
