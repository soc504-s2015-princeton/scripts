#!/usr/bin/env python

# Given an Rmd file, output a valid R file.
# Lines that aren't R code will be commented out with a '#'.
#
# Usage options:
# ./Rmd-to-R.py input.Rmd > output.R
# cat input.Rmd | ./stripanswers.py > output.R
#

import fileinput, sys, re
inblock = False
for line in fileinput.input():
    if inblock and line.strip() == "```":
        inblock = False

    if not inblock:
        sys.stdout.write('# ' + line)
    else:
        sys.stdout.write(line)

    opentag = re.compile('^```{r.*}$')
    if opentag.match(line.strip()) and " echo=FALSE" not in line:
        inblock = True
