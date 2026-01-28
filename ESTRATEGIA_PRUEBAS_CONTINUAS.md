# Estrategia de Pruebas Continuas

**Proyecto:** Playwright Python – Login (Smoke)

## 1. Objetivo
Integrar la calidad dentro del flujo de entrega continua, detectando defectos de forma temprana y reduciendo riesgos en producción mediante automatización y validaciones continuas.

## 2. Tipos de Pruebas
- Pruebas funcionales automatizadas (Smoke).
- Excluidas: regresión completa, performance, seguridad y mobile por costo y tiempo.

## 3. Etapas del Ciclo CI/CD
- Build: preparación y dependencias.
- Automated Testing: ejecución Playwright headless.
- Quality Gate: evaluación de resultados (>=90%).

## 4. Automatización y Priorización
Se priorizan funcionalidades críticas del negocio (login), alto uso y bajo tiempo de ejecución.

## 5. Quality Gate
Análisis de resultados JUnit. El pipeline falla si el porcentaje de éxito es menor al umbral definido.

## 6. Rollback
Estrategia conceptual: rollback automático ante fallos de despliegue (Kubernetes, Azure WebApp o Docker).

## 7. Métricas
- % pruebas exitosas
- Tiempo de pipeline
- Defectos detectados
- MTTR

## 8. Riesgos
Cobertura limitada y dependencia del entorno CI, mitigados con ejecución headless y extensión progresiva.
