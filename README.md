## Configuration

The app reads settings in this order at startup:
1) app/config/settings.local.toml (your personal overrides, ignored by Git)
2) app/config/settings.sample.toml (defaults, tracked in Git)

If a key is missing in local, it falls back to sample. If still missing, the app will use a built-in safe default and warn.

Common keys:
- field_size, final_bracket_size, qualify_wins, eliminate_losses, max_rounds
- tiebreakers_order
- ui.window_width / ui.window_height
- persistence.backend ("json" for v1) and persistence.autosave
