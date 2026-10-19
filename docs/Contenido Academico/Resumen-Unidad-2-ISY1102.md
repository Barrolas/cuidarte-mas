# ISY1102 · Seguridad y Calidad en el Desarrollo de Software
## Resumen de estudio de la Unidad 2 (EA2): "Garantizando la seguridad y calidad del software"

| Dato | Detalle |
|---|---|
| Resultado de aprendizaje | **RA2.** Evalúa la calidad y seguridad del software mediante la ejecución de pruebas funcionales y no funcionales, utilizando metodologías y herramientas que permitan detectar defectos, documentar hallazgos y comunicar resultados de manera ética y profesional. |
| Indicadores de logro | IL2.1 a IL2.5 |
| Actividades | 2.1 Estrategia y plan · 2.2 Casos de prueba · 2.3 Pruebas estáticas y ejecución · 2.4 Hallazgos e informe |
| Evaluaciones asociadas | EF3 (formativa), **EP3** encargo grupal (12 %) y **EP4** presentación individual (28 %) |
| Fuentes | Programa de asignatura PA-ISY1102; presentaciones 2.1.1, 2.2.1, 2.3.1 y 2.4.1; guías 2.1.2, 2.1.3, 2.2.2, 2.3.2 y 2.4.2; pautas EP3 y EP4; formato de informe EP3; carpeta de normativas de la EA1 |
| Versión | 2.0 · 19-10-2026 |

> Este resumen ordena y explica el material de la unidad. No reemplaza las pautas oficiales: si algo no calza, manda la pauta de la evaluación y, después, el programa de asignatura. Al final de cada sección hay preguntas de repaso.

---

## Índice

1. Mapa de la unidad
2. Conceptos base que la unidad da por sabidos
3. IL2.1 · Estrategia y plan de pruebas (2.1.1 – 2.1.3)
4. IL2.2 · Diseño de casos de prueba (2.2.1 – 2.2.2)
5. IL2.3 · Análisis estático y SonarQube (2.3.1)
6. IL2.4 · Ejecución, bitácora e incidentes (2.3.2)
7. IL2.5 · Informe técnico y de certificación (2.4.1 – 2.4.2)
8. Marco ético y normativo de la unidad
9. Herramientas: qué hace cada una y cuándo usarla
10. EP3 y EP4: qué se pide y cómo se evalúa
11. Inconsistencias detectadas en el material
12. Glosario
13. Autoevaluación final

---

## 1. Mapa de la unidad

### 1.1 De la EA1 a la EA2

La EA1 (RA1) se centró en **diseñar**: qué es calidad, qué tipos de prueba existen, qué normas aplican y cómo se arma un plan. La EA2 (RA2) toma ese plan y lo lleva a la práctica: se **diseñan casos ejecutables**, se **analiza el código**, se **ejecutan ciclos de prueba sobre el software real** levantado en Docker, se **clasifican los hallazgos** y se **comunica un dictamen** con respaldo técnico, ético y legal.

La lógica de la unidad es una cadena. Si un eslabón falla, los siguientes pierden valor:

```
Requisito (ERS) → Riesgo → Estrategia → Caso de prueba → Ejecución → Evidencia
      → Incidente (severidad) → Norma afectada → Recomendación → Dictamen
```

Un informe sólido permite recorrer esa cadena en ambos sentidos: desde un requisito hasta su resultado, y desde un incidente hasta el requisito y la norma que lo respaldan. Eso es la **trazabilidad**, y es el hilo que cruza todas las evaluaciones de la unidad.

### 1.2 Indicadores de logro y actividades

| IL | Redacción oficial (pautas EP3/EP4) | Actividad del programa | Material |
|---|---|---|---|
| **IL2.1** | Diseña estrategias de prueba considerando la seguridad y el cumplimiento normativo como componentes esenciales del aseguramiento de la calidad del software. | Act. 2.1 Diseña la estrategia y el plan de pruebas (4 h) | 2.1.1 PPT, 2.1.2 actividad, 2.1.3 guía Docker |
| **IL2.2** | Diseña casos de prueba que permitan verificar los estándares de calidad, seguridad, marcos legales y regulatorios. | Act. 2.2 Desarrolla y documenta casos de prueba (8 h) | 2.2.1 PPT, 2.2.2 actividad |
| **IL2.3** | Aplica herramientas de análisis estático para auditar el código fuente, identificando deficiencias de calidad y vulnerabilidades conforme a criterios legales y normativos. | Act. 2.3 Ejecuta y analiza pruebas estáticas de código (8 h) | 2.3.1 PPT |
| **IL2.4** | Ejecuta ciclos de prueba documentando hallazgos y vulnerabilidades de forma estructurada, utilizando estándares reconocidos de la industria. | Act. 2.3 / 2.4 | 2.3.2 actividad |
| **IL2.5** | Elabora informes técnicos que integren evidencias, hallazgos y recomendaciones, fundamentados en principios éticos, normativos y de mejora continua. | Act. 2.4 Ejecuta y documenta hallazgos, evaluando su impacto y gravedad (8 h) | 2.4.1 PPT, 2.4.2 actividad |

En el programa de asignatura el IL2.2 aparece con otra redacción: "Analiza segmentos de código críticos para detectar vulnerabilidades lógicas y de seguridad que escapan a las herramientas automáticas". Las dos redacciones se complementan: el diseño de casos de caja blanca y la revisión manual de código son justamente la forma de encontrar lo que una herramienta automática no ve (por ejemplo, un endpoint que valida el token pero no el rol).

### 1.3 Cómo se conecta cada actividad con la evaluación

| Actividad | Lo que produce | Dónde se usa en EP3 | Dónde se usa en EP4 |
|---|---|---|---|
| 2.1.2 Plan estratégico | Estrategia por técnica, riesgos, métricas, matriz | §3 Plan de pruebas | IE2 Estrategia (20 %) |
| 2.1.3 Docker | Entorno reproducible del caso | §3.4 Recursos y entorno | Demostración de ejecución |
| 2.2.2 Casos de prueba | Casos IEEE 829, matriz de trazabilidad, bug reports | §4 Diseño de casos, cobertura 100 % | IE4 Tipos de prueba (38 %), IE8 Trazabilidad |
| 2.3.1 SonarQube | Reporte de análisis estático con acciones | Criterios de calidad e incidentes | **IE6 Estático vs. ley (15 %)** |
| 2.3.2 Ejecución | Bitácora, bug reports, resumen | §5 Ejecución e incidentes | IE8 Proceso de ejecución (15 %) |
| 2.4.2 Informe | Dictamen, métricas, riesgos, conclusión | Estructura del informe y análisis ético-normativo | IE10 Recomendaciones (12 %) |

---

## 2. Conceptos base que la unidad da por sabidos

Varios términos se usan en las presentaciones sin definirlos de nuevo. Conviene tenerlos claros porque la rúbrica premia el lenguaje técnico preciso.

### 2.1 Error, defecto, falla e incidente

| Término | Significado | Ejemplo |
|---|---|---|
| **Error (equivocación)** | Acción humana que produce un resultado incorrecto. | El desarrollador compara la contraseña recibida con la guardada en texto plano. |
| **Defecto (bug)** | Imperfección en el código, el diseño o la documentación. | La función de login no usa una función de hash. |
| **Falla** | Comportamiento observable distinto del esperado al ejecutar el sistema. | Quien obtiene la tabla de usuarios ve todas las contraseñas. |
| **Incidente** | Registro formal de una desviación observada durante las pruebas, con su severidad y evidencia. | INC-01 / BUG-001, severidad Crítica. |

La diferencia importa al redactar: una prueba **estática** encuentra defectos sin ejecutar nada; una prueba **dinámica** provoca fallas y las registra como incidentes.

### 2.2 Verificación y validación

- **Verificación:** ¿se construyó el producto correctamente? Se contrasta con la especificación (ERS, diseño, estándares). Las revisiones de código y el análisis estático son verificación.
- **Validación:** ¿se construyó el producto correcto? Se contrasta con la necesidad real del usuario. Las pruebas de aceptación y de usabilidad con usuarios son validación.

### 2.3 Calidad, seguridad y cumplimiento como un solo objetivo

La presentación 2.1.1 insiste en que calidad y seguridad no son planes separados:

- **Enfoque de calidad:** cumplir requisitos funcionales y no funcionales; funcionalidad, rendimiento, experiencia de uso y compatibilidad.
- **Enfoque de seguridad:** prevenir brechas y accesos no autorizados, proteger información sensible, alinearse con normas y fortalecer la confianza del usuario.
- **Cumplimiento:** las normas (leyes, estándares técnicos, políticas internas) se convierten en requisitos verificables. Si una norma no termina en un caso de prueba o en un control revisable, no está realmente integrada al plan.

La integración de los tres es lo que evalúa el IE1 de EP3 (20 %): no basta con definirlos, hay que mostrar su relación con ejemplos del caso.

### 2.4 Principios del testing aplicados (ISTQB)

La unidad cita tres principios de forma explícita y usa otros de manera implícita:

1. **Las pruebas tempranas ahorran costos** (*shift-left*). Detectar un defecto en diseño o en código es mucho más barato que en producción. El material da cifras ilustrativas (hasta 10 veces más caro en producción en 2.2.1 y 2.1.2; hasta 100 veces en 2.3.1). Úsalas como argumento general, no como dato exacto del caso.
2. **El testing exhaustivo no es posible.** Hay que priorizar por riesgo.
3. **Las pruebas muestran la presencia de defectos, no su ausencia.** Un informe "sin hallazgos" no prueba que el sistema sea seguro; solo dice que, con esos casos y esa cobertura, no se encontraron.
4. **Agrupación de defectos:** los defectos tienden a concentrarse en pocos módulos (autenticación, control de acceso, manejo de archivos).
5. **Paradoja del pesticida:** repetir siempre los mismos casos deja de encontrar defectos nuevos; los casos se revisan y amplían.
6. **Las pruebas dependen del contexto:** un sistema de salud no se prueba con los mismos criterios que un sitio informativo.
7. **Falacia de la ausencia de errores:** un sistema sin defectos que no sirve a la necesidad del usuario sigue siendo un mal producto.

### 2.5 Estrategia, nivel, tipo y técnica

Estos cuatro términos se confunden con frecuencia en los informes. La rúbrica de EP3 (IE3, 38 %) y la de EP4 (IE4, 38 %) premian distinguirlos.

| Concepto | Pregunta que responde | Ejemplos |
|---|---|---|
| **Estrategia / enfoque** | ¿Cómo vamos a probar en general? | Basada en riesgos, manual, automatizada, mixta, *shift-left* |
| **Nivel** | ¿Qué parte del sistema probamos? | Unitaria, integración, sistema, aceptación |
| **Tipo** | ¿Qué característica de calidad probamos? | Funcional, rendimiento, seguridad, usabilidad, compatibilidad, regresión |
| **Técnica** | ¿Cómo derivamos los casos concretos? | Partición de equivalencia, valores límite, tabla de decisión, caminos básicos |

Ejemplo de redacción: "Para RF-1.1 (autenticación) se aplica una prueba **funcional** de **nivel sistema**, cuyos casos se derivan con **partición de equivalencia** y **valores límite**, dentro de una **estrategia basada en riesgos** que la ubica en el primer ciclo".

### 2.6 Tipos de prueba: catálogo de referencia

