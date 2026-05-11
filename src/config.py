import os
from dotenv import load_dotenv

# Load sensitive environment variables from .env file
load_dotenv()

# API Credentials - Retrieved from OS Environment or .env
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "your_anthropic_api_key")
POLYMARKET_API_KEY = os.getenv("POLYMARKET_API_KEY", "your_polymarket_api_key")
POLYGON_RPC_URL = os.getenv("POLYGON_RPC_URL", "https://polygon-rpc.com")

# Strategy Parameters
MIN_CONFIDENCE_SCORE = 0.85  # Threshold for AI-driven trade execution
DEFAULT_BET_AMOUNT = 10.0    # Default position size in USDC
MAX_SLIPPAGE = 0.01          # Maximum allowed price slippage (1%)
AI_MODEL_VERSION = "claude-3-5-sonnet-20240620" # Latest Claude 3.5 Sonnet
