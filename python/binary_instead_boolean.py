# check: https://rules.sonarsource.com/java/RSPEC-2178
import utils

import bblfsh

client = bblfsh.BblfshClient("0.0.0.0:9432")
uast = client.parse("../java/binary_instead_boolean.java").uast
ifs = bblfsh.filter(uast, "//*[@roleBitwise and @roleCondition and @roleIf]")

if len(list(ifs)) > 0:
    print("Potential bug: bitwise operator inside if condition")
