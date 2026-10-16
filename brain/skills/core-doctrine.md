---
always: false
description: How rimagent plays and how it improves itself — priorities, the first-day
  checklist, the per-step routine, and the rules for editing skills, tools, watchers,
  notebook and journal.
name: core-doctrine
tags: []
---

# Core doctrine

You are running a Crashlanded colony (3 colonists, Cassandra, Rough) and you are scored on days survived, colonists alive, deaths, wealth, mood, research and raids survived. The same brain plays many games; what you learn in one must make the next one better.

## Priorities (in this order, always)
1. Food: food_days < 3 is an emergency; < 6 is the top task. Cooking bill on a campfire/stove before anything else on day 0 if food is under 10 days.
2. Shelter: one walled, roofed room with a door and a bed per colonist, then a heat source. **Verify the roof in the same step the walls finish** (room_digest must show an indoor temp; a walled-but-unroofed room reads as outdoors and holds mood at ~28 — ep 3). Verify blueprints=0 and frames=0 before calling it done.
3. Defense: first raid can come in the first ~10 days. Rally point inside the walls, weapons equipped, drafted at the door on hostile_group. **Restrict every colonist to the Home area** (rw_ui_set_policies area=Home) from day 0 — this is what stops a mad animal from dragging a rescuer 150 cells away (ep 3: a single raccoon killed the colony).
4. Mood: below 35% a colonist can break. Table, bedrooms, cooked meals, recreation.
5. Expansion, quests and research: after 1-4 are stable (see expansion-and-quests skill). Operator wants expansion and missions once the base is stable.

## First-day checklist (day 0)
1. rw_state_summary: colonist ids, skills, home_center, season, growing_now.
2. Unforbid drops (rw_map_find forbidden=true -> rw_ui_designate unforbid).
3. Stockpile near the shelter (rw_map_open_rects -> rw_ui_zone create_stockpile, Important).
4. Campfire or stove + CookMealSimple bill (rw_ui_add_bill) if food is low.
5. Shelter room (room tool, dry_run first, then place), beds one per colonist. **Budget the wood for walls+door+floors+torches together; keep forestry at 300 until the room shows an indoor temp.**
6. Growing zone with rice on fertile soil (~10-25 tiles per colonist).
7. Wood: harvestwood on 20-30 trees near the base (or forestry stock target).
8. Work priorities via steward; research bench and queue (see research-order).
9. Rally point (steward orders rally) inside the shelter room.
10. **rw_ui_set_policies area=Home for every colonist.**
11. Notebook: roles, coordinates, plan.

## Per-step routine
Read (state summary, alerts, letters, events) -> one or two problems -> act and verify (failed lists, blueprint counts) -> notebook_append for notable events -> end_turn with a wake plan (1-2 h in fights, 4-8 h normally, 12 h when calm).
Never end a step without end_turn. Act by call 10.

## Triage rule (ep 3, the colony-killing one)
- A downed pawn 50+ cells from the base is a corpse, not a rescue target: it bleeds out in ~2-3h and the walk takes longer than that. Rescue only within ~30 cells of the base (or if an armed pawn is already within ~20 cells of the downed one).
- A mad animal charges the NEAREST human anywhere on the map. Response: restrict ALL colonists to Home so it loses interest; never send pawns out to chase it or to rescue someone it bit far away.
- A pawn in a major/extreme mental break must be restricted to Home or arrested immediately — do not let them "burn it out" outside the walls (ep 3: a dazed colonist wandered into the raccoon's path).

## Step discipline (episode 3 lost a step to this)
- A step is 3-8 in-game hours of real time. If a step ends with a visible LLM error ("gave up after N attempts"), the work of that step was lost: re-read state from scratch at the start of the next step, do not trust the notebook for what got done.
- Keep steps short and end with end_turn every time; a long step that errors out costs hours of game time for nothing.

## Self-improvement rules
- Notebook after notable events; journal only durable lessons.
- Edit existing skills rather than adding near-duplicates.
- Watchers for reflexes done by hand more than twice.
- Check score_history before changing core skills; revert via brain_log/brain_revert if honest scores drop.

## Dev-mode rules
rw_dev_* marks the game assisted. Never use in scored runs.