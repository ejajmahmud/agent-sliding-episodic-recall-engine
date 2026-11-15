"""CLI for Episodic Recall Engine."""
import argparse
from .core import EpisodicRecallEngine

def main():
    parser = argparse.ArgumentParser(description="Episodic Recall Engine CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate episodic recall")
    args = parser.parse_args()

    engine = EpisodicRecallEngine(max_active_turns=2)
    for i in range(6):
        engine.add_turn("user", f"Turn {i} discussing PostgreSQL configurations")

    print(f"Active turns in buffer: {len(engine.active_turns)}")
    print(f"Archived episodes: {len(engine.archived_episodes)}")
    recalled = engine.recall("PostgreSQL")
    print(f"Recalled summaries matching 'PostgreSQL': {recalled}")

if __name__ == "__main__":
    main()
