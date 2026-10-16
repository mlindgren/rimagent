---
always: false
description: Pull in when a colonist's mood is below ~40%, a mental break alert fires,
  or when planning day 1-5 furniture (tables, beds, recreation) to prevent breaks.
name: mood-and-mental-breaks
tags:
- mood
- mental-break
- recreation
- rooms
- early-game
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

## Lesson from episode 2 (3 colonists)
- Moods fell from ~60 to 30-38 by day 9 because of: one shared barracks (21 cells, impressiveness -18 to -26), darkness (lamp placed only on day 9), barracks at 33-38 C until passive coolers arrived day 9, hunger, and a rotting corpse left unburied for 2+ days.
- Two colonists near break (Pock 30, Tauno 32) were slept outside or dark for days before anyone acted.
- Required order for a 3-colonist start: (1) one bedroom per colonist or at least a 2-bed room with lamp, (2) table+stool, (3) passive cooler or heater for any room over 30 C, (4) bury every corpse immediately, (5) decor for impressiveness.

## Recreation
- Two types under 15,000 wealth, three after. Horseshoes pin and a chess table (needs Complex furniture) are the early ones.

## Responding to a break
- Minor: wait it out; keep others away from an insulter.
- Major/extreme: draft others clear of the pawn; berserkers only stopped by blunt melee.
- Arrest interrupts most breaks but may trigger berserk.
- Thoughts persist after a break: fix the largest negatives shown by morale_report.