---
# Guía de Niveles Epistémicos TCU
## Referencia Rápida para Clasificación de Material

**Versión:** 1.0 — 2 de julio de 2026

---

## La Escala Epistémica

El proyecto TCU clasifica todo su material en 6 niveles de rigor epistémico.

| Nivel | Nombre | Criterios | Ubicación en repo |
|-------|--------|-----------|-------------------|
| **1** | Evidencia empírica sólida | AUC / p-values / bootstrap / out-of-sample | CORE/ + PAPERS/ |
| **2** | Empírico con caveats | Evidencia estadística pero con limitaciones metodológicas conocidas | CORE/ + PAPERS/ |
| **3** | Consistencia teórica fuerte | Internamente consistente, derivable del formalismo, sin validación cruzada fuerte | CORE/ |
| **4** | Hipótesis plausible | Compatible con evidencia, diseñable como experimento, no testeada aún | EXPLORATIONS/ |
| **5** | Exploratorio especulativo | Analogía cualitativa, sin metodología rigurosa, genera hipótesis | EXPLORATIONS/ |
| **6** | Filosófico / metafísico | No falsable directamente, valor inspiracional | EXPLORATIONS/ |

---

## Cómo Clasificar Material Nuevo

### Nivel 1 requiere:
- [ ] Métrica cuantitativa clara (AUC, MSE, p-value, r, etc.)
- [ ] Test de falsabilidad explícito y superado
- [ ] Validación out-of-sample (temporal o cruzada)
- [ ] Bootstrap de significancia (≥ 1000 iteraciones)
- [ ] Código reproducible y público

### Nivel 2 requiere:
- [ ] Métrica cuantitativa presente
- [ ] p-value < 0.05 (aunque con limitaciones metodológicas conocidas)
- [ ] Reproducible
- [ ] Limitaciones documentadas explícitamente

### Nivel 3 requiere:
- [ ] Derivable formalmente del formalismo TCU
- [ ] Consistente con evidencia Nivel 1-2 existente
- [ ] No contradice ningún hallazgo confirmado

### Nivel 4 requiere:
- [ ] Hipótesis formulada de forma testeable
- [ ] Diseño experimental esbozado (aunque no ejecutado)
- [ ] Compatible con el marco TCU

### Niveles 5-6:
- Material que no alcanza los criterios anteriores pero tiene valor exploratorio, poético o filosófico.

---

## Regla de Ascenso de Nivel

Un documento puede ascender de nivel solo si:
1. Se ejecuta el experimento diseñado.
2. Los resultados pasan los criterios del nivel destino.
3. El upgrade se documenta en el commit message y en el documento mismo.

---

## Regla de Mezcla Prohibida

**Está terminantemente prohibido mezclar material de diferentes niveles sin etiquetado explícito.**

Mezclar Nivel 6 con Nivel 1 en el mismo documento sin separación clara daña la credibilidad del conjunto.

---

*Guía de referencia operativa.*  
*Actualizar cuando cambien los criterios de clasificación.*
