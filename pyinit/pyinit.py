#!/bin/env python3
"""
"""

""" Constants
"""
# synonimns for yes
YES = ["Y", "YES", "YEAH", "YE"]

# the name of the setup file and the mode to open it in
FILENAME = "setup.py"
FILEMODE = "w"

# start and end of the setup.py file
START = """from setuptools import setup
setup(
"""
END = """     )
"""


def quote(to_wrap):
    """wraps a string in single quotes"""
    return "'{0}'".format(to_wrap)

def confirm(settings):
    """show settings and prompt user to confirm them"""
    for s in settings:
        string: str = quote(settings[s]) if isinstance(settings[s], str) else \
          str(settings[s]) if not settings[s][0] == "" else '[]'
        print(s + "=" + string)
    return input("is this okay? > ").upper() in YES

class Default:
    """static class with the default values for the properties and a wrapper to display them"""
    name = ""
    description = ""
    long_description = ""
    version = "1.0.0"
    author = ""
    email = ""
    license_code = "MIT"
    packages = []
    install_requires = []
    scripts = []
    keywords = []
    url = ""

    @classmethod
    def str(cls, string):
        """classmethod to display some text prepended with the word default"""
        if string is None:
            return "default: [null]"
        else:
            return "default: '" + str(string) + "'"

# collect user input
name = input("Name (" + Default.str(Default.name) + ") > ")
version = input("Version ("  + Default.str(Default.version) + ") > ")
description = input("Description (" + Default.str(Default.description) + ") > ")
long_description = input("A more detailed Description (" + Default.str(Default.description) + ") > ")
author = input("Author (" + Default.str(Default.author) + ") > ")
email = input("Author email (" + Default.str(Default.email) + ") > ")
license_code = input("License (" + Default.str(Default.license_code) + ") > ")
packages = list(map(lambda s: s.strip(), input("Packages (comma seperated) ("
                                               + Default.str(Default.packages) + ") > ").split(",")))
install_requires = list(map(lambda s: s.strip(), input("install requires (comma seperated) ("
                                                       + Default.str(Default.install_requires)
                                                       + ") > ").split(",")))
scripts = list(map(lambda s: s.strip(), input("Scripts (comma seperated) ("
                                              + Default.str(Default.scripts) + ") > ").split(",")))
keywords = list(map(lambda s: s.strip(), input("Keywords (comma seperated) ("
                                              + Default.str(Default.keywords) + ") > ").split(",")))
url = input("Url (" + Default.str(Default.url) + ") > ")

# use default settings if the user didn't give an answer
settings = {
    "name": name if name is not "" else Default.name,
    "version": version if version is not "" else Default.version,
    "description": description if description is not "" else Default.description,
    "long_description": long_description if long_description is not "" else \
      Default.long_description,
    "author": author if author is not "" else Default.author,
    "author_email": email if email is not "" else Default.email,
    "license": license_code if license_code is not "" else Default.license_code,
    "url": url if url is not "" else Default.url,
    "packages": packages,
    "install_requires": install_requires,
    "scripts": scripts,
    "keywords": keywords,
}


# quit if the user doesn't like the settings
if not confirm(settings):
    exit(1)

# write the setup.py file
setupfile = open(FILENAME, FILEMODE)

setupfile.write(START)
for s in settings:
    string: str = quote(settings[s]) if isinstance(settings[s], str) else \
      str(settings[s]) if not settings[s][0] == "" else '[]'

    setupfile.write("      " + s + "=" + string + ",\n")
setupfile.write(END)

setupfile.close()
