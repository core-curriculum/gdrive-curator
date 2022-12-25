"""
variables common through projects
"""
import os
from os import path

langs = ("ja", "en")


class dirs:
    def __init__(self, lang: str = "ja"):
        self.lang = lang
        self.base = path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.input = _input_dir(self.base, lang)
        self.output = _output_dir(self.base, lang)


class _input_dir:
    def __init__(self, base: str, lang: str = "ja"):
        self.base = path.join(base, "input")
        self.sheets = _input_sheets_dir(self.base, lang)
        self.docs = _input_docs_dir(self.base, lang)


class _input_docs_dir:
    def __init__(self, _base: str, lang: str = "ja"):
        self.base = os.path.join(_base, "docs")
        self.outcomes = os.path.join(self.base, "outcomes")
        self.docs = os.path.join(self.base, "documents")


class _input_sheets_dir:
    def __init__(self, _base: str, lang: str = "ja"):
        self.base = os.path.join(_base, "sheets")
        self.outcomes = os.path.join(self.base, "outcomes")
        self.general = os.path.join(self.base, "general")


class _output_dir:
    def __init__(self, base: str, lang: str = "ja"):
        self.base = path.join(base, "output", "2022", lang)
        self.outcomes = path.join(self.base, "outcomes")
        self.tables = path.join(self.base, "tables")
        self.docs = path.join(self.base, "documents")
        self.docs_contents = path.join(self.docs, "contents")
        self.dir_2016 = path.join(base, "output", "2016")
        self.relations_2016 = path.join(
            base, "output", "relations", "y2016_to_y2022")
