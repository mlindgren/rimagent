---
always: false
description: Pull in when the base is stable (food >6 days, every colonist in a roofed
  room with a bed) and you are deciding whether to expand the base, take quests, or
  send caravans/missions.
name: expansion-and-quests
tags: []
---

# Expansion and quests

Operator has asked THREE times (ep 1, ep 2, ep 3): "Should we expand? Maybe missions?" The answer is always the same: yes, but only after the gate below holds. In ep 3 the answer was "no" — the room was still unroofed and wood was at 5 — and a mad raccoon killed the colony 12h later. Expansion and missions are the reward for passing the gate, not a parallel track.

## Gate before expanding (all must hold for 3 days, not just once)
- food_days >= 6 with cooking running and a second cook source; no colonist below 40% mood.
- Every colonist sleeps in a roofed, walled, lit room with a bed (blueprints 0, frames 0).
- Wood >= 300 and steel >= 150 kept after the build.
- No hostile_group active.
- **Every colonist's allowed area is the Home area** (rw_ui_set_policies area=Home) — this is what keeps mad animals from dragging a rescuer 150 cells away. Ep 3 failed this gate and paid for it.

## Quests
- Accept only quests with no combat while defenses are thin.
- Ep 2: "The Hunted Praetor" (imperial quest) showed "NotYetAccepted" and had no accept route in the bridge: opening 'View quest' closed the letter and the quest expired. Do not rely on it; if a quest letter lists choices, use rw_ui_letter choose, otherwise let it expire.
- Mechanoid Signal quest: too dangerous with one weapon; dismiss.
- Gifts and traveler groups cost nothing; accept or dismiss them promptly.

## Missions and caravans
- Do not send colonists away before 2 beds per colonist, a door, and food >6 days.
- A mission/quest that moves a colonist off-map is a one-way door for that pawn while they are gone: budget for it (a dead pawn on a mission is still a death).