| Tipo | Propósito | Ejemplo de caso | Herramienta típica |
|---|---|---|---|
| **Funcional** | Comprobar que el sistema hace lo que el requisito dice | Registro de usuario con datos válidos crea la cuenta | Manual, Selenium |
| **Reglas de negocio** | Verificar restricciones del dominio | Un paciente solo ve sus propios exámenes | Manual, Postman/Swagger |
| **Integración** | Verificar la comunicación entre módulos (frontend–API–BD) | Un registro creado por la API aparece en la vista del usuario | Swagger, Selenium |
| **Regresión** | Confirmar que un cambio no rompió lo que funcionaba | Repetir el set de login tras corregir el hash | Selenium automatizado |
| **Humo (*smoke*)** | Confirmar que lo básico funciona antes de seguir | Login y carga de la página principal | Manual |
| **Seguridad: autenticación** | Probar el control de identidad | Credenciales inválidas, intentos repetidos, sesión expirada | Burp, ZAP, John the Ripper |
| **Seguridad: autorización** | Probar el control de acceso por rol | Usuario sin rol de administrador llama a un endpoint de administración | Burp, Postman |
| **Seguridad: entradas** | Probar la resistencia a inyección y datos maliciosos | `' OR '1'='1' --` en el login | SQLMap, ZAP |
| **Seguridad: configuración** | Revisar cabeceras, CORS, mensajes de error, versiones expuestas | Respuesta 500 con el detalle del error interno | Nikto, ZAP |
| **Rendimiento: carga** | Medir tiempos con la carga esperada | 200 usuarios concurrentes, tiempo de respuesta bajo el umbral | JMeter |
| **Rendimiento: estrés** | Encontrar el punto de quiebre | Subir usuarios hasta que la tasa de error supere el 5 % | JMeter |
| **Usabilidad** | Evaluar facilidad de uso con usuarios representativos | 5 usuarios completan una tarea sin ayuda | Observación, encuesta |
| **Accesibilidad** | Verificar uso por personas con discapacidad | Navegación completa con teclado; contraste suficiente | Lighthouse, revisión manual |
| **Compatibilidad** | Verificar funcionamiento en navegadores y dispositivos | Funciona en Chrome, Firefox y Edge, y en pantalla de 5" | Selenium, revisión manual |
| **Disponibilidad / recuperación** | Verificar continuidad y respaldo | Restaurar un respaldo y comprobar que los datos quedan íntegros | Revisión operativa |
| **Cumplimiento normativo** | Verificar que un requisito legal se traduce en un control | Cada descarga de un documento queda registrada con usuario y fecha | Manual, revisión de logs |

**No funcionales (IE5, 15 % en EP3):** la rúbrica pide relacionar cada prueba no funcional con su **propósito y contexto**. No basta con "se hará prueba de rendimiento"; hay que decir qué requisito la exige, qué umbral se usa, por qué ese umbral importa en el negocio y con qué herramienta se mide.

> **Repaso 2.** ¿Qué diferencia hay entre un defecto y una falla? ¿Por qué un informe sin hallazgos no demuestra que el sistema sea seguro? Clasifica "valores límite" y "prueba de carga" como tipo o técnica.

---

## 3. IL2.1 · Estrategia y plan de pruebas

### 3.1 Qué es un plan de pruebas

Según 2.1.1, un plan de pruebas es **un marco estratégico que organiza, estructura y guía todas las actividades de validación del producto**. Su propósito es asegurar la calidad, detectar defectos en etapas tempranas y validar la seguridad antes del lanzamiento. Su valor práctico es triple: reduce riesgos, mejora la comunicación entre equipos y da una base objetiva para decidir si el software se entrega.

Un plan no es una lista de casos. Los casos son una consecuencia del plan.

### 3.2 Elementos del plan

El material reúne los elementos en cuatro bloques (2.1.1: alcance y objetivos, estrategia, recursos y roles, criterios de aceptación) y el formato de EP3 y la rúbrica IE7 los amplían. La lista completa que conviene cubrir es:

| # | Elemento | Qué debe contener | Error típico |
|---|---|---|---|
| 1 | **Introducción** | Contexto del sistema, propósito del plan, estructura del documento | Describir la empresa y no el software |
| 2 | **Alcance** | Qué módulos y requisitos se prueban y **qué queda fuera y por qué** | Omitir las exclusiones |
| 3 | **Objetivos** | Objetivos medibles (general y específicos) | Objetivos vagos: "asegurar la calidad" |
| 4 | **Criterios de calidad** | Usabilidad, rendimiento, estabilidad, confiabilidad, mantenibilidad, seguridad y normativa | Listar atributos sin umbrales |
| 5 | **Estrategia** | Enfoque (manual, automatizado, mixto), etapas, priorización, criterios de entrada y salida | Confundir estrategia con lista de herramientas |
| 6 | **Tipos de prueba** | Cada tipo con su justificación y los requisitos que cubre | Nombrar tipos sin decir para qué |
| 7 | **Criterios de aceptación** | Condiciones transversales para aprobar casos y para cerrar el ciclo | Criterios no medibles |
| 8 | **Recursos** | Humanos (roles), técnicos (software, versiones, navegadores) y entorno (desarrollo, QA) | No declarar versiones |
| 9 | **Herramientas** | Cada herramienta con el tipo de prueba y el requisito que respalda | Herramientas que luego no se usan |
| 10 | **Cronograma** | Fases y fechas, priorizadas por riesgo | Cronograma sin relación con los riesgos |
| 11 | **Riesgos y mitigación** | Retrasos, falta de cobertura, fallos críticos, dependencias externas | Solo riesgos del producto, no del proyecto de pruebas |
| 12 | **Trazabilidad** | Matriz requisito ↔ caso ↔ riesgo ↔ resultado | Matriz parcial |

**Ejemplo de objetivo bien escrito** (2.1.1): "Verificar que el sistema de autenticación implementa cifrado seguro, maneja correctamente las sesiones y previene accesos no autorizados". Es específico, se puede comprobar y apunta a requisitos concretos.

### 3.3 Criterios de entrada, salida y suspensión

| Criterio | Pregunta | Ejemplo |
|---|---|---|
| **Entrada** | ¿Cuándo se puede empezar a ejecutar? | Contenedores arriba; datos de prueba cargados; casos revisados; smoke test aprobado |
| **Suspensión** | ¿Cuándo se detiene la ejecución? | El smoke test falla; el entorno se cae; un defecto bloquea el flujo principal |
| **Reanudación** | ¿Qué se necesita para seguir? | Corrección desplegada y verificada |
| **Salida** | ¿Cuándo se da por terminado el ciclo? | 100 % de los casos de prioridad alta ejecutados; 0 defectos críticos abiertos; cobertura de requisitos sobre el umbral |

### 3.4 Estrategia basada en riesgos

El riesgo combina la **probabilidad** de que algo falle con el **impacto** si falla. La priorización resultante define qué se diseña con más detalle, qué se ejecuta primero y qué recibe revisión de código.

| | Impacto bajo | Impacto medio | Impacto alto |
|---|---|---|---|
| **Probabilidad alta** | Media | Alta | **Crítica** |
| **Probabilidad media** | Baja | Media | Alta |
| **Probabilidad baja** | Baja | Baja | Media |

Criterios que el material entrega para estimar el riesgo:

- **Exposición:** primero los módulos expuestos directamente a internet, como API públicas, formularios de autenticación y pasarelas de pago (2.1.1).
- **Complejidad:** módulos con complejidad ciclomática V(G) > 20 requieren más profundidad, revisión de código, pruebas negativas y de estrés, y prioridad en el cronograma (2.1.2).
- **Sensibilidad de los datos:** credenciales, datos personales y datos sensibles (salud, finanzas).
- **Impacto en el negocio:** funcionalidades centrales para el usuario.

### 3.5 Combinación de enfoques (actividad 2.1.2)

La actividad 2.1.2 pide actuar como **QA Lead** de una aplicación de banca móvil y justificar la mezcla de técnicas. El caso es genérico, pero el razonamiento se traslada a cualquier sistema. El plan debe lograr un sistema confiable, eficiente, seguro, trazable y sostenible en el tiempo.

| Enfoque | Dónde se aplica | Qué detecta |
|---|---|---|
| **Caja negra** | Módulos funcionales vistos por el usuario (transferencias, pagos, registro, formularios) | Errores de validación de datos, de flujo de usuario, de reglas de negocio y de usabilidad y consistencia |
| **Caja blanca** | Lógica crítica donde la precisión es esencial (cálculo de intereses, validación de OTP, cifrado, límites de transacción, control de roles) | Fallos lógicos, desbordamientos, ramas no probadas y vulnerabilidades. Técnicas: caminos independientes, análisis de bucles, cobertura de decisiones y condiciones |
| **Híbrido** | Integración entre aplicación y backend | Errores en la comunicación, en el manejo de errores de la API, en la sincronización de estados y en la integridad de datos en tránsito |

**Análisis de flujo de datos aplicado a seguridad** (paso 2 de 2.1.2). Se sigue cada dato sensible desde que entra hasta que se guarda o se descarta, y se verifica que:

- las credenciales no se almacenen en texto plano;
- no haya filtraciones en logs, variables temporales ni excepciones;
- las sesiones estén cifradas;
- los tokens se invaliden correctamente al cerrar sesión o al expirar.

El material pide incluir escenarios de ataque relevantes "sin convertir la actividad en pentesting": se describe el escenario y el caso que lo detectaría, sin llegar a explotar el sistema.

**Métricas de éxito propuestas** (2.1.2):

| Métrica | Umbral de ejemplo | Por qué importa |
|---|---|---|
| Confiabilidad | ≥ 95 % | El usuario debe poder completar sus operaciones sin fallas |
| Cobertura de requisitos | ≥ 90 % (EP3 exige 100 %) | Ningún requisito queda sin evidencia |
| Defectos críticos detectados antes de producción | ≥ 98 % | Un defecto crítico en producción tiene costo económico, legal y reputacional |
| Reducción del tiempo de ejecución por automatización | Se mide contra la ejecución manual | Permite repetir la regresión en cada cambio |

**Herramienta de gestión** (paso 3): se elige una (TestRail, Azure Test Plans, Jira + Zephyr) y se justifica por cómo mejora la trazabilidad, facilita la reutilización y apoya auditorías y cumplimiento normativo.

**Entregables de 2.1.2:** matriz de trazabilidad (requisito, caso, riesgo, módulo), cronograma basado en riesgos (impacto, probabilidad y complejidad) y protocolo de mantenimiento del plan (cómo se actualizan los casos ante cambios regulatorios, funcionales o de arquitectura).

### 3.6 Recursos, roles e independencia

- **Independencia del testing:** quien prueba no debería ser quien desarrolló; aporta objetividad y mirada crítica.
- **Roles especializados:** líder de QA, testers funcionales, especialistas en automatización y especialistas en seguridad.
- **Entornos:** aislados, reproducibles y con escáneres actualizados.
- **Comunicación:** documentar → revisar con los interesados → comunicar avances → aprobar formalmente antes de ejecutar (ciclo de 2.1.1).

Desafíos comunes que el material identifica y su solución:

