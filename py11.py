movie = ["Drakula\n","Zombie\n", "Silent hill\n", "Ghost town\n", "Black Night"]
with open("name.txt", "w") as m:
    for i in movie:
        m.write(i)

