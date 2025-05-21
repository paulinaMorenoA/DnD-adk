# Google ADK imports
import os
from google.adk import Agent
from google.adk.tools import exit_loop

# Prompt for this agent
from .prompt import EDITOR_PROMPT

# =============================
# Agent Definition
# =============================
# def exit_loop(tool_context: ToolContext):
#   """Call this function ONLY when the critique indicates no further changes are needed, signaling the iterative process should end."""
#   print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
#   tool_context.actions.escalate = True
#   # Return empty dict as tools should typically return JSON-serializable output
#   return {}
editor_agent = Agent(
    name="editor_agent",
    model=os.getenv("MODEL_NAME"),
    description="""
    Enhances the overall quality, clarity, consistency, and professional polish of all content in the D&D mini campaign adventure.
    """,
    instruction=EDITOR_PROMPT,
    output_key="editor_feedback",
    tools=[exit_loop],
)
