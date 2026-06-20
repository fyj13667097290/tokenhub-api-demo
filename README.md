# TokenHub - AI API Relay

> One API key. 518 AI models. No Chinese phone. No VPN.

[![Status](https://img.shields.io/badge/status-live-brightgreen)]()
[![Models](https://img.shields.io/badge/models-518-blue)]()
[![API](https://img.shields.io/badge/API-OpenAI%20compatible-orange)]()

## What is TokenHub?

TokenHub is an AI API aggregation platform that gives you access to **518 models** from 30+ providers through a single OpenAI-compatible endpoint.

Built after getting scammed twice buying API keys on Telegram. Running on $12/month VPS servers. Solo developer.

## Available Models (518 total)

### GPT & Claude (via ofox)
- GPT-5.5, GPT-5.4, GPT-4o, GPT-4.1, GPT-5
- Claude Opus 4.8, Claude Sonnet 4.6, Claude Haiku 4.5

### DeepSeek (Direct)
- deepseek-chat, deepseek-v4-pro, deepseek-v4-flash, deepseek-r1

### Chinese Models (via ofox)
- Qwen 3.7 Max, Qwen 3.7 Plus, Qwen Turbo, Qwen Max
- GLM-5.1, GLM-5, GLM-4.7, MiniMax M2.7

### OpenRouter (340+ models)
- Llama 4 Maverick, Llama 4 Scout
- Mistral Large, Codestral
- NVIDIA Nemotron 550B
- Google Gemma 4 31B, Gemini 2.5 Flash
- Perplexity Sonar Pro
- Cohere Command R+, AI21 Jamba, xAI Grok
- And 300+ more...

### Free Models (9 models, zero cost)
- Gemma 4 31B, Gemini 2.5 Flash Lite
- Kimi K2.6, GLM-5.1, MiniMax M2.5/M2.7
- Mistral Small, Codestral

## Pricing

| Plan | Price | Tokens | Per Million |
|------|-------|--------|-------------|
| Starter | $0.69 | 1M | $0.69/M |
| Basic | $7.00 | 15M | $0.47/M |
| Pro | $26.00 | 70M | $0.37/M |
| Max | $89.00 | 300M | $0.30/M |

Transparent pricing: cost + 30% margin. No hidden multipliers.

WeChat, Alipay, USDT, and credit cards accepted.

## Quick Start

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://t-hub.cc/v1",
    api_key="your-api-key"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

```bash
curl https://t-hub.cc/v1/chat/completions   -H "Authorization: Bearer YOUR_API_KEY"   -H "Content-Type: application/json"   -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"Hi"}]}'
```

## Architecture

```
Client (OpenAI SDK)
    |
    v
Cloudflare (DDoS protection + CDN)
    |
    v
Nginx (HTTPS + rate limiting)
    |
    v
One API (Go gateway, port 3000)
    |
    +--> ofox (GPT, Claude, Qwen, GLM, MiniMax)
    +--> DeepSeek Direct (deepseek models)
    +--> OpenRouter (340+ models, filtered)
    |
    v
Flask Payment System
    +--> LemonSqueezy (credit cards)
    +--> WeChat Pay / Alipay
    +--> USDT (TRC20)
```

## Features

- OpenAI SDK compatible - drop-in replacement
- Model ratio system for fair pricing
- Real-time usage statistics dashboard
- 7-day free trial for new users
- Token management with per-user quota
- Channel monitoring with auto-refresh balances

## Links

- Website: [t-hub.cc](https://t-hub.cc)
- Dashboard: [t-hub.cc/dashboard](https://t-hub.cc/dashboard)
- Stats: [t-hub.cc/stats](https://t-hub.cc/stats)
- Order Lookup: [t-hub.cc/pay/order](https://t-hub.cc/pay/order)

## Status

- 2 paying customers (week 3)
- 518 models online
- $12/month infrastructure cost
- Built and maintained by one person

---

**Found a bug? Want a model added?** Open an issue or reach out on [Twitter/X @TokenHub](https://x.com/TokenHub).
