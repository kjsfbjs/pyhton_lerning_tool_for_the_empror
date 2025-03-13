import random
import json
import os
import time


def load_questions():
    return {
        "easy": [
            {"question": "What is the output of print(2 * 3)?", "answer": "6"},
            {"question": "What keyword is used to define a function in Python?", "answer": "def"},
            {"question": "Which data type is mutable: tuple or list?", "answer": "list"},
            {"question": "How do you start a comment in Python?", "answer": "#"},
            {"question": "What function is used to get user input?", "answer": "input"}
        ],
        "medium": [
            {"question": "What is the output of print(5 // 2)?", "answer": "2"},
            {"question": "Which module is used for random number generation?", "answer": "random"},
            {"question": "How do you declare a variable in Python?", "answer": "Just assign a value"},
            {"question": "What is the keyword to create a loop in Python?", "answer": "for or while"},
            {"question": "What is the data type of None in Python?", "answer": "NoneType"}
        ],
        "hard": [
            {"question": "Which statement is used to handle exceptions in Python?", "answer": "try-except"},
            {"question": "How do you open a file in Python?", "answer": "open"},
            {"question": "What is the difference between a shallow copy and a deep copy?",
             "answer": "A shallow copy copies references, a deep copy copies objects"},
            {"question": "What does the 'lambda' keyword do in Python?", "answer": "Creates an anonymous function"},
            {"question": "What is the purpose of the '__init__' method in Python?",
             "answer": "It initializes a class instance"}
        ]
    }


def load_leaderboard():
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as f:
            return json.load(f)
    return {}


def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard, f, indent=4)


def show_admin_panel():
    print("\n🔐 Admin Panel - Leaderboard Viewer")
    leaderboard = load_leaderboard()
    if not leaderboard:
        print("No scores recorded yet.")
    else:
        print("📜 Leaderboard:")
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        for i, (player, points) in enumerate(sorted_leaderboard, 1):
            print(f"{i}. {player}: {points} points")


def show_all_answers():
    print("\n📖 All Answers:")
    questions = load_questions()
    for level, qs in questions.items():
        print(f"\n🔹 {level.capitalize()} Level:")
        for q in qs:
            print(f"Q: {q['question']}\nA: {q['answer']}\n")


def play_game():
    print("\n🎉 Welcome to Python Learning Game! 🎉\n")
    name = input(
        "Enter your name (or type 'Adeptus Mechanicus' to view leaderboard, 'Questor Imperialis' to see all answers): ").strip().lower()

    if name == "adeptus mechanicus":
        show_admin_panel()
        return
    elif name == "questor imperialis":
        show_all_answers()
        return

    print("\nSelect difficulty level:")
    print("1️⃣ Easy")
    print("2️⃣ Medium")
    print("3️⃣ Hard")

    level_choice = input("Enter your choice (1/2/3): ").strip()
    levels = {"1": "easy", "2": "medium", "3": "hard"}
    level = levels.get(level_choice, "easy")

    print(f"\n🚀 Starting game at {level.capitalize()} level!\n")
    score = 0
    questions = load_questions().get(level, [])
    random.shuffle(questions)

    for q in questions:
        print("\n📌 Question:")
        print(q["question"])
        answer = input("Your answer: ").strip().lower()

        if answer == q["answer"].lower():
            print("✅ Correct! 🎉")
            score += 10
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}")
        time.sleep(1)

    print(f"\n🏁 Game Over! {name}, your score is {score}\n")

    leaderboard = load_leaderboard()
    leaderboard[name] = score
    save_leaderboard(leaderboard)

    print("📜 Leaderboard:")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for i, (player, points) in enumerate(sorted_leaderboard, 1):
        print(f"{i}. {player}: {points} points")

    print("\n🎮 Thanks for playing! Try again to beat your score! 🎮")


if __name__ == "__main__":
    play_game()
