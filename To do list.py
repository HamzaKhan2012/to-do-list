def main():
    tasks = []
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    tasks.append({
                        "desc": parts[0], 
                        "date": parts[1], 
                        "pri": parts[2], 
                        "done": parts[3] == "True"
                    })
    except FileNotFoundError:
        pass

    while True:
        print("\n1. List  2. Add  3. Done  4. Edit  5. Del  6. Exit")
        choice = input("> ")

        if choice == "1":
            for i, t in enumerate(tasks, 1):
                status = "[X]" if t["done"] else "[ ]"
                print(f"{i}. {status} ({t['pri']}) Due: {t['date']} - {t['desc']}")
        
        elif choice == "2":
            desc = input("Task: ")
            date = input("Due: ") or "None"
            pri = input("Priority: ") or "Medium"
            if desc:
                tasks.append({"desc": desc, "date": date, "pri": pri, "done": False})
        
        elif choice in ["3", "4", "5"]:
            try:
                i = int(input("Number: ")) - 1
                if choice == "3":
                    tasks[i]["done"] = True
                elif choice == "4":
                    tasks[i]["desc"] = input(f"New desc [{tasks[i]['desc']}]: ") or tasks[i]["desc"]
                    tasks[i]["date"] = input(f"New date [{tasks[i]['date']}]: ") or tasks[i]["date"]
                    tasks[i]["pri"] = input(f"New priority [{tasks[i]['pri']}]: ") or tasks[i]["pri"]
                elif choice == "5":
                    tasks.pop(i)
            except (ValueError, IndexError):
                print("Invalid number.")

        elif choice == "6":
            break

        with open("tasks.txt", "w") as f:
            for t in tasks:
                f.write(f"{t['desc']}|{t['date']}|{t['pri']}|{t['done']}\n")

if __name__ == "__main__":
    main()
