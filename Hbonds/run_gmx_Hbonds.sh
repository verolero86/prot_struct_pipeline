#!/bin/bash -l

module load gromacs/2021.3-serial
module -t list

if [ $# -lt 1 ]
then
    echo "Usage:"
    echo "    $0 <prot_dir>"
    echo ""
    exit 0
fi

#TLDPROT=P00350
TLDPROT=$1
PROT=AF-${TLDPROT}-F1-model_v4

echo "Processing protein file: $TLDPROT/$PRT"

#pushd $TLDPROT

gmx pdb2gmx -f ${PROT}.pdb -o prt_processed.gro -ff charmm27 -water tip3p
gmx editconf -f prt_processed.gro -o prt_newbox.gro -c -d 1.0 -bt cubic
gmx grompp -f em.mdp -c prt_newbox.gro -p topol.top -o em.tpr -maxwarn 2
echo "1 1" | gmx hbond -f prt_newbox.gro -s em.tpr -hbm -hbn
cat hbond.ndx

#popd

