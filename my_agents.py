# agents.py
from agents import Agent
from tools import get_weather, calculate_math

# Weather Agent
weather_agent = Agent(
    name="WeatherAgent",
    instructions="You help with weather questions using the tool.",
    tools=[get_weather]
)

# Math Agent
math_agent = Agent(
    name="MathAgent",
    instructions="You help with basic math calculations using the tool.",
    tools=[calculate_math]
)

# Triage Agent routes to the right one
triage_agent = Agent(
    name="TriageAgent",
    instructions="Decide if this is a weather or math question and hand off.",
    handoffs=[weather_agent, math_agent]
)
