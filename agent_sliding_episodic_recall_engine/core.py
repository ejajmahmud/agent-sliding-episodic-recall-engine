"""Core sliding episodic recall engine."""
from typing import List, Dict, Optional

class Episode:
    def __init__(self, episode_id: int, summary: str, keywords: List[str]):
        self.episode_id = episode_id
        self.summary = summary
        self.keywords = [k.lower() for k in keywords]

class EpisodicRecallEngine:
    def __init__(self, max_active_turns: int = 5):
        self.max_active_turns = max_active_turns
        self.active_turns: List[Dict[str, str]] = []
        self.archived_episodes: List[Episode] = []
        self._episode_counter = 0

    def add_turn(self, role: str, content: str):
        self.active_turns.append({"role": role, "content": content})
        if len(self.active_turns) >= self.max_active_turns * 2:
            self._compress_oldest_turns()

    def _compress_oldest_turns(self):
        old_turns = self.active_turns[:self.max_active_turns]
        self.active_turns = self.active_turns[self.max_active_turns:]
        self._episode_counter += 1

        summary = f"Discussion on {len(old_turns)} turns involving {old_turns[0]['content'][:30]}"
        words = [w.strip(".,!?") for t in old_turns for w in t["content"].split() if len(w) > 4]
        self.archived_episodes.append(Episode(self._episode_counter, summary, words[:10]))

    def recall(self, keyword: str) -> List[str]:
        kw = keyword.lower()
        results = []
        for ep in self.archived_episodes:
            if any(kw in k for k in ep.keywords) or kw in ep.summary.lower():
                results.append(ep.summary)
        return results
