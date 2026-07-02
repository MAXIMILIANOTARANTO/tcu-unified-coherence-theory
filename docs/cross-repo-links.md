---
# Mapa de Repositorios del Ecosistema Soberano
## Cross-Repo Links y Estructura de Gobernanza

**Versión:** 1.0 — 2 de julio de 2026

---

## Repositorios del Ecosistema

### 1. `tcu-unified-coherence-theory` (Este repo)
**URL:** https://github.com/MAXIMILIANOTARANTO/tcu-unified-coherence-theory  
**Rol:** Teoría base, núcleo matemático, validación empírica  
**Rama principal:** `main`  
**Nivel epistémico:** Toda la escala (1-6, correctamente separados)

### 2. `skills-soberanos`
**URL:** https://github.com/MAXIMILIANOTARANTO/skills-soberanos  
**Rol:** Implementación práctica del ecosistema soberano con Q(t) operativo  
**Conexión con TCU:** Q(t) implementado en 6 dimensiones, validado contra principios TCU  
**Estado de validación:** Ver `VALIDACIÓN_TCU.md` en ese repo

---

## Mapa de Dependencias

```
tcu-unified-coherence-theory (TEORÍA)
    │
    ├── CORE/mathematical-core.md ──────── define el formalismo
    │                                         │
    │                                         ▼
    │                               skills-soberanos/core/
    │                               coherence_engine.py
    │                               (Q(t) implementado)
    │
    ├── STATE/tuc-current-state.md ────── estado canónico de la teoría
    │
    └── PAPERS/README.md ────────────────── validación empírica
            │
            └── Experimento 9 (próximo) ── requiere datos externos
                                           (EEG / LTER datasets)
```

---

## Protocolo de Sincronización

### Cuando TCU evoluciona (nuevo hallazgo en CORE/):
1. Actualizar `PAPERS/` si corresponde.
2. Notificar en `skills-soberanos` (abrir issue o PR de sincronización).
3. Validar que Q(t) en `skills-soberanos` sigue siendo consistente con la actualización teórica.

### Cuando `skills-soberanos` evoluciona (nuevo skill o mejora de Q(t)):
1. Verificar consistencia con principios TCU.
2. Si hay un hallazgo empírico nuevo, documentarlo en TCU (al nivel epistémico correcto).
3. Actualizar `STATE/tuc-current-state.md` si es relevante.

---

## Links Directos de Referencia

| Documento | URL |
|-----------|-----|
| Núcleo matemático TCU | https://github.com/MAXIMILIANOTARANTO/tcu-unified-coherence-theory/blob/main/CORE/mathematical-core.md |
| Estado actual del proyecto | https://github.com/MAXIMILIANOTARANTO/tcu-unified-coherence-theory/blob/main/STATE/tuc-current-state.md |
| Paper canónico | https://github.com/MAXIMILIANOTARANTO/tcu-unified-coherence-theory/blob/main/PAPERS/README.md |
| Validación TCU en skills-soberanos | https://github.com/MAXIMILIANOTARANTO/skills-soberanos/blob/main/VALIDACION_TCU.md |
| Arquitectura del ecosistema | https://github.com/MAXIMILIANOTARANTO/tcu-unified-coherence-theory/blob/main/MASTER_SOVEREIGN_ECOSYSTEM_ARCHITECTURE.md |

---

*Mapa actualizado al 2 de julio de 2026.*
