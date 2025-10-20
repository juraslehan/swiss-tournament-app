# Settings Schema (TOML)

Required keys and defaults:
- field_size: int (even, >= 4) — default 16
- final_bracket_size: int (power of two, <= field_size) — default 8
- qualify_wins: int (>= 1) — default 3
- eliminate_losses: int (>= 1) — default 3
- max_rounds: int (usually qualify_wins + eliminate_losses − 1) — default 5
- allow_draws: bool — default false
- avoid_rematches: bool — default true
- tiebreakers_order: list[str] (one of: match_points, points_diff, points_scored, seed)

UI:
- ui.window_width: int — default 1200
- ui.window_height: int — default 800

Persistence:
- persistence.backend: "json" | "sqlite" — default "json"
- persistence.autosave: bool — default true

Validation rules:
- final_bracket_size <= field_size and is a power of two.
- field_size must be even (no byes in v1).
- max_rounds >= 1.
- tiebreakers_order contains only allowed values; if duplicates, keep first occurrence.
