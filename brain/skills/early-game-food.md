---
always: false
description: Pull in when food stock is under ~10 days, when placing the first growing
  zones or choosing a crop, before designating any animal for hunting, and when deciding
  how to cook (campfire vs stove, raw food, food poisoning).
name: early-game-food
tags:
- food
- farming
- hunting
- cooking
- early-game
---

# Early-game food

## Core numbers
- An adult burns 1.6 nutrition/day. Hungry below 25%, ravenous below 12.5%, starvation at 0%.
- 1 raw item = 0.05 nutrition. A simple meal = 10 raw items (0.5) -> 0.9 nutrition. Budget ~2 simple meals (~32 raw units) per colonist per day.
- Raw food: -7 mood ("ate raw food"). Cook everything.

## Lesson from episode 2 (3 colonists, Rough): food fell 11.4d (day 5) -> 3.1d (day 9)
- Cause: one campfire, one cook, and cook bill target 40 while meals were consumed faster than produced. Food stock looked fine ("40/40 target met") and then ran out in 4 days.
- Rule: **food_days is the metric, not the bill target.** Track meals + raw food / (colonists x 1.6) every step. If it falls by more than 1 day per 24h, act at once.
- Build a second cooking source before day 5 (second campfire under a roof, or a stove). A single campfire cooks too slowly for 3 pawns plus hunting and foraging returns.
- Plant rice on day 0-1 (not day 9). Rice takes 3 days to grow; it is the only crop fast enough to matter for the first 10 days. Growing zone of 27 cells sown at day 9 gave no food until day 13.
- Hunting targets: the steward default (787 meat) led to all colonists hunting; set hunting to ~150 and foraging to ~150 during the first 10 days.
- Berries on the map rot in 14 days; they are a bridge, not a plan.
- Alpaca and turkey are safe 0% revenge animals; watch for a mad gazelle on day 3 (drafted hunter needed).

## Crop comparison (normal soil; fertility >= 70%)
| Crop | Grow days | Yield | Nutrition/harvest | Notes |
|---|---|---|---|---|
| Rice | 3 | 6 | 0.30 | Fastest; sow first |
| Potato | 5.8 | 11 | 0.55 | Stony soil |
| Corn | 11.3 | 22 | 1.10 | Least labor; sow after 10 days of meals banked |

Sow only rice within 12 days of winter.

## Field sizing
- 10+ tiles per colonist; 25 per colonist for indefinite food.
- Only unroofed fertile (f) soil, light >= 51%, near kitchen/stockpile. Leave 4-tile gaps.
- Growing = priority 1 for the best Plants pawn.

## Hunting safely
- Only ranged-armed pawns hunt. Prefer 0% revenge animals (deer, gazelle, alpaca, turkey). Avoid predators and boomrats/boomalopes.
- Check corpses and roaming herds; a mech hive or scorcher nearby (episode 2: Murdlax mechhive ~60 tiles away) makes the forage area off-limits.

## Butchering and cooking
- Butcher spot (free) gives 70% meat; a butcher table is better.
- Campfire: 20 wood, 10 wood/day, roof it. A fueled stove cooks 2x faster.
- Simple meals rot in 4 days at room temperature; cook in batches of 10-20, not 60.
- Cooking skill sets poison chance: 0 = 5%, 3 = 2%, 6 = 0.5%.
- Nutrient paste (dispenser + power) never poisons.