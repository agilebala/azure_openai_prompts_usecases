import sys
import importlib

# List your use cases here, mapping a simple name to the module path.
USE_CASES = {
    "customer_support": "prompts.customer_support",
    "document_summarization": "prompts.document_summarization",
    "code_migration": "prompts.code_migration",
    "product_recommendation": "prompts.product_recommendation",
    "fraud_explanation": "prompts.fraud_explanation",
    "crisis_translation": "prompts.crisis_translation",
    "contract_extraction": "prompts.contract_extraction",
    "knowledge_base_qa": "prompts.knowledge_base_qa",
    "action_item_generator": "prompts.action_item_generator",
    "sentiment_analysis": "prompts.sentiment_analysis",
    "email_drafting": "prompts.email_drafting",
    "text_simplification": "prompts.text_simplification",
    "policy_simulation": "prompts.policy_simulation",
    "it_ticket_resolution": "prompts.it_ticket_resolution",
    "marketing_content": "prompts.marketing_content",
    "compliance_check": "prompts.compliance_check",
    "predictive_maintenance": "prompts.predictive_maintenance",
    "semantic_search": "prompts.semantic_search",
    "onboarding_bot": "prompts.onboarding_bot",
    "report_generation": "prompts.report_generation",
}

def list_use_cases():
    print("\nAvailable Use Cases:")
    for i, key in enumerate(USE_CASES.keys(), 1):
        print(f"{i}. {key}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <use_case>")
        list_use_cases()
        sys.exit(1)

    use_case = sys.argv[1]
    if use_case not in USE_CASES:
        print(f"Unknown use case: {use_case}")
        list_use_cases()
        sys.exit(1)

    try:
        module = importlib.import_module(USE_CASES[use_case])
        module.run()
    except Exception as e:
        print(f"Error running use case '{use_case}': {e}")

if __name__ == "__main__":
    main()
