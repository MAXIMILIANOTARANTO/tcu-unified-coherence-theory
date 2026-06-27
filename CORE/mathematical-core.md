---
# Núcleo Matemático de la Teoría de Coherencia Unificada (TCU)
## Versión Canónica — Nivel 1-2

**Fecha:** 27 de junio de 2026  
**Fuente:** Orquestado desde TCU_DOCUMENTO_LIMPIO_v2.md + TCU_PAPER_FINAL_v3.md

---

## 1. Postulados Fundamentales

### Postulado 1 — Ontología del Campo
Existe un campo complejo de coherencia:

```
C(x,t) : ℝ^{3,1} → ℂ ,    C ∈ L²(Ω)
C(x,t) = A(x,t) · exp(i · φ(x,t))
```

donde:
- A(x,t) ≥ 0 representa la amplitud efectiva (intensidad de organización colectiva)
- φ(x,t) representa la fase colectiva del sistema

Este campo es un **parámetro de orden efectivo**. No es una entidad ontológica primaria en el sentido metafísico fuerte (esa interpretación pertenece al Nivel 5).

### Postulado 2 — Dinámica del Campo (Ecuación Maestra)

```
□C + μ^{2}C + λ|C|²C + κ · I[C] = S(x,t)
```

Donde:
- □C = propagación de información/coherencia a velocidad característica v
- μ²C = inercia / masa efectiva del sistema
- λ|C|²C = término de auto-organización no lineal (formación de solitones y estructuras)
- κ · I[C] = retroalimentación de memoria histórica no local
- S(x,t) = forzamiento externo (shocks, estímulos)

### Operador de Memoria (especificación explícita)

```
I[C](x,t) = ∫_{-∞}^t (1/τ_m) · exp(-(t-s)/τ_m) · C(x,s) ds
```

Este kernel exponencial causal es el más natural para sistemas con memoria que decae. Aparece en modelos de Ginzburg-Landau con retardo, Kuramoto con memoria, y ecuaciones de onda disipativas.

---

## 2. Parámetro de Orden Q(t)

```
Q(t) = |Z(t)|²
Z(t) = (1/N) Σₖ exp(i · φₖ(t))
0 ≤ Q ≤ 1
```

- Q(t) = 1 → sincronización perfecta de fase (coherencia máxima)
- Q(t) = 0 → fases completamente aleatorias (entropía máxima)

En sistemas financieros reales, el **Absorption Ratio (AR1)** funciona como un proxy observable de Q(t) con correlación r ≈ 0.80.

---

## 3. Tiempo de Memoria del Campo (τ_m^field)

Se define a partir de la autocorrelación del proxy de coherencia:

```
τ_m^field = -1 / ln(|ρ_AR1|)
```

Donde ρ_AR1 es la autocorrelación de primer orden de la serie AR1 en una ventana móvil.

**Hallazgo clave validado:**
- Antes de crisis **SHOCK** (exógenas): τ_m^field **disminuye**
- Antes de crisis **MACRO** (endógenas): τ_m^field **aumenta**

Esta separación tiene significancia estadística (p = 0.016).

---

## 4. Taxonomía de Transiciones de Fase

| Tipo | Dominancia | Comportamiento de τ_m | Recuperación | Ejemplo |
|------|------------|-----------------------|--------------|---------|
| **SHOCK** | S(x,t) domina | Disminuye | Más rápida | Crisis 2008 ( Lehman), COVID crash |
| **MACRO** | κ · I[C] domina | Aumenta | Más lenta y compleja | Crisis de deuda soberana, burbujas prolongadas |

Esta taxonomía es uno de los hallazgos más robustos del proyecto (p = 0.007).

---

## 5. Umbral de Coherencia Crítica

```
Q_c ≈ 0.68 ± 0.05
```

Cuando el sistema cruza este umbral hacia arriba, se produce una transición de fase discontinua hacia mayor auto-organización. Hacia abajo, el sistema entra en regímenes de alta entropía y ruido.

---

## 6. Principios de Validación (Nivel 1-2)

Todo lo que se afirma en este documento CORE debe cumplir:

1. Ser reproducible con código público.
2. Tener métricas claras (AUC, p-values, bootstrap).
3. Haber superado tests de falsabilidad explícitos.
4. No mezclar con interpretaciones ontológicas fuertes.

---

*Este núcleo matemático es la base sobre la cual se construye todo lo demás.*