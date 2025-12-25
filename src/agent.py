import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Load .env locally (ignored on Streamlit Cloud)
load_dotenv()

# ChatGroq automatically reads GROQ_API_KEY from environment
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.5
)


class WaterIntakeAgent:
    def analyze_intake(self, intake_ml: int) -> str:
        prompt = f"""
You are a hydration assistant.
The user has consumed {intake_ml} ml of water today.

Evaluate their hydration status and clearly state whether this intake is sufficient.
If it is insufficient, explain why and suggest how much more water they should drink.
Keep the response concise, practical, and easy to understand.
"""
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content


if __name__ == "__main__":
    agent = WaterIntakeAgent()
    print(agent.analyze_intake(1500))





















# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage

# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# llm = ChatGroq(
#     api_key=GROQ_API_KEY,
#     model_name="llama-3.1-8b-instant",
#     temperature=0.5
# )


# class WaterIntakeAgent:
#     def analyze_intake(self, intake_ml: int) -> str:
#         prompt = f"""
# You are a hydration assistant.
# The user has consumed {intake_ml} ml of water today.

# Evaluate their hydration status and clearly state whether this intake is sufficient.
# If it is insufficient, explain why and suggest how much more water they should drink.
# Keep the response concise, practical, and easy to understand.
# """
#         response = llm.invoke([HumanMessage(content=prompt)])
#         return response.content


# if __name__ == "__main__":
#     agent = WaterIntakeAgent()
#     print(agent.analyze_intake(1500))



















# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage


# # Load environment variables
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # Initialize Groq LLM
# llm = ChatGroq(
#     api_key=GROQ_API_KEY,
#     model_name="llama-3.1-8b-instant",
#     temperature=0.5
# )


# class WaterIntakeAgent:
#     def __init__(self):
#         self.history = []

#     def analyze_intake(self, intake_ml):
#         prompt = f"""
# You are a hydration assistant.
# The user has consumed {intake_ml} ml of water today.

# Evaluate their hydration status and clearly state whether this intake is sufficient.
# If it is insufficient, explain why and suggest how much more water they should drink.
# Keep the response concise, practical, and easy to understand.
# """

#         response = llm.invoke([
#             HumanMessage(content=prompt)
#         ])

#         self.history.append({
#             "intake_ml": intake_ml,
#             "response": response.content
#         })

#         return response.content


# # ✅ THIS MUST BE OUTSIDE THE CLASS
# if __name__ == "__main__":
#     agent = WaterIntakeAgent()
#     intake = 1500
#     feedback = agent.analyze_intake(intake)
#     print(f"Hydration Analysis: {feedback}")
