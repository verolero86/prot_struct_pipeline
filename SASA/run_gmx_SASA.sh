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

echo "Processing protein file: $TLDPROT/$PROT"

#pushd $TLDPROT

echo "1" | gmx sasa -f prt_newbox.gro -s em.tpr -or ${PROT}_resarea.xvg

#popd

