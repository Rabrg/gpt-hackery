import argparse
import sys

import openai
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt


def create_chat_message(role, content):
    return {"role": role, "content": content}


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def chatbot(text_path: str, model: str):
    # Read the content of the text file
    text = read_file(text_path)

    # Initialize the rich console
    console = Console()
    console.print(Panel("Welcome to the Socratic Chatbot", box=box.ROUNDED, expand=False))

    # Set up the initial messages
    initial_system_message = create_chat_message(
        role="system",
        content=f"You are Socrates, a wise philosopher. Help the user test their knowledge of the following text:\n\n{text}",
    )
    inital_user_message = create_chat_message(
        role="user",
        content="Test me on my knowledge of the above text. Ask me questions on its key ideas, one at a time; when I sufficiently answer, additionally answer the question in your own words, and move on to the next. If my answer is insufficient or seems like it has gaps, probe me further on the topic.",
    )

    # Create the message history
    messages = [initial_system_message, inital_user_message]

    # Main loop for the interactive chat
    while True:
        try:
            # Generate a response using OpenAI's ChatCompletion endpoint
            response = openai.ChatCompletion.create(model=model, messages=messages)

            assistant_response = response.choices[0].message["content"].strip()

            # Create an assistant message and add it to the conversation
            assistant_message = create_chat_message("assistant", assistant_response)
            messages.append(assistant_message)

            # Display the assistant's response
            console.print(f"[bold green]Socrates[/bold green]: {assistant_response}")

            # Take input from the user
            user_input = Prompt.ask("[bold red]You[/bold red]")
            if user_input.strip().lower() == "exit":
                console.print("Goodbye!")
                break

            # Create a user message and add it to the conversation
            user_message = create_chat_message("user", user_input)
            messages.append(user_message)
        except KeyboardInterrupt:
            console.print("\nGoodbye!")
            sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="An interactive CLI chatbot with Socrates as a guide"
    )
    parser.add_argument("text_path", help="Path to the text file to be used in the chat")
    parser.add_argument("--model", default="gpt-4-32k", help="The model to use for the chat")
    args = parser.parse_args()

    chatbot(args.text_path, args.model)