| Desafío | Solución propuesta |
|---|---|
| Pruebas que empiezan tarde | *Shift-left*: integrar pruebas desde el diseño |
| Falta de especialistas | Capacitación continua, certificaciones y mentorías internas |
| Desalineación entre equipos | Ceremonias regulares, documentación compartida y objetivos comunes |

**Flujo de trabajo de seis pasos** (2.1.1): (1) definir alcance y objetivos medibles; (2) diseñar una estrategia basada en riesgos; (3) planificar recursos y cronograma; (4) elaborar casos funcionales y de seguridad trazables; (5) integrar automatización y KPI de cobertura, eficacia y eficiencia; (6) documentar y revisar de forma continua.

### 3.7 Automatización y seguridad continua

- **Automatización de regresión:** casos repetitivos que se ejecutan en cada cambio de código.
- **Seguridad continua:** SAST y DAST integrados al *pipeline* de integración y despliegue continuo (CI/CD). Este tema se profundiza en la EA3.
- El material presenta cifras de beneficio (70 % menos tiempo de regresión, 3 veces más casos con la misma inversión). Son ilustrativas; en un informe es mejor medir el propio ahorro.

**SAST frente a DAST**

| | SAST (estático) | DAST (dinámico) |
|---|---|---|
| ¿Requiere ejecutar la app? | No | Sí |
| ¿Qué analiza? | Código fuente | Aplicación desplegada, desde afuera |
| ¿Cuándo se usa? | Desde que existe código | Cuando hay un entorno funcionando |
| Fortaleza | Indica archivo y línea | Confirma que la falla es explotable |
| Debilidad | Falsos positivos; no ve la configuración del despliegue | No ve el código; depende de la cobertura del rastreo |
| Herramientas del curso | SonarQube | OWASP ZAP, Burp Suite, Nikto, SQLMap |

### 3.8 Marcos y estándares de referencia del plan

| Marco | Para qué se usa en el plan |
|---|---|
| **IEEE 829** | Plantillas de documentación de pruebas: plan, diseño, casos, procedimientos, registro de incidentes e informe resumen. Fue reemplazado por la serie ISO/IEC/IEEE 29119, pero el curso usa 829 como referencia de plantilla. |
| **ISTQB** | Vocabulario, principios y proceso de pruebas. |
| **OWASP WSTG** | Guía de escenarios de pruebas de seguridad web (autenticación, autorización, sesiones, validación de entradas, manejo de errores). |
| **OWASP Top 10** | Lista de las categorías de riesgo más críticas en aplicaciones web; la edición vigente es la de 2025. Sirve para clasificar hallazgos. |
| **NIST Cybersecurity Framework** | Marco de gestión del riesgo de ciberseguridad a nivel organizacional. La versión 2.0 (2024) tiene seis funciones: Gobernar, Identificar, Proteger, Detectar, Responder y Recuperar. |

### 3.9 Docker en el plan de pruebas (2.1.1 y guía 2.1.3)

**Por qué Docker.** Una **imagen** es una plantilla inmutable que encapsula sistema operativo, bibliotecas, dependencias y configuración. Un **contenedor** es una instancia en ejecución de esa imagen. El flujo es `Dockerfile → imagen → contenedor`. Para pruebas esto significa entornos replicables, versiones controladas, aislamiento y la posibilidad de volver a un estado anterior.

**Buenas prácticas de seguridad en imágenes** (que también pueden ser hallazgos):

| Práctica | Qué revisar |
|---|---|
| Imágenes base oficiales y mínimas (por ejemplo, Alpine) | Menor superficie de ataque |
| Imágenes endurecidas (*hardened*) | Menos vulnerabilidades conocidas desde el inicio |
| Minimizar capas y dependencias | Cada componente extra es un posible vector |
| Privilegios mínimos | El proceso no debería correr como `root` dentro del contenedor |
| Aislamiento | Espacios de nombres y restricción de capacidades de Linux |
| Versionado y etiquetado | Versionado semántico y etiquetas descriptivas con fecha y cambios |
| Secretos fuera de la imagen | Variables sensibles en un `.env` no versionado o en un gestor de secretos |
| Automatización | Construcción y despliegue de imágenes en CI/CD para reducir errores humanos |

**Procedimiento de la guía 2.1.3** (individual, 2 horas, IL2.1):

1. Tener Docker instalado (sitio oficial) y abrir el proyecto en Visual Studio Code.
2. Descomprimir `CodigoFuenteA.zip` o `CodigoFuenteB.zip`, según el caso asignado.
3. Reconocer la estructura:
   - `BACKEND`: código de la API;
   - `FRONTEND`: código del cliente;
   - `.env`: variables de entorno que usa Docker para construir las imágenes;
   - `docker-compose.yml`: define cómo se construyen las imágenes, sus variables y la orquestación entre contenedores;
   - `README.md`: información del proyecto.
4. Iniciar Docker, abrir una terminal en la raíz y ejecutar `docker-compose up -d`.
5. Verificar en Docker que existan **tres contenedores** activos (base de datos, API y cliente) con el nombre del caso.
6. Abrir el cliente y la documentación de la API (Swagger en `/docs`). Los puertos se leen en el contenedor o en `docker-compose.yml`:

| Componente | Caso A (Atlas) | Caso B (Cuidarte+) |
|---|---|---|
| Cliente (frontend) | `http://localhost:3350` | `http://localhost:3333` |
| API y Swagger | `http://localhost:4450/docs` | `http://localhost:4444/docs` |
| PostgreSQL | `localhost:15432` | `localhost:15442` |

Sin un entorno estable no hay ejecución confiable. Por eso el levantamiento del entorno es un **criterio de entrada** del plan, y su descripción (versiones, puertos, datos semilla) forma parte de la sección de recursos del informe.

> **Repaso 3.** Nombra cinco elementos del plan y un error típico de cada uno. ¿Qué módulo priorizarías primero en un sistema con login, reportes y un formulario de contacto, y por qué? ¿Qué diferencia hay entre una imagen y un contenedor?

---

## 4. IL2.2 · Diseño de casos de prueba

### 4.1 Definiciones

- **Caso de prueba (IEEE 610):** conjunto estructurado de entradas, condiciones de ejecución y resultados esperados, desarrollado para validar un requisito específico del sistema.
- **Escenario de prueba:** el **qué**; una situación de alto nivel. Ejemplo (2.2.2): "Validar el proceso de recuperación de contraseña".
- **Caso de prueba:** el **cómo**; los pasos detallados. Del escenario anterior salen al menos tres casos: recuperación con correo válido, intento con correo no registrado y expiración del enlace (este último es de seguridad).

Un buen caso es **específico, medible, reproducible y trazable** (2.1.1). Cualquier integrante del equipo debería poder ejecutarlo y obtener el mismo resultado. Además, los casos bien diseñados sirven de guía uniforme de ejecución, mejoran la colaboración entre desarrollo, QA y negocio, y facilitan la automatización (2.2.1).

### 4.2 Campos del caso de prueba

La unidad trabaja con tres listas de campos que conviene unificar en una sola plantilla:

| Campo | 2.2.2 (IEEE 829) | Formato EP3 | Pauta EP3 | Para qué sirve |
|---|:---:|:---:|:---:|---|
| ID del caso | ✔ | ✔ | ✔ | Identificación única (CP-01, CP-SEG-001) |
| Nombre | | ✔ | | Lectura rápida en la bitácora |
| Descripción / objetivo | | ✔ | ✔ | Qué se busca comprobar |
| Requisito asociado (código ERS) | | ✔ | ✔ | Trazabilidad |
| Tipo de prueba | | | ✔ | Clasificación (IE3) |
| Prioridad (por riesgo) | ✔ | | | Orden de ejecución |
| Precondiciones | ✔ | ✔ | | Estado inicial necesario |
| Pasos de ejecución | ✔ | ✔ | | Acciones atómicas numeradas |
| Datos de prueba / de entrada | ✔ | ✔ | ✔ | Valores exactos usados |
| Resultado esperado | ✔ | ✔ | ✔ | Comportamiento correcto |
| Criterio de aceptación | | ✔ | ✔ | Condición objetiva de aprobación |
| Resultado obtenido | ✔ | | | Se completa al ejecutar |
| Estado | ✔ | | | Aprobado / Falla / Bloqueado |
| Postcondiciones | (2.2.1) | | | Estado en que queda el sistema |

**Ejemplo completo de caso de seguridad** (adaptado del ejemplo de 2.1.1, válido para cualquier sistema con login):

| Campo | Contenido |
|---|---|
| ID | CP-SEG-001 |
| Nombre | Rechazo de inyección SQL en el inicio de sesión |
| Requisito | Requisito de autenticación y de validación de entradas del ERS |
| Tipo | Seguridad (validación de entradas) |
| Prioridad | Alta |
| Precondiciones | Servicio activo; existe al menos un usuario registrado |
| Pasos | 1. Abrir la pantalla de login. 2. Ingresar `' OR '1'='1' --` en usuario y cualquier valor en contraseña. 3. Enviar. 4. Revisar la respuesta y los logs |
| Datos | Usuario: `' OR '1'='1' --`; contraseña: `x` |
| Resultado esperado | Acceso denegado; mensaje genérico; sin detalles de base de datos en la respuesta; evento registrado en el log de seguridad |
| Criterio de aceptación | HTTP 400 o 401, ninguna sesión creada y ningún texto de error SQL visible |

### 4.3 Técnicas de caja negra

Se centran en entradas y salidas, sin conocer la implementación. Validan el sistema desde la perspectiva del usuario.

**a) Partición de equivalencia.** Divide el dominio de entrada en clases donde el sistema debería comportarse igual; basta un valor representativo por clase.

Pasos: (1) identificar el dominio de entrada; (2) dividir en clases equivalentes, válidas e inválidas; (3) elegir un valor por clase.

Ejemplo (2.2.1): campo que acepta números de 1 a 10.

| ID | Valor | Clase | Resultado esperado |
|---|---|---|---|
| TC-01 | 5 | Válida (1–10) | Aceptado |
| TC-02 | -3 | Inválida inferior | Rechazado con mensaje |
| TC-03 | 15 | Inválida superior | Rechazado con mensaje |
| TC-04 | "abc" | Inválida de tipo | Rechazado con mensaje |

Si el dominio tiene dos rangos válidos (1–10 y 20–30), aparecen clases adicionales; el material lo usa para mostrar que las clases dependen del requisito y no de una regla fija.

**b) Análisis de valores límite (BVA).** Prueba los bordes de cada partición, porque ahí aparecen los errores de comparación (usar `<` en lugar de `≤`). Para cada límite se prueba el valor anterior, el límite y el siguiente.

| Caso | Valor | Descripción | Esperado |
|---|---|---|---|
| 1 | 0 | Justo antes del límite inferior | Rechazado |
| 2 | 1 | Límite inferior | Aceptado |
| 3 | 2 | Dentro del rango | Aceptado |
| 4 | 9 | Cerca del límite superior | Aceptado |
| 5 | 10 | Límite superior | Aceptado |
| 6 | 11 | Justo después del límite superior | Rechazado |

Aplicación típica: largo mínimo de contraseña. Si el requisito pide 12 caracteres o más, se prueban 11 (rechazo), 12 (aceptación) y 13 (aceptación). Para un nombre de 1 a 100 caracteres (ejemplo de 2.2.2): 0, 1, 2, 99, 100 y 101.

