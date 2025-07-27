from openai.agents import tool

@tool
def get_weather(location: str) -> str:
    return f"The weather in {location} is sunny with 25°C."

@tool
def calculate_math(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"
