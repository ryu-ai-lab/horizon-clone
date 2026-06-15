import asyncio
import re
from datetime import datetime, timezone
from typing import List
import pytest
from src.models import ContentItem, SourceType, Config, AIConfig, SourcesConfig, FilteringConfig
from src.orchestrator import HorizonOrchestrator
from src.ai.enricher import ContentEnricher

def make_item(item_id: str, source_type: SourceType, score: float) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=source_type,
        title=item_id,
        url=f"https://example.com/{item_id}",
        published_at=datetime.now(timezone.utc),
        ai_score=score,
    )

def test_filtering_removes_below_threshold_items_when_above_threshold_items_exist(tmp_path, monkeypatch):
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=[],
        ),
        sources=SourcesConfig(),
        filtering=FilteringConfig(
            ai_score_threshold=7.0,
            max_items=10,
        ),
    )
    
    from types import SimpleNamespace
    storage = SimpleNamespace(
        save_daily_summary=lambda *args, **kwargs: "dummy_path",
        load_subscribers=lambda *args, **kwargs: [],
    )
    orchestrator = HorizonOrchestrator(config, storage)
    
    # Items where reddit and github are below threshold (7.0), but rss is above
    items = [
        make_item("rss-high", SourceType.RSS, 8.5),
        make_item("rss-low", SourceType.RSS, 4.0),
        make_item("reddit-low-1", SourceType.REDDIT, 5.0),
        make_item("reddit-low-2", SourceType.REDDIT, 3.0),
        make_item("github-low", SourceType.GITHUB, 6.0),
    ]
    
    important_items_passed = []
    
    async def fetch_all_sources(since):
        return items
        
    async def analyze_content(input_items):
        return input_items
        
    async def merge_topic_duplicates(input_items):
        return input_items
        
    async def expand_twitter_discussion(input_items):
        return None
        
    async def enrich_important_items(input_items):
        important_items_passed.extend(input_items)
        
    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "_analyze_content", analyze_content)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", merge_topic_duplicates)
    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", expand_twitter_discussion)
    monkeypatch.setattr(orchestrator, "_enrich_important_items", enrich_important_items)
    monkeypatch.chdir(tmp_path)
    
    class DummySummarizer:
        async def generate_summary(self, *args, **kwargs):
            return "dummy summary"
    monkeypatch.setattr("src.orchestrator.DailySummarizer", DummySummarizer)
    
    asyncio.run(orchestrator.run())
    
    kept_ids = [item.id for item in important_items_passed]
    assert "rss-high" in kept_ids
    assert "reddit-low-1" not in kept_ids
    assert "github-low" not in kept_ids
    assert "rss-low" not in kept_ids
    assert len(kept_ids) == 1


def test_fallback_keeps_top_item_per_source_type_when_all_below_threshold(tmp_path, monkeypatch):
    config = Config(
        ai=AIConfig(
            provider="openai",
            model="test",
            api_key_env="TEST_API_KEY",
            languages=[],
        ),
        sources=SourcesConfig(),
        filtering=FilteringConfig(
            ai_score_threshold=7.0,
            max_items=10,
        ),
    )
    
    from types import SimpleNamespace
    storage = SimpleNamespace(
        save_daily_summary=lambda *args, **kwargs: "dummy_path",
        load_subscribers=lambda *args, **kwargs: [],
    )
    orchestrator = HorizonOrchestrator(config, storage)
    
    # All items are below the threshold of 7.0
    items = [
        make_item("rss-low-1", SourceType.RSS, 6.0),
        make_item("rss-low-2", SourceType.RSS, 4.0),
        make_item("reddit-low-1", SourceType.REDDIT, 5.0),
        make_item("reddit-low-2", SourceType.REDDIT, 3.0),
        make_item("github-low", SourceType.GITHUB, 6.5),
    ]
    
    important_items_passed = []
    
    async def fetch_all_sources(since):
        return items
        
    async def analyze_content(input_items):
        return input_items
        
    async def merge_topic_duplicates(input_items):
        return input_items
        
    async def expand_twitter_discussion(input_items):
        return None
        
    async def enrich_important_items(input_items):
        important_items_passed.extend(input_items)
        
    monkeypatch.setattr(orchestrator, "fetch_all_sources", fetch_all_sources)
    monkeypatch.setattr(orchestrator, "_analyze_content", analyze_content)
    monkeypatch.setattr(orchestrator, "merge_topic_duplicates", merge_topic_duplicates)
    monkeypatch.setattr(orchestrator, "_expand_twitter_discussion", expand_twitter_discussion)
    monkeypatch.setattr(orchestrator, "_enrich_important_items", enrich_important_items)
    monkeypatch.chdir(tmp_path)
    
    class DummySummarizer:
        async def generate_summary(self, *args, **kwargs):
            return "dummy summary"
    monkeypatch.setattr("src.orchestrator.DailySummarizer", DummySummarizer)
    
    asyncio.run(orchestrator.run())
    
    kept_ids = [item.id for item in important_items_passed]
    # We expect the top item from each source type as a fallback:
    # - RSS: "rss-low-1" (6.0)
    # - REDDIT: "reddit-low-1" (5.0)
    # - GITHUB: "github-low" (6.5)
    assert "rss-low-1" in kept_ids
    assert "reddit-low-1" in kept_ids
    assert "github-low" in kept_ids
    assert "rss-low-2" not in kept_ids
    assert "reddit-low-2" not in kept_ids
    assert len(kept_ids) == 3


