# arcade score checker

high_score = 0

while True:
    score = input("Enter your game score (or type 'stop' to end): ")
    score = score.strip().lower()

    if score == "stop":
        print("Game session ended!")
        break

    score = int(score)

    if score > 100:
        print("Wow! That's a new high score!")
        high_score = score
    else:
        print("Good try, keep playing!")