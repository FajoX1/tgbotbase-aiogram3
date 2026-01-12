from typing import List, Tuple

HTML_BASE = 0xE000
FMT_BASE = 0xE100

def freeze_html(text: str) -> Tuple[str, List[str], List[str]]:

    html_tags: List[str] = []
    fmt_tokens: List[str] = []

    out = []
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]

        if ch == "<":
            j = text.find(">", i + 1)
            if j != -1:
                html_tags.append(text[i:j + 1])
                out.append(chr(HTML_BASE + len(html_tags) - 1))
                i = j + 1
                continue
        
        if ch == "{":
            j = text.find("}", i + 1)
            if j != -1:
                fmt_tokens.append(text[i:j + 1])
                out.append(chr(FMT_BASE + len(fmt_tokens) - 1))
                i = j + 1
                continue

        out.append(ch)
        i += 1

    return "".join(out), html_tags, fmt_tokens

def unfreeze_html(
    text: str,
    html_tags: List[str],
    fmt_tokens: List[str],
) -> str:
    
    out = []

    for ch in text:
        code = ord(ch)

        if HTML_BASE <= code < HTML_BASE + len(html_tags):
            out.append(html_tags[code - HTML_BASE])
        elif FMT_BASE <= code < FMT_BASE + len(fmt_tokens):
            out.append(fmt_tokens[code - FMT_BASE])
        else:
            out.append(ch)

    return "".join(out)
