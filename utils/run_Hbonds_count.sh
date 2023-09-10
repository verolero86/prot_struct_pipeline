#!/bin/bash -l


if [ $# -lt 1 ]
then
    echo "Usage:"
    echo "    $0 <prot_dir>"
    echo ""
    exit 0
fi


TLDDIR=/gpfs/alpine/syb111/proj-shared/Projects/Ecoli
HBONDSDIR=${TLDDIR}/Hbonds
PROT=$1
LOGFILE=hbond_${PROT}.log

echo "Processing protein file: $PROT" >> $LOGFILE

$HBONDSDIR/run_gmx_Hbonds.sh $PROT >> $LOGFILE
$HBONDSDIR/count_Hbonds.py >> $LOGFILE

mv num_hbonds.tsv ${PROT}_num_hbonds.tsv

echo "Completed counting H bonds for ${PROT}!"


