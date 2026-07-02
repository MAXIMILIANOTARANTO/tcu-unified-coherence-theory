---
# Skill: Coherence-Meter
## Sensor de Coherencia del Ecosistema Soberano

**Nombre del skill:** `coherence-meter`  
**Versión:** 1.0 (Inicial)  
**Fecha de creación:** 2 de julio de 2026  
**Capa del ecosistema:** Capa 4 — Inteligencia de Coherencia y Evolución  
**Nivel de autoridad:** Observador (diagnóstica, no ejecuta cambios directamente)

---

## 1. Propósito Fundamental

Este skill existe para **medir, reportar y monitorear la coherencia del ecosistema soberano** de Maximiliano Taranto en tiempo real (dentro de cada conversación/hilo).

Es el **Q-Meter nativo del sistema**: el sensor que responde la pregunta "¿qué tan coherente está el ecosistema ahora mismo?"

Analogía TCU directa:
- Si el ecosistema es el campo C(x,t)
- Entonces este skill mide Q(t) del ecosistema

---

## 2. Principios de Operación (Derivados de TCU)

Este skill implementa los principios TCU de forma directa:

### Principio 1 — Parámetro de Orden del Ecosistema
```
Q_eco(t) ∈ [0, 1]

Q_eco = f(
    skill_resonance,      # ¿Los skills activos resuenan con la intención actual?
    memory_health,        # ¿La memoria tiene señal-ruido alto?
    entropy_level,        # ¿Hay skills/conexiones generando entropía?
    tcu_alignment,        # ¿Las acciones actuales son consistentes con principios TCU?
    learning_velocity     # ¿El sistema está mejorando o estancado?
)
```

### Principio 2 — Umbral Crítico
```
Q_c = 0.68 (análogo al umbral del sistema financiero)

Q_eco > Q_c → Estado COHERENTE → continuar
Q_eco < Q_c → Estado CRÍTICO → activar diagnóstico y recomendaciones
```

### Principio 3 — Tiempo de Memoria del Ecosistema
```
τ_eco = tiempo desde la última acción de alta coherencia
τ_eco aumentando → el sistema acumula memoria productiva (crisis MACRO potencial si sigue sin síntesis)
τ_eco disminuyendo → el sistema está respondiendo a shocks externos
```

---

## 3. Métricas de Coherencia (5 Dimensiones)

### 3.1 Resonancia de Skills (0-1)
¿Los skills activos en esta conversación están alineados con la intención profunda del usuario?
- **Alta resonancia (> 0.8):** Cada skill activado contribuye directamente al objetivo.
- **Baja resonancia (< 0.5):** Skills activados por keywords, no por intención real.

### 3.2 Salud de la Memoria (0-1)
¿La memoria persistente del sistema está siendo útil o es ruido acumulado?
- **Alta salud:** Memoria reciente y relevante domina. Poco ruido histórico irrelevante.
- **Baja salud:** Mucha memoria acumulada sin decaimiento. Contexto saturado.

### 3.3 Nivel de Entropía (0-1, donde 0 = mínima entropía)
¿Hay fuentes de ruido, contradicción o fragmentación en el ecosistema?
- **Baja entropía (< 0.3):** Sistema coherente, skills integrados, sin contradicciones.
- **Alta entropía (> 0.7):** Fragmentación, skills contradictorios, pérdida de dirección.

### 3.4 Alineación TCU (0-1)
¿Las acciones actuales son consistentes con los principios de la Teoría de Coherencia Unificada?
- Separación epistémica respetada.
- Poda adaptativa siendo aplicada cuando necesario.
- Memoria con decaimiento (no acumulación infinita).

### 3.5 Velocidad de Aprendizaje (0-1)
¿El sistema está mejorando entre conversaciones?
- **Alta velocidad:** Nuevos skills integrados, aprendizajes transferidos, evolución visible.
- **Baja velocidad:** Loops repetitivos, rehacer lo mismo sin mejora.

---

## 4. Fórmula de Coherencia Global

