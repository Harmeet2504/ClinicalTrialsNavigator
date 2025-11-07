# ClinicalTrialsNavigator
A lightweight GenAI-powered navigator for exploring pediatric clinical trials using natural language. Combines structured filtering with LLM-assisted search to make trial discovery accessible for families and caregivers.

# Installations: Using Ollama, LangChain with a Virtual Environment
1. Install Ollama (System-wide)
Ollama runs as a background service, not inside virtual environment. Install it once on your system:
`curl -fsSL https://ollama.com/install.sh | sh`

2. Pull a Model
After installation, pull a model like Mistral or Phi-3 or llama3:
`ollama pull mistral

3. Activate Your Virtual Environment and then install LangChain and the Ollama integration:
`conda activate env_name
`pip install langchain langchain-community