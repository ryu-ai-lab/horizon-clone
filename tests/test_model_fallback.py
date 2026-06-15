import os
import pytest

# Mock API key environment variable for test
os.environ["GOOGLE_API_KEY"] = "fake_api_key"

from src.ai.client import create_ai_client, ChainedAIClient
from src.models import AIConfig, AIProvider

def test_model_fallback_config_parsing():
    config = AIConfig(
        provider=AIProvider.GEMINI,
        model="gemini-2.5-flash,gemini-2.0-flash,gemini-2.0-flash-lite",
        api_key_env="GOOGLE_API_KEY",
    )
    client = create_ai_client(config)
    assert isinstance(client, ChainedAIClient)
    assert len(client.configs) == 3
    assert client.configs[0].model == "gemini-2.5-flash"
    assert client.configs[1].model == "gemini-2.0-flash"
    assert client.configs[2].model == "gemini-2.0-flash-lite"
    for cfg in client.configs:
        assert cfg.provider == AIProvider.GEMINI
        assert cfg.api_key_env == "GOOGLE_API_KEY"

def test_model_fallback_no_commas():
    config = AIConfig(
        provider=AIProvider.GEMINI,
        model="gemini-2.5-flash",
        api_key_env="GOOGLE_API_KEY",
    )
    client = create_ai_client(config)
    assert not isinstance(client, ChainedAIClient)