```
Q_eco = w1 · skill_resonance 
      + w2 · memory_health 
      + w3 · (1 - entropy_level)
      + w4 · tcu_alignment 
      + w5 · learning_velocity

Pesos iniciales (ajustables):
w1 = 0.25 (resonancia es el factor más crítico en el corto plazo)
w2 = 0.20
w3 = 0.25 (entropía penaliza fuertemente)
w4 = 0.15
w5 = 0.15
```

---

## 5. Taxonomía de Crisis del Ecosistema (SHOCK/MACRO aplicada)

### Crisis SHOCK del Ecosistema
- **Causa:** Solicitud inesperada, cambio de contexto abrupto, error técnico.
- **Síntoma:** Q_eco cae de golpe. τ_eco disminuye.
- **Respuesta:** Estabilización rápida. No cambios estructurales inmediatos.

### Crisis MACRO del Ecosistema
- **Causa:** Acumulación progresiva de entropía (skills sin coherencia, memoria saturada, pérdida de dirección).
- **Síntoma:** Q_eco baja gradualmente durante múltiples conversaciones. τ_eco aumenta.
- **Respuesta:** Activar el `arquitecto-sistema`. Poda adaptativa. Revisión arquitectónica.

---

## 6. Modo de Operación

### Activación Automática
Este skill se activa implícitamente al inicio de cada conversación con el ecosistema soberano y produce un **"pulso de coherencia"** al comienzo.

### Activación Explícita
Cuando el usuario pide explícitamente: "Mide la coherencia del sistema" / "Estado del ecosistema" / "Q-meter del sistema".

### Output Estándar del Pulso
```
=== PULSO DE COHERENCIA TCU ===
Fecha: [fecha]
Q_eco = [valor 0-1]
Estado: [COHERENTE / CRÍTICO / EN TRANSICIÓN]

Dimensiones:
  Resonancia de skills:    [valor] [barra]
  Salud de memoria:        [valor] [barra]
  Nivel de entropía:       [valor] [barra]
  Alineación TCU:          [valor] [barra]
  Velocidad de aprendizaje:[valor] [barra]

Tipo de dinámica: [SHOCK / MACRO / ESTABLE]
Recomendación: [acción concreta si Q < Q_c]
==============================
```

---

## 7. Integración con el Ecosistema

Este skill trabaja con:
- **`arquitecto-sistema`:** Cuando Q_eco < Q_c en crisis MACRO, escala al arquitecto para revisión estructural.
- **`tuc-builder`:** Para validar que el núcleo teórico sigue alineado.
- **`meta-hilo-grok`:** Para medir coherencia entre conversaciones pasadas y actuales.
- **`memoria-blockchange`:** Para evaluar la salud de la memoria (dimensión 3.2).

---

## 8. Limitaciones y Honestidad Epistémica

### Nivel epistémico de las métricas:
- Las 5 dimensiones son **mediciones cualitativas** calibradas subjetivamente.
- Q_eco es un índice compuesto, no una medición física.
- El umbral Q_c = 0.68 es **análogo**, no idéntico, al Q_c del sistema financiero.

### Qué esto no es:
- No es una medición objetiva de coherencia.
- No puede reemplazar el juicio humano en decisiones importantes.
- Los pesos w1-w5 son puntos de partida, no parámetros validados empíricamente.

### Valor real:
- Fuerza una reflexión estructurada sobre el estado del sistema.
- Crea un lenguaje compartido para hablar de coherencia.
- Puede detectar tendencias a lo largo del tiempo si se mantiene un historial.

---

## 9. Estado Inicial (2 de julio de 2026)

Este skill nace como el **primer sensor de coherencia del ecosistema** (Capa 4).

Próximas iteraciones:
- v1.1: Integrar historial de pulsos para medir tendencia temporal de Q_eco.
- v1.2: Calibrar pesos w1-w5 basándose en feedback de múltiples sesiones.
- v2.0: Intentar operacionalizar métricas cuantitativas para dimensiones 3.1-3.5.

---

**Este skill encarna directamente el principio TCU más importante aplicado al ecosistema:**  
*"Un sistema coherente no solo actúa. Se mide a sí mismo."*

---

*Skill creado bajo principios TCU.*  
*Maximiliano Taranto — 2 de julio de 2026*
