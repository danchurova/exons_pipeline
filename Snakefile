
'''
pipeline for analysis of the role of exons position (p) in the gene in its skipping rate
in different NMD-related factors knockdown (delta-psi)
'''

rule filter_exons_psi:
  input:
    "input_data/{sample}.gff"
  output:
    "snakemake_res/exons_psi_{sample}.bed"
  shell:
    "python3 filter_exons_psi.py < {input} > {output}"

rule assign_exons_to_genes:
  input:
    a="input_data/genes_unique.bed",
    b="snakemake_res/exons_psi_{sample}.bed"
  output:
    "snakemake_res/exons_genes_{sample}.bed"
  shell:
    "bedtools intersect -wa -wb -a {input.a} -b {input.b} -s -header > {output}"

rule calculate_p:
  input:
    "snakemake_res/exons_genes_{sample}.bed"
  output:
    "snakemake_res/exons_genes_psi_p_{sample}.bed"
  shell:
    "python3 calculate_p.py < {input} > {output}"

rule calculate_new_p:
  input:
    "snakemake_res/exons_genes_{sample}.bed"
  output:
    "snakemake_res/exons_genes_psi_new_p_{sample}.bed"
  shell:
    "python3 calculate_p_new.py < {input} > {output}"

