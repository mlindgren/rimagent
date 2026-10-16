---
always: false
description: Pull in before designating hunt or tame on any wild animal, when a predator
  or manhunter pack is on the map, or when deciding which animals to keep, pen, train
  or butcher.
name: animals-and-hunting
tags: []
---

# Animals and hunting

## Temperate-forest wildlife
Meat = 140 x body size (butcher spot 70%; kills by damage 66%). Revenge chance triples at close range.

| Animal | Revenge hurt | Revenge tame fail | Size / ~meat | Wildness | Notes |
|---|---|---|---|---|---|
| Squirrel, Hare | 0% | 0% | 0.2 / ~30 | 75% | Low value |
| Turkey | 0% | 0% | 0.6 / 84 | 45% | Easy meat |
| Wild boar | 0% | 0% | 0.85 / 119 | 50% | Herd |
| Deer | 0% | 0% | 1.2 / 168 | 75% | Best early hunt target |
| Alpaca | 0% | 0% | 1.0 / 140 | 25% | 45 wool per shear, pack animal |
| Muffalo | 10% | 0% | 2.4 / 336 | 60% | 120 wool per shear, pack animal |
| Elk | 0% | 0% | 2.1 / 294 | 75% | Herd, milkable |
| Timber wolf | 100% | 30% | 0.85 / 119 | 85% | Predator |
| Cougar | 50% | 30% | 1.0 / 140 | 80% | Predator, 6.7 s stun |
| Grizzly bear | 50% | 30% | 2.15 / 301 | 80% | Predator, 7 s stun, power 200 |
| Raccoon | 0% | 0% | 0.4 / ~56 | 75% | Common mad-animal; combat power 35, bites (bite: 30% infection risk) |

## Hunting rules
1. Ranged only: rw_ui_designate hunt on one animal at a time (rw_map_find kind animal). Hunters shoot from max range, finish the downed animal and haul it. Melee provokes any species.
2. Prefer 0% revenge species (deer, elk, boar, turkey). Never hunt predators with one pawn.
3. Do not hunt while rw_state_threats shows hostiles, in rain or snow (accuracy penalty), or into a muffalo herd. Wounded animals bleed out; do not chase them.
4. Butcher promptly (rw_ui_add_bill on a butcher table); corpses rot in ~2 days when warm.

## Predators
Wolves, cougars and bears hunt anything smaller than themselves, pets and colonists included, when no meat or corpses are nearby. Their first strike stuns, and they keep attacking downed prey.
- On a "predator hunting" alert: rw_ui_draft 2-3 armed pawns and kill it together, or keep everyone indoors and let it eat wildlife. Rescue a downed victim immediately.
- Predators ignore penned animals unless they wander in.

## Manhunter packs and mad animals
Pack points are 40% above a raid's; only fence-passing species are picked. They cannot open doors but bash one they saw you use, and linger 24-54 hours.
- Response: everyone indoors, doors closed, pets restricted inside. Fight only through a held-open door or 1-wide gap with melee blockers. Scaria may rot corpses.
- **A mad animal (single-animal insanity event) charges the NEAREST human — anywhere on the map, not just near the base.** It re-targets if the nearest colonist changes. Correct response:
  1. Restrict EVERY colonist to the Home area (rw_ui_set_policies area) so the animal's nearest human is always inside the walls; it then loses interest. The combat standing order watches it; no drafting needed for a raccoon-scale threat.
  2. **Never send a pawn out to chase it, and never send a pawn far from the base to rescue/tend someone it bit.** A downed pawn 50+ cells from the base is a corpse: it bleeds out in ~2-3h and a 60-150 cell rescue walk takes longer than that. Triage: rescue only if the downed pawn is within ~30 cells of the base or an armed pawn is already nearby; otherwise let them die and mourn (mood cost is smaller than losing the rescuer).
  3. If a colonist must be outside (e.g. a hunter at range), the hunter stays at max range and shoots the animal; the rest stay inside.
  4. Raccoons: combat power ~35, bite wounds (30% infection chance — tend indoors, prompt). One armed pawn ends it in seconds.
- Ep 3 (3 colonists, Rough): a single mad raccoon at day 3, 15h killed the colony. Carol was bitten 60+ cells out, bled to death; the two pawns sent to rescue her were also bitten and downed; all 3 original colonists downed within 4h, Carol dead by 23h. A StrangerInBlack (Danny, Shooting 16, Melee 9) joined at 22h and was the only one left standing. Root cause: pawns were ordered OUT toward the animal/downed pawns instead of being restricted to Home.

## Taming and training
- Tame chance multiplier is 2 x (1 - wildness): dogs/chickens 2x, alpaca 1.5x, muffalo 0.8x, deer 0.5x, bear/cougar 0.4x, wolf 0.3x. Bear, wolf and cougar attack 30% of the time on failure. Handlers need non-meal food matching the diet.
- Tame early: alpaca (wool, caravans, easy), muffalo (wool, pack animal), chickens (population doubles every ~5.7 days, eggs keep 15 days), labrador or husky (0% wildness, advanced trainability).
- Animals above 10.1% wildness lose training and tameness unless penned; keep a handler on Animals (rw_ui_set_work).
- Training: Guard (3 steps) follows a master; Attack (5) can be released on enemies; Rescue (2) and Haul (7) need advanced intelligence (dogs, wolves, cougars, bears). Attack-capable animals add 8% of combat power to raid points.
- Hunger per day: muffalo/elk 0.535, husky 0.5, alpaca 0.275, chicken 0.14; 1 hay or meat = 0.05 nutrition.

## Pens (1.6)
Farm animals (trainability "none": muffalo, alpaca, boar, chicken, turkey, deer, elk) ignore allowed areas and roam off the map unless roped into a pen: a pen marker (30 stuff) enclosed by fences, walls or doors with at least one gate (rw_ui_build Fence / FenceGate / PenMarker). A 20x20 grass pen barely feeds 4 pigs; build big and stock hay for winter. Raiders never target pen animals; cap herds with auto-slaughter.

Sources: Animals; Animal husbandry; Pen; Meat Amount; Wildness; Training; Deer; Elk; Wild boar; Grizzly bear; Timber wolf; Cougar; Alpaca; Muffalo; Hare; Squirrel; Turkey; Chicken; Labrador retriever; Husky; Events; Raccoon