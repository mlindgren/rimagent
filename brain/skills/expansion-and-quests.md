---
always: false
description: Pull in when the base is stable (food >6 days, every colonist in a roofed
  room with a bed) and you are deciding whether to expand the base, take quests, or
  send caravans/missions.
name: expansion-and-quests
tags:
- strategy
- expansion
- quests
---

# Expansion and quests

Operator asked (game 1): "Should we expand the base? Maybe try some missions?" Answer: yes, but only after the basics.

## Gate before expanding (all must hold)
- food_days >= 6 with a cooking bill running; no colonist below 40% mood.
- Every colonist has a bed in a roofed, walled room (blueprints 0, frames 0).
- Wood >= 300 and steel >= 150 kept as reserve after the build.
- No hostile_group active.

## What to expand first (in order)
1. Second room / bedroom for mood (individual rooms, +impressiveness).
2. Stone or wood workshop with a research bench; a stove (FueledStove) once Cooking has a bill.
3. Growing zone sized 10+ tiles per colonist (see early-game-food).
4. Defensive door + sandbags/turret only after the first raid is seen.

## Quests (Royalty/Ideology-era rules, verified in wiki "Quests")
- Without Royalty you get 1 quest per ~10 days (up to 19.9 days apart); with Royalty 2 per 12 days.
- Quests are accepted through letters: rw_state_letters -> rw_ui_letter(action=choose, choice="Accept"). Some expire; many have an accept timer and a completion timer.
- Quest size scales with raid points: a bigger colony gets bigger, more rewarding quests. Early colonies should Accept only quests with no combat (refugees, gifts, caravan requests) and Reject ones that spawn raiders when defenses are not ready.
- Beggars and refugee quests are accepted automatically; a refugee joining is free labour, so keep a bed ready.

## Missions and caravans
- Trade with a passing caravan or a visiting trader needs silver and goods to sell; a caravan request is a letter with a timer.
- Do not send colonists away on missions before 2 beds per colonist and a door exist.

Verify with state each step: new colonist (colonist_joined event), letter resolved, wealth change.