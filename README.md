# TokenHub API Demo

> **The 5 best Chinese AI models, one API key. No Chinese phone required.**
>
> [t-hub.cc](https://t-hub.cc) | [Product Hunt](https://www.producthunt.com/products/tokenhub?launch=tokenhub) | [Dev.to](https://dev.to/tokenhub)

## What is TokenHub?



TokenHub is a **400-model AI API relay (DeepSeek, Llama 4, Mistral, Qwen, GLM)** and **multi-model AI API relay** that gives you:



- ✅ **No phone verification** — bypass the Chinese phone number requirement

- ✅ **Pay-as-you-go** — only pay for what you use, no subscription

- ✅ **OpenAI-compatible API** — drop-in replacement, just change `base_url`

- ✅ **Multiple models** — DeepSeek V3, GLM-4-Flash, MiniMax, and more coming



## Available Models



| Model | Type | Best For | Pricing |

|-------|------|----------|---------|

| `deepseek-v3` | Chat | General purpose, coding, reasoning | $0.27/M tokens |

| `glm-4-flash` | Chat | Fast responses, lightweight tasks | $0.01/M tokens |

| `minimax` | Chat | Creative writing, storytelling | $0.20/M tokens |



> More models coming soon! (GPT-4o, Claude, Gemini — join the waitlist)



## Quick Start (30 seconds)



### 1. Get your API Token

Visit **[t-hub.cc](https://t-hub.cc)** → Register → Create Token → Copy it.



### 2. Install

```bash

pip install openai

```



### 3. Use in your own code

```python

from openai import OpenAI



client = OpenAI(

    base_url="https://t-hub.cc/v1",

    api_key="YOUR_TOKEN_HUB_API_KEY"

)



response = client.chat.completions.create(

    model="deepseek-v3",

    messages=[{"role": "user", "content": "Hello, world!"}]

)

print(response.choices[0].message.content)

```



**That's it!** Your existing OpenAI SDK code works with TokenHub — just change `base_url` and `api_key`.



## Why TokenHub?



### The Problem

Many powerful AI APIs (DeepSeek, GLM, MiniMax) require a **Chinese phone number** to register. Developers outside China are locked out.



### Our Solution

TokenHub acts as a **relay** — we handle the upstream registration, you get a clean OpenAI-compatible API. No phone, no hassle, no minimum commitment.



## Features



- 🔌 **OpenAI SDK compatible** — works with any OpenAI SDK client

- 📊 **Usage dashboard** — track your token consumption in real-time

- 🔑 **Multiple API tokens** — create separate tokens for different projects

- 🛡️ **Rate limiting** — built-in protection against abuse



## FAQ



**Q: Is this legal?**

A: Yes. We are an authorized API relay service. You pay us, we pay the upstream providers.



**Q: How is this different from ?**

A:  charges a markup on every request. We offer **wholesale pricing** — you pay close to the original API cost.



**Q: What about data privacy?**

A: We do NOT store your prompts or completions. Data passes through our servers in transit only.



**Q: Can I use this in production?**

A: Absolutely. TokenHub is built for production workloads with 99.9% uptime SLA.




## Pricing (June 2026 - 54% OFF!)

| Plan | Price | Tokens | Per Million |
|------|-------|--------|-------------|
| Starter | /usr/bin/bash.69 | 1M | /usr/bin/bash.69/M |
| Basic | .00 | 15M | /usr/bin/bash.47/M |
| Pro | 6.00 | 70M | /usr/bin/bash.37/M |
| Max | 9.00 | 300M | /usr/bin/bash.26/M |

Credit card via LemonSqueezy. PayPal + USDT supported.
## Community



- 🌐 **Website**: [t-hub.cc](https://t-hub.cc)

- 📝 **Blog**: [dev.to/tokenhub](https://dev.to/tokenhub)

- 🐦 **Twitter**: [@TokenHubAPI](https://twitter.com/TokenHubAPI) *(coming soon)*



## License



MIT © TokenHub



---



⭐ **Star this repo** if you find it useful! It helps others discover affordable AI APIs.



*

---

## Become an Agent

Earn commissions by referring customers to TokenHub. Zero cost to join. No inventory. No customer support needed.

- 10% commission on every order
- Real-time tracking via dashboard
- Monthly payout via PayPal/WeChat/Alipay

**Contact:** 547178675@qq.com

---

**Keywords:** DeepSeek API, Qwen API, GLM API, Llama 4 API, Mistral API, AI API relay, cheap AI API, OpenAI alternative, no VPN AI

Updated via Ops Center 2026-06-08 02:06 UTC

Updated via Ops Center 2026-06-09 07:12 UTC

Updated via Ops Center 2026-06-11 01:10 UTC

Updated via Ops Center 2026-06-12 04:57 UTC

Updated via Ops Center 2026-06-13 05:49 UTC

Updated via Ops Center 2026-06-13 15:46 UTC

Updated via Ops Center 2026-06-14 05:41 UTC

Updated via Ops Center 2026-06-15 04:44 UTC
