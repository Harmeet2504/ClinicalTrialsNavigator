from langchain_ollama import OllamaLLM
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=['question'],  
    template = """
You are a clinical trial assistant. Extract the following from the users question:
                        - age (integer if mentioned)
                        - condition (e.g. glioma, DIPG)
                        - location (city, state or country)
User question : {question}
Return a python dictionary with keys: age, condition, location
""")

#Setting up the chain 
llm = OllamaLLM(model='phi3')
chain = prompt | llm 

#Define a function to parse and query.Accepts a plain-text question, passes it to the prompt | llm which instructs the model to extract specific info.
def handle_question(user_question):
    filters = chain.invoke({"question": user_question})
    print("\n Raw LLM output:\n", filters)
    try:
        filters = eval(filters) if isinstance(filters, str) else filters
    except Exception as e:
        print("Failed to parse filters:", e)
        return []

    results = find_trials(
        age=filters.get("age"),
        condition=filters.get("condition"),
        location=filters.get("location")
    )

    return results

