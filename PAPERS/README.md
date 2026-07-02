---
# TCU — Documento Científico Canónico
## A Unified Coherence Theory for Complex Systems: Empirical Validation in Financial Markets

**Versión:** 3.0 (Canónica — Paper v3)  
**Fecha:** 2 de julio de 2026  
**Autor:** Maximiliano Taranto  
**Institución:** Archivo Semilla Research Initiative  
**Nivel epistémico:** 1-2 (Núcleo validado)

---

## Abstract

We present the Unified Coherence Theory (TCU), a field-theoretic framework describing the collective coherence dynamics of complex systems. The master equation combines a wave operator with nonlinear self-organization, historical memory feedback, and external forcing:

```
□C + μ²C + λ|C|²C + κ · I[C] = S(x,t)
```

We propose the Absorption Ratio (AR1) as an empirically observable proxy for the order parameter Q(t), achieving r = 0.80 correlation. Applied to financial crisis detection, TCU yields AUC = 0.818 (p = 0.036 vs VIX-only baseline) and reveals a **bimodal crisis taxonomy** — SHOCK (exogenous) vs MACRO (endogenous) — separable at p = 0.007. The field memory time τ_m^field exhibits opposite directional behavior before each crisis type (p = 0.016), providing a mechanistic signature for early warning. These empirical validations establish TCU as a reproducible, falsifiable framework for coherence-based crisis detection in complex systems.

---

## 1. Introducción

Los sistemas complejos — mercados financieros, ecosistemas, redes neuronales — exhiben transiciones de fase colectivas que preceden a crisis o colapsos. La detección temprana de estas transiciones tiene valor científico y aplicado.

La Teoría de Coherencia Unificada (TCU) propone modelar el estado colectivo de un sistema mediante un campo complejo C(x,t) cuya dinámica está gobernada por la ecuación maestra. A diferencia de modelos previos, TCU incorpora explícitamente:
1. Memoria histórica no local con kernel exponencial causal.
2. Auto-organización no lineal (formación de solitones).
3. Forzamiento externo distinguible (taxonomía SHOCK/MACRO).

---

## 2. Formalismo Matemático

### 2.1 Ecuación Maestra

```
□C + μ²C + λ|C|²C + κ · I[C] = S(x,t)
```

**Términos:**
- `□C` — operador d'Alembertiano: propagación de coherencia a velocidad v
- `μ²C` — término de masa/inercia efectiva
- `λ|C|²C` — auto-organización no lineal (Ginzburg-Landau)
- `κ · I[C]` — retroalimentación de memoria histórica
- `S(x,t)` — forzamiento externo (shocks, estímulos)

### 2.2 Operador de Memoria

```
I[C](x,t) = ∫_{-∞}^t (1/τ_m) · exp(-(t-s)/τ_m) · C(x,s) ds
```

Kernel exponencial causal. Pertenece a la familia de ecuaciones de Ginzburg-Landau con memoria, Kuramoto con retardo, y ecuaciones de onda disipativas.

### 2.3 Parámetro de Orden

```
Q(t) = |Z(t)|²
Z(t) = (1/N) Σₖ exp(i · φₖ(t))
```

- Q = 1: sincronización perfecta (coherencia máxima)
- Q = 0: fases aleatorias (entropía máxima)
- Q_c ≈ 0.68 ± 0.05: umbral crítico de transición de fase

### 2.4 Tiempo de Memoria del Campo

```
τ_m^field = -1 / ln(|ρ_AR1|)
```

donde ρ_AR1 es la autocorrelación de primer orden de AR1 en ventana móvil.

---

## 3. Proxy Observable: Absorption Ratio (AR1)

**Definición:** AR1 = fracción de la varianza total del mercado explicada por el primer componente principal en una ventana deslizante de 500 días.

**Validación del proxy:**
- Correlación con Q(t) del modelo: r = 0.80
- Interpretación: AR1 alto → mercado "mode-locked" → alta coherencia

