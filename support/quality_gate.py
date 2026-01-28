import sys
import xml.etree.ElementTree as ET
from pathlib import Path

JUNIT_PATH = Path("reports/junit.xml")

def main(min_pass_rate: float) -> int:
    if not JUNIT_PATH.exists():
        print(f"[QualityGate] ERROR: No existe {JUNIT_PATH}.")
        return 2

    tree = ET.parse(JUNIT_PATH)
    root = tree.getroot()

    tests = int(root.attrib.get('tests', 0))
    failures = int(root.attrib.get('failures', 0)) + int(root.attrib.get('errors', 0))
    skipped = int(root.attrib.get('skipped', 0))
    executed = tests - skipped

    pass_rate = 1.0 if executed == 0 else float(executed - failures) / float(executed)

    # Exporta variable para Azure DevOps si se desea leer en pasos posteriores
    print(f"##vso[task.setvariable variable=passRate;isOutput=true]{pass_rate:.4f}")
    print(f"[QualityGate] Pass rate: {pass_rate:.2%} (executed={executed}, failures={failures})")
    print(f"[QualityGate] Umbral mínimo requerido: {min_pass_rate:.0%}")

    if pass_rate < min_pass_rate:
        print("[QualityGate] RESULT: FAILED (por debajo del umbral)")
        return 1

    print("[QualityGate] RESULT: PASSED")
    return 0

if __name__ == "__main__":
    # Lee el umbral desde variable de entorno AZ DevOps (si no, usa 0.90)
    min_pass_rate_env = None
    # Permite pasar el umbral por argumento: p.ej. `python tools/quality_gate.py 0.9`
    if len(sys.argv) > 1:
        try:
            min_pass_rate_env = float(sys.argv[1])
        except ValueError:
            print("[QualityGate] Argumento inválido para min_pass_rate, usando 0.90 por defecto.")

    min_pass_rate = min_pass_rate_env if min_pass_rate_env is not None else 0.90
    sys.exit(main(min_pass_rate))
