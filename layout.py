import re
import json
from pprint import pprint


def main():
    obj = json.loads(open('keyboard-layout (1).json', 'r').read())
    keys = []
    keymap = {}
    cols, rows = set(), set()
    cnt = 1
    for l in obj:
        for thing in l:
            key = keyify(thing, cnt)
            if key is not None:
                cnt += 1
                keys.append(key)
                r, c = key["row"], key["col"]
                cols.add(c)
                rows.add(r)
                keymap.setdefault(r, {})[c] = key["name"]

    print "            ",
    for c in sorted(list(cols)):
        print "%12s" % c,
    print
    for r in sorted(list(rows)):
        print "%12s" % r,
        for c in sorted(list(cols)):
            if c in keymap[r]:
                print "%12s" % keymap[r][c],
            else:
                print "            ",
        print


def keyify(thing, cnt):
    if not isinstance(thing, basestring):
        return None
    match = re.search("(\d?\d\/\d\d?)", thing)
    row, _, col = match.group(0).partition("/")
    if "\n" not in thing:
        print "No \ -- %s" % thing
        return None
    key = {
        "name": thing[:thing.index("\n")],
        "row": int(row),
        "col": int(col),
    }
    print cnt, "name", key["name"], "endname"
    return key

if __name__ == "__main__":
    main()