Partición y valores límite se usan juntas: la partición define las clases y los valores límite prueban sus fronteras.

**c) Tablas de decisión.** Útiles cuando el resultado depende de combinaciones de condiciones. Componentes: **condiciones**, **combinaciones (reglas)** y **acciones**. Con *n* condiciones binarias hay 2ⁿ reglas. Ventajas: muestran todas las combinaciones, evitan omisiones, revelan inconsistencias en la lógica de negocio y son legibles para personas no técnicas.

Ejemplo (2.2.1): formulario con nombre y correo.

| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| C1 Nombre completo | No | No | Sí | Sí |
| C2 Correo válido | No | Sí | No | Sí |
| Botón habilitado | No | No | No | Sí |
| Permitir envío | No | No | No | Sí |
| Mensaje | Ambos campos | Falta nombre | Correo inválido | — |

Aplicación típica en seguridad: rol del usuario × recurso solicitado × propiedad del recurso → permitir o denegar.

### 4.4 Técnicas de caja blanca

Requieren acceso al código, a los flujos de control y a la arquitectura. Validan que la lógica interna sea correcta y que no queden caminos sin ejecutar.

| Técnica | Qué asegura | Ejemplo |
|---|---|---|
| **Cobertura de sentencias** | Cada línea se ejecuta al menos una vez | Mínimo aceptable, no suficiente |
| **Cobertura de decisiones (ramas)** | Cada `if` se evalúa verdadero y falso | El `if (!user)` del login con usuario existente y con usuario inexistente |
| **Cobertura de condiciones** | Cada condición simple dentro de una expresión compuesta toma ambos valores | `if (token && rol === 'admin')`: token válido sin rol, rol sin token, ambos |
| **Caminos básicos** | Cada camino linealmente independiente se ejecuta al menos una vez | Número de caminos = V(G) |
| **Pruebas de bucles** | Ciclos `for`, `while` y `do-while` con distintas iteraciones | Ver tabla siguiente |
| **Flujo de datos** | Uso correcto de variables: definición–uso | Variable usada sin definir; definida y redefinida sin uso; dato sensible que llega a un log |

**Complejidad ciclomática (McCabe, 1976).** Mide el número de caminos linealmente independientes y, por tanto, el **mínimo de casos** para cubrir todos los caminos básicos.

- Fórmula: **V(G) = E − N + 2P** (E = aristas, N = nodos, P = componentes conectados; para una sola función, P = 1).
- Atajo práctico: V(G) = número de decisiones simples + 1.

Ejemplo: un grafo con 9 aristas, 7 nodos y 1 componente → V(G) = 9 − 7 + 2 = **4** → al menos 4 casos. La pregunta de la pausa de 2.2.1 lo confirma: con V(G) = 5 se necesitan como mínimo 5 casos.

| V(G) | Interpretación (2.2.1) | Acción |
|---|---|---|
| 1–10 | Código simple, fácil de probar | Pruebas normales |
| 11–20 | Complejidad moderada | Más casos, revisión |
| 21–50 | Código complejo | Refactorizar; prioridad alta en el plan |
| > 50 | Muy complejo, alto riesgo | Refactorizar antes de certificar |

**Pruebas de bucles**

| Tipo de bucle | Cómo se prueba |
|---|---|
| Simple (máximo *n*) | 0 iteraciones, 1, 2, un valor típico *m* < *n*, *n*−1, *n* y *n*+1 |
| Anidado | Desde el más interno hacia afuera, dejando los demás en valores mínimos |
| Concatenado | Si son independientes, como simples; si dependen entre sí, como anidados |

### 4.5 Técnicas híbridas

- **Basadas en riesgo:** se elige técnica y profundidad según el riesgo del módulo.
- **Exploratorias estructuradas:** sesiones con objetivo y tiempo definidos, donde el tester aprende y prueba a la vez. Complementan la matriz formal; no la reemplazan.

**Combinación recomendada** (2.2.1): caja negra para interfaces, caja blanca para lógica y enfoque híbrido para integración. En un login: partición y valores límite para las credenciales; caminos básicos para la lógica de autenticación, cifrado y sesión. "Ninguna técnica por sí sola garantiza la calidad".

### 4.6 Proceso de creación de casos

1. **Identificar requisitos:** leer el ERS y extraer condiciones de prueba normales, excepcionales y de borde.
2. **Seleccionar la técnica:** según el contexto, la complejidad y los recursos.
3. **Diseñar casos detallados:** con todos los campos de 4.2.
4. **Revisar y refinar:** revisión por pares para eliminar ambigüedades, omisiones y redundancias.

**Principios** (2.2.1): calidad antes que cantidad; trazabilidad entre requisitos y casos; supuestos y limitaciones documentados; revisión por pares; herramientas adecuadas; medición y mejora continua.

### 4.7 Errores comunes en el diseño (2.2.1)

| Error | Solución |
|---|---|
| Ambigüedad ("el sistema funciona correctamente") | Lenguaje específico, medible y verificable |
| Cobertura insuficiente (sin casos negativos ni de borde) | Combinar técnicas y pensar en modos de falla |
| Redundancia | Consolidar casos duplicados |
| Dependencias no documentadas | Declarar todas las precondiciones |
| Falta de mantenimiento | Revisar los casos con cada cambio de requisitos |
| Casos demasiado complejos | Casos atómicos: un objetivo por caso |

### 4.8 Matriz de pruebas por categoría (actividad 2.2.2)

| Categoría | Pregunta | Escenario sugerido | Técnica / caso |
|---|---|---|---|
| **A. Calidad funcional** | ¿Hace lo que el usuario pidió? | Registro de nuevos usuarios | Valores límite (nombre de 1 y de 100 caracteres) |
| **B. Seguridad** | ¿Resiste ataques comunes? | Bypass de autenticación | Inyección SQL en el login; acceso a una URL interna sin sesión |
| **C. Usabilidad e interfaz** | ¿Es intuitivo y accesible? | Navegación en móviles | Todos los botones se pueden pulsar en pantalla de 5" |

La guía agrega un consejo: si se encuentra un error, documentar el **reporte de defecto** con severidad y pasos para reproducirlo. Eso demuestra un ciclo de calidad completo.

### 4.9 Matriz de trazabilidad

Conecta cada requisito con sus casos y su resultado. Demuestra que ningún requisito quedó sin probar. En EP3 se exige **cobertura del 100 %** de los requisitos del ERS (funcionales, no funcionales, reglas de negocio, seguridad y normativa).

| Requisito | Descripción | Riesgo | Caso(s) | Tipo | Resultado | Incidente |
|---|---|---|---|---|---|---|
| RF-1.1 | Inicio de sesión | Alto | CP-01, CP-SEG-001 | Funcional / Seguridad | Aprobado / Falla | — / INC-xx |
| NFR-PERF-1 | Tiempo de respuesta | Medio | CP-05 | Rendimiento | … | … |
| RB-1 | Regla de negocio | Alto | CP-02 | Reglas de negocio | … | … |

Reglas para que la matriz sirva:

- **Diseñado no es cubierto.** En la ejecución, un requisito está cubierto solo si su caso se ejecutó; si falló, queda cubierto con incidente.
- La cobertura se calcula como requisitos con al menos un caso ejecutado ÷ total de requisitos del ERS.
- Un caso puede cubrir varios requisitos, pero cada requisito debe tener al menos un caso.
- Los requisitos normativos (por ejemplo, registrar quién accede a un dato) también llevan caso.

### 4.10 Herramientas de gestión de casos

TestRail, Jira + Zephyr, Azure Test Plans, qTest, TestLink y PractiTest. Beneficios: documentación centralizada con versiones, reutilización, reportes, trazabilidad entre requisitos, casos y defectos, integración con automatización y colaboración. En el curso puede bastar una planilla bien estructurada, siempre que mantenga la trazabilidad.

> **Repaso 4.** Diseña los casos de valores límite para "edad entre 18 y 65". Calcula V(G) para una función con tres `if` independientes. Arma una tabla de decisión para "rol (admin/médico/paciente) × recurso (propio/ajeno)". ¿Qué diferencia hay entre un escenario y un caso?

---

## 5. IL2.3 · Análisis estático y SonarQube

### 5.1 Qué es una prueba estática

Es el análisis del código fuente, del diseño o de la documentación **sin ejecutar el programa**. Es preventiva: encuentra defectos, vulnerabilidades y malas prácticas antes de que se transformen en fallas. Sus beneficios son la detección temprana, la reducción de costos de depuración y mantenimiento, la mejora de la legibilidad y la mantenibilidad, y el apoyo al cumplimiento normativo y a las auditorías.

| | Estáticas | Dinámicas |
|---|---|---|
| ¿Ejecutan el sistema? | No | Sí |
| Objeto | Código, diseño, documentación | Software en funcionamiento |
| Técnicas | Revisión, inspección, *walkthrough*, análisis automatizado (SAST) | Funcionales, DAST, carga, usabilidad |
| Resultado | Defectos con ubicación exacta | Fallas observadas y su comportamiento |

Son complementarias: el análisis estático señala dónde puede haber un problema y la prueba dinámica confirma si se puede explotar.

### 5.2 Técnicas de revisión manual

| Técnica | Cómo funciona | Formalidad |
|---|---|---|
| **Revisión manual** | Un revisor experto lee el código o la documentación | Baja |
| **Walkthrough** | El autor guía al equipo por el código o el diseño | Media |
| **Inspección** | Revisión formal con roles (moderador, autor, lector, registrador), lista de verificación y registro de defectos | Alta |
| **Análisis automatizado** | Una herramienta busca patrones de error y vulnerabilidades | Automática |

La revisión manual encuentra lo que las herramientas no ven: errores de **lógica de negocio** y de **autorización**. Ejemplos típicos: un endpoint que exige token pero no verifica el rol; un recurso que se entrega sin comprobar que pertenece al usuario; una eliminación física de datos que deberían conservarse; un registro de auditoría que no incluye las lecturas.

### 5.3 Obtención de evidencias en pruebas estáticas

1. **Documentar hallazgos:** cada descubrimiento de la revisión de código y diseño.
2. **Registrar defectos:** con detalle suficiente para corregirlos.
3. **Estandarizar formatos:** plantillas IEEE 829 para consistencia y trazabilidad.

Un registro de defecto estático contiene: descripción, **ubicación exacta (archivo y línea)**, regla o criterio incumplido, gravedad, recomendación y responsable. Se gestiona en Jira, Redmine, una hoja de cálculo compartida o el propio reporte exportado de la herramienta.

### 5.4 SonarQube: qué es y cómo se usa

SonarQube es una plataforma de análisis estático que detecta problemas de **seguridad** (vulnerabilidades), **confiabilidad** (bugs) y **mantenibilidad** (*code smells*) en más de 25 lenguajes, se integra en *pipelines* CI/CD y permite definir **Quality Gates** (umbrales de aprobación). Su documentación es bibliografía obligatoria del curso.

**Flujo del laboratorio (2.3.1):**

1. **Instalar y configurar** SonarQube Server (en el curso, como contenedor Docker).
2. **Importar el proyecto:** crear el proyecto y generar el token de análisis.
3. **Definir reglas:** perfil de calidad (*Quality Profile*) y Quality Gate.
4. **Escanear** el código del backend y del frontend con SonarScanner. Puede tardar de minutos a horas según el tamaño.
5. **Visualizar resultados** en el panel.
6. **Identificar defectos** y áreas críticas.
7. **Registrar evidencia manual:** exportar el reporte, complementarlo con anotaciones de contexto, comentar cada defecto relevante, documentar la acción correctiva y asignar un responsable.

