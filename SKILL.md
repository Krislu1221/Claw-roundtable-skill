---
name: roundtable-v2
description: "Implementation guide for RoundTable v2.0 - a universal multi-agent discussion engine with heterogeneous model routing, MMR intent parsing, and convergence control."
---

# RoundTable v2.0 - Universal Multi-Agent Discussion Engine

## Core Architecture
A robust system for complex task deliberation using multiple Agents with **heterogeneous model routing** (different models for different roles) and **convergence control**.

### Key Features
1.  **Intent Parser (MMR):** Uses Maximal Marginal Relevance to select diverse experts, preventing "echo chambers."
2.  **Adaptive Model Router:**
    -   **Local Mode:** Reads `local_models.json` for explicit model routing (e.g., MiniMax for creative, GLM for logic).
    -   **Public Mode:** Reads `roundtable_config.yaml` for security (no environment scanning).
    -   **Fallback:** Single-model multi-role mode if no config is found.
3.  **Convergence Engine:** Monitors semantic divergence to stop infinite loops and save tokens.

## Module Implementation

### 1. Model Router (`model_router.py`)
Adaptive routing based on capability tags.

```python
class ModelRouter:
    def __init__(self, local_file=None, config_file=None):
        self.mode = "homogeneous"
        self.capability_map = {}
        self.available_models = []
        # Priority: Local JSON (User) > YAML Config (Public)
        if local_file and os.path.exists(local_file):
            self._load_local(local_file)
        elif config_file and os.path.exists(config_file):
            self._load_yaml(config_file)
            
        if len(self.available_models) > 1: self.mode = "heterogeneous"

    def get_model_for_role(self, capability: str) -> str:
        if self.mode == "homogeneous": return None
        # Match capability tags (logic, creative, etc.)
        candidates = [m for m, tags in self.capability_map.items() if capability in tags]
        return candidates[0] if candidates else self.available_models[0]
```

### 2. Intent Parser (`intent_parser.py`)
Matches user input to expert domains while enforcing diversity.

```python
def parse(self, input_text: str, top_k=3):
    # 1. Keyword scoring
    # 2. MMR Selection (Maximize relevance, minimize similarity between selected experts)
    # 3. Return diverse expert list + fuzziness score
    pass
```

### 3. Convergence (`convergence.py`)
Prevents "argument loops."

```python
def check(self, history, current_round, max_rounds):
    if current_round >= max_rounds: return "FORCE_ARBITRATE"
    # Detect repetition or consensus keywords
    if "consensus" in recent_turns: return "STOP"
    return "CONTINUE"
```

## Usage Strategy
1.  **For Local Development:** Use `local_models.json` to define your specific model lineup (e.g., `qwen-logic`, `minimax-creative`).
2.  **For Open Source (ClawHub):** Use `roundtable_config.yaml`. Never scan `os.environ` directly to ensure security compliance.

## File Paths
- `core/model_router.py`
- `core/intent_parser.py`
- `core/prompt_builder.py`
- `core/convergence.py`

---

**版本**: 2.0.0  
**更新日期**: 2026-04-23
