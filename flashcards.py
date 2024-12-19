import json
import argparse

# Define the Flashcard class
class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer
        }

# Function to add a flashcard
def add_flashcard():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcard = Flashcard(question, answer)

    # Load existing flashcards from JSON file
    try:
        with open('flashcards.json', 'r') as file:
            flashcards = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        flashcards = []

    flashcards.append(flashcard.to_dict())

    # Save the updated list of flashcards to the JSON file
    with open('flashcards.json', 'w') as file:
        json.dump(flashcards, file, indent=4)
    print("Flashcard added!")

# Function to display all flashcards
def display_flashcards():
    try:
        with open('flashcards.json', 'r') as file:
            flashcards = json.load(file)

        for index, card in enumerate(flashcards, start=1):
            print(f"\nFlashcard {index}:")
            print(f"Q: {card['question']}")
            print(f"A: {card['answer']}")
    except FileNotFoundError:
        print("No flashcards found.")

# Function to review flashcards interactively
def review_flashcards():
    try:
        with open('flashcards.json', 'r') as file:
            flashcards = json.load(file)

        for card in flashcards:
            print(f"\n{card['question']}")
            input("Press Enter to reveal the answer...")
            print(f"A: {card['answer']}")
            input("Press Enter to continue...")
    except FileNotFoundError:
        print("No flashcards found.")

# Main function to handle CLI commands
def main():
    parser = argparse.ArgumentParser(description="Flashcard Creation App")
    parser.add_argument('command', choices=['add', 'display', 'review'], help="Command to execute")

    args = parser.parse_args()

    if args.command == 'add':
        add_flashcard()
    elif args.command == 'display':
        display_flashcards()
    elif args.command == 'review':
        review_flashcards()

if __name__ == "__main__":
    main()
