import requests
import urllib.parse
import tempfile

def render_latex(expr):
    url = (
        "https://latex.codecogs.com/png.image?"
        + urllib.parse.quote(r"\dpi{1200}\Huge " + expr)
    )

    response = requests.get(url, timeout=20)

    if response.status_code != 200:
        raise Exception("Failed to render image")

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    tmp.write(response.content)
    tmp.close()

    return tmp.name