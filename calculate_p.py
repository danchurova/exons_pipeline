#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
old version
this script callculate p (p= (a-x)/(y-x)-(b-a)+1) for each exon
'''

import sys

for line in sys.stdin:
    chrom, gene_start, gene_end, _, _, strand, gene, _, exon_start, exon_end, exon_name, psi, _ = line.split()
    psi = psi[1:-1]
    gene_start, gene_end, exon_start, exon_end = int(gene_start), int(gene_end), int(exon_start), int(exon_end)
    if strand == '+':
        p = round((exon_start - gene_start)/ ((gene_end - gene_start) - (exon_end - exon_start) +1), 2)
        print("\t".join([chrom, str(gene_start), str(gene_end), strand, gene, str(exon_start), str(exon_end), exon_name, psi, str(p)]))

    elif strand == '-':
        p = round((exon_end - gene_end)/ ((gene_start - gene_end) - (exon_start - exon_end) +1), 2)
        print("\t".join([chrom, str(gene_start), str(gene_end), strand, gene, str(exon_start), str(exon_end), exon_name, psi, str(p)]))
