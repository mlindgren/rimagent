"""Wake the planner on any mental break so it can be handled (separate the
insulter, draft others clear of a berserk) instead of discovered from the
alert bar hours later. Reacts to ledger events only; cheap."""


def watch(ctx, events):
    out = []
    for e in events:
        if e.get("kind") in ("mental_break", "incident"):
            low = (e.get("text") or "").lower()
            if e.get("kind") == "mental_break" or "mental break" in low or "break" in low:
                out.append({"type": "alert",
                            "text": "MENTAL BREAK: " + (e.get("text") or "")[:140],
                            "wake": True})
    return out
