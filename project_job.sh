#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=500M
#SBATCH --job-name=report
#SBATCH --output=reports-%j.out

module load StdEnv/2023 python/3.11.5 scipy-stack/2026a
module list

virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip
pip install --no-index -r ~/project_packages.txt

python Project-HPC-template_GChieme.py