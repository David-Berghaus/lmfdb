from flask import render_template
from lmfdb.knowledge.knowl import knowldb

def interesting_knowls(category, table, url_for_label, label_col="label", regex=None, **kwds):
    # category might be something like ec.q
    main_cat = category.split(".")[0]
    if category[-1] != ".":
        category += "."
    knowls = knowldb.search(category=main_cat, types=["top", "bottom"], filters=["beta", "reviewed"], projection=["id", "title", "type"])
    # Filter to only those with category correct
    knowls = [k for k in knowls if k["id"].startswith(category)]
    # Get the labels and links
    n = len(category)
    unsorted = {}
    labels = []
    for k in knowls:
        label = k["id"][n:]
        label = label[:label.rfind(".")]
        if regex and not regex.match(label):
            continue
        labels.append(label)
        k["label"] = label
        k["link"] = url_for_label(label)
        unsorted[label] = k
    # Use the table for sorting
    sorted_labels = {label: i for (i, label) in enumerate(table.search({label_col: {"$in": labels}}, label_col))}
    # Some labels might not appear (e.g. if an isogeny class knowl was included)
    # and others might appear multiple times (higher genus families, where the "label" is for a family and isn't unique)
    if sorted_labels:
        M = max(sorted_labels.values()) + 1
    else:
        M = 1
    knowls = [unsorted[label] for label in sorted(unsorted.keys(), key=lambda x: sorted_labels.get(x, M))]
    return render_template("interesting.html", knowls=knowls, **kwds)
