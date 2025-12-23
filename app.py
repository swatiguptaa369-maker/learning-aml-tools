import gradio as gr
from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_new_tokens=300
)

def aml_bot(user_input):
    prompt = f"""
You are an AML, KYC, Fraud Risk expert working for a global bank.
Answer professionally with regulatory context.

Question: {user_input}
Answer:
"""
    response = chatbot(prompt)[0]["generated_text"]
    return response

gr.Interface(
    fn=aml_bot,
    inputs="text",
    outputs="text",
    title="AML / KYC / Risk Governance Assistant",
    description="Ask about AML typologies, transaction monitoring, RBI, FATF, Wolfsberg."
).launch()
