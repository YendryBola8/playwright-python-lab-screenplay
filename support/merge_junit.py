import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPORTS_DIR = Path("reports")
OUTPUT = REPORTS_DIR / "junit.xml"

def main():
    xml_files = sorted(REPORTS_DIR.glob("junit-*.xml"))
    if not xml_files:
        print("[MergeJUnit] No se encontraron junit-*.xml en 'reports/'.")
        return 2

    # Crear un testsuite acumulado
    total_tests = total_failures = total_errors = total_skipped = 0
    suite = ET.Element("testsuite", attrib={"name": "merged", "tests": "0", "failures": "0", "errors": "0", "skipped": "0"})

    for f in xml_files:
        tree = ET.parse(f)
        root = tree.getroot()

        # Soporta <testsuite> como root (común en pytest)
        ts = root if root.tag == "testsuite" else root.find("testsuite")
        if ts is None:
            print(f"[MergeJUnit] WARNING: {f} no parece un testsuite válido, se omite.")
            continue

        tests = int(ts.attrib.get("tests", 0))
        failures = int(ts.attrib.get("failures", 0))
        errors = int(ts.attrib.get("errors", 0))
        skipped = int(ts.attrib.get("skipped", 0))

        total_tests += tests
        total_failures += failures
        total_errors += errors
        total_skipped += skipped

        # Copia cada testcase al suite combinado (opcional, útil para publicar resultados)
        for tc in ts.findall("testcase"):
            suite.append(tc)

    # Actualiza totales
    suite.set("tests", str(total_tests))
    suite.set("failures", str(total_failures))
    suite.set("errors", str(total_errors))
    suite.set("skipped", str(total_skipped))

    # Escribe el archivo combinado
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(suite).write(OUTPUT, encoding="utf-8", xml_declaration=True)
    print(f"[MergeJUnit] Escrito {OUTPUT} con tests={total_tests}, failures={total_failures}, errors={total_errors}, skipped={total_skipped}")
    return 0

if __name__ == "__main__":
    sys.exit(main())