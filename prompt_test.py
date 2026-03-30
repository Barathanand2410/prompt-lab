from groq import Groq

import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
prompt = "Explain Artificial Intelligence in simple terms for a beginner."

# Temp 0.2
response1 = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

# Temp 0.7
response2 = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

# Temp 1.2
response3 = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
    temperature=1.2
)

print("\n--- Temp 0.2 ---\n", response1.choices[0].message.content)
print("\n--- Temp 0.7 ---\n", response2.choices[0].message.content)
print("\n--- Temp 1.2 ---\n", response3.choices[0].message.content)