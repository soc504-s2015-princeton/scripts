#!/usr/bin/env python

#
# Usage options:
# ./stripanswers.py input.Rmd > output.Rmd
# cat input.Rmd | ./stripanswers.py > output.Rmd
#

import fileinput, sys, re
inblock = False
for line in fileinput.input():
    if inblock and line.strip() == "```":
        inblock = False

    if not inblock:
        sys.stdout.write(line)

    opentag = re.compile('^```{r.*}$')
    if opentag.match(line.strip()) and " echo=FALSE" not in line:
        sys.stdout.write("# [your code here]\n")
        inblock = True

    if line.strip() == "```{answer}":
        sys.stdout.write("your answer here\n")
        inblock = True
