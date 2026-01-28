
# Playwright Screenplay Automation Framework – Python

> Framework de automatización **E2E UI** con **Python + Playwright** siguiendo el **Patrón Screenplay**, ejecutado con **pytest** y **pytest-bdd**. Incluye ejecución por *markers*, reportes (JUnit) e integración lista para CI/CD (GitHub Actions / Azure DevOps).

---

## 🧭 Tabla de Contenido
- descripción
- arquitectura-patrón-screenplay
- tecnologías
- requisitos
- instalación
- variables-de-entorno
- ejecución-de-pruebas
- estructura-de-directorios
- bdd-features-y-steps
- reportes
- integración-cicd
- buenas-prácticas
- solución-de-problemas
- roadmap
- autor
- licencia

---

## 📌 Descripción
Este repositorio contiene un framework de pruebas **UI end‑to‑end (E2E)** para aplicaciones web. El diseño se basa en **Screenplay**, dividiendo claramente responsabilidades en **acciones** (interacciones atómicas), **tareas** (flujos de negocio), **habilidades** (capacidades del actor), **preguntas** (validaciones) y **mapeo de UI** (selectores). La ejecución se realiza con **pytest**, soporta **BDD** mediante **pytest-bdd**, y expone **marcadores** para segmentar suites: `smoke`, `critical`, `regression`, `login`.

---

## 🧱 Arquitectura (Patrón Screenplay)
- **Actor**: quién ejecuta tareas y realiza preguntas.
- **Abilities**: capacidades que el actor posee (p. ej., `BrowseTheWeb` para usar `Page` de Playwright).
- **Actions**: interacciones atómicas con la UI (`Click`, `Fill`, `Navigate`).
- **Tasks**: flujos de negocio reutilizables (`LoginPractice`, `Logout`).
- **Questions**: consultas/validaciones sobre el estado de la UI (`ConfirmacionMensaje`).
- **UI**: centralización de **selectores** (`Practice`).

---

## 🛠 Tecnologías
- **Python 3.11**
- **Playwright** (Chromium)
- **pytest**, **pytest-bdd**
- **python-dotenv** para configuración (`.env`)
- **Reportes**: `pytest-html`
- **CI/CD**: GitHub Actions / Azure DevOps

---

## ✅ Requisitos
- Python **≥ 3.11**

---

## ⚙️ Instalación
```bash
# 1) Crear un virtualenv
python -m venv .venv

# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# 2) Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 3) Instalar navegadores Playwright
playwright install chromium
```

---

## 🌐 Variables de entorno
Crea un archivo **`.env`** en la raíz del proyecto con las claves mínimas para ejecutar las pruebas en distintos entornos:

```dotenv
# Entorno objetivo
ENVIRONMENT=dev   # dev | qa | prod

# Aplicación bajo prueba
BASE_URL=https://practicetestautomation.com/practice-test-login/

# Credenciales de prueba (solo entornos no productivos)
USERNAME=student
PASSWORD=Password123
```

---

## 🧪 Ejecución de pruebas

### Ejecutar todas las pruebas
```bash
pytest -v
```

### Ejecutar por marcadores
```bash
pytest -m smoke -v
pytest -m critical -v
pytest -m regression -v
pytest -m login -v
```

### Reporte HTML
```bash
pytest --html=reports/report.html --self-contained-html -v
```

### JUnit (para CI/CD)
```bash
pytest --junitxml=reports/junit.xml -v
```

---

## 🗂 Estructura de directorios

```
src/
 ├─ actions/          # Interacciones atómicas (Click, Fill, Navigate)
 ├─ tasks/            # Flujos de negocio (LoginPractice, Logout)
 ├─ abilities/        # Capacidades del actor (BrowseTheWeb)
 ├─ questions/        # Validaciones / lecturas (ConfirmacionMensaje)
 ├─ ui/               # Selectores centralizados (Practice)
 ├─ actor/            # Lógica del Actor
 └─ stage/            # Manejo del escenario (Stage)

tests/
 ├─ features/         # Escenarios BDD
 ├─ step_defs/        # Step definitions (pytest-bdd)
 ├─ conftest.py       # Fixtures generales
 └─ test_login.py     # Ejecución de escenarios

support/
 └─ files.py         # Archivos de configuraciones
 
.env                  # Variables de entorno
pytest.ini            # Markers y convenciones
requirements.txt      # Dependencias
reports/              # HTML, Allure, JUnit
```

---

## 📊 Reportes

### Reporte HTML
Generado con `pytest-html`, embebido en un solo archivo:
```
reports/report.html
```

### JUnit
Consumido por CI/CD:
```
reports/junit.xml
```

### Allure (si está habilitado)
```
allure-results/
allure-report/
```
Recomendación: publicar reportes como **artefactos** en pipelines.

---

## 🔄 Integración CI/CD

### GitHub Actions (resumen)
- Instalar Python y dependencias  
- Instalar Playwright  
- Generar `.env` desde secretos  
- Ejecutar pruebas por marcador  
- Publicar reportes HTML / JUnit / Allure  
- Mantener matrices para ambientes (dev/qa/prod)

### Azure DevOps (resumen)
**Stages recomendados:**
1. **Build** — Python + deps; `playwright install --with-deps`  
2. **Automated Testing** — generar `.env`; ejecutar por marcadores; publicar JUnit/HTML  
3. **Quality Gate** — validar pass rate (p. ej., ≥ 95%) usando `junit.xml`  
4. **Rollback (opcional)** — acción de reversión si el gate falla  

---


---


## 🗺 Roadmap
- Pruebas API (back-end) PENDIENTE
- Integración performance básica (k6/Locust) PENDIENTE
- Dashboard de reportes (Allure en Pages / Azure DevOps Wiki)
- Paralelización con `pytest -n auto`
- Linters (ruff/flake8) y SAST (bandit) en etapa Build

---

## 👤 Autor
**Yendry Viloria Arrieta**

---
