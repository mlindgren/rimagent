---
always: false
description: Pull in when the base is stable (food >6 days, every colonist in a roofed
  room with a bed) and you are deciding whether to expand the base, take quests, or
  send caravans/missions.
name: expansion-and-quests
tags:
- expansion
- quests
- gate
---

# Expansion and quests

Operator asked (ep 1 and ep 2): "Should we expand? Maybe missions?" Answer: yes, but only after the basics hold. Ep 2 never passed the gate (food fell to 3d by day 9, mood 30-38), so no expansion happened.

## Gate before expanding (all must hold for 3 days, not just once)
- food_days >= 6 with cooking running and a second cook source; no colonist below 40% mood.
- Every colonist sleeps in a roofed, walled, lit room with a bed (blueprints 0, frames 0).
- Wood >= 300 and steel >= 150 kept after the build.
- No hostile_group active.

## Quests
- Accept only quests with no combat while defenses are thin.
- Ep 2: "The Hunted Praetor" (imperial quest) showed "NotYetAccepted" and had no accept route in the bridge: opening 'View quest' closed the letter and the quest expired. Do not rely on it; if a quest letter lists choices, use rw_ui_letter choose, otherwise let it expire.
- Mechanoid Signal quest: too dangerous with one weapon; dismiss.
- Gifts and traveler groups cost nothing; accept or dismiss them promptly.

## Missions and caravans
- Do not send colonists away before 2 beds per colonist, a door, and food >6 days.