#!/bin/bash
set -e
scripts="scripts"

for file in *.Rmd
do
  rfile=`basename $file .Rmd`
  $scripts/Rmd-to-R.py $file > $rfile.R
done

exitstatus=0
for file in *.R
do
  Rscript -e "lintr::lint(\"$file\")"
  outputbytes=`Rscript -e "lintr::lint(\"$file\")" | wc -c`
  if [ $outputbytes -gt 0 ]
  then
    exitstatus=1
  fi
done

exit $exitstatus
