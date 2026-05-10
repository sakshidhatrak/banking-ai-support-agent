from langchain.agents import initialize_agent
from langchain.agents import Tool

from tools.emi_calculator import calculate_emi


emi_tool = Tool(
    name="EMI Calculator",
    func=lambda x: calculate_emi(500000, 8.5, 5),
    description="Calculates EMI"
)