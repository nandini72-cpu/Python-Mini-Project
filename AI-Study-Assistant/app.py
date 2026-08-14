import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: Gemini API key not found.")
    print("Please check your .env file.")
    exit()

# Connect to Gemini
client = genai.Client(api_key=api_key)


# Function to communicate with Gemini
def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        error_message = str(e)

        if "503" in error_message or "UNAVAILABLE" in error_message:
            return (
                "⚠️ Gemini is temporarily busy.\n"
                "Please wait a few seconds and try again."
            )

        return (
            "❌ Something went wrong while contacting Gemini.\n\n"
            f"Error: {error_message}"
        )


# Main program
print("=" * 55)
print("              🤖 AI STUDY ASSISTANT")
print("=" * 55)

print("\nType '5' to exit the program.")


while True:

    print("\n" + "-" * 55)
    print("Choose an option:")
    print("1. 📚 Explain a topic")
    print("2. 📝 Generate a quiz")
    print("3. 💼 Generate interview questions")
    print("4. ❓ Ask anything")
    print("5. 🚪 Exit")
    print("-" * 55)

    choice = input("\nEnter your choice (1-5): ")

    # -----------------------------------------
    # OPTION 1: EXPLAIN A TOPIC
    # -----------------------------------------
    if choice == "1":

        topic = input("\nEnter the topic: ")

        prompt = f"""
You are a helpful AI study assistant.

Explain the topic "{topic}" to a college student
who is learning it for the first time.

Give the answer in this format:

1. Definition
2. Simple Explanation
3. Real-world Example
4. Important Points
5. Short Summary

Use simple and easy-to-understand language.
"""

        print("\n🤖 AI Explanation:\n")
        print(ask_gemini(prompt))


    # -----------------------------------------
    # OPTION 2: GENERATE A QUIZ
    # -----------------------------------------
    elif choice == "2":

        topic = input("\nEnter the quiz topic: ")

        prompt = f"""
You are an AI quiz generator.

Create 5 multiple-choice questions about "{topic}".

For every question provide:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:

Make the questions suitable for a college student.
Include a mixture of easy and difficult questions.
"""

        print("\n📝 AI Quiz:\n")
        print(ask_gemini(prompt))


    # -----------------------------------------
    # OPTION 3: INTERVIEW QUESTIONS
    # -----------------------------------------
    elif choice == "3":

        topic = input("\nEnter the interview topic: ")

        prompt = f"""
You are an AI interview preparation assistant.

Generate 5 interview questions about "{topic}".

Include:
- 3 basic questions
- 2 difficult questions

For every question provide:
Question:
Short Answer:
"""

        print("\n💼 Interview Questions:\n")
        print(ask_gemini(prompt))


    # -----------------------------------------
    # OPTION 4: ASK ANYTHING
    # -----------------------------------------
    elif choice == "4":

        question = input("\nAsk your question: ")

        prompt = f"""
You are a helpful AI study assistant.

Answer the following question clearly and
in simple language.

Question:
{question}
"""

        print("\n🤖 Gemini Answer:\n")
        print(ask_gemini(prompt))


    # -----------------------------------------
    # OPTION 5: EXIT
    # -----------------------------------------
    elif choice == "5":

        print("\n👋 Thank you for using AI Study Assistant!")
        print("Good luck with your studies!")
        break


    # -----------------------------------------
    # INVALID OPTION
    # -----------------------------------------
    else:

        print("\n❌ Invalid choice.")
        print("Please enter a number from 1 to 5.")