### 5.5 Cómo leer el panel de SonarQube

| Métrica | Qué mide | Cómo interpretarla |
|---|---|---|
| **Bugs / Confiabilidad** | Código que probablemente produce un comportamiento incorrecto | Calificación de A (sin problemas) a E (al menos un problema bloqueante) |
| **Vulnerabilidades / Seguridad** | Código explotable | Cualquier vulnerabilidad de severidad alta pasa a incidente |
| **Security Hotspots** | Código sensible que **requiere revisión humana**; no es necesariamente una vulnerabilidad | Se revisa y se marca como seguro o a corregir. El porcentaje revisado es una condición del Quality Gate |
| **Code Smells / Mantenibilidad** | Código difícil de mantener (duplicado, complejo, mal nombrado) | Afecta la mantenibilidad; rara vez es crítico por sí solo |
| **Deuda técnica** | Tiempo estimado para corregir los problemas de mantenibilidad | Se compara con el tamaño del proyecto |
| **Cobertura** | Porcentaje de código ejecutado por pruebas automatizadas | Si no hay pruebas unitarias aparece 0 %, y eso ya es un hallazgo |
| **Duplicaciones** | Porcentaje de líneas duplicadas | Aumenta el costo de corregir defectos |
| **Complejidad** | Ciclomática y cognitiva por función o archivo | Conecta con V(G) del punto 4.4 |

**Severidad de los problemas.** Según el modo configurado en la versión instalada, SonarQube muestra la clasificación clásica (*Bug*, *Vulnerability*, *Code Smell*, con severidades *Blocker*, *Critical*, *Major*, *Minor* e *Info*) o la clasificación por cualidad del software (Seguridad, Confiabilidad y Mantenibilidad, con severidades *Blocker*, *High*, *Medium*, *Low* e *Info*). En el informe conviene declarar cuál se usó.

**Quality Gate "Sonar way"** (el predeterminado en SonarQube Server 2025). Se aplica al **código nuevo** y falla si:

- se introducen problemas nuevos;
- no se revisó el 100 % de los *Security Hotspots* nuevos;
- la cobertura del código nuevo es menor a 80 %;
- la duplicación del código nuevo supera el 3 %.

Matiz importante: en un proyecto heredado analizado por primera vez casi todo es "código general" y no "código nuevo", así que el Quality Gate puede aparecer aprobado aunque haya muchos problemas. Para el informe se lee la pestaña de **código general (*Overall Code*)** y se explica esa diferencia.

### 5.6 Del reporte de SonarQube al análisis legal (IE6 de EP4)

La rúbrica de EP4 exige **comunicar los resultados del análisis estático comparándolos con criterios legales o normativos**. Pegar capturas del panel no cumple el criterio. El razonamiento esperado es:

```
Problema de SonarQube → Categoría OWASP Top 10 → Requisito del ERS
      → Deber legal o norma afectada → Severidad → Recomendación
```

| Problema típico de SonarQube | OWASP Top 10:2025 | Lectura normativa (marco del curso) |
|---|---|---|
| Credenciales o secretos escritos en el código | A04 Fallas criptográficas / A02 Configuración de seguridad incorrecta | Deber de cuidar los datos con diligencia (Ley 19.628, art. 11); medidas de seguridad (art. 14 quinquies del texto que introduce la Ley 21.719) |
| Contraseñas sin hash robusto | A04 Fallas criptográficas / A07 Fallas de autenticación | Mismo deber de seguridad; incumple el requisito de hash del ERS |
| Consultas SQL armadas concatenando texto | A05 Inyección | Riesgo de acceso indebido a datos personales; su explotación es delito (Ley 21.459) |
| CORS permisivo o cabeceras de seguridad ausentes | A02 Configuración de seguridad incorrecta | Barreras de acceso insuficientes |
| Errores internos devueltos al cliente | A10 Manejo incorrecto de condiciones excepcionales | Exposición de información técnica; requisito de manejo seguro de errores |
| Dependencias con vulnerabilidades conocidas | A03 Fallas en la cadena de suministro de software | Seguridad del sistema; licencias de terceros (Ley 17.336) |
| Ausencia de registro de eventos de seguridad | A09 Fallas de registro y alertas | Sin registros no hay respuesta ni reporte de incidentes (Ley 21.663) |

### 5.7 Beneficios, retos y recomendaciones (2.3.1)

| Beneficios | Retos | Recomendaciones |
|---|---|---|
| Detección temprana | Disciplina y formación del equipo | Enfoque híbrido: herramienta más revisión manual |
| Mejora continua del código | Resistencia cultural a las revisiones | Capacitación continua |
| Apoyo al cumplimiento y a la auditoría | Coordinar herramientas automáticas con revisiones manuales | Procedimientos claros de registro, seguimiento y cierre |
| | Falsos positivos | Integrar el análisis en CI/CD para tener retroalimentación inmediata |

El material muestra un ejemplo de resultado (15 bugs, 30 *code smells* y 5 vulnerabilidades en un proyecto Java) y recomienda registrar manualmente los defectos críticos para priorizarlos y darles seguimiento en las siguientes iteraciones.

> **Repaso 5.** ¿Qué diferencia hay entre una vulnerabilidad y un *Security Hotspot*? ¿Por qué un Quality Gate aprobado no significa que el código sea seguro? Toma un problema de SonarQube y llévalo hasta una norma.

---

## 6. IL2.4 · Ejecución, bitácora e incidentes

### 6.1 Preparación del entorno (2.3.2, paso 1)

Antes de ejecutar se documenta:

| Aspecto | Qué registrar |
|---|---|
| Hardware y software | Sistema operativo, navegador y versión, base de datos y versión, versión de Docker |
| Datos de prueba | Scripts de base de datos cargados; usuarios semilla; datos **sintéticos** |
| Herramientas de soporte | Capturador de pantalla, acceso a logs, herramientas de prueba listas |
| Versión del software | Commit o etiqueta de la versión probada |

### 6.2 Ciclos de ejecución

| Ciclo | Objetivo | Regla |
|---|---|---|
| **Ciclo 1: smoke test** | Verificar funciones básicas (login, carga de la página principal) | Si falla, la ejecución se detiene: el resto queda **Bloqueado** |
| **Ciclo 2: ejecución de casos** | Seguir el guion de cada caso, comparar obtenido con esperado y registrar evidencia de éxitos y fallas | Se respeta el orden de prioridad por riesgo |
| **Ciclo 3, si corresponde: re-test y regresión** | Confirmar correcciones y que no se rompió otra cosa | Solo después de una corrección |

### 6.3 Estados de un caso

| Estado | Significado |
|---|---|
| **Aprobado (Pass)** | El resultado obtenido coincide con el esperado y cumple el criterio de aceptación |
| **Falla (Fail)** | El resultado no coincide; se abre un reporte de defecto |
| **Bloqueado** | No se pudo ejecutar porque otro defecto o el entorno lo impiden |
| **No ejecutado** | Se diseñó pero no se ejecutó; debe justificarse en el informe |

### 6.4 Reporte de defecto (bug report)

| Campo | Ejemplo |
|---|---|
| ID | BUG-001 / INC-01 |
| Título | Contraseñas almacenadas sin hash |
| Caso y requisito relacionados | CP-SEG-002 · requisito de almacenamiento seguro de credenciales |
| Severidad | Crítica |
| Prioridad | Alta |
| Entorno | Versión, navegador, contenedor |
| Pasos para reproducir | Instrucciones exactas para que el desarrollador vea el problema |
| Resultado esperado / obtenido | Hash bcrypt / texto plano |
| Evidencia | Captura, log, consulta, archivo y línea |
| Estado | Abierto / En corrección / Corregido / Verificado / Cerrado |

**Severidad y prioridad no son lo mismo.** La severidad mide el **impacto técnico** del defecto; la prioridad mide la **urgencia** de corregirlo según el negocio. Un error ortográfico en el nombre de la empresa en la página principal tiene severidad baja y prioridad alta; una falla en una función que casi nadie usa puede tener severidad alta y prioridad media.

### 6.5 Escalas de severidad que usa la unidad

El material usa **tres escalas distintas**. En el informe EP3 conviene usar la del formato oficial y explicar la equivalencia.

| Formato EP3 (oficial del informe) | Actividad 2.3.2 | Actividad 2.4.2 | Descripción (formato EP3) | Tratamiento |
|---|---|---|---|---|
| **Crítico** | Crítica | Críticos | Impide el funcionamiento del sistema o de una función esencial; bloquea el flujo principal. Impacto muy alto | Remediación inmediata |
| **Grave** | Mayor | Mayores | Afecta funcionalidades importantes, pero el sistema funciona parcialmente; existe una alternativa | Corregir con urgencia |
| **Moderado** | Menor | Menores | Afecta funciones secundarias o casos específicos sin detener el flujo principal | Próxima iteración |
| **Leve** | Cosmética | (Menores) | Apariencia, estética o texto; no afecta la funcionalidad | Según disponibilidad |

**Criterio para fallas de seguridad.** La actividad 2.4.2 ubica las fallas de seguridad (por ejemplo, una inyección SQL) y las caídas del sistema como **críticas**. Para clasificar una falla de seguridad conviene preguntarse:

1. ¿Expone datos personales o sensibles?
2. ¿Permite acceder o actuar sin autorización?
3. ¿Se puede explotar sin credenciales o con poco esfuerzo?
4. ¿Incumple un requisito legal directo?

Si la respuesta a la 1 o a la 2 es sí y la 3 también, la falla es crítica aunque el sistema "siga funcionando".

### 6.6 Bitácora de ejecución

| ID caso | Nombre | Estado | Defecto | Observaciones | Fecha / responsable |
|---|---|---|---|---|---|
| CP-001 | Login con SQL | Aprobado | N/A | Mensaje de error genérico | dd-mm-aaaa / nombre |
| CP-002 | Registro de usuario | Falla | BUG-002 | El botón "Enviar" no responde en Chrome | … |
| CP-003 | Compra de producto | Bloqueado | N/A | No se pudo probar por la falla de CP-002 | … |

El formato EP3 agrega dos columnas obligatorias en el detalle de ejecución: **evidencia** y **fecha y persona que ejecuta**.

### 6.7 Informe resumen de pruebas

Responde con números: casos diseñados, ejecutados, aprobados, fallidos, bloqueados y no ejecutados; defectos por severidad; cobertura de requisitos. Cierra con una recomendación: "¿Está listo para producción?" o "¿Requiere un nuevo ciclo de corrección?".

**Fórmulas útiles:**

- Porcentaje de ejecución = ejecutados ÷ diseñados × 100.
- Porcentaje de aprobación = aprobados ÷ ejecutados × 100.
- Cobertura de requisitos = requisitos con caso ejecutado ÷ requisitos del ERS × 100.
- Densidad de defectos por módulo = defectos ÷ módulo (ayuda a ubicar dónde se agrupan).

> **Repaso 6.** ¿Cuándo se marca un caso como Bloqueado y no como Falla? Da un ejemplo de defecto con severidad baja y prioridad alta. ¿Qué escala de severidad usarías en el informe EP3 y por qué?

