---
# Checklist de Validación TCU
## Para Elevación de Nivel Epistémico

**Versión:** 1.0 — 2 de julio de 2026

---

## Checklist: Nivel 4 → Nivel 3

```
HIPÓTESIS:
[ ] La hipótesis es derivable formalmente del formalismo TCU
[ ] No contradice ningún hallazgo Nivel 1-2 existente
[ ] La conexión con la ecuación maestra está explicitada

DISEÑO:
[ ] Existe un diseño experimental para testearla
[ ] Los datos necesarios están identificados
[ ] Las métricas de éxito están definidas
```

## Checklist: Nivel 3 → Nivel 2

```
DATOS:
[ ] Dataset definido y disponible
[ ] Split temporal in-sample / out-of-sample establecido
[ ] Baseline comparador definido

MÉTRICAS:
[ ] Métrica cuantitativa primaria elegida (AUC, p-value, r, etc.)
[ ] Umbral de éxito pre-registrado
[ ] Test de falsabilidad formulado

EJECUCIÓN:
[ ] Código de análisis escrito y revisado
[ ] Análisis ejecutado sin data snooping
[ ] Resultados documentados honestamente (incluidos los negativos)
```

## Checklist: Nivel 2 → Nivel 1

```
ROBUSTEZ:
[ ] Bootstrap de significancia (≥ 1000 iteraciones)
[ ] p-value < 0.05 en out-of-sample
[ ] Sensibilidad a parámetros documentada
[ ] Al menos 1 replicación independiente (datos diferentes o período diferente)

REPRODUCIBILIDAD:
[ ] Código público y documentado
[ ] Datos accesibles (propios o públicos)
[ ] README de reproducción paso a paso

PEER REVIEW:
[ ] Revisado por al menos 1 persona con expertise en el dominio
[ ] Falsaciones intentadas honestamente
[ ] Limitaciones explicitadas en el documento
```

---

## Estado Actual de Materiales Candidatos

| Material | Nivel actual | Próximo nivel | Bloqueante principal |
|----------|-------------|---------------|---------------------|
| Taxonomía SHOCK/MACRO | 1 | — | (Ya en Nivel 1) |
| AR1 como proxy Q(t) | 1-2 | — | (Consolidado) |
| τ_m^field en datos financieros | 2 | 1 | Replicación en dataset diferente |
| Experimento 9 (neuro/ecología) | 4 | 3 | Ejecución del experimento |
| Q-meter para ecosistema agentes | 4 | 3 | Definición formal de métricas |
| S.C.A.N. en crypto | 5 | 4 | Diseño metodológico riguroso |

---

*Checklist operativo. Actualizar con cada nuevo experimento o validación.*
