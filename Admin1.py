# Name:  
# Student Number:  



import json

def input_int(prompt, max_value):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= max_value:
                return value
            else:
                print("Invalid input. Please enter a value between 1 and", max_value)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Invalid input. Please enter something.")

def save_data(data):
    with open("data.txt", "w") as file:
        json.dump(data, file, indent=4)

def main():
    try:
        with open("data.txt", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    print("Welcome to the admin program!")

    while True:
        print("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, or [q]uit.")
        user_choice = input("Enter your choice: ")

        if user_choice == "a":
            category_name = input_something("Enter the category name: ")
            answers = []
            while True:
                answer = input_something("Enter an answer (leave blank to finish): ")
                if not answer:
                    break
                answers.append(answer)
            difficulty = input_int("Enter the difficulty (1-3): ", 3)

            new_category = {
                "category": category_name,
                "answers": answers,
                "difficulty": difficulty
            }
            data.append(new_category)
            save_data(data)
            print("Category added successfully.")

        elif user_choice == "l":
            if not data:
                print("No categories saved.")
            else:
                for index, category in enumerate(data):
                    print(index + 1, "-", category["category"])

        elif user_choice == "s":
            if not data:
                print("No categories saved.")
            else:
                search_term = input_something("Enter a search term: ")
                found_categories = [
                    category for category in data if search_term.lower() in category["category"].lower()
                ]
                if not found_categories:
                    print("No results found.")
                else:
                    for index, category in enumerate(found_categories):
                        print(index + 1, "-", category["category"])

        elif user_choice == "v":
            if not data:
                print("No categories saved.")
            else:
                index = input_int("Enter the index number: ", len(data)) - 1
                category = data[index]
                print("Category:", category["category"])
                print("Answers:", ", ".join(category["answers"]))
                print("Difficulty:", category["difficulty"])

        elif user_choice == "d":
            if not data:
                print("No categories saved.")
            else:
                index = input_int("Enter the index number: ", len(data)) - 1
                if 0 <= index < len(data):
                    category = data[index]
                    print("Category:", category["category"])
                    print("Answers:", ", ".join(category["answers"]))
                    print("Difficulty:", category["difficulty"])
                    data.remove(category)
                    save_data(data)
                    print("Category deleted successfully.")
                else:
                    print("Invalid index number.")

        elif user_choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

