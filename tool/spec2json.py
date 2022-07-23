#!/usr/bin/python3
# Converts specifications to JSON.

import os, sys
import marko, marko.ast_renderer
import frontmatter

def convert(id: int) -> dict:
    result = {}

    path1 = f"../spec/tcg/psc{id:03}.md"
    path2 = f"../spec/tcg/psc{id:03}.md"

    if os.path.exists(path1): file = path1
    elif os.path.exists(path2): file = path2
    else: sys.exit("unknown standard")

    markdown = frontmatter.load(file)
    result["metadata"] = markdown.metadata

    parser = marko.Markdown(renderer=marko.ast_renderer.ASTRenderer)
    content = parser(markdown.content)

    result["content"] = content
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit("usage: ./spec2json.py <id>")
    elif sys.stdout.isatty(): sys.exit("redirect output to a file")

    print(convert(int(sys.argv[1])))
    sys.stderr.write("finished\n")
