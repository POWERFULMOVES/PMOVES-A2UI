# PMOVES.AI Tier Environment: UI
# Docker env_file format — use with docker compose env_file directive

# ============================================================================
# UI Tier Configuration
# ============================================================================

TIER=ui

# Build configuration
NODE_ENV=${NODE_ENV:-production}
NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL:-http://localhost:8080}

# Feature flags
FEATURE_DARK_MODE=${FEATURE_DARK_MODE:-true}
FEATURE_METRICS=${FEATURE_METRICS:-true}

# API endpoints (for client-side calls)
NEXT_PUBLIC_AGENT_ZERO_URL=${NEXT_PUBLIC_AGENT_ZERO_URL:-http://agent-zero:8080}
NEXT_PUBLIC_HIRAG_URL=${NEXT_PUBLIC_HIRAG_URL:-http://hi-rag-gateway-v2:8086}