---

## 7. IL2.5 · Informe técnico y de certificación

### 7.1 Para qué sirve el informe

La presentación 2.4.1 lo compara con un "título de propiedad" de la confianza: es el documento oficial que valida el cumplimiento de requisitos, sirve de evidencia ante reguladores, clientes y partes interesadas, y puede revisarse en auditorías posteriores. Un informe impreciso o incompleto afecta la reputación de quien lo emite y su validez.

### 7.2 Estándares de referencia

| Norma | Ámbito |
|---|---|
| **ISO/IEC 17021-1** | Requisitos para organismos que auditan y certifican sistemas de gestión |
| **ISO/IEC 17065** | Requisitos para organismos que certifican productos, procesos y servicios |
| **ISO 19011** | Directrices para auditar sistemas de gestión (la edición 2018 aplica a cualquier sistema de gestión, no solo a calidad y ambiente) |
| **IAF MD 4** | Documento obligatorio del Foro Internacional de Acreditación sobre el uso de tecnologías de información y comunicación (TIC) en auditorías y evaluaciones |

En el curso estas normas sirven como modelo de **cómo se estructura y se valida un informe de certificación**. Un informe de pruebas de un estudiante no "certifica ISO": usa esa lógica para emitir un dictamen técnico.

### 7.3 Estructura del informe de certificación (2.4.1)

| # | Sección | Contenido |
|---|---|---|
| 1 | **Identificación y portada** | Responsable, cliente, alcance, norma o criterio aplicado, fechas, código único del informe |
| 2 | **Resumen ejecutivo** | 1 a 2 páginas: tipo de evaluación, fechas, equipo, hallazgos positivos, no conformidades críticas y decisión con justificación técnica, en lenguaje claro |
| 3 | **Metodología** | Planificación → ejecución → análisis → reporte. Enfoque basado en riesgos, muestreo y criterios de evaluación |
| 4 | **Hallazgos** | Conformidades, observaciones, no conformidades menores y mayores |
| 5 | **Conclusiones y recomendación** | Evaluación global, decisión (otorgar, denegar u otorgar con condiciones), condiciones y plazos, seguimiento |
| 6 | **Anexos y evidencias** | Plan, registros de evidencia, matriz de trazabilidad, competencias del equipo |

**Clasificación de hallazgos**

| Hallazgo | Significado |
|---|---|
| Conformidad | Evidencia de cumplimiento; muestra fortalezas |
| Observación | Oportunidad de mejora sin incumplimiento |
| No conformidad menor | Desviación que no compromete la efectividad global |
| No conformidad mayor | Incumplimiento que afecta la capacidad del sistema de lograr sus resultados |

**Cómo se documenta una no conformidad:** (1) descripción clara del requisito incumplido y de la desviación; (2) evidencia objetiva con referencias, fechas y ubicaciones; (3) referencia normativa con el número de cláusula o artículo; (4) clasificación justificada como mayor o menor. Omitir la cláusula "para que el cliente lo entienda mejor" es un error, no una simplificación (pausa activa de 2.4.1).

### 7.4 Requisitos de la evidencia y de la redacción

| Evidencia | Significado |
|---|---|
| **Verificable** | Un tercero puede comprobarla de forma independiente |
| **Trazable** | Está numerada, fechada y referenciada en el texto |
| **Suficiente** | Su cantidad y calidad son proporcionales al riesgo y al alcance |

Lenguaje: objetivo, preciso, claro, neutral y consistente. Se evita la primera persona, las opiniones, las conclusiones sin evidencia, las descripciones vagas de no conformidades, la falta de referencias normativas y las inconsistencias entre secciones.

**Errores que invalidan un informe:** hallazgos sin evidencia objetiva; referencias normativas incorrectas o desactualizadas; falta de firmas o aprobaciones; contradicciones entre el resumen ejecutivo y las conclusiones.

### 7.5 Control documental

- **Codificación:** clave del titular, área, número correlativo, versión y clasificación (ejemplo del material: `BOCE-2024-0125-V1-INICIAL`).
- **Registro de cambios:** fecha, descripción, tipo (de forma o de fondo), responsable y aprobación.
- **Revisión y aprobación:** elaboración por el líder → revisión del equipo → validación técnica independiente → aprobación final.
- **Confidencialidad:** clasificar la información, acuerdos de confidencialidad, almacenamiento seguro, distribución controlada, retención y destrucción. Un informe de seguridad describe vulnerabilidades explotables, así que su circulación debe limitarse.
- **Mejora continua del reporte:** fijar objetivos, monitorear, identificar mejoras, implementarlas y verificar resultados.

### 7.6 Informe de certificación de software (actividad 2.4.2)

| Sección | Contenido | Ejemplo del material |
|---|---|---|
| 1. Resumen ejecutivo | ¿El software es apto para su lanzamiento? Dictamen y alcance | Certificado / No certificado / Certificado con reservas |
| 2. Métricas de ejecución | Diseñados, ejecutados, aprobados, fallidos, bloqueados | 50 diseñados; 48 ejecutados (96 %); 42 aprobados; 4 fallidos; 2 bloqueados |
| 3. Gestión de defectos | Críticos, mayores y menores, con riesgo residual | "Un software con defectos críticos abiertos nunca debe ser certificado" |
| 4. Matriz de trazabilidad | Cada requisito con su caso y su resultado | "El anexo más importante para tu profesor" |
| 5. Evaluación de riesgos | Riesgos mitigados y riesgos aceptados | Aceptado: "lentitud sobre 500 usuarios simultáneos, fuera del alcance actual" |
| 6. Conclusión | Veredicto según el criterio de aceptación definido al inicio | "Se requiere el 100 % de casos críticos exitosos" |

Nota sobre el ejemplo de métricas: 42 aprobados sobre 48 ejecutados equivale a 87,5 %; sobre 50 diseñados, a 84 %. Al calcular porcentajes hay que declarar la base.

**Cómo elegir el dictamen**

| Situación | Dictamen |
|---|---|
| Hay al menos un defecto crítico abierto | **No certificado** |
| Sin críticos; hay defectos graves o mayores con plan de corrección y plazos | **Certificado con reservas** (indicando las condiciones) |
| Sin críticos ni graves; se cumplen todos los criterios de aceptación | **Certificado** |

El dictamen técnico y el análisis ético-normativo deben ser coherentes: no se puede certificar un sistema y, en la sección siguiente, describir un incumplimiento legal grave sin resolver.

> **Repaso 7.** Redacta una no conformidad mayor con sus cuatro partes. ¿Qué diferencia hay entre un riesgo mitigado y uno aceptado? Con 2 defectos graves y ninguno crítico, ¿qué dictamen corresponde y qué condiciones pondrías?

---

## 8. Marco ético y normativo de la unidad

### 8.1 Cómo se usa la normativa en esta unidad

La unidad no introduce leyes nuevas desde cero: reutiliza el marco de la EA1 (carpeta de normativas del curso) y exige **aplicarlo a los resultados de las pruebas**. El análisis ético y normativo del informe y las recomendaciones de la presentación se construyen con esta secuencia:

```
Hallazgo técnico → Riesgo para las personas → Norma y artículo → Quién está obligado → Recomendación
```

Tres reglas:

1. **Citar el artículo, no solo la ley.** "Ley 19.628" no basta; "Ley 19.628, art. 11 (deber de diligencia en el cuidado de los datos)" sí.
2. **Separar lo vigente de lo que viene.** No atribuir a una ley derechos o sanciones que están en otra, ni presentar como vigente una norma que todavía no rige.
3. **Identificar al obligado.** Muchas leyes no obligan al software, sino a la organización que lo opera. El software debe **permitir** que esa organización cumpla.

### 8.2 Normas del curso (aplican a cualquier caso)

| Norma | Estado (al 19-10-2026) | Qué aporta al análisis de pruebas |
|---|---|---|
| **Ley 19.628**, protección de la vida privada | Vigente en su texto actual | Define datos personales y sensibles (art. 2); deber de secreto (art. 7); tratamiento de datos sensibles (art. 10); deber de cuidar los datos con la debida diligencia (art. 11); indemnización por tratamiento indebido (art. 23) |
| **Ley 21.719**, protección de datos personales | Publicada el 13-12-2024; **entra en vigencia el 01-12-2026** | Reemplaza gran parte del texto de la Ley 19.628. Agrega deberes de seguridad (art. 14 quinquies), reporte de vulneraciones (art. 14 sexies), infracciones leves, graves y gravísimas, y multas de hasta 5.000, 10.000 y 20.000 UTM (art. 35 del texto nuevo). Crea la Agencia de Protección de Datos Personales. Incorpora principios como licitud, finalidad, proporcionalidad, calidad, responsabilidad, seguridad, transparencia y confidencialidad |
| **Ley 21.663**, Ley Marco de Ciberseguridad | Vigente; la Agencia Nacional de Ciberseguridad (ANCI) opera desde 2025 | Obliga a las instituciones que prestan **servicios esenciales** y a los **operadores de importancia vital**. Exige reportar incidentes al CSIRT Nacional (alerta temprana en 3 horas). Multas según gravedad, mayores para operadores de importancia vital (art. 40) |
| **Ley 21.459**, delitos informáticos | Vigente | Tipifica el ataque a la integridad de un sistema, el acceso ilícito, la interceptación ilícita y el ataque a la integridad de los datos. Sirve para explicar el **impacto** de una vulnerabilidad y para fijar los **límites éticos** de las pruebas |
| **Ley 17.336**, propiedad intelectual | Vigente | Uso de software y componentes de terceros; licencias de dependencias; sanciones (arts. 78 y 79) |
| **Ley 19.799 y Decreto 181**, documento y firma electrónica | Vigente | Aplica cuando el sistema emite o firma documentos electrónicos con valor legal |
| **Ley 21.180**, transformación digital del Estado | Vigente | Aplica a sistemas que se relacionan con organismos públicos |
| **Política Nacional de Ciberseguridad** | Política pública | Marco general; orienta, pero no impone obligaciones directas a un sistema privado |
| **Manual de Accesibilidad Web** (Gobierno de Chile) | Guía técnica | Base para requisitos y pruebas de accesibilidad y usabilidad |

### 8.3 Normas sectoriales: dependen del dominio del caso

El docente puede pedir normas propias del negocio. La pregunta guía es: **¿qué ley regula la actividad que el software apoya?**

| Dominio | Normas sectoriales que suelen aparecer | Ejemplo de prueba que generan |
|---|---|---|
| **Salud** (por ejemplo, Cuidarte+: pacientes, exámenes, documentos clínicos) | Ley 20.584 de derechos y deberes de los pacientes (ficha clínica como dato sensible, acceso restringido y conservación, arts. 12 y 13); Ley 21.668 (interoperabilidad de fichas clínicas); Decreto 41 de 2012 del MINSAL, reglamento de fichas clínicas (registro de quién accede y cuándo, respaldos); normas de atención de urgencia del DFL 1 de 2005 del MINSAL (arts. 141 y 173) | Cada lectura o descarga de un examen queda registrada con usuario y fecha; un profesional no vinculado a la atención no accede a la ficha; los datos no se eliminan físicamente antes del plazo de conservación |
| **Gestión empresarial / pymes** (por ejemplo, Atlas: clientes, contratos y documentos) | Ley 19.628 y Ley 21.719 para los datos de clientes; Ley 19.799 si los contratos se firman electrónicamente | Un editor no modifica contratos; los datos de un cliente no se ven desde otra empresa |
| **Banca y finanzas** (caso de la actividad 2.1.2) | Normativa del regulador financiero; Ley 21.663 si es operador de importancia vital | Bloqueo tras intentos fallidos; invalidación de tokens; cifrado en tránsito |