def test_english_item_bypasses_korean_translation():
    class DummyAIClient:
        async def complete(self, system, user):
            return """{
                "title_en": "Enriched English Title",
                "title_ko": "This should be overwritten",
                "whats_new_en": "Enriched English Summary",
                "whats_new_ko": "This should be overwritten",
                "why_it_matters_en": "Enriched English Importance",
                "why_it_matters_ko": "This should be overwritten",
                "key_details_en": "Enriched English Details",
                "key_details_ko": "This should be overwritten",
                "background_en": "Enriched English Background",
                "background_ko": "This should be overwritten",
                "community_discussion_en": "Enriched English Discussion",
                "community_discussion_ko": "This should be overwritten",
                "sources": []
            }"""
            
    client = DummyAIClient()
    enricher = ContentEnricher(client)
    
    # English item (no CJK)
    english_item = make_item("english-item", SourceType.RSS, 8.0)
    english_item.title = "New Rust compiler release"
    english_item.content = "Rust compiler version 1.80 has been released with new features."
    
    asyncio.run(enricher._enrich_item(english_item))
    
    # Verify ko fields copy the en fields instead of containing Korean
    assert english_item.metadata["title_ko"] == "Enriched English Title"
    assert "Enriched English Summary" in english_item.metadata["detailed_summary_ko"]
    assert english_item.metadata["background_ko"] == "Enriched English Background"
    assert english_item.metadata["community_discussion_ko"] == "Enriched English Discussion"

    # Non-English item (contains CJK/Korean)
    class KoreanAIClient:
        async def complete(self, system, user):
            return """{
                "title_en": "Enriched English Title",
                "title_ko": "번역된 한국어 제목",
                "whats_new_en": "Enriched English Summary",
                "whats_new_ko": "새로운 기능 요약",
                "why_it_matters_en": "Enriched English Importance",
                "why_it_matters_ko": "중요한 이유",
                "key_details_en": "Enriched English Details",
                "key_details_ko": "세부 사항",
                "background_en": "Enriched English Background",
                "background_ko": "배경 지식",
                "community_discussion_en": "Enriched English Discussion",
                "community_discussion_ko": "커뮤니티 토론",
                "sources": []
            }"""
            
    client_ko = KoreanAIClient()
    enricher_ko = ContentEnricher(client_ko)
    
    korean_item = make_item("korean-item", SourceType.RSS, 8.0)
    korean_item.title = "새로운 러스트 컴파일러 출시"
    korean_item.content = "러스트 컴파일러 1.80 버전이 새로운 기능과 함께 출시되었습니다."
    
    asyncio.run(enricher_ko._enrich_item(korean_item))
    
    # Verify ko fields contain the translated Korean text
    assert korean_item.metadata["title_ko"] == "번역된 한국어 제목"
    assert "새로운 기능 요약" in korean_item.metadata["detailed_summary_ko"]
    assert korean_item.metadata["background_ko"] == "배경 지식"
    assert korean_item.metadata["community_discussion_ko"] == "커뮤니티 토론"
