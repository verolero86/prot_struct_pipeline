#!/usr/bin/env python3

# 
# Filename:     count_Hbonds.py
# Author:       vmv
# Description:  takes a .ndx file from Gromacs and counts the number of H bonds
#               between aminoacids in a given protein 
# 

import pandas as pd
import re

hfile='hbond.ndx'
protfile='prt_processed.gro'
numhbondsfile='num_hbonds.tsv'

hd = dict()
aad = dict()

with open(hfile, 'r') as f:
    for i in f.readlines():
        if i.startswith('['):
            my_key = i.replace("[ ", "")
            my_key = my_key.replace(" ]","")
            dic_key = my_key.strip()
        else:
            if dic_key in hd:
                hd[dic_key] += [i.strip()]
            else:
                hd[dic_key] = [i.strip()]


#df = pd.read_csv(protfile, delim_whitespace=True, header=None, skiprows=[0,1], usecols=[0,1,2], skipfooter=1, names=['aaID','element','atomID'])
df = pd.read_fwf(protfile, delim_whitespace=True, header=None, skiprows=[0,1], usecols=[0,1,2,3], skipfooter=1, names=['resID','residue','element','atomID'], colspecs=[(0, 5),(5, 10),(10, 15),(15, 20)])
print(df)

# Prints entire dictionary
# print(hd)


# Prints only H bonds
print(hd['hbonds_Protein'])

hbonds = hd['hbonds_Protein']

num_hbonds = len(hbonds)
print(f"Total number of H bonds: {num_hbonds}")

for hb in hbonds:
    triplet = hb.split()
    d = triplet[0]
    a = triplet[2]
    #print(hb)
    print(f"donor: {[d]}, acceptor: {[a]}")
    d_aaID = str(df[df['atomID'] == int(d)].resID.item()) + "\t" + df[df['atomID'] == int(d)].residue.item()
    a_aaID = str(df[df['atomID'] == int(a)].resID.item()) + "\t" + df[df['atomID'] == int(a)].residue.item()
    print(f"donor aa: {d_aaID}, acceptor aa: {a_aaID}")
    
    if d_aaID in aad:
        if d not in aad[d_aaID]:
            aad[d_aaID] += [d]
        else:
            print(f"{d} is already in H bonds list for {aad[d_aaID]}")
    else:
        aad[d_aaID] = [d]

    if a_aaID in aad:
        if a not in aad[a_aaID]:
            aad[a_aaID] += [a]
        else:
            print(f"{a} is already in H bonds list for {aad[a_aaID]}")
    else:
        aad[a_aaID] = [a]

print(aad)

with open(numhbondsfile,'w') as f:
    print(f"res_id\tresidue\tnum_hbonds",file=f)
    for aa in aad:
        nh = len(aad[aa])
        print(f"aa: {aa}, num_hbonds: {nh}")
        print(f"{aa}\t{nh}",file=f)