---

## 4. Experimentos de Validación (Resumen de 8 Experimentos)

| Experimento | Hallazgo | Métrica | Nivel |
|------------|---------|---------|-------|
| 1 | AR1 captura colapso de coherencia | AUC = 0.818, p = 0.036 | 1 |
| 2 | CSD detecta crisis macro | AUC_macro = 0.832 | 1 |
| 3 | Taxonomía bimodal SHOCK/MACRO | p = 0.007 | 1 |
| 4 | τ_m^field distingue crisis por tipo | p = 0.016 | 2 |
| 5 | AR1 ≈ Q (validación del proxy) | r = 0.80 | 2 |
| 6 | Hilbert sobre retornos diarios | Falsado | Archivado |
| 7 | Bootstrap de significancia | p-values robustos | 1 |
| 8 | Out-of-sample temporal | Consistencia validada | 2 |

---

## 5. Taxonomía de Crisis

### SHOCK (Exógeno)
- S(x,t) domina en la ecuación maestra.
- τ_m^field **disminuye** antes del evento.
- Recuperación relativamente rápida.
- Ejemplo: Colapso Lehman 2008, COVID crash marzo 2020.

### MACRO (Endógeno)
- κ · I[C] domina.
- τ_m^field **aumenta** antes del evento (acumulación de memoria).
- Recuperación más lenta y compleja.
- Ejemplo: Crisis de deuda soberana europea 2010-2012.

**Separación estadística: p = 0.007** — uno de los hallazgos más robustos del proyecto.

---

## 6. Falsaciones Honestas

| Hipótesis Falsada | Resultado | Implicación |
|------------------|-----------|-------------|
| Hilbert sobre retornos diarios → Q(t) | No funciona | Retornos diarios no son señal banda estrecha |
| Q_c es universal (cualquier ventana) | Sensible a ventana | Robustez requiere análisis de sensibilidad |

---

## 7. Reproducibilidad

- Pipeline de validación disponible en: `https://github.com/MAXIMILIANOTARANTO/skills-soberanos`
- Datos: S&P 500 OHLCV, Russell 2000 OHLCV (Yahoo Finance)
- Ventana AR1: 500 días (deslizante)
- Ventana τ_m: 252 días (deslizante)
- Bootstrap: 1000 iteraciones, estratificado por tipo de crisis

---

## 8. Próximos Pasos (Experimento 9)

**Objetivo:** Validación cruzada de la taxonomía SHOCK/MACRO en dominios no financieros.

**Candidatos:**
- Series EEG de epilepsia (datos públicos)
- Series de abundancias ecológicas (LTER)

**Hipótesis a testear:** τ_m^field exhibe comportamiento diferencial antes de crisis SHOCK vs MACRO también en neurociencia y ecología.

---

## 9. Conclusión

TCU proporciona un marco formalizado, reproducible y falsable para:
1. Detectar transiciones de fase en sistemas complejos.
2. Distinguir el tipo de crisis (SHOCK vs MACRO) mediante el comportamiento de τ_m^field.
3. Ofrecer una base teórica unificada (ecuación maestra) para fenómenos de coherencia colectiva.

Los hallazgos tienen significancia estadística sólida (p-values en rango 0.007–0.036) y son reproducibles con el pipeline público.

---

## Referencias

- Ginzburg, V.L. & Landau, L.D. (1950). On the theory of superconductivity.
- Kuramoto, Y. (1984). Chemical Oscillations, Waves, and Turbulence.
- Kritzman, M. et al. (2011). Principal Components as a Measure of Systemic Risk.
- Scheffer, M. et al. (2009). Early-warning signals for critical transitions. Nature.

---

*Documento canónico. Solo material Nivel 1-2.*  
*Maximiliano Taranto — Archivo Semilla Research Initiative — 2 de julio de 2026*
