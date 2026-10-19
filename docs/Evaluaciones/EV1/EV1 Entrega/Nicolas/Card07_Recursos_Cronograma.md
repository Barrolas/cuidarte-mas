# Card 7 — Recursos y cronograma (Nicolás)

**Sección del informe:** 5. Recursos necesarios  
**Rúbrica:** IE4  
**Estado:** Listo para pegar en Word

---

## 5. Recursos necesarios

### 5.1 Recursos humanos

| Rol | Cantidad | Responsabilidad en Cuidarte+ |
|-----|----------|------------------------------|
| Analista / Tester | 1 | Diseña/ejecuta CP-01…CP-06; registra defectos |
| Desarrollador Backend | 1 | Soporte API Express, seeds, corrección hallazgos |
| Desarrollador Frontend | 1 | Soporte React/MUI, responsive, mensajes UI |
| Responsable de seguridad | 1 (puede ser el tester) | Checklist OWASP, RBAC, revisión de logs |
| Usuario adulto mayor (UAT) | ≥5 (ERS §3.1.1) | Sesiones de usabilidad del flujo paciente |
| Dupla académica | Skarlett + Nicolás | Integración normativa + técnica del plan |

### 5.2 Recursos técnicos

| Recurso | Versión / detalle | Uso en pruebas |
|---------|-------------------|----------------|
| Node.js | 18 (backend) / 20 (frontend build) | Runtime |
| React + MUI + Tailwind | Según ERS | UI E2E y usabilidad |
| Express + PostgreSQL 15 | Docker | API y persistencia |
| Docker Compose | `docker-compose.yml` del repo | Ambiente reproducible |
| Postman | Colección propia | Integración y seguridad API |
| Swagger UI | `http://localhost:4444/docs` | Contrato de endpoints |
| Jest | Backend/frontend según alcance | Unitarias |
| OWASP ZAP | Baseline scan | DAST ligero |
| Lighthouse (Chrome) | DevTools | Accesibilidad / performance FE |
| k6 o Apache JMeter | Script CRUD | NFR-PERF-1…3 |
| Navegadores | Chrome, Firefox, Edge (+ Safari si hay Mac) | NFR-COMPAT-1 |
| Dispositivos | Móvil 375px + tablet | NFR-COMPAT-2 |

### 5.3 Entorno de prueba

| Ambiente | URL / acceso típico | Propósito |
|----------|---------------------|-----------|
| Local Docker | Frontend `http://localhost:3333` · API `http://localhost:4444` | Smoke y desarrollo de casos |
| QA / staging | Misma topología con TLS si se configura proxy | Ejecución formal de la suite |

**Cuentas sintéticas (no usar datos reales de pacientes):**

| Usuario | Rol | Contraseña ejemplo (política ERS) |
|---------|-----|-----------------------------------|
| `admin.qa` | Administrador | `PruebaSegura#2026` |
| `medico.qa` | Médico | `PruebaSegura#2026` |
| `paciente.qa` | Paciente | `PruebaSegura#2026` |

Política de contraseña del ERS: mínimo 12 caracteres, mayúscula, minúscula, número y símbolo.

**Datos de prueba:** RUT/nombres ficticios; documentos PDF/JPG de prueba sin información clínica real (minimización / NFR-SEG-8).

### 5.4 Cronograma (3 semanas)

| Semana | Foco | Actividades | Entregables |
|--------|------|-------------|-------------|
| **1** | Preparación | Levantar Docker; seeds de roles; diseñar CP-01…CP-06; colección Postman | Ambiente OK + casos diseñados |
| **2** | P0/P1/P2 | Ejecutar funcional, API, seguridad, auditoría (CP-01…CP-04) | Bitácora de defectos parcial |
| **3** | P3/P4 + cierre | Rendimiento (CP-05), usabilidad/compatibilidad (CP-06), regresión, informe | Resultados + insumos matriz trazabilidad |

```text
Semana 1:  [Ambiente][Diseño casos][Postman base]
Semana 2:  [CP-01][CP-02][CP-03][CP-04] -----> defectos P0/P1
Semana 3:  [CP-05][CP-06][Regresión][Cierre] -> entrega a Skarlett (cobertura)
```

### 5.5 Estimación de esfuerzo

| Bloque de pruebas | % esfuerzo | Horas orientativas (dupla) |
|-------------------|------------|---------------------------|
| Funcional + auditoría | 30% | 9 h |
| Seguridad | 25% | 7,5 h |
| Rendimiento | 15% | 4,5 h |
| Usabilidad / compatibilidad | 20% | 6 h |
| Coordinación y reporte | 10% | 3 h |
| **Total** | **100%** | **~30 h** |

> Las 3 horas pedagógicas del encargo cubren el **diseño** del plan; la tabla anterior modela un ciclo de ejecución hipotético coherente con la estrategia (útil para IE4: recursos + cronograma).

---

**Checklist Card 7**

- [x] Recursos humanos
- [x] Recursos técnicos alineados al repo
- [x] Entorno Docker + cuentas por rol
- [x] Cronograma 3 semanas
- [x] Estimación de esfuerzo
