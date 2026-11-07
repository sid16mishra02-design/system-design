# Animation assets

These original GIF diagrams explain conceptual flows with a persistent system map, an active path, changing component state, and one concise explanation per stage. Each stage lasts exactly 4,000 milliseconds: roughly one second of motion followed by a reading pause. Loops repeat indefinitely. GIFs are embedded directly and visible by default.

The [walkthrough index](../../animations/README.md) includes numbered explanations and full-resolution still sequences. Frames are 1600 × 1000 pixels; motion is rendered at 20 frames/second. Encoders may combine identical motionless frames without changing stage timing.

To regenerate, install Pillow and run `python scripts/render_animations.py`. Story definitions are in `metadata/animation-stories.json`. Use `--only cache-aside` for one diagram. Run `python scripts/validate_animations.py` to decode every frame and verify timing, loops, stills, and visible embeds.
