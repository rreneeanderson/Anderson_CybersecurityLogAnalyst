from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemma-4-31b-it",
    temperature=0.2
)

def analyze_logs(logs):

    prompt = f"""
You are a cybersecurity log analysis assistant.

Analyze the security logs below and create a clear risk report.

Your response must include:

1. Risk Level: LOW, MEDIUM, or HIGH

2. Suspicious Activity:
List any suspicious patterns you notice.

3. Explanation:
Explain why the activity may be suspicious in simple language.

4. Recommended Investigation:
List practical steps a cybersecurity analyst should take next.

Do not invent information that is not in the logs.

Security Logs:
{logs}
"""

    response = llm.invoke(prompt)

    return response.text