from __future__ import annotations

class TAG:
    """
    Represents a basic HTML TAG.

    A TAG can contain text, another TAG, or a list of them.
    """

    def __init__(
        self,
        name: str,
        children: TAG | str | list[TAG | str] = '',
        properties: dict | None = None
    ):
        self.props = self.properties(properties) if properties else ""
        self.text = f"<{name}{self.props}>{self.render(children)}</{name}>"

    def __str__(self) -> str:
        return self.text

    @staticmethod
    def render(children) -> str:
        if isinstance(children, list):
            return ''.join(str(child) for child in children)
        return str(children)

    @staticmethod
    def properties(properties: dict) -> str:
        chain = ""
        for k, v in properties.items():
            chain += f' {k}="{v}"'
        return chain