En un caso de salud, la normativa sanitaria es la que regula de forma específica el dato clínico, así que va primero en el análisis. Omitirla es una falta de cobertura normativa.

### 8.4 Principios éticos aplicados a las pruebas

| Principio | Qué significa en la práctica |
|---|---|
| **Autorización y alcance** | Las herramientas de seguridad (ZAP, Burp, SQLMap, Nikto, John the Ripper) se usan **solo** contra el entorno propio y autorizado (el Docker local del caso). Usarlas contra sistemas ajenos es la conducta que sanciona la Ley 21.459 |
| **Datos sintéticos** | Nunca usar datos reales de personas (RUT, diagnósticos, contratos), aunque el entorno sea local |
| **Honestidad en el reporte** | Reportar todos los hallazgos, también los incómodos. Ocultar un defecto para mejorar el dictamen es una falta profesional |
| **Proporcionalidad** | Demostrar la vulnerabilidad sin causar más daño del necesario (no borrar datos ni saturar un entorno compartido) |
| **Confidencialidad** | El informe describe vulnerabilidades: su distribución se controla |
| **Foco en las personas** | El impacto se mide en las personas afectadas (pacientes, adultos mayores, clientes), no solo en el sistema |
| **Independencia** | El juicio de QA no se subordina a plazos ni a la presión por aprobar |
| **Mejora continua** | Cada hallazgo termina en una recomendación concreta y verificable |

### 8.5 Ejemplo de análisis ético-normativo bien construido

| Elemento | Contenido |
|---|---|
| Hallazgo | Las contraseñas se guardan y comparan en texto plano (archivo y línea) |
| Riesgo | Si se filtra la base de datos, todas las cuentas quedan expuestas; muchas personas reutilizan contraseñas |
| Norma vigente | Ley 19.628, art. 11: el responsable debe cuidar los datos con la debida diligencia |
| Norma próxima | Art. 14 quinquies del texto que introduce la Ley 21.719 (medidas de seguridad), desde el 01-12-2026 |
| Requisito del ERS | Contraseñas con hash bcrypt |
| Obligado | La organización que opera el sistema; el desarrollador entrega un sistema que no le permite cumplir |
| Severidad | Crítica |
| Recomendación | Aplicar bcrypt, forzar el cambio de las contraseñas existentes y agregar un caso de regresión |
| Impacto en el dictamen | Con este defecto abierto el sistema no puede certificarse |

> **Repaso 8.** ¿Por qué no se debe citar la Ley 21.719 como vigente en octubre de 2026? ¿A quién obliga la Ley 21.663? Nombra dos principios éticos que limitan el uso de SQLMap.

---

## 9. Herramientas: qué hace cada una y cuándo usarla

### 9.1 Herramientas del laboratorio de la Evaluación 2

Lista de herramientas disponibles en Docker para los casos A y B, según el material de Eva_02.

| Herramienta | Categoría | Qué hace | Tipo de prueba / requisito que respalda | Evidencia que produce |
|---|---|---|---|---|
| **SonarQube** | SAST / calidad | Analiza el código sin ejecutarlo; detecta bugs, vulnerabilidades, *hotspots* y *code smells* | Análisis estático (IL2.3); mantenibilidad; seguridad del código | Panel, reporte exportado, archivo y línea |
| **OWASP ZAP** | DAST | Proxy y escáner de aplicaciones web; rastrea la app y lanza pruebas pasivas y activas | Seguridad de la app desplegada (configuración, cabeceras, inyección, XSS). Para llegar a las funciones internas se configura con sesión iniciada | Reporte HTML o JSON con alertas y nivel de riesgo |
| **Burp Suite** | Proxy / pruebas manuales | Intercepta y modifica peticiones HTTP y permite repetirlas con cambios | Pruebas manuales de autorización (cambiar un ID, quitar el token, cambiar el rol), sesiones y lógica de negocio | Petición y respuesta capturadas |
| **Nikto** | Escáner de servidor web | Busca configuraciones inseguras, archivos expuestos y versiones conocidas del servidor | Seguridad de configuración del servidor | Listado de hallazgos por URL |
| **SQLMap** | Inyección SQL | Detecta de forma automatizada inyecciones SQL en parámetros | Validación de entradas en el login y en endpoints con parámetros | Resultado por parámetro (vulnerable o no) |
| **John the Ripper** | Auditoría de contraseñas | Intenta recuperar contraseñas a partir de sus hashes con diccionarios y fuerza bruta | Fortaleza de la política de contraseñas y del algoritmo de hash | Contraseñas recuperadas y tiempo empleado |
| **JMeter** | Rendimiento | Simula usuarios concurrentes y mide tiempos, rendimiento y errores | Carga y estrés (requisitos de rendimiento y disponibilidad) | Reporte HTML con percentiles, rendimiento y tasa de error |
| **Selenium** | Automatización funcional | Controla el navegador para repetir flujos de usuario | Funcionales, regresión y compatibilidad entre navegadores | Script, registro de ejecución y capturas |

**Lectura correcta de los resultados:**

- **ZAP y Nikto** generan alertas que pueden ser falsos positivos; cada alerta relevante se confirma a mano antes de convertirla en incidente.
- **SQLMap** se ejecuta solo contra el entorno propio. Si concluye que un parámetro no es vulnerable, ese resultado es evidencia de un caso aprobado.
- **John the Ripper** solo tiene sentido si hay hashes. Si las contraseñas están en texto plano, el hallazgo es todavía más grave y la herramienta no hace falta para demostrarlo.
- **JMeter**: se reportan percentiles (por ejemplo, el percentil 90) y no solo el promedio. Si el código tiene retardos artificiales, se mide con y sin ellos y se explica la diferencia.

### 9.2 Otras herramientas mencionadas en la unidad

| Categoría | Herramientas | Uso |
|---|---|---|
| Automatización funcional | Cypress, Playwright, Appium (móvil) | Alternativas a Selenium |
| Gestión de casos | TestRail, Jira + Zephyr, Azure Test Plans, qTest, TestLink, PractiTest | Repositorio de casos, ejecución y trazabilidad |
| Seguimiento de defectos | Jira, Bugzilla, Redmine | Ciclo de vida de los defectos |
| Infraestructura | Docker, Docker Compose | Entorno reproducible |
| Pruebas de API | Swagger UI (`/docs`), Postman | Pruebas funcionales y de autorización sobre la API |

### 9.3 Cómo justificar una herramienta

La rúbrica premia la justificación. Una fórmula simple:

> "Se usa **[herramienta]** para **[tipo de prueba]** sobre **[requisito o riesgo]**, porque **[capacidad concreta]**. Su resultado se registra como **[evidencia]** en el caso **[ID]**."

Ejemplo: "Se usa JMeter para la prueba de carga del requisito de tiempo de respuesta, porque permite simular 200 usuarios concurrentes y medir el percentil 90. El reporte HTML se adjunta como evidencia del caso CP-05".

> **Repaso 9.** ¿Qué herramienta usarías para probar que un usuario no puede ver un registro de otro usuario? ¿Por qué ZAP sin sesión iniciada da una cobertura limitada? ¿En qué se diferencian ZAP y Nikto?

---

## 10. EP3 y EP4: qué se pide y cómo se evalúa

### 10.1 Datos generales

| | EP3 | EP4 |
|---|---|---|
| Nombre | Verificando la calidad, seguridad y cumplimiento normativo | Igual |
| Tipo | Encargo (informe) | Presentación (defensa) |
| Modalidad | Grupal | Individual |
| Ponderación | 12 % | 28 % |
| Tiempo asignado (pauta) | 1 hora pedagógica | 3 horas pedagógicas |
| Defensa | 10 minutos + 5 de preguntas; orden aleatorio | Igual |
| Entrega | Informe y material de apoyo en AVA | Material de apoyo en AVA |
| Insumos | ERS, imágenes Docker, código fuente, feedback de EP1 | Igual |

Las evaluaciones parciales suman el 60 % de la nota final y el Examen Transversal el 40 %. Los porcentajes de EP3 y EP4 se calculan sobre ese 60 %.

Regla clave de ambas pautas: **la nota de la defensa es individual** y depende solo de lo que cada estudiante demuestre. Si un estudiante no puede explicar el proyecto con claridad, se asume que no participó en su desarrollo. Por eso cada integrante debe dominar el trabajo completo, no solo su parte.

### 10.2 Contenido obligatorio del informe EP3

1. Lo de la EP1 ajustado según la retroalimentación del docente.
2. Casos de prueba con **cobertura del 100 %** de los requisitos del ERS (necesidades, normativa, legal y seguridad).
3. Criterios de calidad, seguridad y cumplimiento normativo del caso.
4. Plan de pruebas: estrategia, tipos de prueba y su justificación, criterios de aceptación y herramientas.
5. Al menos **5 casos representativos** de los distintos tipos de requisito, cada uno con ID, descripción, requisito (código ERS), datos de entrada, resultado esperado, criterio de aceptación y tipo de prueba.
6. Ejecución: resumen, detalle por caso e incidentes con su criticidad.
7. Análisis ético y normativo de los resultados.

**Formato:** Word o PDF; títulos en Arial 12; cuerpo en Arial 11; interlineado 1,5; texto justificado; portada con nombre completo de cada integrante, carrera, sección, docente y fecha; lenguaje formal técnico; capturas de buena calidad y legibles.

**Estructura del formato oficial:** 1 Introducción · 2 Criterios de calidad · 3 Plan de pruebas (3.1 Estrategia, 3.2 Tipos, 3.3 Criterios de aceptación, 3.4 Herramientas y recursos) · 4 Diseño de casos · 5 Ejecución (5.1 Resumen, 5.2 Detalle, 5.3 Criticidad de incidentes). El formato no trae una sección de análisis ético y normativo, pero la pauta la exige: se agrega como sección 6, seguida de conclusiones y anexos (matriz de trazabilidad).

### 10.3 Rúbrica EP3 (dimensión: encargo)

Escala por criterio: 100 % muy buen desempeño · 80 % bueno · 60 % aceptable · 30 % incipiente · 0 % no logrado.

| Criterio | Peso | Qué se necesita para el 100 % | Dónde se demuestra |
|---|---|---|---|
| **IE1** Importancia de calidad, seguridad y cumplimiento legal | 20 % | Claridad y profundidad, ejemplos pertinentes y lenguaje técnico | Introducción, criterios de calidad, análisis ético-normativo |
| **IE3** Clasificación de tipos de prueba y su propósito | **38 %** | Clasificar y describir **todos** los tipos (funcionales, no funcionales, seguridad, rendimiento, etc.), justificando propósito y aplicación | 3.2 Tipos de prueba y casos |
| **IE5** Pruebas no funcionales: propósito y contexto | 15 % | Casos representativos de distintos tipos no funcionales, con criterio de aceptación y propósito coherentes con el contexto | Casos de rendimiento, usabilidad, compatibilidad, seguridad y disponibilidad |
| **IE7** Elementos del plan y su vínculo con requisitos y normas | 15 % | Todos los apartados (introducción, alcance, objetivos, estrategia, recursos y cronograma) con coherencia técnica y vínculo con requisitos y normativa vigente | Sección 3 completa |
| **IE9** Cobertura y coherencia frente a estándares técnicos y legales | 12 % | Evaluar coherencia y cobertura respecto de requisitos y estándares, con análisis crítico | Matriz de trazabilidad y análisis de cobertura |

