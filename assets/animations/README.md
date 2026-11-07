# Animation assets

These original GIF diagrams explain complete conceptual flows with a persistent system map, animated paths, component roles and changing state, an explicit problem and design cost, and a numbered timeline. Each stage lasts exactly 1,000 milliseconds; loops repeat indefinitely. GIFs are embedded directly and visible by default.

The [walkthrough index](../../animations/README.md) includes numbered explanations and full-resolution still sequences. Frames are 1600 × 1000 pixels; motion is rendered at 20 frames/second. Encoders may combine identical motionless frames without changing stage timing.

To regenerate, install Pillow and run `python scripts/render_animations.py`. Story definitions are in `metadata/animation-stories.json`. Use `--only cache-aside` for one diagram. Run `python scripts/validate_animations.py` to decode every frame and verify timing, loops, stills, and visible embeds.
