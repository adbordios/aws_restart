#!/bin/bash

cat preproinsulin-seq.txt | grep -Ev 'ORIGIN|//' | sed 's/[0-9]//g;s/[[:space:]]//g' | tr -d '\n' > preproinsulin-seq-clean.txt
cat preproinsulin-seq-clean.txt | cut -c 1-24 | tr -d '\n' > lsinsulin-seq-clean.txt
cat preproinsulin-seq-clean.txt | cut -c 25-54 | tr -d '\n' > binsulin-seq-clean.txt
cat preproinsulin-seq-clean.txt | cut -c 55-89 | tr -d '\n' > cinsulin-seq-clean.txt
cat preproinsulin-seq-clean.txt | cut -c 90-110 | tr -d '\n' > ainsulin-seq-clean.txt