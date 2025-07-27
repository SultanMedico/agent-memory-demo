# main.py
from my_agents import triage_agent
from my_agents import triage_agent

from memory import shared_context
from agents.run import Runner

if __name__ == "__main__":
    result = Runner.run_sync(
        triage_agent,
        input="What's 23 + 19?",
        context=shared_context
    )

    print("\nFinal Output:\n", result.output)
