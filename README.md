# ClinicalTrialsNavigator
A lightweight GenAI-powered navigator for exploring pediatric clinical trials using natural language. Combines structured filtering with LLM-assisted search to make trial discovery accessible for families and caregivers.

# Installations: Using Ollama, LangChain with a Virtual Environment
1. Install Ollama (System-wide)
Ollama runs as a background service, not inside virtual environment. Install it once on your system:
`curl -fsSL https://ollama.com/install.sh | sh`

2. Pull a Model (Mistral or Phi-3 or llama3) depending on your compute resources and use case. I will istall the lightwieght model, Phi-3. It is smaller in size compared to other models with 4.2B parameters and has quantized versions, utilizing 4-8GB RAM.
`ollama pull phi3`

To check model's metadata (model size, architecture, quantization info)
`ollama show phi3`

To test the model
`ollama run phi3`
and type a question "Eg. What is the currency of France?"

3. Activate Your Virtual Environment and then install LangChain and the Ollama integration:
`conda activate env_name`
`pip install langchain langchain-community`