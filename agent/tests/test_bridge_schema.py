from rimagent.registry import bridge_doc_properties


def test_properties_from_doc_block():
    doc = "{def?: defName, kind?: item|pawn, near?: [x,z]|thingId, radius?: 30, forbidden?: bool, scale?: float} find things"
    props = bridge_doc_properties(doc)
    assert list(props) == ["def", "kind", "near", "radius", "forbidden", "scale"]
    assert props["forbidden"]["type"] == "boolean"
    assert props["radius"]["type"] == "integer"
    assert props["scale"]["type"] == "number"
    assert "type" not in props["kind"] and props["kind"]["description"] == "item|pawn"
    assert "type" not in props["near"]  # nested brackets don't split the property list


def test_alternatives_and_bare_names():
    assert list(bridge_doc_properties("{pawn|thing, amount, def?: Cut|Blunt} apply damage")) == ["pawn", "thing", "amount", "def"]
    assert bridge_doc_properties("{name}") == {"name": {}}
    assert list(bridge_doc_properties("{action, label?, cells?/rect?, plant?: ThingDef} zones")) == ["action", "label", "cells", "rect", "plant"]


def test_docs_without_a_params_block():
    assert bridge_doc_properties("list all rpc methods with docs") == {}
    assert bridge_doc_properties("{unclosed, block") == {}


def test_string_params_are_not_coerced():
    from rimagent.registry import Registry, tool

    @tool()
    def echo(ctx, sha: str, n: int = 0):
        """echo"""
        return {"sha": sha, "n": n}

    r = Registry()
    r.add(echo)
    result, ok = r.execute(None, "echo", {"sha": "5252146", "n": "3"})
    assert ok and result == {"sha": "5252146", "n": 3}
