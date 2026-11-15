"""Automated test suite for Episodic Recall Engine."""
import unittest
from agent_sliding_episodic_recall_engine.core import EpisodicRecallEngine

class TestEpisodicRecallEngine(unittest.TestCase):
    def test_compression_and_recall(self):
        engine = EpisodicRecallEngine(max_active_turns=2)
        engine.add_turn("user", "Configure redis server on port 6379")
        engine.add_turn("assistant", "Redis server is configured")
        engine.add_turn("user", "Now setup nginx reverse proxy")
        engine.add_turn("assistant", "Nginx is ready")

        # Compression triggered
        self.assertGreater(len(engine.archived_episodes), 0)
        recalled = engine.recall("redis")
        self.assertGreater(len(recalled), 0)
