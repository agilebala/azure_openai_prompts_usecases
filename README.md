# Azure OpenAI Prompt Engineering Use Cases

A Python project to test, validate, and demonstrate prompt engineering scenarios using the latest Azure OpenAI models (including GPT-4o).

---

## 🚀 Features

- 20+ prompt engineering use cases
- Supports latest Azure OpenAI API (`2025-04-01-preview`)
- API key and Azure AD authentication (via Managed Identity or Service Principal)
- Cost controls (`max_tokens`, `temperature`) via `.env`
- Modular, extensible, and easy to maintain

---

## 📁 Project Structure
azure_openai_prompts_usecases/
│
├── .env
├── requirements.txt
├── README.md
├── main.py
├── utils/
│ └── openai_client.py
└── prompts/
├── init.py
├── customer_support.py
├── document_summarization.py
├── code_migration.py
├── product_recommendation.py
├── fraud_explanation.py
├── crisis_translation.py
├── contract_extraction.py
├── knowledge_base_qa.py
├── action_item_generator.py
├── sentiment_analysis.py
├── email_drafting.py
├── text_simplification.py
├── policy_simulation.py
├── it_ticket_resolution.py
├── marketing_content.py
├── compliance_check.py
├── predictive_maintenance.py
├── semantic_search.py
├── onboarding_bot.py
└── report_generation.py


---

## ⚙️ Setup

### 1. Clone the Repository


### 2. Create a Virtual Environment

**Using conda:**
conda create -n openai_env python=3.10
conda activate openai_env

### 3. Install Dependencies

AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_DEPLOYMENT
AZURE_OPENAI_API_VERSION
AZURE_OPENAI_MAX_TOKENS=256
AZURE_OPENAI_TEMPERATURE=0.2


- For Azure AD authentication, leave `AZURE_OPENAI_API_KEY` empty and ensure you have the right Azure identity context.

---

## 🧑‍💻 Usage

List available use cases:

python main.py

Run a specific use case (e.g., customer support chatbot):


You will be prompted for any required input (e.g., paste a transcript, enter a question).

---

## 🏗️ Adding New Use Cases

1. Create a new Python file in the `prompts/` directory (e.g., `my_use_case.py`).
2. Implement a `run()` function following the existing pattern.
3. Add your use case to the `USE_CASES` dictionary in `main.py`.

---

## ✅ Testing

- Each use case can be tested independently via the main runner.
- For automated testing, use `pytest` and add test scripts as needed.





