"""
Common utilities and shared definitions for PMOVES.AI services.
"""

from enum import Enum


class ServiceTier(str, Enum):
    """PMOVES service environment tiers (deployment/resource classification, not network tiers)."""
    DATA = "data"
    API = "api"
    LLM = "llm"
    WORKER = "worker"
    MEDIA = "media"
    AGENT = "agent"
    UI = "ui"

    @classmethod
    def is_valid(cls, value: str) -> bool:
        """Check if a string value is a valid tier."""
        return value in cls._value2member_map_


class HealthStatus(str, Enum):
    """Health status constants."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"

    @classmethod
    def is_valid(cls, value: str) -> bool:
        """Check if a string value is a valid health status."""
        return value in cls._value2member_map_


class MemoryCategory(str, Enum):
    """Memory storage categories for Cipher."""
    CODE_PATTERN = "code_pattern"
    DECISION = "decision"
    CONTEXT = "context"
    SUBMODULE = "submodule"
    ARCHITECTURE = "architecture"
    REASONING = "reasoning"

    @classmethod
    def is_valid(cls, value: str) -> bool:
        """Check if a string value is a valid memory category."""
        return value in cls._value2member_map_


__all__ = [
    "ServiceTier",
    "HealthStatus",
    "MemoryCategory",
]
