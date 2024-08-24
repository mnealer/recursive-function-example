import html
import json


def find_close_bracket(val, root=False):
    placement = 0
    while placement < len(val) and len(val) > 0:
        if val[placement] in ["[", "{"]:
            placement += find_close_bracket(val[placement+1:])
        elif val[placement] in ["}", "]"]:
            return placement+1
        placement += 1
        if root:
            break
    return placement


def process_json(blob, key):
    blob = html.unescape(blob)
    blob = blob.replace('\\', '')
    if len(blob.split(key)) > 1:
        data = blob.split(key, 1)[1].strip()
        end = find_close_bracket(data, root=True)
        try:
            return json.loads(data[:end])
        except ValueError:
            return data[:end]
    else:
        return None
