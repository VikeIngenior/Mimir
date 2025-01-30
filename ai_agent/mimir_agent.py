from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

default_model = ChatOpenAI(model="gpt-4")

class MyAIAgent:
    """
    MyAIAgent is a simple AI agent that interacts with a language model to process user queries.

    Attributes:
        model (object): The default AI model used for generating responses.

    Methods:
        __init__(): Initializes the AI agent with a default model.
        get_response(query: str) -> str: Takes a user query as input, invokes the AI model to generate a response,
                                         processes the output, and returns it as a string.
    """

    def __init__(self):
        """
        Initializes the MyAIAgent class by setting up the default AI model.
        """

        self.model = default_model