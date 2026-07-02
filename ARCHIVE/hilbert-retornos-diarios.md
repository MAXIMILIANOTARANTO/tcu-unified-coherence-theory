---
# Método Falsado: Hilbert sobre Retornos Diarios Financieros
## Registro de Falsación Formal

**Método propuesto originalmente:** Transformada de Hilbert sobre retornos diarios para extraer Q(t)  
**Falsado en:** TCU v2.0 / Paper v3  
**Fecha de falsación:** Aproximadamente primer semestre 2026

---

## La Propuesta Original

Usar la señal analítica derivada de la Transformada de Hilbert aplicada a retornos de precio diarios para obtener una fase instantánea φ(t) y, desde ahí, calcular Q(t) como coherencia de fase.

**Razonamiento:** En señales de frecuencia única bien definida, la Transformada de Hilbert funciona perfectamente para extraer fase instantánea. Parecía natural aplicarlo a series financieras.

---

## Por qué Falló

1. **Retornos diarios financieros no son señales de banda estrecha.** La condición fundamental para que la Transformada de Hilbert calcule una fase instantánea significativa es que la señal sea analítica (banda estrecha, cuasi-monocomponente). Los retornos financieros diarios son señales broadband con ruido dominante.

2. **La fase instantánea resultante es física sin interpretación.** Cuando se aplica Hilbert a señales broadband, la "fase instantánea" oscila erráticamente y no captura ninguna dinámica de coherencia real.

3. **Confirmación empírica del fallo:** Al comparar Q(t)_Hilbert con crisis conocidas, la señal no tenía poder predictivo estadísticamente significativo.

---

## Qué Aprendizaje Produjo

Este fracaso llevó directamente a buscar un proxy observable alternativo para Q(t). La búsqueda resultó en el **Absorption Ratio (AR1)**, que:
- Mide la fracción de varianza del mercado explicada por el primer componente principal.
- Tiene interpretación directa como medida de sincronización del sistema.
- Demostró correlación r = 0.80 con Q(t) del modelo.
- Alcanzó AUC = 0.818 (p = 0.036) en detección de crisis financieras.

**El fracaso de Hilbert fue productivo: forzó encontrar un proxy mejor.**

---

## Estado Final

✅ Falsado correctamente y documentado.  
✅ Aprendizaje incorporado al núcleo.  
❌ No usar Hilbert sobre retornos diarios como proxy de Q(t).  
⚠️ Hilbert puede ser útil en otros contextos (datos de alta frecuencia, señales EEG con banda más estrecha — explorar en Experimento 9).

---

*Registro histórico de falsación. Honestidad epistémica radical.*
