#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
this program filter exons and their psi from .gff file
'''

import sys

for line in sys.stdin:
    chrom, source, feature, start, stop, _, strand, _, info = line.strip().split("\t")
    info_list = info.split("; ")
    if feature == 'exon':
        identificator = '_'.join([chrom, start, stop, strand])
        for element in info_list:
            if element.split(' ')[0] == 'psi':
                print(chrom+'\t'+start+'\t'+stop+'\t'+identificator+'\t'+element.split(' ')[1]+'\t'+strand)
        #exons_psi.write(new)
