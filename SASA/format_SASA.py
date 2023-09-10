#!/usr/bin/env python3

# 
# Filename:     format_SASA.py
# Author:       vmv

# Description:  takes a .xvg file from Gromacs and extracts the Solvent
#               Accessible Surface Area (SASA) for each aminoacid in a
#               given protein
# 

import pandas as pd
import re

resareafile='resarea.xvg'
protfile='prt_processed.gro'
sfile='sasa.tsv'

df_resarea = pd.read_csv(resareafile, delim_whitespace=True, header=None, skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12], comment='@', usecols=[0,1], names=['resID','sasa'])
print(df_resarea)
df = pd.read_fwf(protfile, delim_whitespace=True, header=None, skiprows=[0,1], usecols=[0,1,2,3], skipfooter=1, names=['resID','residue'], colspecs=[(0, 5),(5, 10)])
print(df)
df = df.drop_duplicates()
print(df)

with open(sfile,'w') as f:
    print(f"res_id\tresidue\tsasa",file=f)
    for rid in df_resarea['resID']:
        print(f"Searching for resID: {rid}")
        rname = df[df['resID'] == int(rid)].residue.item()
        print(f"resID: {rid}, resname: {rname}")
        rsasa = df_resarea[df_resarea['resID'] == int(rid)].sasa.item()
        print(f"{rid}\t{rname}\t{rsasa}")
        print(f"{rid}\t{rname}\t{rsasa}",file=f)
        

