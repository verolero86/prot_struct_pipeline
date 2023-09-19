#!/bin/bash -l


if [ $# -lt 1 ]
then
    echo "Usage:"
    echo "    $0 <prot_dir>"
    echo ""
    exit 0
fi


TLDDIR=/gpfs/alpine/syb111/proj-shared/Projects/Ecoli
SASADIR=${TLDDIR}/SASA
PROT=$1
LOGFILE=sasa_${PROT}.log

echo "Processing protein file: $PROT" >> $LOGFILE

$SASADIR/run_gmx_SASA.sh $PROT >> $LOGFILE
$SASADIR/format_SASA.py >> $LOGFILE

mv sasa.tsv ${PROT}_sasa.tsv

echo "Completed calculating SASA for ${PROT}!"


