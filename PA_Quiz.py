# Digital Technologies quiz for practice assessment

score = 0

qa = {
    "New Zealand": "wellington",
    "Australia": "canberra",
    "India": "new delhi",
    "China": "beijing"
}

for q in qa:
    print(q)
    ans = input("Enter Capital: " )
    if ans.lower() == qa[q]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

percentage = round(score / len(qa) * 100)

print(f"Your Score is {score} ({percentage}%)")