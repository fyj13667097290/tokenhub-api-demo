"""
TokenHub API Demo
=================
TokenHub (t-hub.cc) - Affordable AI API relay for developers worldwide.
No Chinese phone number required. Pay-as-you-go.
OpenAI-compatible — just change base_url.

Usage:
  1. Get your API token from https://t-hub.cc
  2. pip install openai
  3. python demo.py
"""
import os
from openai import OpenAI

YOUR_TOKEN = os.environ.get("TOKEN_HUB_API_KEY", "YOUR_TOKEN")
client = OpenAI(base_url="https://t-hub.cc/v1", api_key=YOUR_TOKEN)

print("=" * 50)
print("Example 1: DeepSeek V3 — best value for everyday tasks")
print("=" * 50)
r = client.chat.completions.create(
    model="deepseek-v3",
    messages=[{"role":"system","content":"You are helpful."},{"role":"user","content":"Hello! What can you do?"}],
    max_tokens=200)
print(r.choices[0].message.content)
print()

print("=" * 50)
print("Example 2: GLM-4-Flash — fast and affordable")
print("=" * 50)
r = client.chat.completions.create(
    model="glm-4-flash",
    messages=[{"role":"user","content":"Explain API relay in one sentence."}],
    max_tokens=100)
print(r.choices[0].message.content)
print()

print("=" * 50)
print("Example 3: MiniMax — great for creative writing")
print("=" * 50)
r = client.chat.completions.create(
    model="minimax",
    messages=[{"role":"user","content":"Write a haiku about coding."}],
    max_tokens=80)
print(r.choices[0].message.content)
print()

print("=" * 50)
print("Done! Visit https://t-hub.cc to get your API token.")
print("=" * 50)
