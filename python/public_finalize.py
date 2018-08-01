# check: https://rules.sonarsource.com/java/RSPEC-1174

import utils

import bblfsh

client = bblfsh.BblfshClient("0.0.0.0:9432")

uast = client.parse("../java/public_finalize.java").uast

methods = utils.get_methods(uast)
for m in methods:
    if m.return_ is None and m.name == "finalize" and 'public' in m.modifiers:
        print("Don't use a public finalize()")