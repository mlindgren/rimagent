---
always: false
description: Pull in when a colonist's mood is below ~40%, a mental break alert fires,
  or when planning day 1-5 furniture (tables, beds, recreation) to prevent breaks.
name: mood-and-mental-breaks
tags: []
---

# Mood and mental breaks

## Thresholds
- Base mood by difficulty: Rough/Strive 32; Losing is Fun 22. Thoughts add to it.
- Mental break threshold 35% (minor), major 20%, extreme 5%. Read the per-pawn value.

## Early debuffs (exact values)
| Thought | Mood | Fix |
|---|---|---|
| Ate without table | -3 | Table + stool, built before the first meal |
| Ate raw food | -7 | Cook |
| Slept outside | -4 | Enclosed, roofed room |
| Slept on ground | -4 | Bed |
| Slept in cold/heat | -4 | Heater/cooler, torch or passive cooler |
| Darkness | penalty | Torch lamp inside every bedroom |
| Barracks vs bedroom | -4 to -5 | One bedroom per pawn, not a shared barracks |
| Impressiveness low | -3 to -6 | Decor, clean floors, bigger room |
| Rotting corpse | -6 | Bury corpses the same day (grave/dumping zone) |

**"Slept outside/cold" is a roof problem, not a wall problem.** A fully walled room with no roof reads as outdoors for every pawn (ep 3: 3 days of this held mood at 28 and produced a daze on day 3). Check `room_digest` for an indoor temp the same step the walls finish; fix the enclosure (door still a frame, gap) or designate the roof area manually. See base-building for the wood budget.

## Recreation
- Two types under 15,000 wealth, three after. Horseshoes pin and a chess table (needs Complex furniture) are the early ones.

## Responding to a break
- Minor: wait it out; keep others away from an insulter.
- Major/extreme: draft others clear of the pawn; berserkers only stopped by blunt melee.
- **A major break (e.g. wandering in psychosis) is a death sentence for the pawn if they wander out of the Home area** — ep 3: Villegas hit a major daze at mood 17 and wandered 15 cells from base straight into a mad raccoon's path and got bitten. If a pawn is in a major/extreme break, restrict them to the Home area (rw_ui_set_policies area=Home) or arrest them immediately; do not "let it burn out" while they are outside the walls.
- Arrest interrupts most breaks but may trigger berserk.
- Thoughts persist after a break: fix the largest negatives shown by morale_report.

## Episode 3 (3 colonists, Rough, 2-day cap): a minor break on day 1
- Carol hit an insulting spree (minor break) at mood ~28 on day 1, 5h — the colony's only break all game. Mood fell 51 -> 46 -> 39 over two days.
- Minor breaks last ~4 in-game days (major 0.8d, extreme 0.5d), so a minor break at mood 28 on day 1 of a 2-day game costs most of the game's mood score.
- Rule: if a colonist is below ~40% mood within the first 24h, fix the top 2-3 negatives from morale_report immediately (table+stool, lamp, second recreation type, burying corpses) rather than waiting — a break then lasts days, not hours.
- Insulting spree: the insulter needs 2+ other colonists within reach; separating the group (send one pawn away, or arrest the insulter to end the break early) stops the mood bleed.
- The mental_break watcher wakes you on any break; act on it the same step.