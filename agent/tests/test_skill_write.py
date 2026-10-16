from rimagent import skills


def test_rewrite_keeps_tags_and_always_unless_given(tmp_path, monkeypatch):
    monkeypatch.setattr(skills, "SKILLS", tmp_path)
    skills.write("core doctrine", "how to play", "v1", tags=["doctrine", "priorities"], always=True)

    skills.write("core doctrine", "how to play", "v2")  # a rewrite that omits tags/always
    (s,) = skills.load_all()
    assert (s.body, s.tags, s.always) == ("v2", ["doctrine", "priorities"], True)

    skills.write("core doctrine", "how to play", "v3", tags=[], always=False)  # explicit values still win
    (s,) = skills.load_all()
    assert (s.tags, s.always) == ([], False)


def test_new_skill_defaults(tmp_path, monkeypatch):
    monkeypatch.setattr(skills, "SKILLS", tmp_path)
    skills.write("fresh", "d", "body")
    (s,) = skills.load_all()
    assert (s.tags, s.always) == ([], False)
