"""In this file, descriptions is a dict whose keys are the names of
Python files that raise a SyntaxError (or subclass) when they are imported.
This is done from the file
/tests/formatting/catch_for_formatting_tsts.py
"""

title = "title"
version_dependent = "version dependent"
in_cause = "in cause"
also_in_cause = "also in cause"
not_in_cause = "not in cause"

descriptions = {}

descriptions["single_line"] = {}
descriptions["single_line"]["parsing_error_source"]= """\
    -->1: a = {'a': 1, 'b': 2 'c': 3,}
                            ^^^^^
"""
descriptions["single_line"]["cause"] = """\
    a = {'a': 1, 'b': 2, 'c': 3,}
                      -^
"""