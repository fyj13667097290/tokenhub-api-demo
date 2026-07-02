# TokenHub — AI大模型聚合平台 🚀

> **500+ AI Models. One API Key. Chat + Image + Video.**
>
> 🔗 **[t-hub.cc](https://t-hub.cc)** | 🎮 **[Playground](https://t-hub.cc/playground)**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Models](https://img.shields.io/badge/models-500%2B-purple.svg)](https://t-hub.cc/playground)

---

## What is TokenHub?

TokenHub is an **all-in-one AI aggregation platform** — browse 500+ models, generate text, images, and videos from a single web interface or API.

| Feature | Description |
|---------|-------------|
| 💬 **Chat** | 500+ models in one interface. GPT, Claude, DeepSeek, GLM, Gemini, Mistral, Llama, Qwen... |
| 🎨 **Image Generation** | GPT-Image 2, Gemini Image. Multiple styles: anime, oil painting, cyberpunk, watercolor. |
| 🎬 **Video Generation** | Text-to-video via Minimax API. 5-10 second videos in 2-3 minutes. |
| 🔑 **One Key** | Chat + Image + Video — all from a single API key. |
| 🌍 **No Chinese ID** | No phone verification, no Alipay, no real-name authentication required. |
| 🆓 **Free Models** | 30 free calls/day on GLM-5.1, Gemma 4, Kimi K2.6, Mistral Small, etc. |

---

## Quick Start

### Option A: Web Playground (no code)
Open **[https://t-hub.cc/playground](https://t-hub.cc/playground)** → Enter API Key → Start using 500+ models instantly.

### Option B: API (OpenAI-compatible)

```bash
pip install openai
```

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://t-hub.cc/v1",
    api_key="YOUR_TOKEN_HUB_API_KEY"
)

# Chat
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)

# Image
response = client.images.generate(
    model="gpt-image-2",
    prompt="A cute cat on a sunny beach",
    size="1024x1024"
)
print(response.data[0].url)

# Video (via dedicated endpoint)
import requests
resp = requests.post("https://t-hub.cc/video-api/generate", json={
    "prompt": "A drone flyover of a mountain lake at sunset",
    "duration": 5,
    "api_key": "YOUR_TOKEN_HUB_API_KEY"
})
print(resp.json())  # {job_id: "...", status: "queued"}
```

---

## Pricing

| Plan | Price | Tokens | Free Model Calls/Day | Paid Models |
|------|-------|--------|:---:|:---:|
| **Starter** | $0.10/mo | 1M | 30 | ❌ |
| **Basic** | $7/mo | 15M | 150 | ❌ |
| **Pro** | $26/mo | 70M | 500 | ✅ |
| **Max** | $89/mo | 300M | 1000 | ✅ |

- **Free models**: GLM-5.1, Gemma 4 31B, Gemma 4 26B, Kimi K2.6, MiniMax M2.5/M2.7, Mistral Small, Codestral — 30 calls/day on Starter
- **Payment**: Credit Card, WeChat Pay, Alipay, USDT
- **No hidden fees**: Token consumption = model_price × group_ratio. All pricing transparent at `/pricing-calc`

---

## Architecture

```
Browser (t-hub.cc)
    │
    ├─ /playground    → Static HTML/JS (SPA, bilingual CN/EN)
    ├─ /v1/           → Rate Limiter (:5095) → One API (:3000)
    ├─ /video-api/    → Video Service (:5097) → Minimax/Kling API
    ├─ /pay/ /dashboard/ → Flask App (:5000)
    ├─ /monitor-api/  → Monitor Service (:5096)
    └─ /admin/ /ops/  → Flask Admin (:5099/:5098)
```

| Component | Tech | Port | Purpose |
|-----------|------|:---:|---------|
| **One API** | Go | 3000 | Model routing, token management, quota tracking |
| **Flask App** | Python | 5000 | Payment, dashboard, pricing calculator |
| **Rate Limiter** | Python | 5095 | Free model daily call limits, 429 enforcement |
| **Monitor Service** | Python | 5096 | System metrics, model pricing sync |
| **Video Service** | Python | 5097 | Async video generation with billing integration |
| **Nginx** | Nginx | 80/443 | SSL termination, reverse proxy, rate limiting |
| **Database** | SQLite | — | Lightweight, no external DB dependency |

---

## Key Features

### 🔐 Rate Limiting
Free models are limited per plan tier (30-1000 calls/day). Exceeding the limit returns HTTP 429. Paid models are unlimited (token consumption only).

### 💰 Unified Billing
Text, image, and video all billed through the same token system. Pricing controlled by a centralized profit-margin calculator (`pricing_calc_v2.py`). Change one number, all model ratios + video pricing update automatically.

### 🎬 Video Generation
- Async submission → background polling → auto-refund on failure
- Supports Minimax Video API and Kling API
- Token cost: configurable per second, linked to global profit margin
- Full billing integration: validate key → check quota → deduct → generate → refund on fail

### 🌍 Bilingual
Full Chinese/English toggle. Language preference saved to localStorage.

### 📊 Admin Dashboard
Monitor system health, channel status, model usage statistics, revenue tracking at `/monitor`, `/stats`, `/admin`.

---

## Deployment

**Server**: Vultr VPS (1 vCPU, 1GB RAM, 3GB swap) — $6/month
**OS**: Ubuntu 22.04
**Domain**: t-hub.cc (Cloudflare CDN + SSL)

```bash
# Core services managed by systemd:
systemctl status one-api      # Docker container
systemctl status video-svc    # Video generation (5097)
systemctl status rate-limiter # Rate limiter (5095)
```

---

## FAQ

**Q: Is this legal?**
A: Yes. We are an authorized API relay. You pay us in tokens, we pay upstream providers.

**Q: How is this different from OpenRouter?**
A: TokenHub provides a full web playground (chat + image + video), transparent pricing with profit-margin control, and free model tiers with daily limits.

**Q: Do you store my data?**
A: No. Prompts and completions pass through in transit only. We do not log content.

**Q: Can I use this in production?**
A: Yes. Built for production workloads. Rate limiting, fail2ban, and geo-blocking are configured.

---

## Links

| Page | URL |
|------|-----|
| Homepage | [t-hub.cc](https://t-hub.cc) |
| Playground | [t-hub.cc/playground](https://t-hub.cc/playground) |
| Pricing | [t-hub.cc/pay](https://t-hub.cc/pay) |
| Admin | [t-hub.cc/admin](https://t-hub.cc/admin) |
| Monitor | [t-hub.cc/monitor](https://t-hub.cc/monitor) |

---

MIT © TokenHub

*Keywords: AI API aggregation, ChatGPT API, Claude API, DeepSeek API, AI model playground, video generation API, AI API relay, OpenAI compatible, affordable LLM API*

Updated via Ops Center 2026-06-28 01:57 UTC

Updated via Ops Center 2026-06-29 04:57 UTC

Updated via Ops Center 2026-07-02 03:01 UTC
