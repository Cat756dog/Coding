import json
import time
from urllib import request, parse
from urllib.error import HTTPError
from multiprocessing import Pool
from itertools import chain
import networkx as nx


def link_to_title(link):
    return link["title"]


def clean_if_key(page, key):
    if key in page:
        return map(link_to_title, page[key])
    return []


def get_Wiki_links(pageTitle):
    safe_title = parse.quote(pageTitle)

    url = (
        "https://en.wikipedia.org/w/api.php?action=query&"
        "prop=links|linkshere&pllimit=500&lhlimit=500&"
        "titles={}&format=json&formatversion=2"
    ).format(safe_title)

    req = request.Request(
        url,
        headers={
            "User-Agent": "NikoWikiGraphBot/1.0 (contact: example@email.com)"
        }
    )

    try:
        response = request.urlopen(req)
        page = response.read()
    except HTTPError as e:
        print(f"HTTP error on {pageTitle}: {e}")
        return {"title": pageTitle, "in-links": [], "out-links": []}

    j = json.loads(page)
    jpage = j["query"]["pages"][0]

    inbound = clean_if_key(jpage, "linkshere")
    outbound = clean_if_key(jpage, "links")

    # Small delay to reduce rate-limit risk
    time.sleep(0.1)

    return {
        "title": pageTitle,
        "in-links": list(inbound),
        "out-links": list(outbound),
    }


def flatten_network(page):
    return page["in-links"] + page["out-links"]


def page_to_edges(page):
    out_edges = [(page["title"], p) for p in page["out-links"]]
    in_edges = [(p, page["title"]) for p in page["in-links"]]
    return out_edges + in_edges


if __name__ == "__main__":

    # Root article
    root = get_Wiki_links("Parallel_computing")

    # First layer network
    initial_network = flatten_network(root)

    # Limit pool size to avoid API abuse
    with Pool(4) as P:
        all_pages = P.map(get_Wiki_links, initial_network)
        edges = P.map(page_to_edges, all_pages)

    edges = chain.from_iterable(edges)

    # Build directed graph
    G = nx.DiGraph()

    for e in edges:
        G.add_edge(*e)

    # Export graph file
    nx.readwrite.gexf.write_gexf(G, "MyGraph.gexf")

    print("Graph saved as MyGraph.gexf")