from langchain_ollama import OllamaLLM
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
import ast
import re
# from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=['question'],  
    template = """
You are a clinical trial assistant. Extract the following from the users question:
                        - age (integer if mentioned)
                        - condition (e.g. glioma, DIPG)
                        - location (city, state or country)
User question : {question}
Return ONLY a valid python dictionary with keys: age, condition, location.
Do not include comments, explanations or extra text.
Example format: {{'age': 7, 'condition': 'glioma', 'location': 'New Jersey'}}
""")

#Setting up the chain 
llm = OllamaLLM(model='phi3')
chain = prompt | llm 

def clean_llm_output(text):
    """
    Cleans LLM output by removing triple backticks, language tags, and inline comments.
    Returns a string that can be safely parsed.
    """
    # Remove triple backticks and language tags like ```python
    text = re.sub(r"```(?:python)?", "", text).strip("` \n")

    # Remove inline comments (e.g., # explanation)
    text = re.sub(r"#.*", "", text)

    # Remove any lines that aren't part of the dictionary
    lines = [line for line in text.splitlines() if "{" in line or "}" in line or ":" in line]
    cleaned = "\n".join(lines).strip()

    return cleaned

#Define a function to parse and query.Accepts a plain-text question, passes it to the prompt | llm which instructs the model to extract specific info.
def handle_question(user_question):
    filters = chain.invoke({"question": user_question})
    print("\n Raw LLM output:\n", filters)
    try:
        if isinstance(filters, str):
            cleaned = clean_llm_output(filters)
            filters = ast.literal_eval(cleaned)

    except Exception as e:
        print("Failed to parse filters:", e)
        return []

    results = find_trials(
        age=filters.get("age"),
        condition=filters.get("condition"),
        location=filters.get("location")
    )

    return results

