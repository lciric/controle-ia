set -uo pipefail
PY="$1"
for CPU in "AMD EPYC 7543 32-Core Processor" "Intel(R) Xeon(R) Processor @ 2.10GHz" "inconnu"; do
case "$CPU" in *EPYC*) ENV_CPU=();; *) ENV_CPU=(ATEN_CPU_CAPABILITY=avx2 MKL_CBWR=AVX2);; esac
echo "processeur : $CPU ; environnement de l'étape A en plus : ${ENV_CPU[*]:-aucun (EPYC, processeur de P3)}"
echo "étape A : environnement CUBLAS_WORKSPACE_CONFIG=:4096:8${ENV_CPU[*]:+ ${ENV_CPU[*]}}"
env CUBLAS_WORKSPACE_CONFIG=:4096:8 "${ENV_CPU[@]}" PYTHONPATH=src "$PY" -c 'import os; print({k: os.environ.get(k) for k in ("CUBLAS_WORKSPACE_CONFIG", "ATEN_CPU_CAPABILITY", "MKL_CBWR", "PYTHONPATH")})'; echo "code $?"
done
