---
# Nivel 4-5 — TCU Aplicado a Neurociencia y Ecología
## Horizonte de Alto Valor: Experimento 9

**Nivel epistémico:** 4-5 (Exploración con alto potencial de validación)  
**Dominio:** Neurociencia computacional, ecología de series temporales

---

## ⚠️ Etiqueta Epistémica

A diferencia de otros documentos en EXPLORATIONS/, este tiene **alto potencial de ascender a Nivel 2-3** con el diseño experimental correcto. Es la extensión más prometedora del núcleo científico actual.

---

## Por qué la Neurociencia y Ecología son los Dominios Clave

El hallazgo más robusto del proyecto TCU es la taxonomía bimodal SHOCK/MACRO (p = 0.007) y el comportamiento diferencial de τ_m^field antes de cada tipo de crisis.

Esta taxonomía fue validada exclusivamente en **mercados financieros**. Su validez como principio general requiere validación cruzada en dominios distintos.

La neurociencia y la ecología son los candidatos más prometedores porque:
1. Tienen series temporales de coherencia medibles (EEG/fMRI para neuro, abundancias para ecología).
2. Tienen tipos de "crisis" distinguibles (epilepsia/sueño para neuro, colapso poblacional/recuperación para ecología).
3. Existen datasets públicos de alta calidad.

---

## Propuesta: Experimento 9

### Hipótesis
La taxonomía SHOCK/MACRO y el comportamiento diferencial de τ_m^field antes de cada tipo de transición son generalizables más allá de los mercados financieros.

### Dominio Candidato 1: Neurociencia
- **Datos:** Series EEG de pacientes con epilepsia (datasets públicos disponibles).
- **Proxy de Q(t):** Phase Locking Value (PLV) inter-electrodos, análogo al AR1 financiero.
- **Tipos de crisis:** Seizure exógeno (análogo SHOCK) vs deterioro progresivo de la conectividad (análogo MACRO).
- **Predictor:** τ_m^field calculado sobre PLV.

### Dominio Candidato 2: Ecología
- **Datos:** Series temporales de abundancias de poblaciones (LTER, GBIF).
- **Proxy de Q(t):** Sincronía inter-poblacional (similar al AR1).
- **Tipos de crisis:** Colapso súbito por evento climático extremo (SHOCK) vs extinción local progresiva (MACRO).
- **Predictor:** τ_m^field + Critical Slowing Down (CSD) ya implementado.

### Diseño Metodológico
1. Mismo pipeline de validación que Experimentos 1-8 (Paper v3).
2. Split temporal out-of-sample.
3. Métricas: AUC, p-values bootstrap, comparación vs baseline.
4. Test explícito: ¿τ_m^field predice el tipo de crisis con AUC > 0.70?

---

## Impacto Potencial

Si el Experimento 9 tiene éxito, elevaría el estatus científico del proyecto de forma dramática:
- La taxonomía SHOCK/MACRO pasaría de ser un hallazgo financiero a un **principio general de sistemas complejos**.
- El paper de validación cruzada sería publicable en journals de alto impacto (PNAS, Nature Communications, etc.).

---

## Estado Actual

- **Diseño:** En elaboración (este documento es el borrador conceptual).
- **Datos:** Por identificar (candidatos en repositorios públicos).
- **Código:** Pipeline base disponible en repositorio `skills-soberanos`.
- **Prioridad:** Alta (mencionada como máxima en STATE/tuc-current-state.md).

---

*Este documento representa el horizonte de mayor valor científico inmediato.*  
*Potencial de ascender a PAPERS/ tras validación empírica.*
