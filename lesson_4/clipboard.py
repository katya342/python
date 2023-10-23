import pyperclip

def get_from_clipboard() -> str:
    return pyperclip.paste()


def add_bullet_point(lines) -> str:
    for key, value in enumerate(lines):
        lines[key] = "* " + value

    return lines
    