### 10.4 Contenido obligatorio de la presentación EP4

- Enfoque estratégico de las pruebas.
- Herramientas seleccionadas y su justificación.
- Ejecución de las pruebas realizadas.
- Clasificación de los defectos identificados.
- Reflexiones sobre calidad, seguridad, normativa y aspectos legales de los resultados.

### 10.5 Rúbrica EP4 (dimensión: presentación)

| Criterio | Peso | Qué se necesita para el 100 % | Cómo prepararlo |
|---|---|---|---|
| **IE2** Estrategia y justificación de seguridad y normativa | 20 % | Claridad, dominio y fluidez; justificación sólida con ejemplos concretos | Una lámina con la estrategia por riesgo y un ejemplo de requisito legal convertido en caso |
| **IE4** Tipos de prueba aplicados, origen e impacto | **38 %** | Explicar con precisión cada tipo, **de dónde nace** (requisito, riesgo, norma) y **qué impacto** tiene su resultado | Para cada tipo: requisito → caso → resultado → impacto |
| **IE6** Análisis estático frente a criterios legales | 15 % | Presentar los resultados de SonarQube con claridad y compararlos con criterios legales o normativos con capacidad crítica | Tabla problema → OWASP → norma → severidad (ver 5.6) |
| **IE8** Proceso de ejecución y trazabilidad | 15 % | Proceso claro, ordenado y lógico, con trazabilidad completa con los requisitos | Flujo smoke → ciclos → bitácora → incidentes, con un caso seguido de punta a punta |
| **IE10** Recomendaciones con evidencia y principios éticos y normativos | 12 % | Recomendaciones con evidencia técnica sólida y referencias explícitas a principios éticos y normativos | Cada recomendación con su incidente y su artículo |

### 10.6 Lectura conjunta de las dos rúbricas

- El **38 %** de cada rúbrica está en los **tipos de prueba**. Es el tema que más conviene dominar.
- La rúbrica de EP3 no nombra de forma explícita la ejecución ni el análisis estático, pero el encargo los exige y la EP4 los evalúa (IE6 e IE8). Hay que cubrir ambos.
- **Coherencia entre documentos:** lo que se dice en la defensa debe coincidir con el informe (mismos ID de casos, mismas severidades, mismo dictamen).
- **Preguntas probables en la defensa:** por qué se eligió una herramienta; qué significa una métrica de SonarQube; por qué un incidente es crítico y no grave; qué artículo respalda una recomendación; cómo se calculó la cobertura; qué se haría distinto en un nuevo ciclo.

### 10.7 Guion sugerido para 10 minutos de defensa

| Minuto | Contenido | Criterio |
|---|---|---|
| 0–1 | Contexto del sistema y alcance | IE2 |
| 1–3 | Estrategia por riesgo; seguridad y normativa en el plan | IE2 |
| 3–6 | Tipos de prueba aplicados: origen, ejemplo y resultado | IE4 |
| 6–7 | SonarQube frente a criterios legales | IE6 |
| 7–8,5 | Proceso de ejecución y trazabilidad, con un caso de punta a punta | IE8 |
| 8,5–10 | Defectos por severidad, dictamen y recomendaciones éticas y normativas | IE10 |

---

## 11. Inconsistencias detectadas en el material

Conocerlas evita copiar errores al informe y permite responder con seguridad si el docente pregunta.

| Dónde | Qué dice | Observación |
|---|---|---|
| Guía 2.1.2 | Encabezado "EA1" | La actividad pertenece a la EA2 (IL2.1) |
| Guía 2.3.2 | Encabezado "IL2.3" | El contenido es ejecución de pruebas (IL2.4) |
| Guía 2.4.2 | Encabezado "IL2.4" y objetivo sobre análisis estático | El contenido es el informe de certificación (IL2.5) |
| Guías 2.2.2 y 2.3.2 | Mismo objetivo copiado | El objetivo de 2.3.2 debería referirse a la ejecución |
| IL2.2 | Redacción distinta en el programa y en las pautas | Ver 1.2: ambas se complementan |
| PPT 2.1.1, indicadores | Menciona "Equipos de Protección Personal", "Sistema de Administración de Seguridad" y "producto manufacturado" | Son indicadores de seguridad industrial y manufactura; no aplican al software. En su lugar: incidentes de seguridad, tiempo de respuesta ante incidentes, vulnerabilidades por severidad, densidad de defectos |
| PPT 2.4.1 | ISO 19011 "para sistemas de calidad y ambiental" | Desde 2011 aplica a cualquier sistema de gestión |
| PPT 2.4.1 | IAF MD 4 como "uso obligatorio de documentos normativos del IAF" | IAF MD 4 trata el uso de TIC en auditorías y evaluaciones |
| Escalas de severidad | Tres escalas distintas (formato EP3, 2.3.2 y 2.4.2) | Usar la del formato EP3 y declarar la equivalencia (ver 6.5) |
| Pautas EP3 y EP4 | "La Evaluación Parcial 2 corresponde…"; EP4 es individual pero habla de "grupos" | Texto heredado de otra pauta |
| Programa | Grupos de máximo 3 integrantes | El docente puede autorizar otra conformación |
| Bibliografía obligatoria | Spring Security | El código de los casos del curso es Node.js/Express; los principios de autenticación y autorización igual aplican |
| Cifras de beneficio (10x, 100x, 70 %, 95 %) | Presentadas como datos generales | Usarlas como argumento ilustrativo, no como medición del caso |

---

## 12. Glosario

| Término | Definición breve |
|---|---|
| **Bloqueado** | Caso que no puede ejecutarse por un defecto previo o por el entorno |
| **BVA** | *Boundary Value Analysis*, análisis de valores límite |
| **Caja blanca** | Diseño de pruebas con conocimiento del código |
| **Caja negra** | Diseño de pruebas desde entradas y salidas, sin ver el código |
| **CI/CD** | Integración y despliegue continuos |
| **Code smell** | Indicio de código difícil de mantener |
| **Complejidad ciclomática** | Número de caminos independientes de un programa, V(G) |
| **Contenedor** | Instancia en ejecución de una imagen Docker |
| **Criterio de aceptación** | Condición objetiva para aprobar un caso o cerrar un ciclo |
| **DAST** | Pruebas dinámicas de seguridad sobre la aplicación en ejecución |
| **Deuda técnica** | Esfuerzo pendiente para corregir problemas de mantenibilidad |
| **Dictamen** | Decisión final: Certificado, Certificado con reservas o No certificado |
| **ERS** | Especificación de Requerimientos de Software |
| **Evidencia objetiva** | Registro verificable, trazable y suficiente que respalda un hallazgo |
| **Hotspot de seguridad** | Código sensible que requiere revisión humana |
| **Imagen Docker** | Plantilla inmutable con todo lo necesario para ejecutar una aplicación |
| **No conformidad** | Incumplimiento de un requisito (mayor o menor) |
| **OWASP** | Fundación que publica guías abiertas de seguridad de aplicaciones (Top 10, WSTG) |
| **Prioridad** | Urgencia de corrección según el negocio |
| **Quality Gate** | Conjunto de condiciones que el código debe cumplir para aprobarse en SonarQube |
| **Regresión** | Reaparición de un defecto, o aparición de uno nuevo, después de un cambio |
| **SAST** | Análisis estático de seguridad del código fuente |
| **Severidad** | Impacto técnico de un defecto |
| **Shift-left** | Adelantar las pruebas a las primeras etapas del ciclo de vida |
| **Smoke test** | Prueba rápida de funciones básicas antes de ejecutar el resto |
| **Trazabilidad** | Relación verificable entre requisitos, casos, resultados e incidentes |
| **Walkthrough** | Revisión guiada por el autor del código o documento |
| **WSTG** | *Web Security Testing Guide* de OWASP |

---

## 13. Autoevaluación final

Marca cada punto solo si puedes explicarlo sin mirar el material.

**Plan y estrategia (IL2.1)**
- [ ] Distingo estrategia, nivel, tipo y técnica con un ejemplo de cada uno.
- [ ] Enumero los elementos del plan y sé qué contiene cada uno.
- [ ] Defino criterios de entrada, suspensión y salida para un ciclo.
- [ ] Priorizo módulos con una matriz de probabilidad e impacto.
- [ ] Explico por qué Docker es un criterio de entrada y nombro cuatro buenas prácticas de seguridad en imágenes.

**Casos de prueba (IL2.2)**
- [ ] Escribo un caso completo con todos los campos del formato EP3.
- [ ] Aplico partición de equivalencia, valores límite y tablas de decisión a un requisito real.
- [ ] Calculo V(G) y explico qué implica para la cantidad de casos.
- [ ] Construyo una matriz de trazabilidad y calculo la cobertura.

**Análisis estático (IL2.3)**
- [ ] Explico la diferencia entre análisis estático y dinámico, y entre SAST y DAST.
- [ ] Leo el panel de SonarQube: bugs, vulnerabilidades, *hotspots*, *code smells*, cobertura y duplicación.
- [ ] Explico por qué un Quality Gate aprobado no garantiza seguridad en un proyecto heredado.
- [ ] Conecto un problema de SonarQube con OWASP Top 10, con el ERS y con una norma.

**Ejecución (IL2.4)**
- [ ] Describo el flujo smoke → ejecución → bitácora → reporte de defecto → resumen.
- [ ] Clasifico un defecto con la escala del formato EP3 y justifico severidad y prioridad.
- [ ] Calculo porcentajes de ejecución y de aprobación declarando la base.

**Informe (IL2.5)**
- [ ] Elijo un dictamen y lo defiendo con métricas y criterios de aceptación.
- [ ] Redacto una no conformidad con descripción, evidencia, referencia normativa y clasificación.
- [ ] Distingo riesgos mitigados de riesgos aceptados.

**Ética y normativa**
- [ ] Cito al menos tres normas con artículo y explico a quién obligan.
- [ ] Separo lo vigente de lo que entra en vigencia (Ley 21.719, 01-12-2026).
- [ ] Identifico las normas sectoriales del dominio de mi caso.
- [ ] Explico los límites éticos del uso de herramientas de seguridad.

**Evaluaciones**
- [ ] Sé qué pide cada criterio de las rúbricas EP3 y EP4 y dónde lo demuestro.
- [ ] Puedo presentar el trabajo completo del grupo en 10 minutos, no solo mi parte.

---

*Elaborado a partir del Programa de Asignatura PA-ISY1102, las presentaciones y guías de la EA_2 (2.1.1 a 2.4.2), las pautas y el formato de informe de EP3 y EP4, y la carpeta de normativas de la EA1. Las condiciones del Quality Gate "Sonar way" se contrastaron con la documentación oficial de SonarQube Server 2025. La vigencia de las leyes se revisó al 19-10-2026; antes de entregar conviene confirmar en LeyChile que no haya cambios.*
