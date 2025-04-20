import os
from tinytroupe.openai_utils import client, OpenAIClient
from dotenv import load_dotenv

def test_basic_chat():
    """Test a basic chat completion with the OpenAI API"""
    # Create a simple conversation
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
    
    # Make the API call
    response = client().send_message(
        messages,
        model="o4-mini",  # or "o3" if you want to test that model
        max_completion_tokens=100
    )
    
    print("\nResponse:")
    print(f"Role: {response['role']}")
    print(f"Content: {response['content']}")

def test_structured_output():
    """Test a chat completion with structured output"""
    messages = [
        {"role": "system", "content": "You are a helpful assistant that provides structured responses."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
    
    
if __name__ == "__main__":
    # Check if API key is set

    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set")
        exit(1)
    
    print("Testing basic chat...")
    test_basic_chat()
    