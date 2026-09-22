import os
import ollama
from google import genai


OLLAMA_MODEL = "llama3.2:3b"
GEMINI_MODEL = "gemini-2.5-flash"


def generate_answer(question, context):

    prompt = f"""
You are a document question-answering assistant.

Your job is to answer the user's question using ONLY the information
provided in the document context.

DOCUMENT CONTEXT:
{context}

USER QUESTION:
{question}

STRICT RULES:

1. Answer only what the question asks.
2. Use only information explicitly supported by the document context.
3. Do not combine information from different topics unless the document
   explicitly connects them.
4. Do not add general knowledge.
5. Do not guess or infer missing information.
6. If the question asks for a definition, provide only the definition
   relevant to that question.
7. If the question asks for types, categories, steps, or multiple items,
   list all items explicitly supported by the context.
8. If the context does not contain enough information, say exactly:
   "I could not find enough information in the document."
9. Keep the answer concise and directly related to the question.
10. Do not mention the retrieval process, chunks, embeddings, or FAISS.
11. Do not generate page numbers in the answer.
12. Do not include information that belongs to another topic merely
    because it appears somewhere in the context.

ANSWER:
"""

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if gemini_api_key:

        client = genai.Client(
            api_key=gemini_api_key
        )

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]