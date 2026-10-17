# Nota futura — Plan de pruebas ante caída de dependencias externas

**Fecha:** 2026-09-22  
**Contexto:** ISY1102 / Cuidarte+ y sistemas chilenos con integraciones externas  
**Uso:** incorporar en ciclos posteriores (EV2+, ampliación de NFR-DIS / resiliencia / cumplimiento)

---

## 1. Enfasis acordado

El plan de pruebas **no debe asumir** que los sistemas externos siempre están disponibles. Hay que diseñar casos explícitos de **caída, degradación y recuperación** de dependencias como:

| Dependencia (ejemplos) | Dominio típico | Riesgo de negocio |
|------------------------|----------------|-------------------|
| **SII** | Declaraciones, boletas, DTE, autenticación tributaria | Multas, plazos fiscales, bloqueo de emisión |
| **Previred** | Cotizaciones, remuneraciones, AFC/salud/AFP | Incumplimiento laboral/previsional, planilla incompleta |
| **FONASA / ISAPRE** (análogo salud) | Prestaciones, cobertura | Flujo clínico incompleto |
| **Registro Civil / ClaveÚnica** | Identidad | Login o alta de pacientes fallida |
| **Pasarela de pago (Transbank, etc.)** | Cobros | Ingresos detenidos |
| **SMTP / SMS / WhatsApp API** | Notificaciones | Usuario sin aviso de resultados |
| **Storage / BD / cola** | Persistencia propia | Disponibilidad del núcleo |

Para **Cuidarte+** hoy las integraciones estatales fuertes son futuras (FONASA, Registro Civil); el mismo **patrón de prueba** aplica si el producto o el caso semestral incorpora SII/Previred u otros terceros.

---

## 2. Qué más considerar (además de “el sistema externo está caído”)

### 2.1 Modos de falla (no solo off/on)

| Modo | Qué simular | Qué verificar |
|------|-------------|---------------|
| Caída total | Timeout / connection refused / 503 | Mensaje claro; no pantallazo; no datos corruptos |
| Degradación | Latencia alta (p. ej. 10–30 s) | Timeouts propios; no colgar UI/hilos |
| Error parcial | 200 con payload inválido; 401/403; firma inválida | Validación y rechazo seguro |
| Intermitencia | Fallos 1 de cada N | Reintentos con límite; sin duplicar transacciones |
| Mantenimiento anunciado | Ventana conocida | Modo degradado / banner / cola diferida |

### 2.2 Comportamiento del sistema propio

- **Degradación elegante:** ¿qué flujos críticos siguen (p. ej. ver pacientes/exámenes) aunque falle el tercero?
- **Cola / reintento:** ¿se encolan envíos a SII/Previred y se reprocesan al volver?
- **Idempotencia:** reintento no debe duplicar DTE, cotización o pago.
- **Circuit breaker / fail-fast:** dejar de martillar al tercero caído.
- **Configuración de timeout** distinta a la del delay artificial de desarrollo.
- **Mensajería al usuario/admin:** error accionable, sin filtrar secretos ni stack traces.
- **Auditoría:** registrar intento fallido, código de error externo y correlación (RF-5 / NFR-SEG-6).
- **Reconciliación:** al recuperar el servicio, job que complete lo pendiente y reporte inconsistencias.

### 2.3 Cumplimiento y calendario (muy relevante con SII/Previred)

- Plazos legales (declaraciones, remesas) → prueba de **alerta temprana** si el lote no se pudo enviar.
- Evidencia de “intentó y falló por causa externa” (log + timestamp) ante fiscalización.
- Minimización: no reenviar datos de más al recuperarse (Ley 21.719).
- Continuidad / ciberseguridad: incidente de disponibilidad reportable según criticidad (Ley 21.663 si aplica al contexto).

### 2.4 Cascadas y dependencias internas

- Caída de **API propia**, **PostgreSQL**, **storage de documentos**, **JWT/auth**.
- Caída de **DNS / red / proxy TLS**.
- Un tercero caído no debe tumbar **todo** el monolito (aislamiento de fallos).

### 2.5 Recuperación (tan importante como la caída)

1. Servicio externo vuelve.  
2. Cola drenada sin duplicados.  
3. Estados de negocio coherentes (pendiente → enviado → aceptado/rechazado).  
4. Notificación a operadores.  
5. Prueba de regresión corta del flujo feliz.

---

## 3. Tipos de prueba a sumar al plan

| Tipo | Objetivo | Ejemplo de caso |
|------|----------|-----------------|
| **Resiliencia / chaos ligero** | Falla inyectada del stub del tercero | Mock SII → 503; Previred → timeout |
| **Negocio degradado** | Core usable sin el tercero | Cuidarte+: clinical CRUD OK sin FONASA |
| **Recuperación** | Reproceso idempotente | Reenvío de lote Previred al 200 OK |
| **Rendimiento bajo falla** | Cola no explota memoria/CPU | N reintentos acotados |
| **Seguridad bajo error** | No leak de tokens del tercero | Logs saneados |
| **Usabilidad** | Mensaje comprensible (adulto mayor / operador) | “Servicio externo no disponible; reintento automático” |
| **Cumplimiento** | Evidencia de intento + alerta de plazo | Dashboard de lotes fallidos |

Herramientas tipicas: mocks/stubs (WireMock, MSW, stub en Express), feature flags, contratos Postman con escenarios de error, monitoreo sintético.

---

## 4. Plantilla corta de caso (para pegar en informes futuros)

| Campo | Contenido |
|-------|-----------|
| ID | CP-RES-0x |
| Descripción | Verificar comportamiento ante indisponibilidad de \<SII \| Previred \| …\> |
| Requerimiento | NFR-DIS-*; RF del flujo que usa el tercero; NFR-SEG-6 |
| Datos | Stub: HTTP 503 / timeout 30 s / respuesta malformada |
| Esperado | Flujo degradado documentado; auditoría del fallo; sin corrupción; reintento acotado |
| Aceptación | Core crítico operable **o** bloqueo controlado con mensaje y cola; al recuperar, sin duplicados |
| Tipo | No funcional — Disponibilidad / resiliencia |

---

## 5. Prioridad sugerida para el equipo

1. Inventario de **todas** las dependencias externas del ERS/caso.  
2. Clasificar: crítica (bloquea negocio legal) vs opcional (notificación).  
3. Un caso de **caída** + un caso de **recuperación** por dependencia crítica.  
4. Ligar a matriz de cobertura (IE5) y a NFR-DIS / normativa aplicable.  
5. No confundir con el `delayMiddleware` de demo: la latencia de prueba de resiliencia debe ser **explícita y controlada** (stub), no un sleep global que falsee NFR-PERF.

---

## 6. Relación con EV1 ya entregada

En EV1 la medición prolongada de **NFR-DIS-1 (99,5%)** y el chaos formal quedaron como **brecha / fuera de alcance**. Esta nota fija el **énfasis para el futuro**: disponibilidad no es solo “el server responde”, sino **qué pasa cuando SII, Previred u otros terceros no responden**.
