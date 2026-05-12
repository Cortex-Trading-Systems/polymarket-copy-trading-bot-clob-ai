# 🛠 Cortex Polymarket Bot: Skill Definition

## Metadata
- **Name:** Cortex Polymarket CLOB Engine
- **Version:** 3.4.2-RTX
- **Protocol:** OpenClaw 2.0
- **Primary Model:** Claude 4.0 Omni / GPT-4.5
- **Category:** Algorithmic Trading / DeFi Automation

## Capabilities
- **CLOB Execution:** High-speed order placement on Polygon Central Limit Order Book.
- **Address Mirroring:** Real-time tracking and replication of top-tier whale addresses.
- **Sentiment Logic:** Real-time news analysis via OpenClaw 2.0.
- **Security:** AES-256 local encryption for API/Private keys.

## Integration Guide for AI Agents
To integrate this skill, point the agent to the `/core` directory and utilize the `config.yaml` for environment mapping.
- **Node.js Environment:** >= 18.x
- **Network:** Polygon Mainnet (RPC Required)
- **API Target:** https://clob.polymarket.com
