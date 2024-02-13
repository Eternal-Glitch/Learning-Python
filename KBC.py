questions = [
    ["Where is the lotus temple located:",'India','Japan','Australia','China',3],
    ["World's most famous martial artist:",'Jackie Chan','Bruce Lee','Mohammad Ali','Kyobo Amitsu',2],
    ["Tallest building ever made in the world:",'Maze bank','Eiffel Tower','Tower of pisa','Burj Khalifa',4],
    ["A country with most discipline:",'Japan','Dubai','Russia','United Kingdom',1],
    ["Where is the lotus temple located:",'India','Japan','Australia','China',2],
    ["Where is the lotus temple located:",'India','Japan','Australia','China',3],
    ["Where is the lotus temple located:",'India','Japan','Australia','China',4],
    ["Where is the lotus temple located:",'India','Japan','Australia','China',2],
    ["Where is the lotus temple located:",'India','Japan','Australia','China',1],
    ["Where is the lotus temple located:",'India','Japan','Australia','China',1]
]

levels = [1000, 2000, 3000, 5000, 10000, 25000, 75000, 100000, 250000, 500000]
money = 0

for i in range(0,len(questions)):
    q = questions[i]
    print(f"The prize for this question is {levels[i]}")
    print(f"{q[0]}:")
    print(f"A. {q[1]}       B.{q[2]}")
    print(f"C. {q[3]}       D.{q[4]}")
    ans = int(input("Enter your choice (1-4):"))
    if ans == q[5]:
        print("Sahiii Jawwaab!!!")
        if i == 3 or i == 6 or i ==8:
            money = levels[i]
        
    else:
        print("Galat jawab!! :(")
        money = levels[i-1]
        break

print(f"You won {money} money.")
print("To kya karoge aap itni dhanrashi ka hehh??")
