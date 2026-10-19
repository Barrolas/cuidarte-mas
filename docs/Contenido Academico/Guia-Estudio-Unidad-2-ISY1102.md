<!-- PORTADA -->
# Guía de Estudio · Unidad 2

**Duoc UC · Escuela de Informática y Telecomunicaciones**

**ISY1102 · Seguridad y Calidad en el Desarrollo de Software**

**Unidad 2 (Experiencia de Aprendizaje 2): Garantizando la seguridad y calidad del software**

**Guía de estudio: definiciones, procesos, técnicas, herramientas, marco normativo y evaluación**

Versión 1.0 · octubre de 2026

<!-- /PORTADA -->

## Control del documento

| Campo | Detalle |
|---|---|
| Título | Guía de Estudio · Unidad 2 · ISY1102 |
| Asignatura | ISY1102 Seguridad y Calidad en el Desarrollo de Software |
| Resultado de aprendizaje | RA2 |
| Indicadores de logro | IL2.1, IL2.2, IL2.3, IL2.4 e IL2.5 |
| Evaluaciones asociadas | EP3 (encargo grupal, 12 %) y EP4 (presentación individual, 28 %) |
| Versión | 1.0 |
| Fecha | 19-10-2026 |
| Clasificación | Uso académico |
| Vigencia normativa revisada | 19-10-2026 |

**Alcance.** La guía desarrolla la totalidad de los contenidos de la Unidad 2: estrategia y plan de pruebas con enfoque en calidad y seguridad; entornos de prueba con Docker; técnicas avanzadas de diseño de casos de prueba; pruebas estáticas de código, obtención de evidencias y registro de resultados con SonarQube; ejecución de pruebas en laboratorio y gestión de defectos; y elaboración de informes finales de certificación. Incorpora, además, el marco ético y normativo aplicable, las herramientas del laboratorio y los criterios de las evaluaciones EP3 y EP4.

**Criterio de prioridad.** Ante cualquier diferencia entre esta guía y los documentos oficiales de la asignatura, prevalecen la pauta de la evaluación correspondiente y el Programa de Asignatura.

---

## Índice

1. Introducción
2. Objetivos de aprendizaje de la unidad
3. Capítulo 1. Marco conceptual de la calidad y la seguridad del software
4. Capítulo 2. Estrategias y enfoques de diseño del plan de pruebas con enfoque en calidad y seguridad (tema 2.1.1)
5. Capítulo 3. Plan de pruebas en entornos de contenedores Docker (tema 2.1.1, segunda parte)
6. Capítulo 4. Aplicación: plan de pruebas estratégico (actividad 2.1.2)
7. Capítulo 5. Levantamiento del entorno Docker del caso semestral (guía 2.1.3)
8. Capítulo 6. Técnicas avanzadas de diseño de casos de prueba (tema 2.2.1)
9. Capítulo 7. Aplicación: creación de casos de prueba con técnicas específicas (actividad 2.2.2)
10. Capítulo 8. Pruebas estáticas de código, obtención de evidencias y registro de resultados (tema 2.3.1)
11. Capítulo 9. Ejecución de pruebas en un entorno de laboratorio (actividad 2.3.2)
12. Capítulo 10. Elaboración de informes finales de certificación (tema 2.4.1)
13. Capítulo 11. Aplicación: informe de certificación de software (actividad 2.4.2)
14. Capítulo 12. Herramientas del laboratorio
15. Capítulo 13. Marco ético y normativo
16. Capítulo 14. Evaluaciones EP3 y EP4
17. Capítulo 15. Observaciones técnicas sobre conceptos de la unidad
18. Glosario
19. Referencias
20. Anexo A. Lista de verificación de cobertura de contenidos
21. Anexo B. Autoevaluación final

---

## Introducción

La Unidad 2 de ISY1102 traslada el aseguramiento de la calidad desde el diseño hacia la verificación. En la Unidad 1 se establecieron los conceptos de calidad, los tipos de prueba, el marco legal y la estructura de un plan de pruebas. En la Unidad 2 ese plan se convierte en una estrategia ejecutable: se diseñan casos de prueba con técnicas formales, se analiza el código fuente sin ejecutarlo, se ejecutan ciclos de prueba sobre un software real desplegado en contenedores, se registran y clasifican los hallazgos, y se comunica un dictamen técnico con respaldo ético y normativo.

La unidad se organiza como una cadena de trabajo en la que cada producto alimenta al siguiente:

```
Requisito (ERS) → Riesgo → Estrategia → Caso de prueba → Ejecución → Evidencia
      → Incidente (severidad) → Norma afectada → Recomendación → Dictamen
```

El concepto que articula toda la cadena es la **trazabilidad**: la posibilidad de recorrer, en ambos sentidos, la relación entre un requisito, los casos que lo verifican, los resultados obtenidos, los incidentes registrados y las normas que fundamentan la recomendación. Un informe de calidad que no permite reconstruir esa relación carece de valor probatorio.

**Organización de la guía.** Cada capítulo corresponde a un tema de la unidad, en el orden de la ruta de aprendizaje de la asignatura. Los capítulos teóricos (2, 3, 6, 8 y 10) desarrollan definiciones formales, explicaciones, clasificaciones, procesos paso a paso, tablas comparativas, ejemplos aplicados, errores frecuentes, relación con estándares y preguntas de repaso. Los capítulos de aplicación (4, 5, 7, 9 y 11) desarrollan las actividades prácticas asociadas. Los capítulos 12 a 14 integran herramientas, normativa y evaluación. El Anexo A permite comprobar que cada contenido de la unidad está cubierto.

---

## Objetivos de aprendizaje de la unidad

### Resultado de aprendizaje

**RA2.** Evalúa la calidad y seguridad del software mediante la ejecución de pruebas funcionales, no funcionales, utilizando metodologías y herramientas que permitan detectar defectos, documentar hallazgos y comunicar resultados de manera ética y profesional.

### Indicadores de logro

| IL | Enunciado | Actividad de la ruta de aprendizaje | Capítulos |
|---|---|---|---|
| **IL2.1** | Diseña estrategias de prueba considerando la seguridad y el cumplimiento normativo como componentes esenciales del aseguramiento de la calidad del software. | Act. 2.1 Diseña la estrategia y el plan de pruebas | 2, 3, 4, 5 |
| **IL2.2** | Diseña casos de prueba que permitan verificar los estándares de calidad, seguridad, marcos legales y regulatorios. *(En el Programa de Asignatura: analiza segmentos de código críticos para detectar vulnerabilidades lógicas y de seguridad que escapan a las herramientas automáticas.)* | Act. 2.2 Desarrolla y documenta casos de prueba | 6, 7 |
| **IL2.3** | Aplica herramientas de análisis estático para auditar el código fuente, identificando deficiencias de calidad y vulnerabilidades conforme a criterios legales y normativos. | Act. 2.3 Ejecuta y analiza pruebas estáticas de código | 8 |
| **IL2.4** | Ejecuta ciclos de prueba documentando hallazgos y vulnerabilidades de forma estructurada, utilizando estándares reconocidos de la industria. | Act. 2.3 / Act. 2.4 | 9 |
| **IL2.5** | Elabora informes técnicos que integren evidencias, hallazgos y recomendaciones, fundamentados en principios éticos, normativos y de mejora continua. | Act. 2.4 Ejecuta y documenta hallazgos, evaluando su impacto y gravedad | 10, 11 |

Las dos redacciones del IL2.2 son complementarias. El diseño de casos de caja blanca y la revisión manual del código son, precisamente, los medios para detectar los defectos lógicos que una herramienta automatizada no identifica, como un servicio que valida la existencia de un token pero no el rol del usuario que lo presenta.

### Objetivos específicos

Al finalizar el estudio de la unidad, el estudiante debe ser capaz de:

1. Definir un plan de pruebas y sus componentes, y justificar la integración de calidad, seguridad y cumplimiento normativo en él.
2. Diseñar una estrategia de pruebas basada en riesgos que combine enfoques de caja negra, caja blanca e híbridos.
3. Planificar un entorno de pruebas reproducible y seguro con contenedores Docker.
4. Aplicar técnicas formales de diseño de casos: partición de equivalencia, análisis de valores límite, tablas de decisión, caminos básicos, condiciones, bucles y flujo de datos.
5. Calcular e interpretar la complejidad ciclomática.
6. Documentar casos de prueba con una estructura estandarizada y trazable a los requisitos.
7. Ejecutar pruebas estáticas manuales y automatizadas, obtener evidencias y registrar resultados con SonarQube.
8. Ejecutar ciclos de prueba, registrar bitácoras y reportes de defectos, y clasificar su severidad.
9. Elaborar un informe final de certificación con dictamen, métricas, hallazgos, riesgos y recomendaciones.
10. Relacionar los hallazgos técnicos con la normativa chilena y los principios éticos aplicables.

### Relación de la unidad con las evaluaciones

| Tema | Producto | Uso en EP3 (informe) | Uso en EP4 (defensa) |
|---|---|---|---|
| 2.1 Estrategia y plan | Estrategia por riesgo, métricas, matriz, entorno | Sección 3, Plan de pruebas | IE2 Estrategia (20 %) |
| 2.2 Casos de prueba | Casos estandarizados, matriz de trazabilidad | Sección 4, cobertura del 100 % | IE4 Tipos de prueba (38 %) e IE8 |
| 2.3 Pruebas estáticas y ejecución | Reporte SonarQube, bitácora, reportes de defectos | Sección 5 e incidentes | IE6 (15 %) e IE8 (15 %) |
| 2.4 Informe de certificación | Dictamen, riesgos, recomendaciones | Estructura del informe y análisis ético-normativo | IE10 (12 %) |

---

## Capítulo 1. Marco conceptual de la calidad y la seguridad del software

Este capítulo reúne los conceptos que la unidad emplea de manera transversal. Su dominio es requisito para comprender los capítulos siguientes y para utilizar un lenguaje técnico preciso, aspecto que las rúbricas de EP3 y EP4 valoran de forma explícita.

### 1.1 Calidad del software

**Definición.** La calidad del software es el grado en que un producto satisface los requisitos explícitos e implícitos de sus partes interesadas y, con ello, aporta valor. La norma ISO/IEC 25010:2023 la operacionaliza mediante un **modelo de calidad del producto** con nueve características:

| Característica (ISO/IEC 25010:2023) | Significado | Tipo de prueba asociado |
|---|---|---|
| Adecuación funcional | Grado en que el producto ofrece funciones completas, correctas y apropiadas | Funcionales, reglas de negocio |
| Eficiencia de desempeño | Comportamiento temporal, uso de recursos y capacidad | Carga, estrés, rendimiento |
| Compatibilidad | Coexistencia e interoperabilidad con otros productos | Integración, compatibilidad |
| Capacidad de interacción | Facilidad para que usuarios específicos interactúen con el producto (antes "usabilidad"); incluye inclusividad y protección frente a errores del usuario | Usabilidad, accesibilidad |
| Fiabilidad | Ausencia de fallas, disponibilidad, tolerancia a fallos y recuperabilidad | Disponibilidad, recuperación, estabilidad |
| Seguridad (*security*) | Confidencialidad, integridad, no repudio, responsabilidad, autenticidad y resistencia | Seguridad (autenticación, autorización, entradas, configuración) |
| Mantenibilidad | Modularidad, reutilización, analizabilidad, modificabilidad y capacidad de ser probado | Análisis estático, revisión de código |
| Flexibilidad | Adaptabilidad, escalabilidad, instalabilidad y reemplazabilidad (antes "portabilidad") | Compatibilidad, despliegue |
| Protección (*safety*) | Capacidad de evitar estados que pongan en riesgo a personas, bienes o el ambiente | Pruebas de condiciones límite y de fallo seguro |

### 1.2 Seguridad del software

**Definición.** La seguridad del software es la capacidad del producto para proteger la información y los datos de modo que personas o sistemas accedan a ellos solo en el grado que corresponde a su nivel de autorización, y para resistir ataques. Se expresa habitualmente con la tríada **confidencialidad, integridad y disponibilidad**, complementada con **autenticidad**, **no repudio** y **responsabilidad (trazabilidad de acciones)**.

### 1.3 Cumplimiento normativo

**Definición.** El cumplimiento normativo es la conformidad del software, y de la organización que lo opera, con leyes, reglamentos, estándares técnicos y políticas internas. En el contexto de las pruebas, cada exigencia normativa debe traducirse en un requisito verificable y, a su vez, en uno o más casos de prueba o controles revisables. Una norma que no se traduce en una verificación no se encuentra integrada al plan.

### 1.4 Error, defecto, falla e incidente

| Término | Definición | Ejemplo |
|---|---|---|
| **Error (equivocación)** | Acción humana que produce un resultado incorrecto | Implementar la comparación de contraseñas sin función de hash |
| **Defecto** | Imperfección en un producto de trabajo (código, diseño, documentación) que puede causar una falla | La rutina de autenticación almacena la contraseña en texto plano |
| **Falla** | Desviación observable del comportamiento esperado al ejecutar el sistema | La consulta de la tabla de usuarios muestra todas las contraseñas legibles |
| **Incidente** | Registro formal de una desviación observada durante las pruebas, con su descripción, severidad y evidencia | INC-01, severidad crítica |

Las pruebas estáticas detectan **defectos** sin ejecutar el sistema; las pruebas dinámicas provocan **fallas** y las registran como **incidentes**.

### 1.5 Verificación y validación

- **Verificación:** confirmación, mediante evidencia objetiva, de que el producto cumple los requisitos especificados. Responde a la pregunta "¿se construyó correctamente el producto?". Las revisiones, inspecciones y el análisis estático son actividades de verificación.
- **Validación:** confirmación de que el producto satisface las necesidades del uso previsto. Responde a la pregunta "¿se construyó el producto correcto?". Las pruebas de aceptación y de usabilidad con usuarios representativos son actividades de validación.

### 1.6 Los siete principios de las pruebas (ISTQB)

El programa de estudio *Certified Tester Foundation Level* v4.0 de ISTQB establece siete principios generales:

| # | Principio | Implicancia práctica |
|---|---|---|
| 1 | Las pruebas muestran la presencia de defectos, no su ausencia | Un resultado sin hallazgos no demuestra que el sistema sea seguro; solo indica que, con esos casos y esa cobertura, no se detectaron defectos |
| 2 | Las pruebas exhaustivas son imposibles | Se requieren técnicas de diseño, priorización y enfoque basado en riesgos |
| 3 | Las pruebas tempranas ahorran tiempo y dinero | Los defectos eliminados temprano no generan defectos derivados; fundamenta el enfoque *shift-left* |
| 4 | Los defectos se agrupan | Pocos componentes concentran la mayoría de los defectos (principio de Pareto); es un insumo del análisis de riesgos |
| 5 | Las pruebas se desgastan | Repetir los mismos casos reduce su capacidad de detectar defectos nuevos; los casos y datos deben renovarse, aunque la repetición es útil en la regresión automatizada |
| 6 | Las pruebas dependen del contexto | Un sistema de salud no se prueba con los mismos criterios que un sitio informativo |
| 7 | Falacia de la ausencia de defectos | Un sistema verificado y sin defectos conocidos puede igualmente no satisfacer a sus usuarios; la verificación debe complementarse con validación |

En la unidad se trabajan de forma explícita los principios 1, 2 y 3 bajo los nombres de **demostración de defectos**, **testing enfocado** y **pruebas tempranas**.

### 1.7 Estrategia, nivel, tipo y técnica de prueba

Estos cuatro conceptos se confunden con frecuencia. La rúbrica de EP3 (IE3, 38 %) y la de EP4 (IE4, 38 %) valoran su distinción.

| Concepto | Pregunta que responde | Ejemplos |
|---|---|---|
| **Estrategia o enfoque** | ¿Cómo se abordará la prueba en general? | Basada en riesgos, manual, automatizada, mixta, *shift-left* |
| **Nivel** | ¿Qué parte del sistema se prueba? | Unitaria (componente), integración, sistema, aceptación |
| **Tipo** | ¿Qué característica de calidad se evalúa? | Funcional, rendimiento, seguridad, usabilidad, compatibilidad, regresión |
| **Técnica** | ¿Cómo se derivan los casos concretos? | Partición de equivalencia, valores límite, tablas de decisión, caminos básicos |

**Ejemplo de redacción correcta.** "El requisito de autenticación se verifica mediante una prueba de tipo funcional, en el nivel de sistema, cuyos casos se derivan con partición de equivalencia y análisis de valores límite, dentro de una estrategia basada en riesgos que la ubica en el primer ciclo de ejecución."

### 1.8 Catálogo de tipos de prueba

| Tipo | Propósito | Ejemplo de caso | Herramienta habitual |
|---|---|---|---|
| Funcional | Comprobar que el sistema realiza lo que establece el requisito | El registro con datos válidos crea la cuenta | Manual, Selenium |
| Reglas de negocio | Verificar restricciones propias del dominio | Un paciente solo visualiza sus propios exámenes | Manual, Swagger, Postman |
| Integración | Verificar la comunicación entre componentes (cliente, API, base de datos, servicios externos) | Un registro creado por la API se refleja en la interfaz | Swagger, Selenium |
| Regresión | Confirmar que un cambio no afectó funcionalidades existentes | Repetir el conjunto de autenticación después de una corrección | Selenium automatizado |
| Humo (*smoke*) | Verificar que las funciones básicas operan antes de continuar | Inicio de sesión y carga de la página principal | Manual |
| Seguridad: autenticación | Evaluar el control de identidad | Credenciales inválidas, intentos repetidos, expiración de sesión | Burp Suite, ZAP, John the Ripper |
| Seguridad: autorización | Evaluar el control de acceso por rol y por propiedad del recurso | Un usuario sin privilegios invoca un servicio de administración | Burp Suite, Postman |
| Seguridad: validación de entradas | Evaluar la resistencia a inyección y a datos maliciosos | Cadena `' OR '1'='1' --` en el formulario de acceso | SQLMap, ZAP |
| Seguridad: configuración | Revisar cabeceras, CORS, mensajes de error y versiones expuestas | Respuesta de error con detalle interno | Nikto, ZAP |
| Rendimiento: carga | Medir el comportamiento con la carga esperada | 200 usuarios concurrentes bajo el umbral de respuesta | JMeter |
| Rendimiento: estrés | Determinar el punto de degradación o quiebre | Incremento de usuarios hasta superar una tasa de error definida | JMeter |
| Usabilidad | Evaluar la facilidad de uso con usuarios representativos | Cinco usuarios completan una tarea sin asistencia | Observación, cuestionarios |
| Accesibilidad | Verificar el uso por personas con discapacidad | Navegación completa con teclado; contraste suficiente | Lighthouse, revisión manual |
| Compatibilidad | Verificar el funcionamiento en navegadores, dispositivos y resoluciones | Interfaz operable en una pantalla de 5 pulgadas | Selenium, revisión manual |
| Disponibilidad y recuperación | Verificar continuidad operativa y restauración | Restaurar un respaldo y comprobar la integridad de los datos | Revisión operativa |
| Cumplimiento normativo | Verificar que una exigencia legal se implementa como control | Cada descarga de un documento queda registrada con usuario y fecha | Revisión manual, registros |

**Pruebas funcionales y no funcionales.** Las pruebas funcionales verifican *qué* hace el sistema; las no funcionales verifican *cómo* lo hace (rendimiento, seguridad, usabilidad, compatibilidad, fiabilidad). Cada prueba no funcional debe vincularse a un requisito, un umbral medible, una justificación de negocio y una herramienta de medición.

### 1.9 Preguntas de repaso

1. Distinga entre defecto y falla, e indique qué tipo de prueba detecta cada uno.
2. Explique por qué un informe sin hallazgos no permite afirmar que un sistema es seguro.
3. Clasifique "análisis de valores límite", "prueba de carga", "nivel de integración" y "enfoque basado en riesgos" según sean estrategia, nivel, tipo o técnica.
4. Relacione tres características de ISO/IEC 25010:2023 con un tipo de prueba y una herramienta.
5. Explique la diferencia entre verificación y validación con un ejemplo de cada una.

---

## Capítulo 2. Estrategias y enfoques de diseño del plan de pruebas con enfoque en calidad y seguridad (tema 2.1.1)

**Indicador de logro:** IL2.1. **Propósito del capítulo:** comprender qué es un plan de pruebas, cuáles son sus elementos esenciales y cómo se diseña una estrategia que integre calidad, seguridad y cumplimiento normativo.

### 2.1 Problema de partida: calidad o seguridad

El tema se introduce con una situación de decisión: ante el lanzamiento de una aplicación que administra los ahorros de una persona, y con la posibilidad de probar una sola cosa, ¿se privilegiaría que el botón "Enviar" funcione (calidad) o que nadie pueda robar la contraseña (seguridad)? La segunda pregunta de la dinámica, denominada **riesgo fantasma**, solicita identificar el error más costoso causado por no probar a tiempo.

La conclusión que se desprende es que la disyuntiva es falsa: un sistema que funciona pero es inseguro no es de calidad, y un sistema seguro que no funciona no aporta valor. La idea rectora del tema es que la calidad no es un accidente, sino el resultado de una ejecución disciplinada, y que el plan de pruebas es el marco que proporciona esa disciplina.

### 2.2 Definición, propósito e importancia del plan de pruebas

**Definición.** Un **plan de pruebas** es el documento que constituye el marco estratégico que organiza, estructura y guía todas las actividades de validación de un producto de software. Describe qué se probará, cómo, con qué recursos, en qué plazo, bajo qué criterios y con qué riesgos.

**Propósito fundamental.** Asegurar la calidad del producto, detectar defectos en etapas tempranas y validar la seguridad antes del lanzamiento.

**Importancia.** El plan:

- reduce los riesgos de forma significativa, porque concentra el esfuerzo donde el impacto es mayor;
- mejora la comunicación entre los equipos de desarrollo, QA, seguridad y negocio, al fijar un lenguaje y unos compromisos comunes;
- garantiza entregas confiables, porque establece criterios objetivos para decidir cuándo un producto está listo.

**Marco de estándares.** La plantilla clásica de plan de pruebas proviene de IEEE 829 (*Standard for Software and System Test Documentation*). En la actualidad, IEEE 829 ha sido reemplazado por la serie **ISO/IEC/IEEE 29119**, cuya Parte 3 (2021) define la documentación de pruebas, incluido el plan. La estructura de IEEE 829 sigue siendo útil como plantilla de estudio.

### 2.3 Integración de calidad y seguridad

| Enfoque en calidad | Enfoque en seguridad |
|---|---|
| Asegura el cumplimiento riguroso de los requisitos funcionales y no funcionales, de modo que el software responda a las expectativas del usuario | Implementa medidas proactivas para prevenir vulnerabilidades, mitigar amenazas y proteger la integridad de los datos y de los sistemas críticos |
| Validación exhaustiva de la funcionalidad | Prevención de brechas y accesos no autorizados |
| Rendimiento eficiente y sostenido | Protección de la información sensible |
| Experiencia de uso intuitiva | Alineación con normativas y estándares vigentes |
| Compatibilidad con entornos y plataformas | Fortalecimiento de la confianza del usuario |

La integración de ambos enfoques permite desarrollar productos robustos, confiables y seguros. En términos de diseño del plan, integrar significa que **cada requisito crítico tiene al menos un caso funcional y uno de seguridad**, y que la seguridad no se reduce a una fase posterior y aislada.

### 2.4 Elementos clave de un plan de pruebas efectivo

| # | Elemento | Contenido mínimo |
|---|---|---|
| 01 | **Alcance y objetivos** | Definición precisa de qué se prueba, qué no se incluye y por qué |
| 02 | **Estrategia de pruebas** | Tipos, niveles y enfoques: manual, automatizado, basado en riesgos |
| 03 | **Recursos y roles** | Equipos con responsabilidades específicas y cronograma realista |
| 04 | **Criterios de aceptación** | Condiciones de entrada y salida, identificación de riesgos y estrategias de mitigación |

La estructura completa que se exige en las evaluaciones (rúbrica EP3, IE7) amplía estos cuatro elementos:

| Sección del plan | Contenido | Error frecuente |
|---|---|---|
| Introducción | Propósito, contexto del sistema y referencias (ERS, normas) | Describir el software sin indicar el propósito de la prueba |
| Alcance | Módulos y funciones incluidos; exclusiones justificadas | Omitir lo que queda fuera o no justificarlo |
| Objetivos | Metas medibles y verificables | Redactar objetivos genéricos ("probar el sistema") |
| Estrategia | Enfoque, niveles, tipos y técnicas; justificación por riesgo | Enumerar tipos de prueba sin justificar su elección |
| Criterios de entrada | Condiciones para iniciar la ejecución | No definirlos |
| Criterios de salida o aceptación | Condiciones para finalizar y certificar | Usar criterios no medibles ("que funcione bien") |
| Criterios de suspensión y reanudación | Cuándo se detiene y cuándo se retoma la ejecución | Ignorar el caso de un entorno caído |
| Recursos y roles | Personas, responsabilidades, herramientas, entornos | Asignar herramientas sin indicar quién las opera |
| Entorno de pruebas | Infraestructura, versiones, datos de prueba | No especificar versiones |
| Cronograma | Fases, hitos y orden por riesgo | Cronograma lineal sin prioridad |
| Riesgos y mitigación | Riesgos del producto y del proyecto, con su plan de respuesta | Confundir riesgo con defecto |
| Entregables | Casos, bitácoras, reportes de defectos, informe final | No listar el informe final |
| Métricas | Indicadores con meta y fórmula | Métricas sin umbral |

**Criterios de entrada (ejemplo).** Entorno Docker levantado y estable; versión del software congelada e identificada; datos de prueba cargados; casos de prueba revisados y aprobados; herramientas instaladas y configuradas.

**Criterios de salida (ejemplo).** 100 % de los casos de prioridad alta ejecutados; cero defectos críticos abiertos; defectos mayores corregidos o aceptados formalmente con plan de mitigación; cobertura de requisitos de al menos 90 %; Quality Gate aprobado en el código nuevo.

**Criterios de suspensión (ejemplo).** El smoke test falla; el entorno deja de estar disponible; un defecto bloqueante impide ejecutar más del 30 % de los casos planificados.

### 2.5 Alcance y objetivos

El alcance y los objetivos se construyen en tres pasos:

1. **Definición de funcionalidades críticas:** identificar las áreas de mayor impacto en el negocio y las funciones que requieren más atención.
2. **Áreas de seguridad prioritarias:** mapear los módulos expuestos a amenazas y establecer los controles de seguridad necesarios.
3. **Objetivos específicos medibles:** validar las funciones centrales, verificar el rendimiento bajo carga y asegurar la protección de los datos sensibles.

**Ejemplo de objetivo.** "Verificar que el sistema de autenticación implementa cifrado seguro, maneja correctamente las sesiones y previene accesos no autorizados."

**Objetivos medibles: criterio SMART.** Un objetivo de prueba es adecuado cuando es específico, medible, alcanzable, pertinente y acotado en el tiempo.

| Objetivo deficiente | Objetivo adecuado |
|---|---|
| Probar el login | Verificar que el 100 % de los intentos de acceso con credenciales inválidas se rechaza con un mensaje genérico y queda registrado |
| Revisar el rendimiento | Comprobar que el 95 % de las solicitudes de consulta de agenda responde en menos de 2 segundos con 100 usuarios concurrentes |
| Asegurar los datos | Verificar que ningún usuario con rol paciente obtiene datos de otro paciente al modificar el identificador del recurso |

### 2.6 Estrategia y enfoque de pruebas

**Definición.** La **estrategia de pruebas** es la descripción de alto nivel de cómo se abordarán las pruebas para cumplir los objetivos: qué niveles y tipos se aplicarán, con qué técnicas, con qué grado de automatización y con qué prioridad.

Componentes de la estrategia que se trabajan en la unidad:

| Componente | Definición |
|---|---|
| Pruebas funcionales | Validación de los requisitos de negocio y de los flujos principales del usuario |
| Pruebas de integración | Verificación de la comunicación entre módulos y con sistemas externos |
| Pruebas de rendimiento | Evaluación de la velocidad, la escalabilidad y la estabilidad bajo carga |
| Enfoque basado en riesgos | Priorización de las pruebas en los módulos de mayor impacto potencial para el negocio y los usuarios |
| Automatización estratégica | Incorporación de pruebas automatizadas para la regresión continua y la validación recurrente de seguridad |

#### 2.6.1 Enfoque basado en riesgos

**Definición.** El **riesgo** es la combinación de la probabilidad de que ocurra un evento adverso y del impacto que tendría. En pruebas, el enfoque basado en riesgos asigna el esfuerzo de prueba en proporción al nivel de riesgo de cada área.

**Pasos:**

1. Identificar los riesgos del producto (por ejemplo, acceso no autorizado a fichas clínicas) y del proyecto (por ejemplo, retraso del entorno).
2. Estimar la probabilidad (1 a 3) y el impacto (1 a 3).
3. Calcular el nivel de riesgo: probabilidad × impacto.
4. Priorizar: el riesgo alto se prueba primero y con mayor profundidad.
5. Definir la mitigación y revisar la matriz en cada ciclo.

**Matriz de riesgo 3 × 3**

| Probabilidad \ Impacto | Bajo (1) | Medio (2) | Alto (3) |
|---|---|---|---|
| **Alta (3)** | 3 Medio | 6 Alto | 9 Crítico |
| **Media (2)** | 2 Bajo | 4 Medio | 6 Alto |
| **Baja (1)** | 1 Bajo | 2 Bajo | 3 Medio |

**Ejemplo de priorización.** Ejecutar primero las pruebas de seguridad en los módulos expuestos directamente a internet, como API públicas, formularios de autenticación y pasarelas de pago.

**Ejemplo aplicado (sistema de salud).**

| Riesgo | P | I | Nivel | Respuesta en el plan |
|---|---|---|---|---|
| Acceso de un paciente a la ficha de otro | 2 | 3 | 6 Alto | Casos de autorización por propiedad del recurso en el primer ciclo |
| Contraseñas almacenadas sin función de hash | 3 | 3 | 9 Crítico | Revisión de código y prueba con John the Ripper; criterio de salida bloqueante |
| Degradación de la agenda en horario punta | 2 | 2 | 4 Medio | Prueba de carga con JMeter en el segundo ciclo |
| Texto ilegible en pantallas pequeñas | 2 | 1 | 2 Bajo | Revisión de compatibilidad al final del ciclo |

#### 2.6.2 Enfoques de caja negra, caja blanca e híbrido

| Enfoque | Base del diseño | Pregunta que responde | Se aplica a |
|---|---|---|---|
| **Caja negra** | Especificación (requisitos, entradas y salidas) | ¿El sistema hace lo que debe? | Validación de entradas, flujos, reglas de negocio, usabilidad |
| **Caja blanca** | Estructura interna (código, caminos, condiciones) | ¿El código está bien construido y cubre todas sus ramas? | Lógica crítica, autenticación, cálculo, manejo de errores |
| **Híbrido (caja gris)** | Especificación más conocimiento parcial de la estructura | ¿La integración entre componentes es correcta y segura? | Comunicación entre cliente, API y base de datos; estados y errores |

#### 2.6.3 Seguridad en la estrategia: SAST y DAST

| Técnica | Definición | Momento | Ejemplo |
|---|---|---|---|
| **SAST** (*Static Application Security Testing*) | Análisis del código fuente sin ejecutarlo para detectar patrones vulnerables | Durante el desarrollo, en cada integración | SonarQube |
| **DAST** (*Dynamic Application Security Testing*) | Análisis de la aplicación en ejecución, enviando solicitudes y observando las respuestas | Con el sistema desplegado en un entorno de pruebas | OWASP ZAP, Burp Suite, Nikto |

Ambas técnicas son complementarias: SAST encuentra defectos en el código que podría no ejecutarse durante la prueba; DAST encuentra problemas de configuración y de comportamiento que no se observan en el código.

### 2.7 Diseño de casos de prueba con enfoque en calidad y seguridad

Tres grupos de casos componen el diseño:

- **Casos funcionales:** validan los requisitos del negocio y los flujos completos del usuario.
- **Casos de seguridad:** cubren autenticación, autorización y validación de entradas críticas.
- **Guías OWASP:** proporcionan los estándares para las pruebas de seguridad web.

**Propiedades de un buen caso de prueba.** Debe ser específico, medible, reproducible y trazable a los requisitos originales, e incluir precondiciones claras, pasos detallados y resultados esperados verificables.

**OWASP WSTG.** La *Web Security Testing Guide* de OWASP es una guía metodológica para probar la seguridad de aplicaciones web. Su versión estable vigente es la 4.2 (la 5.0 está en desarrollo). Organiza las pruebas por categorías, con códigos de identificación, por ejemplo: recopilación de información, configuración y despliegue, gestión de identidad, autenticación, autorización, gestión de sesiones, validación de entradas, manejo de errores, criptografía, lógica de negocio y cliente.

**OWASP Top 10:2025.** Documento de concientización que reúne las diez categorías de riesgo más críticas en aplicaciones web. La edición vigente es la de 2025:

| Código | Categoría | Ejemplo en un sistema de salud |
|---|---|---|
| A01:2025 | Broken Access Control (control de acceso roto) | Un paciente consulta la ficha de otro paciente cambiando un identificador |
| A02:2025 | Security Misconfiguration (configuración de seguridad incorrecta) | Mensajes de error con detalle interno; CORS abierto |
| A03:2025 | Software Supply Chain Failures (fallas en la cadena de suministro) | Dependencias con vulnerabilidades conocidas |
| A04:2025 | Cryptographic Failures (fallas criptográficas) | Contraseñas sin función de hash; tráfico sin TLS |
| A05:2025 | Injection (inyección) | Inyección SQL en el formulario de acceso |
| A06:2025 | Insecure Design (diseño inseguro) | Recuperación de contraseña sin verificación de identidad |
| A07:2025 | Authentication Failures (fallas de autenticación) | Sin límite de intentos; tokens que no expiran |
| A08:2025 | Software or Data Integrity Failures (fallas de integridad) | Actualizaciones o datos aceptados sin verificación |
| A09:2025 | Security Logging and Alerting Failures (fallas de registro y alerta) | Accesos a fichas clínicas sin registro |
| A10:2025 | Mishandling of Exceptional Conditions (manejo indebido de condiciones excepcionales) | Excepciones que exponen la traza o dejan el sistema en estado inseguro |

### 2.8 Principios fundamentales aplicados

| Principio | Enunciado | Aplicación en el plan |
|---|---|---|
| **Pruebas tempranas** | Detectar defectos y vulnerabilidades desde las fases iniciales reduce los costos de manera exponencial | Revisión de requisitos y análisis estático antes de la ejecución |
| **Testing enfocado** | Las pruebas exhaustivas no son posibles; priorizar áreas críticas y de alto riesgo es fundamental | Matriz de riesgo y orden de ejecución |
| **Demostración de defectos** | La ejecución de pruebas demuestra la presencia de defectos, pero no su ausencia total | Redacción prudente del dictamen |

Estos principios corresponden a los principios 3, 2 y 1 del programa ISTQB CTFL v4.0 (Capítulo 1, sección 1.6 de esta guía).

### 2.9 Ejemplo aplicado: caso de prueba de seguridad contra inyección SQL

**Inyección SQL.** Vulnerabilidad en la que datos controlados por el usuario se incorporan a una consulta SQL sin separación entre código y datos, lo que permite alterar la lógica de la consulta.

| Campo | Contenido |
|---|---|
| Objetivo | Validar que el sistema rechaza y registra los intentos de inyección SQL |
| Pasos | Enviar entradas maliciosas en los campos de formulario; verificar la respuesta del sistema; analizar el manejo de errores |
| Dato de prueba | `' OR '1'='1' --` |
| Resultado esperado | El sistema bloquea el ataque, no expone información sensible y registra el evento en los registros de seguridad |

**Por qué funciona el ataque.** Si la consulta se construye concatenando texto, por ejemplo `SELECT * FROM usuarios WHERE correo = '` + entrada + `'`, la entrada `' OR '1'='1' --` cierra la comilla, agrega una condición siempre verdadera y comenta el resto de la consulta. La consulta devuelve registros sin validar la contraseña.

**Control esperado.** Consultas parametrizadas (por ejemplo, `WHERE correo = $1` con el valor enviado aparte), validación de entradas por lista de permitidos, mensajes de error genéricos y registro del intento.

**Error frecuente.** Dar por superado el caso solo porque no se obtuvo acceso. El resultado esperado tiene tres partes y las tres deben verificarse: bloqueo, ausencia de información sensible en la respuesta y registro del evento.

### 2.10 Planificación de recursos y roles

**Independencia del testing.** Equipos independientes de desarrollo y de pruebas garantizan objetividad y una perspectiva crítica. Quien construye un componente tiende a probarlo con los supuestos con que lo construyó.

**Roles especializados.**

| Rol | Responsabilidades |
|---|---|
| Líder de QA | Planificación, estrategia, coordinación, métricas, dictamen final y comunicación con las partes interesadas |
| Tester funcional | Diseño y ejecución de casos funcionales, registro de evidencias y defectos |
| Especialista en automatización | Construcción y mantenimiento de pruebas automatizadas y de su integración en el pipeline |
| Especialista en seguridad | Pruebas de seguridad, análisis estático y dinámico, clasificación de vulnerabilidades |

**Herramientas adecuadas.** Entornos de prueba aislados, frameworks de automatización y escáneres de vulnerabilidades actualizados.

**Matriz RACI.** Herramienta para asignar responsabilidades: R (*responsible*, ejecuta), A (*accountable*, rinde cuentas y aprueba), C (*consulted*, es consultado) e I (*informed*, es informado). Ejemplo: en la aprobación del plan, el líder de QA es A, los testers son R en la redacción de sus secciones, el equipo de desarrollo es C y el cliente es I.

### 2.11 Cronograma y gestión de riesgos

- **Planificación iterativa:** el cronograma se alinea con ciclos ágiles, DevOps y CI/CD para entregas continuas.
- **Identificación de riesgos del proyecto:** retrasos, falta de cobertura, fallas críticas y dependencias externas.
- **Estrategias de mitigación:** planes de contingencia, priorización dinámica y comunicación proactiva.

**Riesgo del producto y riesgo del proyecto.**

| Tipo | Definición | Ejemplo |
|---|---|---|
| Riesgo del producto | Posibilidad de que el software falle o no cumpla una característica de calidad | Fuga de datos clínicos |
| Riesgo del proyecto | Posibilidad de que las actividades de prueba no se cumplan en plazo, costo o alcance | El entorno Docker no levanta el día de la ejecución |

### 2.12 Integración de automatización y herramientas

| Elemento | Descripción |
|---|---|
| Automatización de la regresión | Pruebas repetitivas ejecutadas automáticamente en cada cambio de código para detectar regresiones de forma temprana |
| Seguridad continua | Análisis estático (SAST) y dinámico (DAST) integrados en el pipeline de desarrollo |
| Herramientas especializadas | Selenium para pruebas funcionales; OWASP ZAP y Burp Suite para seguridad web |

**Beneficios ilustrativos.** En el tema se presentan tres cifras como referencia del aporte de la automatización: reducción de 70 % en el tiempo de ejecución de la regresión, capacidad de ejecutar tres veces más casos con la misma inversión y 95 % de consistencia entre ejecuciones. Deben entenderse como valores ilustrativos y no como resultados medidos de un estudio identificado; en un informe propio se deben reemplazar por mediciones del proyecto.

**Qué conviene automatizar.** Casos estables, repetitivos, de alto valor y con resultado esperado determinista (regresión de autenticación, flujos principales). **Qué no conviene automatizar.** Casos exploratorios, de usabilidad o que cambian en cada versión.

**Pipeline CI/CD.** Secuencia automatizada de construcción, prueba y despliegue que se ejecuta ante cada cambio. Un orden típico es: compilación → pruebas unitarias → análisis estático (SonarQube y Quality Gate) → construcción de la imagen → despliegue en el entorno de prueba → pruebas funcionales automatizadas → DAST.

### 2.13 Evaluación y métricas de calidad

**Definición.** Una **métrica** es una medida cuantitativa de un atributo del producto o del proceso. Un **indicador** es una métrica comparada con una meta que permite tomar decisiones.

**Nota técnica.** En la lista de indicadores del tema aparecen algunas métricas propias de la manufactura y de la seguridad industrial (tasa de defectos por millón de unidades, calificación del producto manufacturado, eliminación de tolerancias críticas, uso de equipos de protección personal y calificación de un sistema de administración de seguridad). Dichas métricas no se aplican al software; su equivalente en pruebas de software se presenta en la tabla siguiente. Las métricas de seguridad aplicables del tema son el número de incidentes registrados y el tiempo promedio de respuesta ante incidentes críticos.

| Métrica | Fórmula | Meta de ejemplo |
|---|---|---|
| Cobertura de requisitos | Requisitos con al menos un caso / requisitos totales × 100 | 100 % en EP3 |
| Tasa de ejecución | Casos ejecutados / casos planificados × 100 | 100 % de prioridad alta |
| Tasa de aprobación | Casos aprobados / casos ejecutados × 100 | ≥ 95 % |
| Densidad de defectos | Defectos / tamaño (KLOC o número de funciones) | Decreciente entre ciclos |
| Eficacia de detección (DDE) | Defectos detectados en pruebas / (detectados en pruebas + detectados en producción) × 100 | ≥ 98 % de defectos críticos antes de producción |
| Defectos críticos abiertos | Conteo | 0 para certificar |
| Tiempo medio de corrección | Suma de tiempos de corrección / número de defectos | Según severidad |
| Tiempo medio de respuesta ante incidentes de seguridad | Suma de tiempos de respuesta / número de incidentes | Definido por la política |
| Cobertura de código nuevo | Según SonarQube | ≥ 80 % (Quality Gate Sonar way) |
| Duplicación en código nuevo | Según SonarQube | ≤ 3 % |

### 2.14 Documentación y comunicación

El ciclo de documentación del plan consta de cuatro acciones:

1. **Documentar:** plan detallado, casos de prueba y resultados claros.
2. **Revisar:** validación temprana con las partes interesadas clave.
3. **Comunicar:** actualizaciones constantes entre los equipos.
4. **Aprobar:** confirmación formal antes de la ejecución.

La comunicación entre desarrollo, QA, seguridad y negocio requiere canales definidos y reuniones regulares de sincronización.

### 2.15 Caso ilustrativo: plan con enfoque en seguridad en una empresa de comercio electrónico

Una empresa de comercio electrónico que procesaba datos sensibles de clientes presentaba vulnerabilidades críticas antes del lanzamiento. La empresa:

1. **Integró OWASP WSTG** en su plan de pruebas.
2. **Detectó de forma proactiva** 47 vulnerabilidades, 12 de ellas críticas.
3. **Corrigió todas** las vulnerabilidades antes del lanzamiento.

Los resultados informados fueron una reducción de 70 % en los incidentes de seguridad posteriores a la puesta en producción, en comparación con proyectos anteriores, y un ahorro estimado de USD 250.000 en costos de remediación y daño reputacional evitados. Se trata de un caso de "Empresa X" sin fuente identificable, por lo que su valor es didáctico: muestra la secuencia guía → detección → corrección antes del lanzamiento → medición del efecto.

### 2.16 Desafíos comunes y cómo superarlos

| Desafío | Efecto | Solución |
|---|---|---|
| Pruebas tardías | Retrasan la detección de fallas críticas y aumentan el costo de corrección | Aplicar *shift-left testing*, integrando pruebas desde las primeras fases del diseño |
| Falta de recursos especializados | La escasez de expertos en seguridad y pruebas avanzadas limita la efectividad del plan | Capacitación continua, certificaciones y mentorías internas |
| Desalineación entre equipos | La falta de comunicación genera expectativas diferentes y pruebas incompletas | Ceremonias regulares, documentación compartida y objetivos comunes claros |

**Shift-left testing.** Práctica de desplazar las actividades de prueba hacia el inicio del ciclo de vida (revisión de requisitos y diseño, análisis estático, pruebas unitarias), con el fin de detectar defectos cuando su corrección es más barata.

### 2.17 Herramientas y recursos para elaborar el plan

| Categoría | Recursos |
|---|---|
| Plantillas y frameworks | Plantillas estructuradas IEEE 829; frameworks ágiles de testing; modelos de casos reutilizables; listas de verificación de criterios de aceptación |
| Guías y estándares | OWASP WSTG; OWASP Top 10; programa de estudio y buenas prácticas de ISTQB; NIST Cybersecurity Framework |
| Automatización | Selenium, Cypress, Playwright, Appium |
| Seguridad | OWASP ZAP, Burp Suite, SonarQube |
| Gestión | Jira, TestRail, Azure DevOps, Zephyr |

**NIST Cybersecurity Framework 2.0 (2024).** Marco para la gestión de riesgos de ciberseguridad organizado en seis funciones: Gobernar (*Govern*), Identificar (*Identify*), Proteger (*Protect*), Detectar (*Detect*), Responder (*Respond*) y Recuperar (*Recover*). En un plan de pruebas se emplea para justificar controles; por ejemplo, el registro de accesos a fichas clínicas responde a la función Detectar.

### 2.18 Flujo de trabajo optimizado para la estrategia de pruebas

1. **Definir alcance y objetivos medibles:** delimitar qué se evaluará, establecer prioridades y formular criterios de éxito verificables.
2. **Diseñar una estrategia basada en riesgos:** seleccionar tipos de pruebas y enfoques adecuados para las áreas críticas, considerando impacto y probabilidad.
3. **Planificar recursos y cronograma operativo:** asignar roles, herramientas y tiempos realistas a cada fase.
4. **Elaborar casos de prueba exhaustivos:** redactar casos funcionales y de seguridad con criterios claros de validación y trazabilidad.
5. **Integrar automatización y métricas clave:** implementar herramientas automatizadas y definir indicadores (KPI) de cobertura, eficacia y eficiencia.
6. **Documentar y revisar de forma continua:** mantener registros actualizados, incorporar hallazgos y ajustar la estrategia a medida que el sistema evoluciona.

### 2.19 Reflexión: la prueba de la perspectiva

La pregunta de reflexión del tema es: si hoy un atacante lograra eludir el sistema de autenticación, ¿el plan de pruebas actual tiene un caso diseñado para detectar cómo sucedió?

- Si la respuesta es negativa, deben revisarse la integración de las guías OWASP y el diseño de los casos de seguridad.
- Si es afirmativa, debe verificarse si ese caso está automatizado para ejecutarse en cada cambio de código y detectar regresiones a tiempo.

### 2.20 Conclusiones del tema

- **Base del éxito:** un plan bien diseñado es el fundamento de un software confiable, seguro y de calidad.
- **Integración temprana:** incorporar calidad y seguridad desde el inicio reduce costos y riesgos a largo plazo.
- **Mejora continua:** la planificación estructurada, la colaboración y el aprendizaje constante sostienen los resultados.
- **Puntos clave:** aplicar *shift-left testing*; asegurar la independencia del equipo de pruebas; utilizar métricas e indicadores para medir la eficacia del proceso.

### 2.21 Errores frecuentes

1. Enumerar tipos de prueba sin justificar su elección por riesgo o requisito.
2. Formular objetivos y criterios de aceptación no medibles.
3. Omitir los criterios de entrada, salida y suspensión.
4. Tratar la seguridad como una sección aparte y no como casos asociados a cada requisito crítico.
5. Presentar cifras ilustrativas como si fueran mediciones propias.
6. Confundir el riesgo (posibilidad) con el defecto (hecho comprobado).
7. Asignar herramientas sin justificar su uso ni indicar el responsable.

### 2.22 Relación con estándares

| Estándar | Relación con el tema |
|---|---|
| IEEE 829 / ISO/IEC/IEEE 29119-3:2021 | Estructura del plan y de la documentación de pruebas |
| ISO/IEC/IEEE 29119-2:2021 | Procesos de prueba, incluida la gestión basada en riesgos |
| ISTQB CTFL v4.0 | Principios, niveles, tipos y técnicas de prueba |
| OWASP WSTG v4.2 y OWASP Top 10:2025 | Diseño de casos de seguridad y priorización de vulnerabilidades |
| NIST CSF 2.0 | Justificación de controles de ciberseguridad |
| ISO/IEC 25010:2023 | Características de calidad que orientan los tipos de prueba |

### 2.23 Preguntas de repaso

1. Defina plan de pruebas y enuncie su propósito fundamental.
2. Enumere los cuatro elementos clave del plan y explique el contenido mínimo de cada uno.
3. Redacte un objetivo de prueba medible para un módulo de agendamiento de horas.
4. Calcule el nivel de riesgo de un evento de probabilidad media e impacto alto en una matriz 3 × 3 e indique su prioridad.
5. Explique la diferencia entre SAST y DAST y señale una herramienta de cada tipo.
6. Describa el resultado esperado completo de un caso contra inyección SQL.
7. Explique por qué la independencia del equipo de pruebas favorece la objetividad.
8. Indique qué métricas de la lista de indicadores del tema no corresponden al software y proponga su equivalente.
9. Ordene los seis pasos del flujo de trabajo de la estrategia de pruebas.
10. Señale la categoría de OWASP Top 10:2025 a la que pertenece una contraseña almacenada en texto plano.

---

## Capítulo 3. Plan de pruebas en entornos de contenedores Docker (tema 2.1.1, segunda parte)

**Indicador de logro:** IL2.1. **Propósito del capítulo:** comprender por qué los contenedores son la base del entorno de pruebas del caso semestral y qué prácticas de calidad y seguridad deben aplicarse a las imágenes.

### 3.1 Importancia de un plan robusto en entornos de contenedores

Un plan de pruebas sólido debe contemplar validaciones que garanticen la integridad de cada componente del sistema. En el caso semestral, el enfoque utiliza imágenes Docker como base de las pruebas, porque permiten crear entornos **reproducibles y consistentes** en los que las validaciones son precisas y controladas.

**Objetivo principal.** Garantizar la integridad, la confiabilidad y la protección en entornos de contenedores mediante estrategias sistemáticas de validación, verificación y monitoreo continuo de seguridad.

### 3.2 Conceptos fundamentales

| Concepto | Definición |
|---|---|
| **Docker** | Plataforma que empaqueta y ejecuta aplicaciones en contenedores |
| **Imagen Docker** | Plantilla inmutable que encapsula todos los componentes necesarios para ejecutar una aplicación: capa de sistema operativo, bibliotecas, dependencias y configuraciones. Su inmutabilidad garantiza una ejecución consistente en cualquier entorno |
| **Contenedor** | Instancia en ejecución de una imagen, aislada de otros procesos del sistema anfitrión |
| **Dockerfile** | Archivo de texto que declara, instrucción por instrucción, cómo construir una imagen |
| **Capa** | Resultado de cada instrucción del Dockerfile; las imágenes se componen de capas superpuestas |
| **Registro (*registry*)** | Repositorio de imágenes, por ejemplo Docker Hub |
| **Docker Compose** | Herramienta que define y levanta aplicaciones de varios contenedores mediante un archivo `docker-compose.yml` |
| **Volumen** | Almacenamiento persistente que sobrevive a la eliminación del contenedor |
| **Mapeo de puertos** | Asociación `puerto_anfitrión:puerto_contenedor` que expone un servicio, por ejemplo `3333:80` |

**Beneficios de las imágenes para las pruebas:**

- contenedores replicables y uniformes, con independencia del entorno de despliegue;
- control de versiones preciso, con trazabilidad de cambios y posibilidad de volver a estados anteriores;
- personalización total para entornos de prueba específicos o simulaciones controladas;
- aislamiento entre aplicaciones, que evita conflictos por dependencias compartidas.

**Relación con la calidad de la prueba.** Un resultado de prueba solo es válido si el entorno es conocido y reproducible. Si el entorno de prueba difiere del de producción, un caso aprobado puede fallar después; con imágenes versionadas, cualquier miembro del equipo puede reproducir una falla con exactamente las mismas versiones.

### 3.3 Levantamiento de imágenes: metodología

El proceso de levantamiento de imágenes requiere una metodología estructurada que comienza con la definición de los requisitos y las dependencias:

1. **Creación y captura:** construcción sistemática de imágenes específicas para pruebas, documentando cada paso y decisión técnica.
2. **Definición con Dockerfile:** uso de Dockerfile para definir entornos exactos, de modo que cada dependencia y configuración quede declarada de forma explícita.
3. **Implementación práctica:** por ejemplo, un Dockerfile personalizado para una aplicación Node.js con versiones específicas, variables de entorno controladas y optimizaciones para pruebas.

**Ejemplo de Dockerfile para una API Node.js orientado a pruebas**

```dockerfile
# Imagen base oficial, versión fija y variante mínima
FROM node:20-alpine

# Directorio de trabajo
WORKDIR /app

# Dependencias primero, para aprovechar la caché de capas
COPY package*.json ./
RUN npm ci --omit=dev

# Código de la aplicación
COPY src ./src

# Variables de entorno controladas
ENV NODE_ENV=test

# Usuario sin privilegios (la imagen oficial incluye el usuario "node")
USER node

EXPOSE 4000
CMD ["node", "src/index.js"]
```

Cada línea responde a una práctica: versión fija (reproducibilidad), variante mínima (menor superficie de ataque), instalación determinista con `npm ci` (versiones exactas del archivo de bloqueo), usuario sin privilegios (mínimo privilegio) y variables de entorno declaradas (configuración controlada).

### 3.4 Del Dockerfile al contenedor en ejecución

```
Dockerfile ──(docker build)──► Imagen Docker ──(docker run / docker compose up)──► Contenedor en ejecución
```

Cada etapa contribuye a un entorno de pruebas robusto y reproducible: el Dockerfile documenta, la imagen fija y el contenedor ejecuta.

### 3.5 Estrategias para el diseño del plan con imágenes Docker

| Estrategia | Descripción |
|---|---|
| Objetivos claros de calidad y seguridad | Métricas medibles y criterios de aceptación alineados con los estándares de la industria y los requisitos del negocio |
| Selección de imágenes base | Priorizar imágenes oficiales y minimizadas, como Alpine Linux, que ofrecen menor superficie de ataque y mayor eficiencia; la imagen base afecta directamente la seguridad y el rendimiento |
| Versionado y etiquetado | Versionado semántico (MAYOR.MENOR.PARCHE) y etiquetas descriptivas, con registro de cambios y fecha de creación de cada versión |
| Automatización integral | Automatizar la construcción, el levantamiento y el despliegue de imágenes mediante pipelines CI/CD para reducir errores humanos |

**Error frecuente.** Usar la etiqueta `latest`. Esa etiqueta cambia con el tiempo, de modo que dos ejecuciones del mismo plan pueden correr sobre versiones diferentes y el resultado deja de ser reproducible.

### 3.6 Buenas prácticas de seguridad en imágenes Docker

| Práctica | Descripción | Verificación posible |
|---|---|---|
| **Imágenes endurecidas** | Imágenes diseñadas para minimizar las vulnerabilidades conocidas y ofrecer una base segura | Escaneo de la imagen en busca de vulnerabilidades conocidas (CVE) |
| **Minimización de capas** | Reducir capas y dependencias innecesarias; cada componente adicional es un posible vector de ataque | Revisión del Dockerfile; tamaño de la imagen |
| **Mínimo privilegio** | No ejecutar procesos como *root* dentro del contenedor; usar usuarios con los permisos estrictamente necesarios | `docker exec <contenedor> whoami` no debe devolver `root` |
| **Aislamiento avanzado** | Espacios de nombres (*namespaces*) de Linux y restricción de capacidades (*capabilities*) como barrera adicional entre contenedores y anfitrión | Revisión de la configuración de Compose (por ejemplo, ausencia de `privileged: true`) |

Otras prácticas que complementan las anteriores: no incluir secretos en la imagen ni en el repositorio (el archivo `.env` no debe versionarse con credenciales reales), no exponer el puerto de la base de datos al exterior cuando no es necesario y declarar la red interna entre servicios.

### 3.7 Herramientas recomendadas para planificar pruebas

| Categoría | Herramientas | Función |
|---|---|---|
| Gestión de casos | TestRail, Zephyr | Organizar, ejecutar y rastrear casos de forma centralizada y colaborativa |
| Automatización | Selenium, Appium | Automatizar pruebas web y móviles, reduciendo el esfuerzo manual repetitivo |
| Seguimiento de incidencias | Jira, Bugzilla | Registrar, seguir y resolver defectos con trazabilidad completa |

### 3.8 Errores frecuentes

1. Probar sobre un entorno no identificado (sin versión de imagen ni fecha de levantamiento).
2. Ejecutar contenedores como *root* o en modo privilegiado.
3. Guardar credenciales reales en el archivo `.env` o en el repositorio.
4. Exponer el puerto de la base de datos sin necesidad.
5. No registrar el entorno de prueba como evidencia del informe.

### 3.9 Preguntas de repaso

1. Defina imagen, contenedor y Dockerfile, y explique su relación.
2. Explique por qué la inmutabilidad de la imagen favorece la validez de los resultados de prueba.
3. Indique cuatro estrategias de diseño del plan con imágenes Docker.
4. Describa cuatro buenas prácticas de seguridad en imágenes y la forma de verificarlas.
5. Explique el riesgo de utilizar la etiqueta `latest` en un entorno de pruebas.

---

## Capítulo 4. Aplicación: plan de pruebas estratégico (actividad 2.1.2)

**Indicador de logro:** IL2.1. **Modalidad:** individual, 45 minutos. **Propósito:** pasar de la creación de casos aislados a una visión integral del aseguramiento de la calidad, en la que las decisiones técnicas se fundamentan en riesgo, seguridad, trazabilidad y optimización de recursos desde las primeras etapas del ciclo de vida.

### 4.1 Situación

Se asume el rol de líder de QA (*QA Lead*) para el lanzamiento de una aplicación de banca móvil. El plan debe garantizar que el sistema sea **confiable, eficiente, seguro, trazable y sostenible en el tiempo**, y debe anticipar riesgos, priorizar esfuerzos y justificar cada decisión técnica. El caso es genérico; su método se traslada luego al caso semestral.

### 4.2 Paso 1: definición de la estrategia de pruebas

**a) Caja negra para la validación de interfaces.** Se aplica a los módulos funcionales (transferencias, pagos, recargas, gestión de tarjetas) y permite detectar errores de:

| Tipo de error | Ejemplo de caso |
|---|---|
| Validación de datos | Monto negativo, cero o con más decimales de los permitidos |
| Flujo de usuario | Abandonar una transferencia a mitad del proceso y retomarla |
| Reglas de negocio | Transferir un monto superior al límite diario |
| Usabilidad y consistencia | Mensajes y botones coherentes entre pantallas |

**b) Caja blanca para la lógica crítica.** Se aplica a procesos internos donde la precisión es esencial (cálculo de intereses, validación de OTP, cifrado, límites de transacción) mediante:

- **pruebas de caminos independientes:** un caso por cada camino básico, según la complejidad ciclomática;
- **análisis de bucles:** cero, una, varias y el máximo de iteraciones (por ejemplo, número de reintentos de OTP);
- **cobertura de decisiones y condiciones:** cada decisión y cada condición atómica evaluadas como verdaderas y falsas.

Estas técnicas previenen fallas lógicas, desbordamientos y vulnerabilidades; por ejemplo, una condición mal evaluada en la validación de OTP puede permitir el acceso con un código expirado.

**c) Enfoque híbrido para la integración.** Combina técnicas estructurales y funcionales para validar:

- la comunicación entre la aplicación móvil y el *backend*;
- el manejo de errores en la API (códigos de estado y mensajes);
- la sincronización de estados (saldo actualizado tras una transferencia);
- la integridad de los datos en tránsito (TLS, firma o verificación de mensajes).

### 4.3 Paso 2: evaluación de riesgos y seguridad

La banca móvil es un entorno de alto riesgo: un defecto que llega a producción puede multiplicar su costo de corrección hasta diez veces.

**a) Identificación de módulos críticos.** Se identifican los componentes con complejidad ciclomática elevada (V(G) > 20) y se justifica que requieren mayor profundidad de pruebas, revisión de código, pruebas negativas y de estrés, y prioridad en el cronograma. La justificación técnica es que una V(G) superior a 20 indica alta complejidad y alto riesgo de defectos, además de exigir al menos ese número de casos para cubrir los caminos básicos.

**b) Seguridad de datos y flujo de información.** Una estrategia de **análisis de flujo de datos** (seguimiento de cada variable desde su definición hasta su uso) debe garantizar que:

| Exigencia | Pregunta de verificación | Técnica |
|---|---|---|
| Las credenciales no se almacenan en texto plano | ¿La contraseña llega a la base de datos solo como resultado de una función de hash con sal? | Revisión de código; consulta a la tabla de usuarios |
| No hay filtraciones en registros, variables temporales ni excepciones | ¿Algún `log` o mensaje de error contiene contraseñas, tokens o datos personales? | Revisión de código; SonarQube; prueba de errores forzados |
| Las sesiones están cifradas | ¿El token viaja solo por HTTPS y se almacena de forma segura? | Inspección del tráfico con Burp Suite o ZAP |
| Los tokens se invalidan correctamente | ¿El token deja de ser válido al cerrar sesión o al expirar? | Reutilizar un token tras el cierre de sesión |

**Escenarios de ataque pertinentes**, sin convertir la actividad en una prueba de penetración: reutilización de un token tras el cierre de sesión; fuerza bruta sobre el OTP; manipulación del monto en la solicitud interceptada; inyección en campos de búsqueda.

### 4.4 Paso 3: herramientas y métricas

**Herramienta de gestión de pruebas** (TestRail, Azure Test Plans o Jira con Zephyr). Su elección se justifica por tres aportes:

- **trazabilidad:** vínculo entre requisito, caso, ejecución y defecto;
- **reutilización:** repositorio de casos y conjuntos de regresión;
- **soporte a auditorías y cumplimiento:** historial de ejecuciones, responsables y evidencias.

**Métricas de éxito**

| Métrica | Meta | Relevancia en banca |
|---|---|---|
| Confiabilidad (tasa de aprobación en la regresión) | ≥ 95 % | Las operaciones financieras exigen comportamiento estable |
| Reducción del tiempo de ejecución por automatización | Meta definida por el equipo | Permite regresión completa en cada versión |
| Cobertura de requisitos | ≥ 90 % | Asegura que ninguna exigencia regulatoria quede sin verificar |
| Defectos críticos detectados antes de producción | ≥ 98 % | Un defecto crítico en producción afecta dinero y confianza |

### 4.5 Entregables

**a) Matriz de trazabilidad.** Relaciona requisitos, casos de prueba, riesgos y módulos afectados.

| ID requisito | Requisito | Módulo | Riesgo | Nivel | Casos | Técnica |
|---|---|---|---|---|---|---|
| RF-01 | Transferencia a terceros con límite diario | Transferencias | Transferencia sobre el límite | Alto | CP-01, CP-02, CP-03 | Valores límite, tabla de decisión |
| RF-02 | Validación de OTP de seis dígitos con expiración | Autenticación | Acceso con OTP expirado | Crítico | CP-04, CP-05 | Caminos básicos, condiciones |
| RNF-SEG-01 | Contraseñas almacenadas con hash | Usuarios | Fuga de credenciales | Crítico | CP-06 | Flujo de datos, revisión de código |

**b) Cronograma basado en riesgos.** La prioridad se fija según impacto, probabilidad y complejidad.

| Semana | Actividad | Justificación |
|---|---|---|
| 1 | Análisis estático, revisión de módulos con V(G) > 20, casos de autenticación y OTP | Riesgo crítico; la detección temprana reduce el costo |
| 2 | Transferencias, pagos y límites; seguridad de sesión | Riesgo alto, impacto financiero directo |
| 3 | Integración aplicación–API, rendimiento | Riesgo medio |
| 4 | Usabilidad, compatibilidad, regresión final e informe | Riesgo bajo; cierre |

**c) Protocolo de mantenimiento del plan.** Procedimiento para actualizar los casos ante cambios regulatorios, funcionales o de arquitectura:

1. **Disparador:** nueva normativa, cambio de requisito o cambio de arquitectura.
2. **Análisis de impacto:** identificar en la matriz los requisitos, casos y riesgos afectados.
3. **Actualización:** modificar, crear o retirar casos; recalcular el nivel de riesgo.
4. **Revisión y aprobación:** validación por el líder de QA.
5. **Control de versiones:** nueva versión del plan con registro de cambios.
6. **Regresión:** ejecutar los casos afectados y los de regresión asociados.

### 4.6 Traslado al caso semestral

| Elemento de la actividad | Equivalente en un sistema de salud como Cuidarte+ |
|---|---|
| Transferencias, pagos | Agendamiento de horas, registro de pacientes, consulta de antecedentes |
| Validación de OTP | Inicio de sesión y control de roles |
| Credenciales en texto plano | Almacenamiento de contraseñas de pacientes y profesionales |
| Integridad en tránsito | Comunicación cliente–API–base de datos con datos de salud |
| Regulación bancaria | Ley 19.628 / Ley 21.719 (datos personales y sensibles), Ley 20.584 (derechos del paciente y ficha clínica), Ley 21.663 (ciberseguridad) |

### 4.7 Errores frecuentes

1. Elegir técnicas sin vincularlas a módulos concretos.
2. Declarar módulos críticos sin calcular ni estimar su complejidad.
3. Definir métricas sin meta numérica.
4. Entregar una matriz que no incluye la columna de riesgo.
5. Omitir el protocolo de mantenimiento.

### 4.8 Preguntas de repaso

1. Indique qué enfoque (caja negra, blanca o híbrido) corresponde a la validación de OTP, a la interfaz de pagos y a la sincronización del saldo.
2. Justifique por qué un módulo con V(G) > 20 requiere prioridad en el cronograma.
3. Enumere cuatro exigencias del análisis de flujo de datos aplicadas a credenciales y sesiones.
4. Indique las cuatro columnas mínimas de la matriz de trazabilidad de la actividad.
5. Describa los pasos de un protocolo de mantenimiento del plan.

---

## Capítulo 5. Levantamiento del entorno Docker del caso semestral (guía 2.1.3)

**Indicador de logro:** IL2.1. **Modalidad:** individual, 2 horas. **Objetivo:** levantar y conocer el entorno de desarrollo del caso semestral, sobre el cual se verifican la calidad, la seguridad y el cumplimiento legal y normativo de un software real.

### 5.1 Prerrequisitos

- Docker instalado (Docker Desktop, desde https://www.docker.com/).
- Visual Studio Code.
- El archivo de código fuente del caso asignado: `CodigoFuenteA.zip` (caso A, Atlas) o `CodigoFuenteB.zip` (caso B, Cuidarte+).

### 5.2 Estructura del proyecto

| Elemento | Contenido |
|---|---|
| `BACKEND/` | Código fuente de la API |
| `FRONTEND/` | Código fuente del cliente |
| `.env` | Variables de entorno que utiliza Docker para generar las imágenes; incluye valores predefinidos que pueden personalizarse |
| `docker-compose.yml` | Definición de la construcción de las imágenes, las variables de entorno y la orquestación entre contenedores |
| `README.md` | Información descriptiva del proyecto |
| `.gitignore`, `package.json` | Archivos de control de versiones y de dependencias del proyecto |

### 5.3 Procedimiento

1. Descomprimir el código fuente del caso.
2. Abrir Visual Studio Code e importar la carpeta con la opción **Abrir carpeta**.
3. Reconocer la estructura de carpetas (tabla 5.2).
4. Iniciar Docker.
5. Abrir una terminal en el directorio raíz del proyecto.
6. Ejecutar `docker-compose up -d` (en versiones recientes también `docker compose up -d`). La opción `-d` ejecuta los contenedores en segundo plano. Los mensajes pueden variar; lo importante es que no aparezcan errores.
7. Verificar en Docker Desktop, sección **Containers**, que las imágenes se crearon y que los contenedores están en ejecución. Deben aparecer tres componentes con el nombre del caso (Atlas o Cuidarteplus).
8. Abrir el cliente en el navegador (en el ejemplo, http://localhost:3333). El puerto puede variar según el caso; se confirma en la columna de puertos del contenedor.
9. Abrir la documentación de la API en `/docs` (en el ejemplo, http://localhost:4444/docs), donde aparece la definición de los servicios.

### 5.4 Resultado esperado en el caso B (Cuidarte+)

La salida de `docker-compose up -d` muestra la construcción de las imágenes del *backend* y del *frontend*, la creación del volumen de datos de PostgreSQL y el inicio de tres contenedores:

| Contenedor | Imagen | Puertos (anfitrión:contenedor) | Acceso |
|---|---|---|---|
| `cuidarteplus-postgres-ev` | `postgres` | `15442:5432` | `jdbc:postgresql://localhost:15442` |
| `cuidarteplus-backend-ev` | imagen del *backend* | `4444:4000` | API en http://localhost:4444 y Swagger en http://localhost:4444/docs |
| `cuidarteplus-frontend-ev` | imagen del *frontend* | `3333:80` | Cliente en http://localhost:3333 |

El contenedor de base de datos aparece en estado *Healthy*, lo que indica que superó su comprobación de salud antes de iniciar el *backend*.

La documentación Swagger, titulada "cuidarteplus API (español)" (versión 1.0.0, especificación OpenAPI 3.0), expone, entre otros, los servicios `POST /autenticacion/login` (iniciar sesión), `POST /autenticacion/registro` (registrar nuevo usuario), `GET /usuarios` (listar usuarios), `POST /usuarios` (crear usuario) y `GET /usuarios/{id}` (obtener usuario). Servicios como `GET /usuarios/{id}` son candidatos directos a pruebas de autorización por propiedad del recurso (OWASP A01:2025).

### 5.5 Uso del entorno en el plan de pruebas

| Elemento del entorno | Uso en pruebas |
|---|---|
| Cliente (puerto 3333) | Pruebas funcionales, de usabilidad, compatibilidad y accesibilidad (caja negra); automatización con Selenium |
| API y Swagger (puerto 4444) | Pruebas de servicios, autorización por rol y por recurso, validación de entradas, manejo de errores; DAST con ZAP, Burp Suite, Nikto y SQLMap; carga con JMeter |
| Base de datos (puerto 15442) | Verificación de persistencia, de almacenamiento de contraseñas y de integridad de datos |
| Código `BACKEND/` y `FRONTEND/` | Análisis estático con SonarQube; revisión manual de rutas y controles de acceso (caja blanca) |
| `docker-compose.yml` y `.env` | Revisión de configuración segura: secretos, puertos expuestos, usuario de ejecución |

**Evidencia del entorno para el informe.** Captura de los contenedores en ejecución, versión de las imágenes, fecha y hora de levantamiento, y captura de Swagger. Esta evidencia sustenta la sección de entorno de pruebas del informe EP3.

### 5.6 Comandos útiles y solución de problemas

| Situación | Comando o acción |
|---|---|
| Ver contenedores en ejecución | `docker ps` |
| Ver registros de un servicio | `docker compose logs backend` (nombre según el archivo Compose) |
| Detener el entorno | `docker compose down` |
| Reiniciar con datos limpios | `docker compose down -v` y luego `docker compose up -d` (elimina el volumen de datos) |
| Reconstruir tras cambios en el código | `docker compose up -d --build` |
| Puerto ocupado | Cambiar el puerto del anfitrión en `.env` o en `docker-compose.yml`, o detener el proceso que lo usa |
| El *backend* no conecta a la base de datos | Revisar las variables de conexión en `.env` y el estado *Healthy* del contenedor de PostgreSQL |

### 5.7 Errores frecuentes

1. Ejecutar el comando fuera del directorio raíz del proyecto.
2. Suponer los puertos del ejemplo sin confirmarlos en el contenedor.
3. No registrar la evidencia del entorno antes de iniciar la ejecución.
4. Usar `docker compose down -v` sin advertir que borra los datos de prueba.

### 5.8 Preguntas de repaso

1. Describa la función de cada elemento de la estructura del proyecto.
2. Explique el significado del mapeo `3333:80`.
3. Indique cómo se comprueba que el entorno está correctamente levantado.
4. Señale qué tipo de prueba se ejecuta sobre cada uno de los tres contenedores.
5. Explique qué evidencias del entorno deben incluirse en el informe.

---

## Capítulo 6. Técnicas avanzadas de diseño de casos de prueba (tema 2.2.1)

**Indicador de logro:** IL2.2. **Propósito del capítulo:** dominar las técnicas formales que permiten derivar casos de prueba de manera sistemática, justificable y con cobertura medible.

### 6.1 Problema de partida: el tester como investigador

El tema se abre con dos preguntas: ¿qué es lo peor que podría ocurrir si se entrega un software que parece funcionar bien, pero no tiene un solo caso de prueba documentado?, y ¿qué hace que un caso de prueba sea bueno: su complejidad o su claridad? La respuesta orienta todo el tema: un caso de prueba no es un trámite administrativo, sino la herramienta principal para reducir costos y tiempos en el ciclo de vida del software (idea atribuida en el tema al autor Mc Mullin), y su valor depende de su claridad, no de su complejidad.

### 6.2 Fundamentos de los casos de prueba

**Definición (IEEE 610).** Un **caso de prueba** es un conjunto estructurado de entradas, condiciones de ejecución y resultados esperados, desarrollado para validar un requisito específico del sistema. El glosario IEEE 610.12 fue posteriormente reemplazado por el vocabulario ISO/IEC/IEEE 24765, que conserva el concepto.

**Importancia.** Los casos de prueba son la base para garantizar la calidad, detectar errores tempranamente y asegurar que la funcionalidad cumple con las expectativas.

**Beneficios.** Mejoran la comunicación entre los equipos, aumentan la cobertura de pruebas y contribuyen a reducir costos operativos y tiempos de desarrollo.

**Papel de los casos bien diseñados**

| Función | Descripción |
|---|---|
| Guía uniforme de ejecución | Instrucciones claras y consistentes que aseguran que todos los miembros del equipo ejecuten las pruebas del mismo modo, sin ambigüedades |
| Colaboración | Lenguaje común entre desarrolladores, testers y partes interesadas |
| Automatización | Permiten automatizar y reutilizar las pruebas en ciclos posteriores |

**Conceptos relacionados**

| Concepto | Definición |
|---|---|
| Condición de prueba | Aspecto verificable de un requisito (por ejemplo, "el correo debe tener formato válido") |
| Escenario de prueba | Descripción de alto nivel de *qué* se prueba |
| Caso de prueba | Especificación de *cómo* se prueba: precondiciones, pasos, datos y resultado esperado |
| Procedimiento o guion de prueba | Secuencia de casos y acciones para su ejecución |
| Conjunto (*suite*) de prueba | Agrupación de casos con un fin común, por ejemplo la regresión de autenticación |
| Oráculo de prueba | Fuente que permite determinar el resultado esperado (requisito, norma, cálculo de referencia) |
| Cobertura | Grado, expresado en porcentaje, en que un conjunto de pruebas ejercita un elemento de cobertura (requisitos, sentencias, decisiones) |

### 6.3 Clasificación de las técnicas de diseño

| Familia | Base | Perspectiva | Técnicas |
|---|---|---|---|
| **Caja negra** | Entradas y salidas, sin conocer la implementación | Usuario final | Partición de equivalencia; análisis de valores límite; tablas de decisión |
| **Caja blanca** | Estructura interna: código fuente, flujo de control, arquitectura | Desarrollador y auditor de código | Caminos básicos; cobertura de sentencias; condiciones; bucles; flujo de datos |
| **Híbridas** | Combinación de ambas | Equilibrada, para maximizar la cobertura | Pruebas basadas en riesgos; pruebas exploratorias estructuradas |

**Pruebas exploratorias estructuradas.** Diseño y ejecución simultáneos, guiados por una misión o carta de prueba (*test charter*) con objetivo, alcance y tiempo acotado, y con registro de lo explorado. Se diferencian de la prueba improvisada porque dejan evidencia y se orientan por riesgo.

### 6.4 Partición de equivalencia

**Definición.** Técnica de caja negra que divide el dominio de entrada (o de salida) en **clases de equivalencia**, conjuntos de valores que el sistema debería procesar de la misma manera. Su premisa es que, si un valor de una clase funciona correctamente, todos los valores de esa clase deberían comportarse igual.

**Pasos:**

1. **Identificar el dominio de entrada:** analizar todas las entradas posibles y sus características.
2. **Dividir en clases equivalentes:** agrupar las entradas que producen el mismo comportamiento, válidas e inválidas.
3. **Seleccionar valores representativos:** elegir un valor de cada clase.

**Ejemplo con dos rangos válidos.** Un sistema acepta valores en los rangos 1–10 y 20–30. Se identifican la clase válida 1–10, la clase válida 20–30 y la clase de valores inválidos fuera de ambos rangos. Un valor de cada clase basta para la validación. En un análisis más fino, la clase inválida se divide en tres: menores que 1, entre 11 y 19, y mayores que 30, porque cada una corresponde a una comparación distinta en el código.

**Ejemplo completo (rango 1 a 10, solo numérico).** Requisito: el campo debe aceptar exclusivamente valores numéricos entre 1 y 10, inclusive; cualquier otro valor debe rechazarse con un mensaje de error.

| Clase | Descripción |
|---|---|
| Válida | Valores numéricos entre 1 y 10 |
| Inválida inferior | Valores numéricos menores que 1 |
| Inválida superior | Valores numéricos mayores que 10 |
| Inválida de tipo | Valores no numéricos (letras, símbolos) |

| ID | Valor | Clase | Resultado esperado |
|---|---|---|---|
| TC-01 | 5 | Válida (1–10) | Aceptado |
| TC-02 | -3 | Inválida inferior | Rechazado con mensaje de error |
| TC-03 | 15 | Inválida superior | Rechazado con mensaje de error |
| TC-04 | "abc" | Inválida de tipo | Rechazado con mensaje de error |

**Regla práctica.** Las clases válidas pueden combinarse en un mismo caso; las inválidas deben probarse **de a una por caso**, para que un rechazo pueda atribuirse con certeza a una causa.

### 6.5 Análisis de valores límite (BVA)

**Definición.** Técnica de caja negra que prueba los valores ubicados en las fronteras de las particiones de equivalencia, donde la experiencia muestra que se concentra una gran parte de los errores.

**Fundamento.** Los errores de comparación, como escribir `<` en lugar de `<=`, se manifiestan precisamente en los límites.

**Valores que se prueban**

| Zona | Valores |
|---|---|
| Límite inferior | mínimo − 1, mínimo, mínimo + 1 |
| Valores centrales | uno o más valores representativos del rango |
| Límite superior | máximo − 1, máximo, máximo + 1 |

Esta forma se conoce como BVA de tres valores. La variante de dos valores prueba solo el límite y su vecino exterior (0, 1, 10 y 11 en el ejemplo).

**Ejemplo (rango 1 a 10)**

| Caso | Valor | Descripción | Resultado esperado |
|---|---|---|---|
| 1 | 0 | Justo antes del límite inferior | Rechazado con mensaje de error |
| 2 | 1 | Límite inferior exacto | Aceptado |
| 3 | 2 | Dentro del rango | Aceptado |
| 4 | 9 | Próximo al límite superior | Aceptado |
| 5 | 10 | Límite superior exacto | Aceptado |
| 6 | 11 | Justo después del límite superior | Rechazado con mensaje de error |

Los valores 0, 1, 10 y 11 son los más relevantes, porque detectan el uso incorrecto de operadores de comparación.

**Visualización conjunta de partición y límites**

| Zona | Significado | Valores |
|---|---|---|
| Clase inválida inferior | Valores menores que el mínimo | -5, -1, 0 |
| Límite inferior crítico | Transición de inválido a válido | 0, 1, 2 |
| Clase válida central | Valores dentro del rango | 3, 5, 8 |
| Límite superior crítico | Transición de válido a inválido | 9, 10, 11 |
| Clase inválida superior | Valores mayores que el máximo | 12, 15, 100 |

La partición asegura que cada comportamiento esté representado; el análisis de límites asegura que las transiciones entre comportamientos estén bien implementadas. Por eso ambas técnicas se aplican juntas.

**Ejemplo aplicado a un registro.** Si el nombre debe tener entre 2 y 100 caracteres, los valores de prueba son 1, 2, 3, 99, 100 y 101 caracteres.

### 6.6 Tablas de decisión

**Definición.** Técnica de caja negra que representa de forma sistemática todas las combinaciones de condiciones de entrada y las acciones esperadas para cada combinación. Es adecuada cuando el comportamiento depende de varias condiciones combinadas.

**Ventajas:**

- visualización clara de todas las combinaciones posibles;
- identificación sistemática de casos sin omisiones;
- detección de inconsistencias en la lógica de negocio;
- documentación comprensible para partes interesadas no técnicas.

**Componentes:**

1. **Condiciones:** variables o factores que afectan el comportamiento.
2. **Combinaciones (reglas):** todas las combinaciones posibles de los valores de las condiciones. Con *n* condiciones binarias hay 2ⁿ reglas.
3. **Acciones:** resultados esperados para cada combinación.

**Ejemplo (formulario con dos campos obligatorios).** El botón de envío debe habilitarse solo cuando ambos campos están completos y válidos. C1: el nombre completo está lleno; C2: el correo tiene formato válido.

| Regla | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| C1 Nombre completo | No | No | Sí | Sí |
| C2 Correo válido | No | Sí | No | Sí |
| Botón habilitado | No | No | No | Sí |
| Permitir envío | No | No | No | Sí |
| Mensaje de error | Ambos campos | Falta nombre | Correo inválido | — |

La tabla genera cuatro casos de prueba (2² = 4) que cubren todas las combinaciones.

**Ejemplo aplicado de seguridad (acceso a una ficha).** Condiciones: C1 sesión válida; C2 rol profesional; C3 el profesional atiende al paciente. Con tres condiciones hay ocho reglas; la tabla puede simplificarse cuando una condición hace irrelevantes las demás (si C1 es falsa, el acceso se deniega sin importar C2 y C3).

| Regla | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| C1 Sesión válida | No | Sí | Sí | Sí |
| C2 Rol profesional | — | No | Sí | Sí |
| C3 Atiende al paciente | — | — | No | Sí |
| Acción | 401 No autenticado | 403 Prohibido | 403 Prohibido | 200 Acceso y registro del acceso |

### 6.7 Técnicas de caja blanca

Las técnicas de caja blanca requieren conocer el código fuente y la estructura interna. Permiten validar no solo que el sistema funcione, sino que lo haga de manera eficiente y que todas sus rutas hayan sido ejercitadas.

| Técnica | Definición |
|---|---|
| **Caminos básicos** | Garantiza que cada camino lógico independiente se ejecute al menos una vez |
| **Pruebas de condiciones** | Valida las expresiones condicionales (`if`, `switch`, operadores lógicos) para que cada rama funcione en todos los escenarios |
| **Pruebas de bucles** | Valida los ciclos (`for`, `while`, `do-while`) con distintos números de iteraciones, incluidos cero y muchas |
| **Cobertura de sentencias** | Mide el porcentaje de sentencias ejecutadas al menos una vez |
| **Flujo de datos** | Verifica el uso correcto de las variables desde su definición hasta su uso |

**Niveles de cobertura estructural (de menor a mayor exigencia)**

| Cobertura | Exige | Fórmula |
|---|---|---|
| Sentencias | Cada sentencia ejecutada al menos una vez | Sentencias ejecutadas / sentencias totales × 100 |
| Decisiones (ramas) | Cada decisión evaluada como verdadera y como falsa | Resultados de decisión ejercitados / resultados totales × 100 |
| Condiciones | Cada condición atómica evaluada como verdadera y como falsa | Resultados de condición ejercitados / totales × 100 |
| Decisión/condición | Ambas exigencias anteriores a la vez | — |
| Caminos básicos | Un conjunto de caminos linealmente independientes | V(G) caminos |

El 100 % de cobertura de decisiones implica el 100 % de cobertura de sentencias, pero no a la inversa. Un `if` sin `else` puede cubrir todas sus sentencias con un solo caso verdadero, sin probar nunca la rama falsa.

### 6.8 Complejidad ciclomática

**Definición.** La complejidad ciclomática, propuesta por Thomas J. McCabe en 1976, es una métrica que mide el número de caminos linealmente independientes en el grafo de flujo de control de un programa. Indica el número mínimo de casos de prueba necesarios para cubrir los caminos básicos.

**Fórmulas equivalentes:**

- V(G) = E − N + 2P, donde E es el número de aristas, N el de nodos y P el de componentes conectados (P = 1 para una función).
- V(G) = número de nodos de decisión + 1.
- V(G) = número de regiones cerradas del grafo + 1.

**Interpretación**

| V(G) | Interpretación | Acción |
|---|---|---|
| 1–10 | Código simple, fácil de probar | Pruebas estándar |
| 11–20 | Complejidad moderada | Mayor cantidad de casos y revisión |
| 21–50 | Código complejo | Refactorización recomendada; revisión de código obligatoria |
| > 50 | Código muy complejo | Alto riesgo; difícil de probar y mantener |

**Ejemplo con el método de caminos básicos**

```javascript
function login(correo, clave) {
  if (!correo || !clave) return 400;          // decisión 1
  const u = buscarUsuario(correo);
  if (!u) return 401;                          // decisión 2
  if (u.bloqueado) return 423;                 // decisión 3
  if (!verificarHash(clave, u.hash)) return 401; // decisión 4
  return emitirToken(u);
}
```

- **Decisiones + 1:** 4 + 1 = **5**.
- **Grafo:** nodos 1 (decisión 1), 2 (retorno 400), 3 (búsqueda y decisión 2), 4 (retorno 401), 5 (decisión 3), 6 (retorno 423), 7 (decisión 4), 8 (retorno 401), 9 (retorno del token) y 10 (salida). Hay N = 10 nodos y E = 13 aristas (ocho de las decisiones y cinco de los retornos a la salida). V(G) = 13 − 10 + 2 = **5**.
- Si se cuentan por separado las dos condiciones de `!correo || !clave`, la complejidad sube a 6 y se agrega un caso (correo presente con clave vacía).

| Camino | Datos | Resultado esperado |
|---|---|---|
| 1 | Correo vacío | 400 |
| 2 | Correo no registrado | 401 |
| 3 | Usuario bloqueado | 423 |
| 4 | Clave incorrecta | 401 |
| 5 | Credenciales válidas | Token emitido |

**Pregunta de comprobación del tema.** Una función con V(G) = 5 requiere como mínimo **5 casos de prueba** para ejecutar todos los caminos independientes al menos una vez (alternativa B). La alternativa C es incorrecta, porque la complejidad ciclomática es una propiedad estructural del código y no depende de las entradas del usuario.

### 6.9 Pruebas de bucles

Los bucles son fuente frecuente de desbordamientos, condiciones de término incorrectas y problemas de rendimiento.

| Tipo de bucle | Estrategia |
|---|---|
| **Simple** (máximo *n* iteraciones) | Probar 0 iteraciones (omitir el bucle), 1, 2, un valor típico *m* < *n*, *n* − 1, *n* y *n* + 1 |
| **Anidado** | Comenzar por el bucle más interno, con los externos en valores mínimos, y avanzar hacia afuera; validar las combinaciones críticas |
| **Concatenado** | Si son independientes, tratar cada uno como bucle simple; si están relacionados, tratarlos como anidados |

**Ejemplo.** Un bloqueo tras cinco intentos fallidos: se prueban 0, 1, 2, 3, 4, 5 y 6 intentos, verificando que el bloqueo ocurre exactamente en el quinto y que el sexto es rechazado.

### 6.10 Análisis de flujo de datos

**Definición.** Técnica de caja blanca que sigue cada variable a lo largo del programa, desde su **definición** (asignación de un valor) hasta su **uso** (lectura en un cálculo o en una condición).

**Anomalías que detecta**

| Patrón | Significado | Ejemplo |
|---|---|---|
| Definición–uso (du) | Patrón correcto; cada par debe cubrirse con una prueba | `hash = bcrypt(clave)` seguido de `guardar(hash)` |
| Definición–redefinición sin uso (dd) | Una asignación no sirve para nada; puede indicar un error de lógica | `token = generar(); token = null;` |
| Uso sin definición previa (ur) | Se lee una variable que no tiene valor | Usar `rol` antes de cargarlo desde el token |

**Aplicación en seguridad.** Seguir el recorrido de un dato sensible (contraseña, token, diagnóstico) permite verificar que no llega a un registro de eventos, a un mensaje de error o a la base de datos en texto plano.

### 6.11 Combinación de técnicas

Ninguna técnica por sí sola garantiza la calidad. La práctica profesional combina:

- **caja negra para interfaces:** entradas, salidas y comportamiento del usuario;
- **caja blanca para la lógica:** caminos internos y flujo de control;
- **enfoque híbrido para la integración:** ambos enfoques en pruebas complejas.

**Ejemplo (inicio de sesión).** Partición de equivalencia y valores límite para los tipos de credenciales (válidas, inválidas, vacías, de longitud máxima); caminos básicos para la lógica de autenticación, la verificación de la contraseña y el manejo de la sesión; prueba híbrida de la secuencia cliente–API–base de datos.

**Guía de selección**

| Situación | Técnica recomendada |
|---|---|
| Campo con rango numérico o de longitud | Partición de equivalencia + valores límite |
| Regla con varias condiciones combinadas | Tabla de decisión |
| Función con varias ramas o lógica de seguridad | Caminos básicos y condiciones |
| Reintentos, paginación, recorridos de listas | Pruebas de bucles |
| Manejo de datos sensibles | Flujo de datos |
| Tiempo limitado y alto riesgo | Basada en riesgos |
| Funcionalidad nueva o poco documentada | Exploratoria estructurada |

### 6.12 Proceso de creación de casos de prueba

1. **Identificar requisitos:** analizar la documentación de requisitos, las especificaciones funcionales y los criterios de aceptación; identificar todas las condiciones de prueba, incluidos los casos normales, excepcionales y de borde.
2. **Seleccionar la técnica adecuada:** según el contexto, la complejidad y los recursos (caja negra para validación funcional, caja blanca para verificación estructural o una combinación).
3. **Diseñar casos detallados:** identificador único, descripción clara, precondiciones, pasos de ejecución, datos de entrada precisos, resultados esperados verificables y poscondiciones.
4. **Revisar y refinar:** revisión por pares para detectar ambigüedades, omisiones o redundancias; asegurar que los casos sean reproducibles, mantenibles y alineados con los objetivos de calidad.

### 6.13 Herramientas de gestión de casos de prueba

**Beneficios**

| Beneficio | Descripción |
|---|---|
| Documentación centralizada | Repositorio único con control de versiones e historial de cambios |
| Reutilización | Reaprovechamiento de casos existentes; menos duplicación |
| Reportes avanzados | Métricas, tableros y reportes ejecutivos para decisiones basadas en evidencia |
| Trazabilidad completa | Vínculo entre pruebas, requisitos, defectos y resultados de ejecución |
| Automatización integrada | Conexión con frameworks de automatización y reporte de resultados en tiempo real |
| Colaboración | Comentarios, notificaciones y asignación de tareas |

**Herramientas destacadas:** TestRail, Jira + Zephyr, Azure Test Plans, qTest, TestLink y PractiTest.

### 6.14 Errores comunes en el diseño de casos

| Error | Consecuencia | Solución |
|---|---|---|
| Ambigüedad en la descripción | Resultados vagos como "el sistema funciona correctamente" impiden una verificación objetiva | Lenguaje específico, medible y verificable |
| Cobertura insuficiente | Sin casos extremos, de error o negativos, quedan vulnerabilidades sin detectar | Aplicar varias técnicas y pensar en modos de falla |
| Redundancia excesiva | Varios casos que validan lo mismo desperdician recursos | Revisar y consolidar duplicados |
| Dependencias no documentadas | Precondiciones o datos implícitos generan fallas impredecibles | Especificar todas las precondiciones |
| Falta de mantenimiento | Los casos se desincronizan de los requisitos | Revisión con cada cambio |
| Casos demasiado complejos | Validar varias funciones en un caso dificulta encontrar la causa raíz | Casos atómicos y enfocados |

### 6.15 Buenas prácticas y principios

**Buenas prácticas:** claridad y precisión (cada paso reproducible por cualquier miembro del equipo); selección inteligente de la técnica según complejidad, criticidad, recursos y plazos; combinación estratégica de técnicas; mantenimiento continuo ante cada cambio de requisitos.

**Principios para el éxito:**

1. Priorizar la calidad sobre la cantidad de casos.
2. Mantener la trazabilidad entre requisitos y casos.
3. Documentar explícitamente las suposiciones y limitaciones.
4. Fomentar la revisión por pares para detectar omisiones.
5. Usar herramientas apropiadas para la gestión y la automatización.
6. Medir y mejorar continuamente la efectividad de las pruebas.

### 6.16 Conclusiones del tema

Los casos diseñados con técnicas formales marcan la diferencia entre probar un software y garantizar su calidad: son la primera línea de defensa contra fallas que afectan a los usuarios, la reputación y los costos. El tema resume ese valor con tres cifras de referencia: corregir un defecto en etapas tempranas cuesta hasta diez veces menos que corregirlo en producción; las técnicas avanzadas pueden reducir el tiempo de prueba hasta en 40 %; y los sistemas con casos bien diseñados alcanzan niveles de confiabilidad superiores al 95 %. Al igual que en el Capítulo 2, son valores orientativos sin un estudio identificado como fuente. La invitación final del tema es aplicar tablas de decisión, análisis de flujo de datos y caminos básicos en el proyecto propio.

### 6.17 Relación con estándares

| Estándar | Relación |
|---|---|
| IEEE 610.12 / ISO/IEC/IEEE 24765 | Definición de caso de prueba y vocabulario |
| ISO/IEC/IEEE 29119-4:2021 | Técnicas de diseño de pruebas: partición, valores límite, tablas de decisión, cobertura de sentencias y decisiones, entre otras |
| ISO/IEC/IEEE 29119-3:2021 (antes IEEE 829) | Documentación de la especificación de casos |
| ISTQB CTFL v4.0, capítulo 4 | Técnicas de caja negra, caja blanca y basadas en la experiencia |
| McCabe (1976) | Complejidad ciclomática |

### 6.18 Preguntas de repaso

1. Defina caso de prueba según IEEE 610 y diferencie caso de escenario.
2. Para un campo de edad válido entre 18 y 65 años, identifique las clases de equivalencia y los valores límite de tres valores.
3. Construya la tabla de decisión de un descuento que se aplica si el cliente es socio y la compra supera $50.000.
4. Calcule V(G) para un grafo con 11 aristas y 9 nodos, e indique su interpretación.
5. Explique por qué el 100 % de cobertura de sentencias no garantiza el 100 % de cobertura de decisiones.
6. Diseñe los casos de bucle para una función que permite un máximo de tres reintentos.
7. Identifique la anomalía de flujo de datos en: `rol = obtenerRol(); rol = "admin"; autorizar(rol);`.
8. Indique por qué las clases inválidas se prueban de a una por caso.

---

## Capítulo 7. Aplicación: creación de casos de prueba con técnicas específicas (actividad 2.2.2)

**Indicador de logro:** IL2.2. **Modalidad:** individual, 45 minutos. **Objetivo:** diseñar casos de prueba efectivos que garanticen la calidad funcional y no funcional de un producto de software.

### 7.1 Escenario y caso de prueba

Un **escenario** es el *qué*, una descripción de alto nivel; un **caso de prueba** es el *cómo*, los pasos detallados.

| Nivel | Ejemplo |
|---|---|
| Escenario | Validar el proceso de recuperación de contraseña de un usuario |
| Caso 1 | Recuperación exitosa con correo válido |
| Caso 2 | Intento de recuperación con correo no registrado |
| Caso 3 | Validación de la expiración del enlace de recuperación (seguridad) |

### 7.2 Plantilla estándar del caso de prueba

| Campo | Descripción |
|---|---|
| ID del caso | Código único, por ejemplo CP-SEG-001 |
| Prioridad | Alta, media o baja, según el riesgo |
| Precondiciones | Estado inicial necesario, por ejemplo "el servidor debe estar en línea" |
| Pasos de ejecución | Lista numerada de acciones atómicas |
| Datos de prueba | Valores exactos utilizados, por ejemplo Usuario_test@mail.com |
| Resultado esperado | Comportamiento correcto del sistema |
| Resultado obtenido | Lo que realmente ocurrió; se completa al ejecutar |
| Estado | Aprobado, Falla o Bloqueado |

El encargo EP3 agrega tres campos que deben incorporarse en el caso semestral: **requisito del ERS** asociado, **criterio de aceptación** y **tipo de prueba**. La plantilla completa recomendada es la siguiente:

| Campo | Ejemplo |
|---|---|
| ID | CP-SEG-001 |
| Título | Rechazo de inyección SQL en el inicio de sesión |
| Requisito del ERS | Código del requisito de seguridad de autenticación |
| Tipo / nivel / técnica | Seguridad / sistema / partición de equivalencia (entrada maliciosa) |
| Prioridad | Alta (riesgo crítico) |
| Precondiciones | Entorno Docker levantado; usuario de prueba registrado |
| Pasos | 1. Abrir la pantalla de acceso. 2. Ingresar `' OR '1'='1' --` en el correo y cualquier valor en la contraseña. 3. Presionar "Ingresar". 4. Revisar la respuesta y los registros |
| Datos | `' OR '1'='1' --` / `x` |
| Resultado esperado | Acceso denegado con mensaje genérico; sin detalle técnico en la respuesta; intento registrado |
| Criterio de aceptación | Se cumplen las tres condiciones del resultado esperado |
| Resultado obtenido | Se completa en la ejecución |
| Estado | Aprobado / Falla / Bloqueado |
| Evidencia | Captura de pantalla y de la respuesta HTTP, con fecha y hora |
| Defecto asociado | BUG-xxx, si corresponde |

### 7.3 Matriz de pruebas en tres categorías

| Categoría | Pregunta | Escenario | Técnica o caso sugerido |
|---|---|---|---|
| **A. Calidad funcional** | ¿El software hace lo que el usuario pidió? | Registro de nuevos clientes | Valores límite: nombres de 1 y de 100 caracteres |
| **B. Seguridad** | ¿Es el sistema resistente a ataques comunes? | Elusión de la autenticación | Inyección SQL en el inicio de sesión; acceso a una URL interna sin sesión iniciada |
| **C. Usabilidad y calidad de interfaz** | ¿Es el software intuitivo y accesible? | Navegación en dispositivos móviles | Todos los botones deben poder pulsarse en una pantalla de 5 pulgadas |

**Desarrollo de la categoría A con valores límite** (nombre entre 2 y 100 caracteres, como supuesto de ejemplo):

| ID | Longitud | Resultado esperado |
|---|---|---|
| CP-FUN-001 | 1 | Rechazo con mensaje de longitud mínima |
| CP-FUN-002 | 2 | Aceptado |
| CP-FUN-003 | 100 | Aceptado |
| CP-FUN-004 | 101 | Rechazo con mensaje de longitud máxima |

### 7.4 Matriz de trazabilidad

**Definición.** La **matriz de trazabilidad de requisitos** es la tabla que vincula cada requisito con los casos de prueba que lo verifican y, en la ejecución, con sus resultados y defectos. Demuestra que ningún requisito quedó sin probar y permite analizar el impacto de un cambio.

| Requisito | Descripción | Casos | Resultado | Defecto | Estado del requisito |
|---|---|---|---|---|---|
| RF-1.1 | Inicio de sesión con correo y contraseña | CP-FUN-010, CP-SEG-001, CP-SEG-002 | 2 aprobados, 1 falla | BUG-003 | No cumple |
| NFR-PERF-1 | Respuesta de consulta < 2 s con 100 usuarios | CP-REN-001 | Aprobado | — | Cumple |
| RB-1 | Un paciente solo ve sus propios datos | CP-SEG-005 | Falla | BUG-001 | No cumple |

Los códigos siguen la nomenclatura del ERS del caso (RF, NFR y RB); las descripciones y los resultados de la tabla son ilustrativos.

Cobertura = requisitos con al menos un caso / requisitos totales × 100. EP3 exige **100 %**, incluidos los requisitos de necesidades, normativos, legales y de seguridad.

**Trazabilidad hacia adelante y hacia atrás.** Hacia adelante, desde el requisito al caso, comprueba la cobertura. Hacia atrás, desde el caso al requisito, comprueba que todo caso responde a una necesidad y evita casos sin propósito.

### 7.5 Reporte de defecto

Cuando se detecta un error en el caso semestral, se documenta su reporte de defecto con severidad y pasos de reproducción; con ello se demuestra un ciclo de calidad completo (diseño → ejecución → defecto → seguimiento). La estructura del reporte se desarrolla en el Capítulo 9.

### 7.6 Errores frecuentes

1. Redactar escenarios como si fueran casos, sin pasos ni datos concretos.
2. Escribir resultados esperados no verificables.
3. Omitir el requisito del ERS asociado, lo que rompe la trazabilidad.
4. Mezclar varias verificaciones en un caso.
5. No incluir casos negativos ni de seguridad para requisitos críticos.

### 7.7 Preguntas de repaso

1. Diferencie escenario de caso de prueba con un ejemplo propio.
2. Enumere los ocho campos de la plantilla y los tres que agrega EP3.
3. Diseñe un caso de seguridad para el acceso a una URL interna sin sesión.
4. Explique qué significa una cobertura de requisitos del 100 % y cómo se demuestra.
5. Explique la diferencia entre trazabilidad hacia adelante y hacia atrás.

---

## Capítulo 8. Pruebas estáticas de código, obtención de evidencias y registro de resultados (tema 2.3.1)

**Indicador de logro:** IL2.3. **Propósito del capítulo:** comprender el análisis del código sin ejecutarlo, aplicar técnicas de revisión manual y automatizada, ejecutar SonarQube en laboratorio y registrar evidencias trazables.

### 8.1 Problema de partida: el centinela silencioso

El tema plantea la pregunta: ¿y si fuera posible detener una falla antes de que ocurra? Las pruebas estáticas cumplen la función de un centinela silencioso, porque analizan el código fuente de forma exhaustiva sin ejecutarlo. El tema afirma que detectar un error en esta etapa puede ser hasta cien veces más económico que hacerlo en producción. Este multiplicador, al igual que otros de la unidad (10 veces en los temas 2.1.2 y 2.2.1), expresa la idea de que el costo de corrección crece con la etapa en que se detecta el defecto; el factor exacto varía según la fuente y el contexto y no debe presentarse como una cifra medida.

### 8.2 Definición y beneficios

**Definición.** Una **prueba estática** es el análisis del código fuente, del diseño o de la documentación **sin ejecutar el programa**. Es un enfoque preventivo que identifica errores potenciales, vulnerabilidades y malas prácticas antes de que se conviertan en fallas durante la ejecución.

**Beneficios:**

- detección de defectos en etapas tempranas, cuando su corrección es más eficiente y menos costosa;
- reducción de los costos de depuración y mantenimiento;
- optimización del ciclo de desarrollo, al prevenir problemas en fases posteriores;
- mejora de la legibilidad, la mantenibilidad y la calidad estructural del código.

### 8.3 Pruebas estáticas y pruebas dinámicas

| Aspecto | Pruebas estáticas | Pruebas dinámicas |
|---|---|---|
| Definición | Análisis de código, diseño y documentación sin ejecutar el programa | Ejecución del software en tiempo real para detectar fallas durante su funcionamiento |
| ¿Ejecutan el sistema? | No | Sí |
| Detectan | Defectos (causas), con ubicación exacta | Fallas (efectos) y su comportamiento observable |
| Momento | Desde los requisitos y el diseño | Con el software construido y desplegado |
| Técnicas | Revisión, *walkthrough*, inspección, análisis automatizado (SAST) | Funcionales, integración, carga, DAST, usabilidad |
| Herramientas del curso | SonarQube | Selenium, ZAP, Burp Suite, Nikto, SQLMap, JMeter |

Ambas metodologías son **complementarias**. El análisis estático señala dónde puede existir un problema; la prueba dinámica confirma si se manifiesta o si puede explotarse.

### 8.4 Técnicas de pruebas estáticas

| Técnica | Descripción | Formalidad | Roles |
|---|---|---|---|
| **Revisión manual** | Análisis detallado del código fuente y de la documentación técnica por parte de expertos | Baja a media | Revisor |
| **Inspección en equipo / walkthrough** | Revisión colaborativa del código y del diseño | *Walkthrough*: media; inspección: alta | *Walkthrough*: el autor guía la revisión. Inspección: moderador, autor, lector, registrador y revisores, con lista de verificación y métricas |
| **Análisis automatizado** | Uso de herramientas especializadas para detectar patrones de error y vulnerabilidades | Automática | Herramienta y analista que interpreta |

**Proceso de una inspección formal:** planificación (alcance, roles, lista de verificación) → preparación individual → reunión de inspección y registro de defectos → corrección por el autor → seguimiento y verificación → cierre con métricas.

**Lo que solo encuentra la revisión manual.** Las herramientas automáticas detectan patrones; no comprenden la intención del negocio. Una revisión manual de las rutas de una API puede encontrar, por ejemplo, un servicio que exige un token pero no verifica el rol; un recurso que se entrega sin comprobar que pertenece al usuario que lo solicita; o una eliminación física de datos que deberían conservarse. Esta capacidad corresponde a la redacción del IL2.2 del Programa de Asignatura.

**Lista de verificación para la revisión manual de una API**

| # | Pregunta |
|---|---|
| 1 | ¿Cada ruta protegida exige autenticación? |
| 2 | ¿Cada ruta verifica el rol autorizado? |
| 3 | ¿Se comprueba que el recurso solicitado pertenece al usuario o que este tiene derecho a verlo? |
| 4 | ¿Las consultas a la base de datos son parametrizadas? |
| 5 | ¿Las contraseñas se almacenan con una función de hash robusta y sal? |
| 6 | ¿Los mensajes de error enviados al cliente son genéricos? |
| 7 | ¿Los secretos (claves JWT, credenciales de base de datos) están fuera del código? |
| 8 | ¿Se registran los accesos y las operaciones sobre datos sensibles? |
| 9 | ¿Las entradas se validan en el servidor y no solo en el cliente? |
| 10 | ¿Los tokens tienen expiración y pueden revocarse? |

### 8.5 Obtención de evidencias manuales

**Definición.** Una **evidencia** es un registro objetivo que demuestra un hecho observado durante la prueba o la revisión: captura, registro de eventos, extracto de código con archivo y línea, reporte exportado o consulta a la base de datos.

**Pasos:**

1. **Documentar hallazgos:** registrar en detalle cada descubrimiento de las revisiones de código y de diseño.
2. **Registrar defectos:** capturar errores, defectos y recomendaciones con el detalle suficiente para resolverlos.
3. **Estandarizar formatos:** utilizar plantillas normalizadas, como las de IEEE 829, para asegurar consistencia y trazabilidad.

**Registro de un hallazgo estático**

| Campo | Ejemplo |
|---|---|
| ID | EST-001 |
| Archivo y línea | `BACKEND/src/routes/ejemplo.js`, línea 42 (ilustrativo) |
| Descripción | La respuesta de error devuelve el mensaje interno de la excepción |
| Regla o criterio | Manejo seguro de errores; OWASP A10:2025 |
| Gravedad | Moderada / Grave según el dato expuesto |
| Evidencia | Extracto del código y captura de la respuesta |
| Recomendación | Devolver un mensaje genérico y registrar el detalle solo en el servidor |
| Responsable | Equipo de *backend* |
| Estado | Abierto |

### 8.6 Registro de resultados: importancia y buenas prácticas

| Práctica | Aporte |
|---|---|
| Evidencias claras | Facilitan el seguimiento sistemático y la corrección oportuna de los defectos |
| Plantillas estandarizadas | Formatos para el plan de pruebas, los casos de prueba y los resúmenes ejecutivos |
| Informes estructurados | Incluyen la descripción del defecto, su ubicación exacta en el código y el nivel de gravedad |

**Herramientas de apoyo al registro manual**

| Tipo | Ejemplos | Uso |
|---|---|---|
| Sistemas de gestión de incidencias | Jira, Redmine | Rastrear y gestionar los defectos de forma centralizada |
| Documentos colaborativos | Hojas de cálculo estructuradas y documentos compartidos | Trabajo en equipo |
| Integración con análisis automático | Conexión con herramientas como SonarQube | Trazabilidad completa del proceso |

### 8.7 SonarQube

**Definición.** SonarQube es una plataforma de análisis estático de código que detecta automáticamente vulnerabilidades de seguridad, errores (*bugs*) y problemas de mantenibilidad (*code smells*).

**Características:**

- soporta más de 25 lenguajes de programación;
- se integra en pipelines CI/CD;
- proporciona métricas detalladas de calidad;
- permite definir **Quality Gates** personalizados.

**Conceptos de SonarQube**

| Concepto | Definición |
|---|---|
| **Issue (problema)** | Incumplimiento de una regla detectado en el código |
| **Regla** | Patrón de código que la herramienta verifica |
| **Quality Profile** | Conjunto de reglas activas para un lenguaje |
| **Quality Gate** | Conjunto de condiciones que el proyecto debe cumplir para aprobarse |
| **Código nuevo (*New Code*)** | Código agregado o modificado desde una referencia (versión anterior o período definido) |
| **Código general (*Overall Code*)** | Todo el código del proyecto |
| **SonarScanner** | Programa que analiza el código y envía los resultados al servidor |
| **Token de análisis** | Credencial que autoriza al escáner a publicar resultados en un proyecto |

### 8.8 Preparación del entorno de laboratorio

1. **Instalación y configuración:** despliegue de SonarQube Server (en el curso, como contenedor Docker) y configuración de los parámetros básicos.
2. **Importación del proyecto:** creación del proyecto y carga del código fuente que será analizado.
3. **Definición de reglas:** establecimiento de los estándares de calidad (Quality Profile) y del Quality Gate que se aplicarán.

### 8.9 Ejecución del análisis

| Etapa | Descripción |
|---|---|
| Escaneo automático | Análisis del código fuente completo del proyecto |
| Visualización de resultados | Panel (*dashboard*) con métricas y gráficos de calidad |
| Identificación de defectos | Detección de áreas críticas que requieren mejora |

El escaneo puede tardar desde minutos hasta horas, según el tamaño del proyecto y la complejidad del código.

**Ejemplo de ejecución del escáner** (los valores entre corchetes se reemplazan):

```bash
sonar-scanner \
  -Dsonar.projectKey=cuidarteplus-backend \
  -Dsonar.sources=BACKEND/src \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.token=[token de análisis]
```

### 8.10 Lectura del panel de SonarQube

| Métrica | Qué mide | Interpretación |
|---|---|---|
| **Bugs / Confiabilidad** | Código que probablemente produce un comportamiento incorrecto | Calificación de A (sin problemas) a E |
| **Vulnerabilidades / Seguridad** | Código que puede explotarse | Toda vulnerabilidad de severidad alta se registra como incidente |
| **Security Hotspots** | Código sensible a la seguridad que **requiere revisión humana**; no es necesariamente una vulnerabilidad | Se revisa y se marca como seguro o como problema; el porcentaje revisado es una condición del Quality Gate |
| **Code Smells / Mantenibilidad** | Código difícil de mantener: duplicado, complejo o mal estructurado | Afecta la mantenibilidad; rara vez es crítico por sí solo |
| **Deuda técnica** | Tiempo estimado para corregir los problemas de mantenibilidad | Se compara con el tamaño del proyecto |
| **Cobertura** | Porcentaje de código ejercitado por pruebas automatizadas | Un 0 % indica ausencia de pruebas unitarias, lo que constituye un hallazgo |
| **Duplicaciones** | Porcentaje de líneas duplicadas | Aumenta el costo de corregir defectos |
| **Complejidad** | Complejidad ciclomática y cognitiva | Se conecta con V(G) del Capítulo 6 |

**Severidades.** Según el modo configurado, SonarQube muestra la clasificación estándar (*Bug*, *Vulnerability*, *Code Smell*, con severidades *Blocker*, *Critical*, *Major*, *Minor* e *Info*) o el modo MQR, por cualidades del software (Seguridad, Confiabilidad y Mantenibilidad, con severidades *Blocker*, *High*, *Medium*, *Low* e *Info*). El informe debe declarar el modo utilizado.

**Quality Gate predeterminado "Sonar way".** Se aplica al código nuevo y exige:

- ningún problema nuevo;
- 100 % de los Security Hotspots nuevos revisados;
- cobertura del código nuevo de al menos 80 %;
- duplicación en el código nuevo de 3 % como máximo.

**Matiz de interpretación.** En un proyecto heredado que se analiza por primera vez, casi todo el código es "código general" y no "código nuevo". Por ello, el Quality Gate puede aparecer aprobado aunque existan muchos problemas. El informe debe leer la pestaña de **código general** y explicar esa diferencia. Un Quality Gate aprobado no equivale a un código seguro.

### 8.11 Obtención y registro manual de evidencias en SonarQube

1. Exportar reportes detallados de todos los hallazgos.
2. Complementar con anotaciones manuales de contexto.
3. Agregar comentarios específicos sobre cada defecto.
4. Documentar las acciones correctivas propuestas.
5. Asignar responsables para cada corrección.

**Falsos positivos.** Un hallazgo que la herramienta informa, pero que no constituye un problema real en el contexto. Se marca justificadamente y se documenta el criterio. Lo contrario, un **falso negativo**, es un defecto real que la herramienta no detecta; para reducirlos se complementa con revisión manual.

### 8.12 Ejemplo de análisis con SonarQube

En un proyecto Java analizado se obtuvieron **15 bugs** (errores funcionales que requieren corrección inmediata), **30 code smells** (problemas de mantenibilidad) y **5 vulnerabilidades** (problemas de seguridad que comprometen la integridad del sistema). La práctica recomendada fue registrar manualmente los defectos críticos para priorizarlos y darles seguimiento en las siguientes iteraciones.

**Lectura recomendada de un resultado como este:** primero las vulnerabilidades (riesgo para los datos), luego los bugs de severidad alta (riesgo funcional) y al final los code smells, salvo que se concentren en un módulo crítico, lo que eleva su prioridad.

### 8.13 Del reporte de SonarQube al análisis normativo

La rúbrica de EP4 (IE6) exige comunicar los resultados del análisis estático **comparándolos con criterios legales y normativos**. Insertar capturas del panel no cumple el criterio. La cadena de razonamiento esperada es:

```
Problema de SonarQube → Categoría OWASP Top 10:2025 → Requisito del ERS
      → Norma o deber legal afectado → Severidad → Recomendación
```

| Problema típico | OWASP Top 10:2025 | Lectura normativa |
|---|---|---|
| Credenciales o secretos en el código | A04 Fallas criptográficas / A02 Configuración incorrecta | Deber de cuidado de los datos (Ley 19.628, art. 11); deber de seguridad del art. 14 quinquies incorporado por la Ley 21.719 (rige desde el 01-12-2026) |
| Contraseñas sin hash robusto | A04 / A07 Fallas de autenticación | Mismo deber de seguridad; incumplimiento del requisito de seguridad del ERS |
| Consultas SQL concatenando texto | A05 Inyección | Riesgo de acceso indebido a datos personales; el acceso ilícito es delito (Ley 21.459, art. 2) |
| CORS permisivo o cabeceras ausentes | A02 Configuración incorrecta | Barreras de acceso insuficientes |
| Errores internos devueltos al cliente | A10 Manejo indebido de condiciones excepcionales | Exposición de información técnica |
| Dependencias con vulnerabilidades conocidas | A03 Fallas en la cadena de suministro | Seguridad del sistema; uso de componentes de terceros (licencias, Ley 17.336) |
| Ausencia de registro de eventos de seguridad | A09 Fallas de registro y alerta | Sin registros no es posible detectar ni reportar incidentes (Ley 21.663, art. 9) |

### 8.14 Beneficios, retos y recomendaciones

| Beneficios | Retos | Recomendaciones |
|---|---|---|
| **Detección temprana:** reduce de forma exponencial los costos de corrección | **Disciplina y formación:** inversión en capacitación y compromiso organizacional sostenido | **Enfoque híbrido:** análisis automático más revisiones manuales profundas |
| **Mejora continua:** incremento sostenido de la calidad mediante análisis recurrente | **Resistencia cultural:** oposición inicial a las revisiones por percepción de carga adicional | **Capacitación continua** en técnicas y herramientas |
| **Cumplimiento normativo:** facilita la adhesión a estándares y los procesos de auditoría | **Integración efectiva:** coordinar herramientas automáticas con procesos manuales | **Procesos claros** de documentación, seguimiento y cierre de defectos |
| | Falsos positivos que consumen tiempo | **Automatización inteligente:** análisis estático en el pipeline CI/CD para retroalimentación inmediata |

### 8.15 Integración en el ciclo de desarrollo

La integración de las pruebas estáticas en el ciclo de vida del desarrollo (SDLC) se traduce en dos prácticas: ejecutar el análisis en cada integración del pipeline CI/CD, con el Quality Gate como condición para continuar, y combinarlo con revisiones manuales en los puntos de mayor riesgo (por ejemplo, antes de integrar cambios en autenticación o autorización). Así, el análisis estático deja de ser una actividad puntual y se convierte en un control permanente, coherente con el enfoque *shift-left* del Capítulo 2.

### 8.16 Conclusiones del tema

- Las pruebas estáticas son esenciales para garantizar la calidad desde las primeras etapas.
- La obtención manual de evidencias complementa el análisis automático y le aporta contexto.
- SonarQube facilita la ejecución y el registro sistemático de las pruebas en laboratorio.
- Estas prácticas mejoran la confiabilidad, la mantenibilidad y la seguridad del software.

### 8.17 Errores frecuentes

1. Presentar el panel de SonarQube sin interpretación ni vínculo normativo.
2. Concluir que el código es seguro porque el Quality Gate aparece aprobado.
3. Confundir un Security Hotspot con una vulnerabilidad confirmada.
4. No registrar archivo y línea de cada hallazgo.
5. No revisar los falsos positivos ni justificar su descarte.
6. Analizar solo el *backend* y omitir el *frontend*.

### 8.18 Relación con estándares

| Estándar | Relación |
|---|---|
| IEEE 829 / ISO/IEC/IEEE 29119-3 | Plantillas de registro de evidencias e informes |
| ISO/IEC 25010:2023 | Mantenibilidad, fiabilidad y seguridad como características evaluadas por SonarQube |
| OWASP Top 10:2025 | Clasificación de las vulnerabilidades detectadas |
| ISTQB CTFL v4.0, capítulo 3 | Pruebas estáticas, revisiones y sus tipos |

### 8.19 Preguntas de repaso

1. Defina prueba estática y enumere cuatro beneficios.
2. Compare pruebas estáticas y dinámicas en cuatro aspectos.
3. Diferencie revisión manual, *walkthrough* e inspección según formalidad y roles.
4. Explique la diferencia entre una vulnerabilidad y un Security Hotspot.
5. Explique por qué un Quality Gate aprobado no garantiza un código seguro en un proyecto heredado.
6. Enumere los cinco pasos de la documentación manual de evidencias en SonarQube.
7. Relacione un problema de SonarQube con una categoría OWASP, un requisito y una norma.

---

## Capítulo 9. Ejecución de pruebas en un entorno de laboratorio (actividad 2.3.2)

**Indicador de logro:** IL2.4 (el encabezado de la actividad indica IL2.3). **Modalidad:** individual, 45 minutos. **Propósito:** ejecutar los casos diseñados de forma controlada, registrar evidencias y gestionar los defectos encontrados.

### 9.1 Preparación del entorno

Antes de ejecutar se asegura la estabilidad del entorno y se documenta:

| Aspecto | Contenido del registro |
|---|---|
| Hardware y software | Versión del navegador, sistema operativo y base de datos; versión de Docker |
| Datos de prueba | Confirmación de que se cargaron los scripts de base de datos; usuarios de prueba; uso de datos sintéticos, nunca reales |
| Herramientas de soporte | Capturador de pantalla y acceso a los registros de eventos listos |
| Versión del software | Identificación de la versión, *commit* o fecha del código probado |

### 9.2 Ciclos de ejecución

**Definición.** Un **ciclo** (o pasada) de ejecución es una ronda completa de ejecución de un conjunto de casos sobre una versión determinada del software.

| Ciclo | Objetivo | Regla |
|---|---|---|
| **Ciclo 1: prueba de humo (*smoke test*)** | Verificar que las funciones básicas operan (inicio de sesión, carga de la página principal) | Si falla, la ejecución se detiene y el resto de los casos queda **bloqueado**, porque no es posible probar el sistema |
| **Ciclo 2: ejecución de casos** | Ejecutar los pasos exactos del diseño, contrastar el resultado obtenido con el esperado y registrar evidencia de resultados exitosos y fallidos | Se respeta el orden de prioridad por riesgo |
| **Ciclo de reprueba y regresión** | Confirmar las correcciones (*re-test*) y verificar que no se afectaron otras funciones (regresión) | Se ejecuta después de cada corrección |

### 9.3 Estados de un caso de prueba

| Estado | Significado |
|---|---|
| **Aprobado** (*Pass*) | El resultado obtenido coincide con el esperado y cumple el criterio de aceptación |
| **Falla** (*Fail*) | El resultado obtenido no coincide; se abre un reporte de defecto |
| **Bloqueado** (*Blocked*) | No pudo ejecutarse porque otro defecto o el entorno lo impiden |
| **No ejecutado** | Diseñado pero no ejecutado; debe justificarse en el informe (el formato EP3 lo solicita como "sin ejecutar") |

### 9.4 Reporte de defecto

**Definición.** El **reporte de defecto** (*bug report*) es el documento que describe una desviación entre el resultado esperado y el obtenido, con la información necesaria para reproducirla, clasificarla y corregirla.

| Campo | Contenido | Ejemplo |
|---|---|---|
| ID | Identificador único | BUG-001 |
| Título | Síntesis del problema | Contraseñas almacenadas sin función de hash |
| Caso y requisito | Trazabilidad | CP-SEG-002 · requisito de almacenamiento seguro |
| Severidad | Impacto técnico | Crítica |
| Prioridad | Urgencia de corrección | Alta |
| Entorno | Versión, navegador, contenedor | Contenedor *backend*, fecha de levantamiento |
| Pasos para reproducir | Instrucciones exactas para que el desarrollador observe el error | 1. Registrar un usuario. 2. Consultar la tabla de usuarios. |
| Resultado esperado / obtenido | Comparación | Valor con hash / texto plano |
| Evidencia | Captura del error o mensaje del sistema, registro, consulta | Captura con fecha y hora |
| Estado | Ciclo de vida | Abierto |

**Ciclo de vida del defecto:** Nuevo → Asignado → En corrección → Corregido → Reprobado (*re-test*) → Cerrado, o Reabierto si la corrección no funciona. Otros estados posibles: Rechazado (no es defecto), Duplicado, Diferido (se corregirá en una versión posterior).

**Severidad y prioridad**

| Concepto | Mide | Quién la define |
|---|---|---|
| **Severidad** | El impacto técnico del defecto sobre el sistema | Equipo de QA |
| **Prioridad** | La urgencia de corregirlo según el negocio | Negocio o líder del proyecto |

Un error ortográfico en el nombre de la institución en la página principal tiene severidad baja y prioridad alta; una falla en una función que casi no se usa puede tener severidad alta y prioridad media.

### 9.5 Escalas de severidad de la unidad

Los documentos de la unidad emplean tres escalas. Para el informe EP3 se recomienda usar la del formato oficial y explicar la equivalencia.

| Formato EP3 | Actividad 2.3.2 | Actividad 2.4.2 | Descripción (formato EP3) | Impacto | Tratamiento |
|---|---|---|---|---|---|
| **Crítico** | Crítica (bloquea el negocio) | Críticos (fallas de seguridad, caídas) | Impide completamente el funcionamiento del sistema o de una función esencial; bloquea el flujo principal | Muy alto; el sistema no puede usarse | Remediación inmediata |
| **Grave** | Mayor | Mayores (funciones principales que no cumplen el requisito) | Afecta funciones importantes; el sistema funciona parcialmente; existe una alternativa, pero la experiencia se ve comprometida | Alto | Corrección urgente |
| **Moderado** | Menor | Menores (estéticos o de usabilidad) | Afecta funciones secundarias o casos específicos sin detener el flujo principal | Medio; el usuario trabaja con molestias | Próxima iteración |
| **Leve** | Cosmética | (Menores) | Apariencia, estética o texto; no afecta la funcionalidad | Bajo | Según disponibilidad |

**Criterio para fallas de seguridad.** La actividad 2.4.2 clasifica las fallas de seguridad, como la inyección SQL, como críticas. Para justificar la severidad de una falla de seguridad se recomienda responder cuatro preguntas:

1. ¿Expone datos personales o sensibles?
2. ¿Permite acceder o actuar sin autorización?
3. ¿Puede explotarse sin credenciales o con poco esfuerzo?
4. ¿Incumple un requisito legal directo?

Si la respuesta a la primera o a la segunda es afirmativa, y también lo es la tercera, la falla es crítica aunque el sistema siga funcionando.

### 9.6 Bitácora de ejecución

**Definición.** La **bitácora de ejecución** es el registro cronológico de la ejecución de cada caso, con su estado, defecto asociado y observaciones.

| ID caso | Nombre | Estado | Defecto asociado | Observaciones |
|---|---|---|---|---|
| CP-001 | Inicio de sesión con SQL | Aprobado | N/A | El sistema mostró un mensaje de error genérico |
| CP-002 | Registro de usuario | Falla | BUG-002 | El botón "Enviar" no responde en Chrome |
| CP-003 | Compra de producto | Bloqueado | N/A | No pudo probarse por la falla del registro (CP-002) |

El ejemplo muestra la diferencia entre Falla (CP-002, el sistema no se comporta como se espera) y Bloqueado (CP-003, el caso no puede ejecutarse por una falla previa). El formato EP3 agrega dos columnas obligatorias en el detalle de ejecución: **evidencia** y **fecha y persona que ejecuta**.

### 9.7 Informe resumen de pruebas

Al cerrar la ejecución se elabora un breve informe que responde: ¿cuántos casos se ejecutaron?, ¿cuántos se aprobaron? y la recomendación: ¿el software está listo para producción o requiere un nuevo ciclo de corrección?

**Fórmulas**

- Porcentaje de ejecución = ejecutados / diseñados × 100.
- Porcentaje de aprobación = aprobados / ejecutados × 100.
- Cobertura de requisitos = requisitos con caso ejecutado / requisitos del ERS × 100.
- Densidad de defectos por módulo = defectos / módulo, útil para localizar dónde se agrupan (principio 4 de ISTQB).

### 9.8 Errores frecuentes

1. Ejecutar sin registrar el entorno ni la versión probada.
2. Continuar la ejecución cuando el *smoke test* falló.
3. Marcar como Falla un caso que en realidad quedó Bloqueado.
4. Reportar defectos sin pasos de reproducción ni evidencia.
5. Confundir severidad con prioridad.
6. Usar datos personales reales como datos de prueba.

### 9.9 Preguntas de repaso

1. Indique qué se documenta en la preparación del entorno.
2. Explique la regla de detención del *smoke test*.
3. Diferencie Falla de Bloqueado con un ejemplo.
4. Enumere los campos de un reporte de defecto y explique la diferencia entre severidad y prioridad.
5. Establezca la equivalencia entre las tres escalas de severidad de la unidad.
6. Calcule el porcentaje de aprobación si se ejecutaron 40 casos y se aprobaron 34.

---

## Capítulo 10. Elaboración de informes finales de certificación (tema 2.4.1)

**Indicador de logro:** IL2.5. **Propósito del capítulo:** conocer los estándares que orientan los informes de certificación, su estructura, los requisitos de la evidencia y de la redacción, y el control documental que les otorga validez.

### 10.1 Problema de partida: el peso de la firma

El informe de certificación se presenta como el "título de propiedad" de la confianza de una organización. Si un organismo certificador emite un informe impreciso o incompleto, arriesga:

- **reputación:** la calidad del informe afecta directamente la imagen de la entidad ante el mercado;
- **validez legal:** estos documentos son evidencia ante reguladores y partes interesadas;
- **acreditación:** un error técnico puede provocar que el propio organismo pierda su acreditación durante una revisión.

### 10.2 Importancia estratégica del informe

**Definición.** El **informe final de certificación** es el documento oficial que valida el cumplimiento de requisitos normativos. Constituye la culminación del proceso de auditoría o evaluación y sirve como evidencia ante organismos reguladores, clientes y partes interesadas.

| Función del informe | Impacto institucional |
|---|---|
| Valida el cumplimiento de requisitos y documenta el resultado de la evaluación | Fortalece la confianza del mercado y facilita la acreditación cuando es preciso, completo y documentado |
| Demuestra profesionalismo, rigor técnico y transparencia | Puede revisarse en auditorías de acreditación, por lo que debe reflejar excelencia técnica y metodológica |

**Conceptos de evaluación de la conformidad**

| Concepto | Definición |
|---|---|
| Evaluación de la conformidad | Demostración de que se cumplen requisitos especificados de un producto, proceso, sistema, persona u organismo |
| Auditoría | Proceso sistemático, independiente y documentado para obtener evidencia objetiva y evaluarla con el fin de determinar el grado en que se cumplen los criterios |
| Criterios de auditoría | Conjunto de requisitos usado como referencia (norma, ley, requisito del ERS) |
| Certificación | Atestación por una tercera parte de que se cumplen requisitos especificados |
| Acreditación | Reconocimiento formal de la competencia de un organismo de evaluación de la conformidad |
| Auditoría de primera, segunda y tercera parte | Interna; realizada por un cliente o parte interesada; realizada por un organismo independiente, como en la certificación |

### 10.3 Estándares internacionales aplicables

| Estándar | Descripción en el tema | Estado verificado al 19-10-2026 |
|---|---|---|
| **ISO/IEC 17021-1** | Requisitos para organismos que realizan auditorías y certificación de sistemas de gestión | Vigente la edición ISO/IEC 17021-1:2015 (confirmada en 2020) |
| **ISO/IEC 17065** | Evaluación de la conformidad de productos, procesos y servicios | Vigente la edición ISO/IEC 17065:2012; se encuentra en revisión |
| **ISO 19011** | Directrices para la auditoría de sistemas de gestión | La edición 2018 fue retirada el 27-05-2026 y reemplazada por ISO 19011:2026. Desde la edición 2011 se aplica a cualquier sistema de gestión, no solo a los de calidad y ambiente |
| **IAF MD 4** | Documento obligatorio del Foro Internacional de Acreditación (IAF) | Trata del uso de tecnologías de información y comunicación (TIC) con fines de auditoría y evaluación de la conformidad. La edición 3 (fechada el 30-01-2025) es de aplicación desde el 30-01-2026 |

Estos estándares establecen requisitos mínimos de estructura, contenido y formato para que un informe de certificación sea reconocido internacionalmente. En el contexto de la asignatura, un informe de pruebas elaborado por estudiantes no constituye una certificación ISO; utiliza la lógica de esos estándares para emitir un **dictamen técnico** fundamentado.

### 10.4 Estructura fundamental del informe

| # | Sección | Contenido |
|---|---|---|
| 01 | **Identificación y portada** | Datos del organismo, del cliente, alcance y fecha de emisión |
| 02 | **Resumen ejecutivo** | Síntesis de los hallazgos principales y decisión de certificación |
| 03 | **Metodología aplicada** | Proceso de auditoría y criterios utilizados |
| 04 | **Hallazgos detallados** | Conformidades, no conformidades y oportunidades de mejora |
| 05 | **Conclusiones y recomendaciones** | Decisión fundamentada sobre la certificación y pasos siguientes |
| 06 | **Anexos y evidencias** | Documentación de soporte y registros de auditoría |

### 10.5 Sección de identificación

Datos esenciales:

1. nombre y logotipo del organismo certificador;
2. número de acreditación vigente;
3. identificación completa del cliente (razón social, RUT y contacto);
4. ubicación de las instalaciones auditadas;
5. alcance de la certificación solicitada (procesos, servicios o productos evaluados);
6. norma o estándar aplicable (por ejemplo, ISO/IEC 27001 o NCh-ISO 9001);
7. fecha de auditoría y fecha de emisión del informe;
8. código único de identificación del informe.

**Equivalencia en un informe de pruebas de software:** equipo de QA (en lugar del organismo), sistema y versión evaluados, entorno y fechas de ejecución, ERS y normas aplicadas como criterios, y código del informe.

### 10.6 Resumen ejecutivo

| Aspecto | Contenido |
|---|---|
| Propósito | Proporcionar a los lectores ejecutivos una visión rápida y completa del resultado, que permita comprender la decisión sin leer el informe completo |
| Elementos | Tipo de auditoría, fechas, equipo, principales hallazgos positivos, no conformidades críticas y decisión final con su justificación técnica |
| Extensión | Entre 1 y 2 páginas, con lenguaje claro, directo y profesional, sin tecnicismos excesivos |

### 10.7 Metodología

**Fases:**

1. **Planificación:** revisión documental previa, plan de auditoría y asignación de recursos.
2. **Ejecución:** entrevistas, observación directa, revisión de registros y verificación de procesos.
3. **Análisis:** evaluación de evidencias, clasificación de hallazgos y validación de la conformidad.
4. **Reporte:** documentación formal de resultados y emisión de conclusiones.

**Transparencia metodológica.** La sección debe demostrar que la evaluación siguió procedimientos sistemáticos, objetivos y reproducibles, y detallar el **enfoque basado en riesgos**, las **técnicas de muestreo** y los **criterios de evaluación** aplicados.

| Fase de auditoría | Equivalente en pruebas de software |
|---|---|
| Planificación | Plan de pruebas, análisis de riesgos, diseño de casos |
| Ejecución | Ciclos de ejecución, análisis estático, pruebas de seguridad |
| Análisis | Clasificación de incidentes por severidad; vínculo con normas |
| Reporte | Informe final con dictamen |

### 10.8 Clasificación de hallazgos

| Hallazgo | Definición |
|---|---|
| **Conformidad** | Evidencia de cumplimiento de los requisitos; se documenta para demostrar las fortalezas del sistema |
| **Observación (oportunidad de mejora)** | Situación que no constituye incumplimiento, pero que puede mejorarse o derivar en uno |
| **No conformidad menor** | Desviación que no compromete la efectividad global del sistema |
| **No conformidad mayor** | Incumplimiento que afecta la capacidad del sistema para lograr sus resultados |

**Relación con la severidad de los defectos.** En un informe de software, un defecto crítico abierto se asimila a una no conformidad mayor; un defecto grave o moderado puede corresponder a una no conformidad menor según su impacto; y una mejora de usabilidad sin incumplimiento corresponde a una observación.

### 10.9 Documentación de no conformidades

1. **Descripción clara:** indicar qué requisito se incumple y en qué consiste la desviación observada.
2. **Evidencia objetiva:** referencias a documentos revisados, entrevistas y observaciones, con fechas y ubicaciones.
3. **Referencia normativa:** citar la cláusula o requisito específico, con número de sección y texto pertinente.
4. **Clasificación:** justificar técnicamente si la desviación es mayor o menor según su impacto.

**Ejemplo de no conformidad mayor en software**

| Parte | Redacción |
|---|---|
| Descripción | El sistema almacena las contraseñas de los usuarios sin aplicar una función de hash, en contra del requisito de seguridad de almacenamiento de credenciales del ERS |
| Evidencia | Consulta a la tabla de usuarios del 19-10-2026, 10:40 (UTC-3), anexo C-03; caso CP-SEG-002 con resultado Falla |
| Referencia | Requisito de seguridad del ERS; OWASP Top 10:2025 A04; Ley 19.628, art. 11 (deber de cuidado de los datos) |
| Clasificación | Mayor: expone credenciales de todos los usuarios ante cualquier acceso a la base de datos y compromete el objetivo de protección de datos del sistema |

### 10.10 Requisitos de la evidencia objetiva

| Requisito | Definición |
|---|---|
| **Verificabilidad** | Toda afirmación se respalda con evidencias que terceros pueden verificar de forma independiente, incluidos los organismos de acreditación |
| **Trazabilidad** | Registros que permiten reconstruir el proceso; evidencias numeradas, fechadas y referenciadas en el cuerpo del informe |
| **Suficiencia** | Cantidad y calidad de evidencias proporcionales a la complejidad del alcance y al nivel de riesgo de cada área |

### 10.11 Redacción técnica y profesional

| Características del lenguaje | Errores que deben evitarse |
|---|---|
| **Objetividad:** hechos verificables, sin opiniones personales | Lenguaje ambiguo o impreciso |
| **Precisión:** términos técnicos correctos según la norma aplicable | Conclusiones sin evidencia de soporte |
| **Claridad:** estructura de párrafos lógica y coherente | Descripciones vagas de las no conformidades |
| **Neutralidad:** tono profesional sin juicios de valor | Inconsistencias entre secciones |
| **Consistencia:** terminología uniforme | Falta de referencias normativas específicas |
| | Redacción en primera persona |

| Redacción inadecuada | Redacción adecuada |
|---|---|
| "Creemos que el login es inseguro." | "El caso CP-SEG-001 evidenció que el servicio de inicio de sesión acepta credenciales vacías (anexo C-01)." |
| "El sistema funciona bastante bien." | "Se aprobaron 34 de 40 casos ejecutados (85 %)." |
| "Hay problemas con los datos." | "Se observó la exposición del mensaje interno de la excepción en la respuesta del servicio `GET /usuarios/{id}`." |

### 10.12 Reflexión: el filtro del auditor

Ante una desviación, omitir la cláusula específica de la norma "para que el cliente lo entienda mejor" es un **error crítico**, no una buena práctica. Todo informe debe citar la cláusula o requisito incumplido, con número de sección y texto pertinente, para garantizar su rigor técnico y su validez. La claridad se obtiene explicando la cláusula, no eliminándola.

### 10.13 Conclusiones y recomendación

1. **Evaluación global:** análisis integral del desempeño del sistema, con fortalezas y áreas de mejora.
2. **Decisión de certificación:** recomendación fundamentada de otorgar, denegar u otorgar con condiciones.
3. **Condiciones y plazos:** acciones correctivas requeridas y plazo para implementarlas antes de emitir el certificado.
4. **Seguimiento:** frecuencia y tipo de auditorías de seguimiento para mantener la certificación.

### 10.14 Anexos y documentación de soporte

| Anexo | Contenido | Equivalente en pruebas de software |
|---|---|---|
| A. Plan de auditoría | Cronograma aprobado, procesos, equipo y criterios | Plan de pruebas |
| B. Lista de asistencia | Participantes en reuniones de apertura y cierre, con firmas | Registro de reuniones del equipo y de validación con el cliente |
| C. Registros de evidencia | Fotografías, documentos revisados, registros muestreados y notas de entrevistas | Capturas, reportes de SonarQube, bitácora, reportes de defectos |
| D. Competencias del equipo | Currículos resumidos, certificados y declaraciones de imparcialidad firmadas | Roles y responsabilidades del equipo de QA |

### 10.15 Control de versiones y trazabilidad documental

**Sistema de codificación.** Todo documento se identifica con un código que incluye:

| Elemento | Descripción |
|---|---|
| Clave única y nombre del titular | Identificador que vincula el documento con su responsable |
| Área de emisión | Unidad que genera el documento |
| Número secuencial | Correlativo dentro del sistema documental |
| Versión | Indicador de control de cambios (V1.0, V2.1) |
| Clasificación | Nivel de acceso: pública, restringida o reservada |

Ejemplo de codificación: `BOCE-2024-0125-V1-INICIAL`. Una codificación equivalente para el caso semestral podría ser `ISY1102-CUIDARTE-INF-001-V1.0-RESTRINGIDO`.

**Registro de cambios**

| Fecha | Versión | Descripción del cambio | Tipo | Responsable | Aprobación |
|---|---|---|---|---|---|
| dd-mm-aaaa | V1.0 | Emisión inicial | — | Líder de QA | Equipo |
| dd-mm-aaaa | V1.1 | Corrección del cálculo de cobertura | Fondo | Integrante | Líder de QA |

El tipo de modificación puede ser **de forma** (presentación, formato) o **de fondo** (contenido, criterios).

### 10.16 Revisión y aprobación interna

1. **Elaboración por el auditor líder:** borrador inicial que integra los hallazgos de todo el equipo.
2. **Revisión por el equipo:** verificación de exactitud y completitud.
3. **Validación técnica:** un revisor técnico independiente verifica el cumplimiento de estándares y procedimientos internos.
4. **Aprobación gerencial:** la dirección autoriza la emisión final mediante firma electrónica o física.

Este proceso de varios niveles asegura controles de calidad rigurosos antes de la emisión oficial.

### 10.17 Confidencialidad y protección de datos

1. **Clasificación de la información:** identificar datos sensibles comerciales, técnicos o personales que requieren protección especial según la regulación aplicable (el tema menciona el RGPD europeo; en Chile corresponde la Ley 19.628 y, desde el 01-12-2026, la Ley 21.719).
2. **Acuerdos de confidencialidad:** todo el personal involucrado firma cláusulas que cubren la información del cliente.
3. **Almacenamiento seguro:** sistemas cifrados para el almacenamiento digital y control de acceso físico para documentos impresos.
4. **Distribución controlada:** circulación limitada a partes autorizadas, con registro de entregas y acuse de recibo.
5. **Retención y destrucción:** plazos de retención según requisitos legales y destrucción segura de la información obsoleta.

Un informe de seguridad describe vulnerabilidades explotables; por ello su circulación debe restringirse hasta que estén corregidas.

### 10.18 Errores críticos que invalidan un informe

| Error | Descripción |
|---|---|
| Ausencia de evidencias objetivas | Hallazgos sin soporte documental verificable por terceros |
| Referencias normativas incorrectas | Cláusulas o versiones de normas que no corresponden o están desactualizadas |
| Falta de firmas autorizadas | Emisión sin aprobación formal de los responsables designados |
| Inconsistencias internas | Contradicciones entre el resumen ejecutivo y las conclusiones |

Estos errores pueden anular el informe en una auditoría de acreditación, comprometer la credibilidad del organismo y generar conflictos legales. El segundo error es directamente aplicable a la propia unidad: citar ISO 19011 sin indicar que la edición vigente es la de 2026 constituye una referencia desactualizada.

### 10.19 Herramientas digitales

| Herramientas | Función |
|---|---|
| Software de gestión de auditorías | Captura digital de evidencias en terreno y generación automatizada de informes |
| Sistemas de gestión documental | Control de versiones, flujos de aprobación y almacenamiento seguro |
| Plantillas estandarizadas | Consistencia de formato y cumplimiento de requisitos estructurales |

**Beneficios de la digitalización:** reducción de tiempos de elaboración; minimización de errores de transcripción; trazabilidad completa con auditoría retrospectiva; incorporación de multimedia; acceso remoto para revisiones; respaldo automático de la información.

### 10.20 Mejora continua del proceso de reporte

1. **Establecer objetivos:** metas de calidad, tiempo y satisfacción del cliente.
2. **Monitorear el desempeño:** indicadores de calidad, retroalimentación de clientes y observaciones de acreditación.
3. **Identificar mejoras:** en plantillas, procedimientos y capacitación.
4. **Implementar cambios:** actualizar documentación, formar al personal y ajustar las herramientas.
5. **Verificar resultados:** medir la efectividad de las mejoras con indicadores.

El ciclo corresponde a la lógica Planificar–Hacer–Verificar–Actuar. La excelencia en los informes se plantea como un proceso continuo de refinamiento y no como un estado final.

**Pregunta de cierre del tema.** Si el informe es la culminación de la auditoría, ¿cómo puede el auditor líder pasar de ser un redactor de hallazgos a ser un facilitador de la confianza mediante la transparencia técnica? Una respuesta posible es que el informe no solo enumere problemas, sino que explique su impacto, su evidencia y la ruta para corregirlos, de modo que quien decide confíe en el proceso que llevó a la conclusión.

### 10.21 Errores frecuentes en informes de estudiantes

1. Emitir un dictamen favorable con defectos críticos abiertos.
2. Redactar en primera persona o con juicios de valor.
3. No numerar ni fechar las evidencias.
4. Presentar un resumen ejecutivo que contradice la conclusión.
5. Citar leyes sin artículo, o normas sin edición.

### 10.22 Preguntas de repaso

1. Explique por qué el informe de certificación tiene valor legal e institucional.
2. Enumere los cuatro estándares del tema e indique su ámbito y edición vigente.
3. Enumere las seis secciones del informe y los ocho datos de la identificación.
4. Diferencie conformidad, observación, no conformidad menor y no conformidad mayor.
5. Redacte una no conformidad con sus cuatro partes.
6. Explique los tres requisitos de la evidencia objetiva.
7. Construya el código de un informe con los cinco elementos de la codificación.
8. Describa los cuatro niveles de revisión y aprobación.
9. Indique cuatro errores que invalidan un informe.

---

## Capítulo 11. Aplicación: informe de certificación de software (actividad 2.4.2)

**Indicador de logro:** IL2.5 (el encabezado de la actividad indica IL2.4). **Modalidad:** individual, 45 minutos. **Propósito:** estructurar el informe que comunica si el software es apto para su lanzamiento.

### 11.1 Estructura del informe

| # | Sección | Contenido |
|---|---|---|
| 1 | Resumen ejecutivo | Declaración breve sobre el estado del software: ¿es apto para su lanzamiento? Dictamen (Certificado, No certificado, Certificado con reservas) y alcance (módulos probados) |
| 2 | Métricas de ejecución | Cuantificación del esfuerzo y de los resultados; los datos numéricos dan objetividad a la certificación |
| 3 | Gestión de defectos | Clasificación de los errores para evaluar el riesgo residual |
| 4 | Matriz de trazabilidad | Demuestra que cada requisito del cliente tiene un caso asociado y un resultado; es el anexo más importante |
| 5 | Evaluación de riesgos | Riesgos que persisten después de las pruebas: mitigados y aceptados |
| 6 | Conclusión y recomendación final | Veredicto técnico basado en los criterios de aceptación definidos al inicio |

### 11.2 Métricas de ejecución

| Indicador | Valor del ejemplo |
|---|---|
| Casos diseñados | 50 |
| Casos ejecutados | 48 (96 %) |
| Casos exitosos (*Pass*) | 42 (87 %) |
| Casos fallidos (*Fail*) | 4 |
| Casos bloqueados | 2 |

**Nota de cálculo.** 42 de 48 equivale a 87,5 %; sobre 50 casos diseñados equivale a 84 %. Además, la suma 42 + 4 + 2 = 48 indica que los bloqueados se contaron dentro de los "ejecutados". Al informar porcentajes se debe declarar la base de cálculo y la convención usada para los bloqueados.

### 11.3 Gestión de defectos

| Categoría | Definición en la actividad |
|---|---|
| **Críticos** | Fallas de seguridad (por ejemplo, inyección SQL) o caídas del sistema |
| **Mayores** | Funcionalidades principales que no funcionan según el requisito |
| **Menores** | Errores estéticos o de usabilidad que no impiden la operación |

**Regla:** un software con defectos críticos abiertos nunca debe ser certificado.

**Riesgo residual.** Riesgo que permanece después de aplicar las pruebas y las correcciones. Se informa para que quien decide conozca lo que acepta.

### 11.4 Evaluación de riesgos

| Tipo | Definición | Ejemplo |
|---|---|---|
| Riesgo mitigado | Riesgo reducido mediante una corrección verificada | Se corrigió la vulnerabilidad de acceso no autorizado en el módulo administrativo |
| Riesgo aceptado | Riesgo conocido que se asume de forma explícita, con justificación | El sistema presenta lentitud con más de 500 usuarios simultáneos (fuera del alcance actual) |

### 11.5 Conclusión y dictamen

- **Criterio de aceptación** (ejemplo): se requiere el 100 % de los casos críticos exitosos.
- **Resultado** (ejemplo): se cumplió el criterio; por lo tanto, se recomienda la certificación.

**Criterio para elegir el dictamen**

| Situación | Dictamen |
|---|---|
| Al menos un defecto crítico abierto | **No certificado** |
| Sin críticos; defectos mayores o graves con plan de corrección y plazos | **Certificado con reservas**, con las condiciones indicadas |
| Sin críticos ni mayores; todos los criterios de aceptación cumplidos | **Certificado** |

El dictamen técnico y el análisis ético-normativo deben ser coherentes: no es posible certificar un sistema y, en la sección siguiente, describir un incumplimiento legal grave sin resolver.

### 11.6 Ejemplo de resumen ejecutivo

> Entre el [fecha] y el [fecha] se evaluó la versión [x] del sistema [nombre], desplegada en contenedores Docker, sobre los módulos de autenticación, gestión de usuarios y [módulos]. Se diseñaron [n] casos de prueba con cobertura del 100 % de los requisitos del ERS, de los cuales se ejecutaron [n]. Se registraron [n] incidentes: [n] críticos, [n] graves, [n] moderados y [n] leves. Dado que persisten [n] incidentes críticos asociados al almacenamiento de credenciales y al control de acceso, el dictamen es **No certificado**. La certificación podrá reevaluarse tras la corrección y reprueba de los incidentes INC-01 e INC-02.

### 11.7 Errores frecuentes

1. Calcular porcentajes sin declarar la base.
2. Omitir la matriz de trazabilidad o presentarla sin resultados.
3. No distinguir riesgos mitigados de riesgos aceptados.
4. Emitir el dictamen sin vincularlo al criterio de aceptación definido en el plan.

### 11.8 Preguntas de repaso

1. Enumere las seis secciones del informe de certificación de software.
2. Calcule los porcentajes del ejemplo con base en los casos diseñados y en los ejecutados.
3. Explique por qué un software con defectos críticos abiertos no debe certificarse.
4. Diferencie riesgo mitigado y riesgo aceptado con un ejemplo de un sistema de salud.
5. Indique el dictamen que corresponde con dos defectos mayores y ninguno crítico, y las condiciones que deberían fijarse.

---

## Capítulo 12. Herramientas del laboratorio

**Propósito del capítulo:** reunir en un solo lugar las herramientas de la unidad, su función, el tipo de prueba que respaldan, la evidencia que generan y la forma correcta de interpretar sus resultados.

### 12.1 Herramientas disponibles para la Evaluación 2

Para los casos A y B se dispone, en contenedores Docker, del siguiente conjunto de herramientas:

| Herramienta | Categoría | Función | Tipo de prueba o requisito que respalda | Evidencia que produce |
|---|---|---|---|---|
| **SonarQube** | SAST / calidad de código | Analiza el código sin ejecutarlo; detecta bugs, vulnerabilidades, Security Hotspots y code smells | Análisis estático (IL2.3); mantenibilidad; seguridad del código | Panel, reporte exportado, archivo y línea |
| **OWASP ZAP** | DAST | Proxy y escáner de aplicaciones web; recorre la aplicación y ejecuta análisis pasivos y activos | Seguridad de la aplicación desplegada: configuración, cabeceras, inyección, XSS. Para llegar a las funciones internas se configura con sesión iniciada | Reporte HTML o JSON con alertas y nivel de riesgo |
| **Burp Suite** | Proxy / pruebas manuales | Intercepta, modifica y repite solicitudes HTTP | Pruebas de autorización (cambiar un identificador, quitar el token, cambiar el rol), de sesión y de lógica de negocio | Solicitud y respuesta capturadas |
| **Nikto** | Escáner de servidor web | Busca configuraciones inseguras, archivos expuestos y versiones conocidas del servidor | Seguridad de la configuración del servidor | Listado de hallazgos por URL |
| **SQLMap** | Inyección SQL | Detecta de forma automatizada inyecciones SQL en parámetros | Validación de entradas en el inicio de sesión y en servicios con parámetros | Resultado por parámetro: vulnerable o no |
| **John the Ripper** | Auditoría de contraseñas | Intenta recuperar contraseñas a partir de sus hashes mediante diccionarios y fuerza bruta | Fortaleza de la política de contraseñas y del algoritmo de hash | Contraseñas recuperadas y tiempo empleado |
| **JMeter** | Rendimiento | Simula usuarios concurrentes y mide tiempos, rendimiento y errores | Carga y estrés (requisitos de rendimiento y disponibilidad) | Reporte HTML con percentiles, rendimiento y tasa de error |
| **Selenium** | Automatización funcional | Controla el navegador para repetir flujos de usuario | Funcionales, regresión y compatibilidad entre navegadores | Script, registro de ejecución y capturas |

### 12.2 Interpretación correcta de los resultados

- **ZAP y Nikto** generan alertas que pueden ser falsos positivos; cada alerta relevante se confirma manualmente antes de registrarla como incidente. Un análisis de ZAP sin sesión iniciada solo cubre las páginas públicas.
- **SQLMap** se ejecuta únicamente contra el entorno propio. Si concluye que un parámetro no es vulnerable, ese resultado es evidencia de un caso aprobado.
- **John the Ripper** solo es pertinente si existen hashes. Si las contraseñas se almacenan en texto plano, el hallazgo es más grave y la herramienta no es necesaria para demostrarlo.
- **JMeter**: se informan percentiles (por ejemplo, el percentil 90 o 95) y no solo el promedio, porque el promedio oculta las respuestas lentas. Si el código contiene retardos artificiales, se mide con y sin ellos y se explica la diferencia.
- **SonarQube**: se lee el código general y no solo el código nuevo (Capítulo 8).

### 12.3 Otras herramientas de la unidad

| Categoría | Herramientas | Uso |
|---|---|---|
| Automatización funcional | Selenium, Cypress, Playwright; Appium para móviles | Ejecución automática de flujos y regresión |
| Gestión de casos | TestRail, Jira + Zephyr, Azure Test Plans, Azure DevOps, qTest, TestLink, PractiTest | Repositorio de casos, ejecución y trazabilidad |
| Seguimiento de defectos | Jira, Bugzilla, Redmine | Ciclo de vida de los defectos |
| Infraestructura | Docker, Docker Compose | Entorno reproducible |
| Pruebas de API | Swagger UI (`/docs`), Postman | Pruebas funcionales y de autorización sobre la API |
| Desarrollo | Visual Studio Code | Revisión del código y de la configuración |

### 12.4 Correspondencia entre herramientas y OWASP Top 10:2025

| Categoría OWASP | Herramientas útiles |
|---|---|
| A01 Control de acceso roto | Burp Suite, Postman, revisión manual |
| A02 Configuración incorrecta | Nikto, ZAP, revisión de `docker-compose.yml` y `.env` |
| A03 Cadena de suministro | Revisión de dependencias (por ejemplo, `npm audit`), SonarQube |
| A04 Fallas criptográficas | Revisión manual, John the Ripper, consulta a la base de datos |
| A05 Inyección | SQLMap, ZAP, SonarQube |
| A06 Diseño inseguro | Revisión de requisitos y del diseño |
| A07 Fallas de autenticación | Burp Suite, John the Ripper, casos manuales de intentos repetidos y expiración |
| A08 Integridad de software y datos | Revisión manual |
| A09 Registro y alerta | Revisión de la tabla o archivo de auditoría tras ejecutar los casos |
| A10 Condiciones excepcionales | Casos de error forzado, ZAP, SonarQube |

### 12.5 Justificación de una herramienta

Las rúbricas valoran la justificación. Una estructura recomendada es:

> "Se utiliza **[herramienta]** para **[tipo de prueba]** sobre **[requisito o riesgo]**, porque **[capacidad concreta]**. Su resultado se registra como **[evidencia]** en el caso **[ID]**."

Ejemplo: "Se utiliza JMeter para la prueba de carga del requisito de tiempo de respuesta, porque permite simular 200 usuarios concurrentes y medir el percentil 90. El reporte HTML se adjunta como evidencia del caso CP-05."

### 12.6 Preguntas de repaso

1. Indique qué herramienta permite probar que un usuario no accede a un registro de otro usuario y explique el procedimiento.
2. Explique por qué un análisis de ZAP sin sesión iniciada tiene cobertura limitada.
3. Diferencie ZAP de Nikto.
4. Explique por qué en una prueba de carga se informa el percentil 90 y no solo el promedio.
5. Redacte la justificación de SQLMap con la estructura de 12.5.

---

## Capítulo 13. Marco ético y normativo

**Propósito del capítulo:** aplicar el marco legal y ético a los resultados de las pruebas, de modo que cada hallazgo técnico se traduzca en un riesgo para las personas, una norma afectada y una recomendación.

### 13.1 Uso de la normativa en la unidad

La unidad no introduce leyes desde cero: reutiliza el marco de la Unidad 1 y exige **aplicarlo a los resultados**. El análisis ético y normativo se construye con la secuencia:

```
Hallazgo técnico → Riesgo para las personas → Norma y artículo → Sujeto obligado → Recomendación
```

**Reglas:**

1. **Citar el artículo, no solo la ley.** "Ley 19.628" no basta; "Ley 19.628, art. 11 (deber de cuidado de los datos)" sí.
2. **Distinguir lo vigente de lo que entrará en vigencia.** No atribuir a una ley derechos o sanciones que están en otra, ni presentar como vigente una norma que aún no rige.
3. **Identificar al sujeto obligado.** Muchas leyes no obligan al software, sino a la organización que lo opera; el software debe **permitir** que esa organización cumpla.

### 13.2 Normas generales del curso

| Norma | Estado al 19-10-2026 | Aporte al análisis de pruebas |
|---|---|---|
| **Ley 19.628**, sobre protección de la vida privada | Vigente en su texto actual | Define datos personales y datos sensibles (art. 2); deber de secreto (art. 7); tratamiento de datos sensibles (art. 10); deber de cuidado de los datos con la debida diligencia (art. 11); indemnización por tratamiento indebido (art. 23) |
| **Ley 21.719**, sobre protección de datos personales | Publicada el 13-12-2024; **entra en vigencia el 01-12-2026** | Reemplaza gran parte del texto de la Ley 19.628. Incorpora deberes de seguridad (art. 14 quinquies), reporte de vulneraciones (art. 14 sexies), infracciones graves y gravísimas (arts. 34 ter y 34 quáter) y multas de hasta 5.000, 10.000 y 20.000 UTM (art. 35). Crea la Agencia de Protección de Datos Personales |
| **Ley 21.663**, Ley Marco de Ciberseguridad | Vigente; la Agencia Nacional de Ciberseguridad opera desde 2025 | Obliga a las instituciones que prestan servicios esenciales (art. 4 incluye la prestación institucional de salud) y a los operadores de importancia vital. Reporte de incidentes al CSIRT Nacional: alerta temprana en 3 horas y actualización en 72 horas (art. 9). Infracciones y multas (arts. 38 y 40) |
| **Ley 21.459**, sobre delitos informáticos | Vigente | Tipifica el ataque a la integridad de un sistema (art. 1), el acceso ilícito (art. 2), la interceptación ilícita (art. 3) y el ataque a la integridad de los datos (art. 4). Explica el impacto de una vulnerabilidad y fija los límites éticos de las pruebas |
| **Ley 17.336**, sobre propiedad intelectual | Vigente | Uso de software y componentes de terceros; licencias de dependencias; sanciones (arts. 78 y 79) |
| **Ley 19.799 y DS 181 de 2002**, documento electrónico y firma electrónica | Vigentes | Aplican si el sistema emite o firma documentos electrónicos con valor legal |
| **Ley 21.180**, de transformación digital del Estado | Vigente | Aplica a sistemas que se relacionan con organismos públicos |
| **Política Nacional de Ciberseguridad** | Política pública | Marco orientador; no impone obligaciones directas a un sistema privado |
| **Manual de Accesibilidad Web del Gobierno de Chile** | Guía técnica | Base para requisitos y pruebas de accesibilidad |

### 13.3 Normas sectoriales

La pregunta guía es: ¿qué norma regula la actividad que el software apoya?

| Dominio | Normas | Pruebas que generan |
|---|---|---|
| **Salud** (por ejemplo, Cuidarte+) | Ley 20.584, derechos y deberes de los pacientes (art. 12: la ficha clínica es dato sensible; art. 13: acceso restringido a quienes participan en la atención, conservación por 15 años); Ley 21.668, interoperabilidad de fichas clínicas; DS 41 de 2012 del MINSAL, reglamento de fichas clínicas (art. 8: respaldo y barreras de acceso; art. 9: registro de las personas que acceden y de las fechas) | Cada lectura o descarga de un examen queda registrada con usuario y fecha; un profesional no vinculado a la atención no accede a la ficha; los datos no se eliminan físicamente antes del plazo de conservación |
| **Gestión empresarial** (por ejemplo, Atlas) | Ley 19.628 y Ley 21.719 para los datos de clientes; Ley 19.799 si los contratos se firman electrónicamente | Un perfil editor no modifica contratos; los datos de un cliente no son visibles desde otra empresa |
| **Banca** (actividad 2.1.2) | Normativa del regulador financiero; Ley 21.663 si la entidad es operador de importancia vital | Bloqueo tras intentos fallidos; invalidación de tokens; cifrado en tránsito |

En un caso de salud, la normativa sanitaria es la que regula de forma específica el dato clínico; por ello encabeza el análisis.

### 13.4 Principios éticos aplicados a las pruebas

| Principio | Aplicación |
|---|---|
| **Autorización y alcance** | Las herramientas de seguridad se usan solo contra el entorno propio y autorizado (el entorno Docker local del caso). Usarlas contra sistemas ajenos es la conducta que sanciona la Ley 21.459 |
| **Datos sintéticos** | No se usan datos reales de personas (RUT, diagnósticos, contratos), aunque el entorno sea local |
| **Honestidad en el reporte** | Se informan todos los hallazgos, también los desfavorables. Ocultar un defecto para mejorar el dictamen es una falta profesional |
| **Proporcionalidad** | Se demuestra la vulnerabilidad sin causar más daño del necesario |
| **Confidencialidad** | La distribución del informe se controla, porque describe vulnerabilidades explotables |
| **Foco en las personas** | El impacto se mide en las personas afectadas (pacientes, clientes), no solo en el sistema |
| **Independencia** | El juicio de QA no se subordina a plazos ni a la presión por aprobar |
| **Mejora continua** | Cada hallazgo termina en una recomendación concreta y verificable |

Estos principios son coherentes con el Código de Ética y Conducta Profesional de ACM (2018) y con el código de ética de ISTQB, que promueven el interés público, la integridad del juicio profesional y la honestidad en la comunicación de resultados.

### 13.5 Ejemplo de análisis ético-normativo

| Elemento | Contenido |
|---|---|
| Hallazgo | Las contraseñas se almacenan y comparan en texto plano (archivo y línea) |
| Riesgo | Si se filtra la base de datos, todas las cuentas quedan expuestas; muchas personas reutilizan contraseñas en otros servicios |
| Norma vigente | Ley 19.628, art. 11: deber de cuidado de los datos con la debida diligencia |
| Norma próxima | Art. 14 quinquies del texto incorporado por la Ley 21.719 (medidas de seguridad), desde el 01-12-2026 |
| Requisito del ERS | Almacenamiento de contraseñas con función de hash |
| Sujeto obligado | La organización que opera el sistema; el sistema, tal como está, no le permite cumplir |
| Severidad | Crítica |
| Recomendación | Aplicar una función de hash robusta con sal (por ejemplo, bcrypt), forzar el cambio de las contraseñas existentes y agregar un caso de regresión |
| Efecto en el dictamen | Con este defecto abierto el sistema no puede certificarse |

### 13.6 Errores frecuentes

1. Citar la Ley 21.719 como vigente antes del 01-12-2026.
2. Afirmar que la Ley 21.663 obliga al software y no a la institución.
3. Citar leyes sin artículo.
4. Omitir la normativa sectorial del dominio del caso.
5. Usar datos reales en las pruebas.

### 13.7 Preguntas de repaso

1. Explique por qué no se debe citar la Ley 21.719 como vigente en octubre de 2026.
2. Indique a quién obliga la Ley 21.663 y qué exige su art. 9.
3. Nombre dos principios éticos que limitan el uso de SQLMap.
4. Construya un análisis ético-normativo completo para un servicio que entrega datos de otro paciente.
5. Explique qué norma sectorial exige registrar quién accede a la ficha clínica.

---

## Capítulo 14. Evaluaciones EP3 y EP4

### 14.1 Datos generales

| Aspecto | EP3 | EP4 |
|---|---|---|
| Nombre | Verificando la calidad, seguridad y cumplimiento normativo | Igual |
| Tipo | Encargo (informe) | Presentación (defensa) |
| Modalidad | Grupal | Individual |
| Ponderación | 12 % | 28 % |
| Tiempo asignado en la pauta | 1 hora pedagógica | 3 horas pedagógicas |
| Defensa | 10 minutos de exposición y 5 de preguntas; orden aleatorio | Igual |
| Entrega | Informe y material de apoyo en AVA | Material de apoyo en AVA |
| Insumos | ERS, imágenes Docker, código fuente y retroalimentación de EP1 | Igual |

La nota de la defensa es **individual** y depende de lo que cada estudiante demuestre. Si un estudiante no puede explicar el proyecto con claridad, se considera que no participó en su desarrollo; por ello cada integrante debe dominar el trabajo completo.

### 14.2 Contenido obligatorio del informe EP3

1. Lo elaborado en EP1, ajustado según la retroalimentación del docente.
2. Casos de prueba con **cobertura del 100 %** de los requisitos del ERS (necesidades, normativa, legal y seguridad).
3. Criterios de calidad, seguridad y cumplimiento normativo del caso.
4. Plan de pruebas: estrategia, tipos de prueba y su justificación, criterios de aceptación y herramientas.
5. Al menos **cinco casos representativos** de los distintos tipos de requisito, cada uno con ID, descripción, requisito (código del ERS), datos de entrada, resultado esperado, criterio de aceptación y tipo de prueba.
6. Ejecución: resumen, detalle por caso e incidentes con su criticidad.
7. Análisis ético y normativo de los resultados.

**Formato:** Word o PDF; títulos en Arial 12 y cuerpo en Arial 11; interlineado 1,5; texto justificado; portada con nombre completo de cada integrante, carrera, sección, docente y fecha; lenguaje formal y técnico; capturas legibles.

**Estructura del formato oficial:** 1 Introducción; 2 Criterios de calidad; 3 Plan de pruebas (3.1 Estrategia, 3.2 Tipos de prueba, 3.3 Criterios de aceptación, 3.4 Herramientas y recursos); 4 Diseño de casos de prueba; 5 Ejecución de pruebas (5.1 Resumen, 5.2 Detalle, 5.3 Criticidad de incidentes). El formato no incluye una sección de análisis ético y normativo, pero el encargo la exige; se recomienda agregarla como sección 6, seguida de conclusiones y anexos (matriz de trazabilidad).

### 14.3 Rúbrica EP3

Escala de cada criterio: 100 % (muy buen desempeño), 80 % (buen desempeño), 60 % (aceptable), 30 % (incipiente) y 0 % (no logrado).

| Criterio | Peso | Exigencia para el 100 % | Sección del informe |
|---|---|---|---|
| **IE1** Importancia de la calidad, la seguridad y el cumplimiento legal | 20 % | Claridad y profundidad, ejemplos pertinentes y lenguaje técnico | Introducción, criterios de calidad, análisis ético-normativo |
| **IE3** Clasificación de los tipos de prueba y su propósito | **38 %** | Clasificar y describir todos los tipos (funcionales, no funcionales, seguridad, rendimiento, entre otros), justificando su propósito y aplicación | 3.2 y casos |
| **IE5** Pruebas no funcionales: propósito y contexto | 15 % | Casos representativos de distintos tipos no funcionales, con criterio de aceptación y propósito coherentes con el contexto | Casos de rendimiento, usabilidad, compatibilidad, seguridad y disponibilidad |
| **IE7** Elementos del plan y su vínculo con requisitos y normas | 15 % | Todos los apartados (introducción, alcance, objetivos, estrategia, recursos y cronograma) con coherencia técnica y vínculo con requisitos y normativa vigente | Sección 3 |
| **IE9** Cobertura y coherencia frente a estándares técnicos y legales | 12 % | Evaluación de la coherencia y la cobertura respecto de requisitos y estándares, con análisis crítico | Matriz de trazabilidad y análisis de cobertura |

### 14.4 Contenido obligatorio de la presentación EP4

- Enfoque estratégico de las pruebas.
- Herramientas seleccionadas y su justificación.
- Ejecución de las pruebas realizadas.
- Clasificación de los defectos identificados.
- Reflexiones sobre calidad, seguridad, normativa y aspectos legales de los resultados.

### 14.5 Rúbrica EP4

| Criterio | Peso | Exigencia para el 100 % | Preparación |
|---|---|---|---|
| **IE2** Estrategia y justificación de seguridad y normativa | 20 % | Claridad, dominio y fluidez; justificación sólida con ejemplos concretos | Estrategia por riesgo y un requisito legal convertido en caso |
| **IE4** Tipos de prueba aplicados, origen e impacto | **38 %** | Explicar con precisión cada tipo, de dónde nace (requisito, riesgo, norma) y qué impacto tiene su resultado | Para cada tipo: requisito → caso → resultado → impacto |
| **IE6** Análisis estático frente a criterios legales | 15 % | Presentar los resultados de SonarQube y compararlos con criterios legales o normativos con capacidad crítica | Tabla problema → OWASP → norma → severidad (8.13) |
| **IE8** Proceso de ejecución y trazabilidad | 15 % | Proceso claro, ordenado y lógico, con trazabilidad completa con los requisitos | *Smoke test* → ciclos → bitácora → incidentes, con un caso seguido de principio a fin |
| **IE10** Recomendaciones con evidencia y principios éticos y normativos | 12 % | Recomendaciones con evidencia técnica sólida y referencias explícitas a principios éticos y normativos | Cada recomendación con su incidente y su artículo |

### 14.6 Lectura conjunta de las rúbricas

- El **38 %** de cada rúbrica corresponde a los **tipos de prueba**; es el contenido de mayor peso.
- La rúbrica de EP3 no nombra de forma explícita la ejecución ni el análisis estático, pero el encargo los exige y EP4 los evalúa (IE6 e IE8).
- Debe existir coherencia entre el informe y la defensa: mismos identificadores de casos, mismas severidades y mismo dictamen.
- Preguntas probables en la defensa: por qué se eligió una herramienta; qué significa una métrica de SonarQube; por qué un incidente es crítico y no grave; qué artículo respalda una recomendación; cómo se calculó la cobertura; qué se haría distinto en un nuevo ciclo.

### 14.7 Estructura sugerida para la defensa de 10 minutos

| Minuto | Contenido | Criterio |
|---|---|---|
| 0–1 | Contexto del sistema y alcance | IE2 |
| 1–3 | Estrategia por riesgo; seguridad y normativa en el plan | IE2 |
| 3–6 | Tipos de prueba aplicados: origen, ejemplo y resultado | IE4 |
| 6–7 | SonarQube frente a criterios legales | IE6 |
| 7–8,5 | Proceso de ejecución y trazabilidad, con un caso de principio a fin | IE8 |
| 8,5–10 | Defectos por severidad, dictamen y recomendaciones | IE10 |

---

## Capítulo 15. Observaciones técnicas sobre conceptos de la unidad

Conocer estas precisiones evita trasladar imprecisiones al informe y permite responder con seguridad ante preguntas del docente.

| Ámbito | Situación | Precisión |
|---|---|---|
| Encabezado de la actividad 2.1.2 | Indica "EA1" | La actividad pertenece a la Unidad 2 (IL2.1) |
| Encabezado de la actividad 2.3.2 | Indica "IL2.3" | El contenido corresponde a la ejecución de pruebas (IL2.4) |
| Encabezado de la actividad 2.4.2 | Indica "IL2.4" y un objetivo sobre análisis estático | El contenido corresponde al informe de certificación (IL2.5) |
| Objetivos de 2.2.2 y 2.3.2 | Comparten el mismo texto | El objetivo de 2.3.2 debería referirse a la ejecución |
| IL2.2 | Redacción distinta en el Programa y en las pautas | Ambas redacciones son complementarias (ver Objetivos) |
| Indicadores de calidad y seguridad (tema 2.1.1) | Incluyen métricas de manufactura y seguridad industrial | No aplican al software; ver equivalencias en 2.13 |
| ISO 19011 (tema 2.4.1) | Descrita como directriz "de calidad y ambiental", edición 2018 | Desde 2011 se aplica a cualquier sistema de gestión; la edición vigente es ISO 19011:2026 |
| ISO/IEC 17021-1 (bibliografía del tema 2.4.1) | Citada con año 2018 | La edición vigente es de 2015 |
| IAF MD 4 (tema 2.4.1) | Descrito como "uso obligatorio de documentos normativos del IAF" | Trata el uso de TIC con fines de auditoría y evaluación de la conformidad; todos los documentos MD del IAF son obligatorios para sus miembros, pero ese no es el objeto del MD 4 |
| IEEE 829 | Citado como plantilla vigente | Reemplazado por ISO/IEC/IEEE 29119-3; su estructura sigue siendo útil como modelo |
| Escalas de severidad | Tres escalas distintas (formato EP3, 2.3.2 y 2.4.2) | Usar la del formato EP3 y declarar la equivalencia (9.5) |
| Métricas del ejemplo de 2.4.2 | 42 aprobados equivalen a "87 %" | 87,5 % sobre 48 ejecutados; 84 % sobre 50 diseñados; los bloqueados se contaron como ejecutados |
| Partición de equivalencia con dos rangos | Se identifican tres clases | En un análisis fino hay cinco: dos válidas y tres inválidas (6.4) |
| Pautas EP3 y EP4 | "La Evaluación Parcial 2 corresponde…"; EP4 es individual pero menciona "grupos" | Texto heredado de otra pauta |
| Programa de Asignatura | Grupos de máximo tres integrantes | El docente puede autorizar otra conformación |
| Bibliografía obligatoria | Incluye Spring Security | El código de los casos es Node.js/Express; los principios de autenticación y autorización son igualmente aplicables |
| Cifras de beneficio (10x, 100x, 70 %, 3x, 95 %, 40 %, USD 250.000) | Presentadas como datos generales | Deben usarse como argumento ilustrativo, no como medición del caso |
| Índice del tema 2.3.1 | Incluye "Integración en el ciclo de desarrollo (SDLC)" | Se desarrolla mediante la integración en CI/CD (8.15) |

---

## Glosario

| Término | Definición |
|---|---|
| **Acreditación** | Reconocimiento formal de la competencia de un organismo de evaluación de la conformidad |
| **Análisis de flujo de datos** | Técnica de caja blanca que sigue cada variable desde su definición hasta su uso para detectar anomalías |
| **Análisis de valores límite (BVA)** | Técnica de caja negra que prueba los valores en las fronteras de las particiones |
| **Auditoría** | Proceso sistemático, independiente y documentado para obtener y evaluar evidencia objetiva frente a criterios |
| **Bitácora de ejecución** | Registro cronológico de la ejecución de los casos, con estado, defecto y observaciones |
| **Bloqueado** | Estado de un caso que no puede ejecutarse por un defecto previo o por el entorno |
| **Bug** | En SonarQube, problema de confiabilidad: código que probablemente produce un comportamiento incorrecto |
| **Caja blanca** | Enfoque de diseño de pruebas basado en la estructura interna del código |
| **Caja gris (híbrido)** | Enfoque que combina la especificación con conocimiento parcial de la estructura interna |
| **Caja negra** | Enfoque de diseño de pruebas basado en la especificación, sin conocer la implementación |
| **Camino básico** | Camino linealmente independiente del grafo de flujo de control |
| **Caso de prueba** | Conjunto estructurado de entradas, condiciones de ejecución y resultados esperados para validar un requisito (IEEE 610) |
| **Certificación** | Atestación por una tercera parte de que se cumplen requisitos especificados |
| **CI/CD** | Integración continua y entrega o despliegue continuos |
| **Ciclo de ejecución** | Ronda completa de ejecución de un conjunto de casos sobre una versión del software |
| **Clase de equivalencia** | Conjunto de valores que el sistema debería procesar de la misma manera |
| **Code smell** | Indicio de código difícil de mantener |
| **Complejidad ciclomática** | Número de caminos linealmente independientes de un programa: V(G) = E − N + 2P |
| **Conformidad** | Evidencia de cumplimiento de un requisito |
| **Contenedor** | Instancia en ejecución de una imagen Docker, aislada del anfitrión |
| **Cobertura** | Grado, en porcentaje, en que las pruebas ejercitan un elemento (requisitos, sentencias, decisiones) |
| **Criterio de aceptación** | Condición objetiva para aprobar un caso o un producto |
| **Criterio de entrada** | Condición que debe cumplirse para iniciar una actividad de prueba |
| **Criterio de salida** | Condición que debe cumplirse para dar por terminada una actividad de prueba |
| **Criterio de suspensión** | Condición que obliga a detener la ejecución hasta que se resuelva |
| **DAST** | Pruebas dinámicas de seguridad sobre la aplicación en ejecución |
| **Defecto** | Imperfección en un producto de trabajo que puede causar una falla |
| **Deuda técnica** | Esfuerzo estimado para corregir problemas de mantenibilidad |
| **Dictamen** | Decisión final del informe: Certificado, Certificado con reservas o No certificado |
| **Docker Compose** | Herramienta que define y levanta aplicaciones de varios contenedores |
| **Dockerfile** | Archivo que declara cómo construir una imagen Docker |
| **Error** | Acción humana que produce un resultado incorrecto |
| **ERS** | Especificación de Requerimientos de Software |
| **Escenario de prueba** | Descripción de alto nivel de qué se prueba |
| **Estrategia de pruebas** | Descripción de alto nivel de cómo se abordarán las pruebas para cumplir los objetivos |
| **Evidencia objetiva** | Registro verificable, trazable y suficiente que respalda un hallazgo |
| **Falla** | Desviación observable del comportamiento esperado al ejecutar el sistema |
| **Falso negativo** | Defecto real que una herramienta no detecta |
| **Falso positivo** | Hallazgo informado por una herramienta que no es un problema real |
| **Hallazgo** | Resultado de evaluar la evidencia frente a los criterios: conformidad, observación o no conformidad |
| **Imagen Docker** | Plantilla inmutable con todo lo necesario para ejecutar una aplicación |
| **Imagen endurecida** | Imagen configurada para minimizar vulnerabilidades y superficie de ataque |
| **Incidente** | Registro formal de una desviación observada durante las pruebas |
| **Inspección** | Revisión estática formal, con roles, lista de verificación y registro de defectos |
| **Inyección SQL** | Vulnerabilidad en que datos del usuario alteran la lógica de una consulta SQL |
| **Matriz de trazabilidad** | Tabla que vincula requisitos con casos, resultados y defectos |
| **Métrica** | Medida cuantitativa de un atributo del producto o del proceso |
| **Mínimo privilegio** | Principio según el cual un proceso o usuario dispone solo de los permisos estrictamente necesarios |
| **No conformidad mayor** | Incumplimiento que afecta la capacidad del sistema para lograr sus resultados |
| **No conformidad menor** | Desviación que no compromete la efectividad global del sistema |
| **Observación** | Oportunidad de mejora que no constituye incumplimiento |
| **Oráculo de prueba** | Fuente que permite determinar el resultado esperado |
| **OWASP** | Fundación que publica guías abiertas de seguridad de aplicaciones (Top 10, WSTG) |
| **Partición de equivalencia** | Técnica de caja negra que divide el dominio de entrada en clases equivalentes |
| **Plan de pruebas** | Documento que organiza, estructura y guía todas las actividades de validación del software |
| **Prioridad** | Urgencia de corrección de un defecto según el negocio |
| **Prueba de humo (smoke test)** | Verificación rápida de las funciones básicas antes de ejecutar el resto de los casos |
| **Prueba estática** | Análisis del código, del diseño o de la documentación sin ejecutar el programa |
| **Prueba dinámica** | Prueba que ejecuta el software para observar su comportamiento |
| **Prueba exploratoria estructurada** | Diseño y ejecución simultáneos, guiados por una misión y con registro de lo explorado |
| **Quality Gate** | Conjunto de condiciones que el código debe cumplir para aprobarse en SonarQube |
| **Quality Profile** | Conjunto de reglas activas para un lenguaje en SonarQube |
| **RACI** | Matriz de responsabilidades: responsable, quien rinde cuentas, consultado e informado |
| **Regresión** | Aparición de un defecto en una función que operaba correctamente, como efecto de un cambio |
| **Reporte de defecto** | Documento que describe una desviación con la información necesaria para reproducirla y corregirla |
| **Riesgo** | Combinación de la probabilidad de un evento adverso y de su impacto |
| **Riesgo aceptado** | Riesgo conocido que se asume de forma explícita y justificada |
| **Riesgo mitigado** | Riesgo reducido mediante una corrección verificada |
| **Riesgo residual** | Riesgo que permanece después de las pruebas y correcciones |
| **SAST** | Análisis estático de seguridad del código fuente |
| **Security Hotspot** | Código sensible a la seguridad que requiere revisión humana |
| **Severidad** | Impacto técnico de un defecto |
| **Shift-left** | Práctica de adelantar las pruebas a las primeras etapas del ciclo de vida |
| **SonarScanner** | Programa que analiza el código y envía los resultados al servidor SonarQube |
| **Suite de prueba** | Agrupación de casos con un fin común |
| **Tabla de decisión** | Técnica de caja negra que representa combinaciones de condiciones y sus acciones |
| **Trazabilidad** | Relación verificable entre requisitos, casos, resultados, incidentes y normas |
| **Validación** | Confirmación de que el producto satisface las necesidades del uso previsto |
| **Verificación** | Confirmación de que el producto cumple los requisitos especificados |
| **Vulnerabilidad** | Debilidad que puede ser explotada para comprometer la seguridad |
| **Walkthrough** | Revisión estática guiada por el autor del código o documento |
| **WSTG** | *Web Security Testing Guide* de OWASP |

---

## Referencias

### Estándares y marcos técnicos

- International Organization for Standardization. (2023). *ISO/IEC 25010:2023. Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*. https://www.iso.org/standard/78176.html
- International Organization for Standardization. (2021–2024). *ISO/IEC/IEEE 29119. Software and systems engineering — Software testing* (Parte 1:2022, conceptos generales; Parte 2:2021, procesos de prueba; Parte 3:2021, documentación de pruebas; Parte 4:2021, técnicas de prueba; Parte 5:2024, pruebas dirigidas por palabras clave). https://www.iso.org
- Institute of Electrical and Electronics Engineers. (2008). *IEEE 829-2008. Standard for Software and System Test Documentation* (reemplazado por ISO/IEC/IEEE 29119-3).
- Institute of Electrical and Electronics Engineers. (1990). *IEEE 610.12-1990. Standard Glossary of Software Engineering Terminology* (reemplazado por ISO/IEC/IEEE 24765).
- International Organization for Standardization. (2026). *ISO 19011:2026. Guidelines for auditing management systems* (reemplaza a ISO 19011:2018, retirada el 27-05-2026). https://www.iso.org/standard/70017.html
- International Organization for Standardization. (2015). *ISO/IEC 17021-1:2015. Conformity assessment — Requirements for bodies providing audit and certification of management systems — Part 1: Requirements*. https://www.iso.org/standard/61651.html
- International Organization for Standardization. (2012). *ISO/IEC 17065:2012. Conformity assessment — Requirements for bodies certifying products, processes and services*. https://www.iso.org/standard/46568.html
- International Accreditation Forum. (2025). *IAF MD 4:2025, Issue 3. IAF Mandatory Document for the Use of Information and Communication Technology (ICT) for Conformity Assessment Purposes* (de aplicación desde el 30-01-2026). https://iaf.nu/en/iaf-documents/
- International Software Testing Qualifications Board. (2023). *Certified Tester Foundation Level (CTFL) Syllabus, v4.0*. https://www.istqb.org
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://www.nist.gov/cyberframework
- OWASP Foundation. (2025). *OWASP Top 10:2025*. https://owasp.org/Top10/2025/
- OWASP Foundation. (2020). *Web Security Testing Guide, v4.2*. https://owasp.org/www-project-web-security-testing-guide/
- McCabe, T. J. (1976). A complexity measure. *IEEE Transactions on Software Engineering, SE-2*(4), 308–320.
- Association for Computing Machinery. (2018). *ACM Code of Ethics and Professional Conduct*. https://www.acm.org/code-of-ethics

### Documentación de herramientas

- SonarSource. (2025). *SonarQube Server documentation* (Quality Gates, Quality Profiles, métricas y modos de severidad). https://docs.sonarsource.com/sonarqube-server/
- Docker Inc. *Docker documentation* (Dockerfile, Docker Compose, buenas prácticas de construcción). https://docs.docker.com/
- OWASP Foundation. *Zed Attack Proxy (ZAP) documentation*. https://www.zaproxy.org/docs/
- Apache Software Foundation. *Apache JMeter User's Manual*. https://jmeter.apache.org/usermanual/
- Selenium Project. *Selenium documentation*. https://www.selenium.dev/documentation/

### Normativa chilena (Biblioteca del Congreso Nacional, LeyChile: https://www.bcn.cl/leychile)

- Ley 19.628, sobre protección de la vida privada.
- Ley 21.719, que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales (publicada el 13-12-2024; vigencia desde el 01-12-2026).
- Ley 21.663, Ley Marco de Ciberseguridad.
- Ley 21.459, que establece normas sobre delitos informáticos.
- Ley 17.336, sobre propiedad intelectual.
- Ley 19.799, sobre documentos electrónicos, firma electrónica y servicios de certificación, y Decreto 181 de 2002.
- Ley 21.180, de transformación digital del Estado.
- Ley 20.584, que regula los derechos y deberes de las personas en relación con acciones vinculadas a su atención en salud.
- Ley 21.668, que modifica la Ley 20.584 en materia de interoperabilidad de fichas clínicas.
- Decreto 41 de 2012, del Ministerio de Salud, reglamento sobre fichas clínicas.

### Documentos de la asignatura

- Duoc UC. *Programa de Asignatura ISY1102 Seguridad y Calidad en el Desarrollo de Software*.
- Duoc UC. *Pauta EP3: encargo, y formato de informe de seguridad y calidad en el desarrollo de software*.
- Duoc UC. *Pauta EP4: presentación*.

---

## Anexo A. Lista de verificación de cobertura de contenidos

La tabla relaciona cada contenido de la Unidad 2 con la sección de esta guía que lo desarrolla. La columna "Tema" indica el código del contenido en la ruta de aprendizaje.

### A.1 Tema 2.1.1 Estrategias y enfoques de diseño del plan de pruebas con enfoque en calidad y seguridad

| # | Contenido | Sección |
|---|---|---|
| 1 | Dinámica inicial "¿Qué tan robusto es tu escudo?": punto crítico, riesgo fantasma, idea clave | 2.1 |
| 2 | Definición de plan de pruebas, propósito fundamental e importancia | 2.2 |
| 3 | Integración de calidad y seguridad: enfoque en calidad y en seguridad, con sus cuatro aspectos cada uno | 2.3 |
| 4 | Cuatro elementos clave del plan efectivo | 2.4 |
| 5 | Alcance y objetivos: funcionalidades críticas, áreas de seguridad prioritarias, objetivos medibles; ejemplo de autenticación | 2.5 |
| 6 | Estrategia y enfoque: funcionales, integración, rendimiento, basado en riesgos, automatización estratégica | 2.6 |
| 7 | Diseño de casos con enfoque en calidad y seguridad: casos funcionales, de seguridad, guías OWASP; propiedades del caso | 2.7 |
| 8 | Principios del testing: pruebas tempranas, testing enfocado, demostración de defectos | 2.8 y 1.6 |
| 9 | Ejemplo de caso de seguridad contra inyección SQL (`' OR '1'='1' --`) | 2.9 |
| 10 | Recursos y roles: independencia, roles especializados, herramientas adecuadas | 2.10 |
| 11 | Cronograma y gestión de riesgos: planificación iterativa, identificación, mitigación, ejemplo de priorización | 2.11 y 2.6.1 |
| 12 | Automatización y herramientas: regresión, seguridad continua (SAST/DAST), herramientas; cifras 70 %, 3x, 95 % | 2.12 y 2.6.3 |
| 13 | Evaluación y métricas: indicadores de calidad y de seguridad | 2.13 y 15 |
| 14 | Documentación y comunicación: documentar, revisar, comunicar, aprobar | 2.14 |
| 15 | Caso real de la "Empresa X": WSTG, 47 vulnerabilidades (12 críticas), 70 %, USD 250.000 | 2.15 |
| 16 | Desafíos comunes: pruebas tardías, falta de recursos especializados, desalineación; soluciones | 2.16 |
| 17 | Herramientas y recursos: plantillas IEEE 829, WSTG, Top 10, ISTQB, NIST CSF; automatización, seguridad y gestión | 2.17 |
| 18 | Flujo de trabajo optimizado en seis pasos | 2.18 |
| 19 | Pausa activa "El desafío de la perspectiva" | 2.19 |
| 20 | Plan con Docker: importancia de un plan robusto, contexto del caso semestral, objetivos principales | 3.1 |
| 21 | Imagen Docker: definición y beneficios clave | 3.2 |
| 22 | Levantamiento de imágenes: creación y captura, Dockerfile, ejemplo Node.js | 3.3 |
| 23 | Del Dockerfile al contenedor en ejecución (diagrama) | 3.4 |
| 24 | Estrategias de diseño con imágenes: objetivos, imágenes base (Alpine), versionado, automatización | 3.5 |
| 25 | Buenas prácticas de seguridad: imágenes endurecidas, minimización de capas, mínimo privilegio, aislamiento | 3.6 |
| 26 | Herramientas recomendadas: TestRail/Zephyr, Selenium/Appium, Jira/Bugzilla | 3.7 |
| 27 | Conclusión: base del éxito, integración temprana, mejora continua; cita de cierre | 2.20 |
| 28 | Cierre: shift-left, independencia del testing, métricas | 2.20 y 2.16 |
| 29 | Bibliografía del tema: IEEE 829, OWASP WSTG y Top 10, ISTQB, NIST CSF, metodologías ágiles; herramientas | 2.17, 2.22 y Referencias |

### A.2 Actividad 2.1.2 Diseño de un plan de pruebas estratégico

| # | Contenido | Sección |
|---|---|---|
| 30 | Objetivo y situación (QA Lead de banca móvil; atributos confiable, eficiente, seguro, trazable, sostenible) | 4.1 |
| 31 | Paso 1: caja negra, caja blanca y enfoque híbrido | 4.2 |
| 32 | Paso 2: módulos con V(G) > 20; análisis de flujo de datos; escenarios de ataque | 4.3 |
| 33 | Paso 3: herramienta de gestión y métricas de éxito | 4.4 |
| 34 | Entregables: matriz de trazabilidad, cronograma basado en riesgos, protocolo de mantenimiento | 4.5 |

### A.3 Guía 2.1.3 Levantamiento de imágenes en Docker del caso semestral

| # | Contenido | Sección |
|---|---|---|
| 35 | Objetivo y prerrequisitos | 5 y 5.1 |
| 36 | Estructura del proyecto (BACKEND, FRONTEND, .env, docker-compose.yml, README.md) | 5.2 |
| 37 | Procedimiento de levantamiento y verificación | 5.3 |
| 38 | Contenedores, puertos (15442:5432, 4444:4000, 3333:80) y Swagger de la API | 5.4 |

### A.4 Tema 2.2.1 Técnicas avanzadas de diseño de casos de prueba

| # | Contenido | Sección |
|---|---|---|
| 39 | Desafío del tester "detective"; idea atribuida a Mc Mullin | 6.1 |
| 40 | Definición IEEE 610, importancia y beneficios | 6.2 |
| 41 | Papel crítico de los casos: guía uniforme, colaboración, automatización | 6.2 |
| 42 | Clasificación: caja negra, caja blanca, híbridas, con sus técnicas | 6.3 |
| 43 | Partición de equivalencia: definición, tres pasos, ejemplo 1–10 y 20–30 | 6.4 |
| 44 | Análisis de valores límite: definición, importancia, valores, ejemplo 0, 1, 2, 9, 10, 11 | 6.5 |
| 45 | Tablas de decisión: ventajas y componentes | 6.6 |
| 46 | Visualización conjunta de partición y límites | 6.5 |
| 47 | Caja blanca: caminos básicos, condiciones, bucles | 6.7 |
| 48 | Complejidad ciclomática: definición, fórmula, interpretación, ejemplo V(G) = 5 | 6.8 |
| 49 | Pruebas de bucles (simples, anidados, concatenados) y flujo de datos | 6.9 y 6.10 |
| 50 | Combinación de técnicas y ejemplo de inicio de sesión | 6.11 |
| 51 | Proceso de creación en cuatro pasos | 6.12 |
| 52 | Pausa de pregunta (V(G) = 5; respuesta B) y reflexión sobre partición y límites | 6.8 y 6.5 |
| 53 | Ejemplo de partición TC-01 a TC-04 | 6.4 |
| 54 | Ejemplo de valores límite (seis casos) | 6.5 |
| 55 | Ejemplo de tabla de decisión R1–R4 | 6.6 |
| 56 | Herramientas de gestión: seis beneficios y seis herramientas | 6.13 |
| 57 | Errores comunes (seis) | 6.14 |
| 58 | Buenas prácticas (cuatro) y principios (seis) | 6.15 |
| 59 | Conclusión (10x, 40 %, 95 %) e "Inversión en excelencia" | 6.16 |
| 60 | Bibliografía: IEEE 610, McCabe (1976), Mc Mullin; herramientas de gestión | 6.17 y Referencias |

### A.5 Actividad 2.2.2 Creación de casos de prueba utilizando técnicas específicas

| # | Contenido | Sección |
|---|---|---|
| 61 | Escenario frente a caso de prueba; ejemplo de recuperación de contraseña | 7.1 |
| 62 | Plantilla estándar (ocho campos) | 7.2 |
| 63 | Matriz de pruebas: funcional, seguridad, usabilidad | 7.3 |
| 64 | Matriz de trazabilidad y reporte de defecto | 7.4 y 7.5 |

### A.6 Tema 2.3.1 Ejecuta y analiza pruebas estáticas de código

| # | Contenido | Sección |
|---|---|---|
| 65 | "El centinela silencioso" (hasta 100 veces más económico) | 8.1 |
| 66 | Definición de prueba estática y beneficios | 8.2 |
| 67 | Pruebas estáticas frente a dinámicas | 8.3 |
| 68 | Técnicas: revisión manual, inspecciones/walkthroughs, análisis automatizado | 8.4 |
| 69 | Obtención de evidencias manuales en tres pasos | 8.5 |
| 70 | Registro de resultados: evidencias claras, plantillas, informes estructurados | 8.6 |
| 71 | Herramientas de apoyo: Jira/Redmine, documentos colaborativos, integración | 8.6 |
| 72 | SonarQube: definición y características | 8.7 |
| 73 | Preparación del laboratorio: instalación, importación, reglas | 8.8 |
| 74 | Ejecución del análisis: escaneo, visualización, identificación; duración | 8.9 |
| 75 | Obtención y registro manual de evidencias en SonarQube (cinco pasos) | 8.11 |
| 76 | Ejemplo: 15 bugs, 30 code smells, 5 vulnerabilidades | 8.12 |
| 77 | Beneficios clave, retos comunes, recomendaciones | 8.14 |
| 78 | Integración en el ciclo de desarrollo (SDLC) | 8.15 |
| 79 | Conclusión y bibliografía | 8.16 y 8.18 |

### A.7 Actividad 2.3.2 Ejecución de pruebas en un entorno de laboratorio

| # | Contenido | Sección |
|---|---|---|
| 80 | Preparación del entorno | 9.1 |
| 81 | Ciclo 1 (*smoke test*) y ciclo 2 (ejecución de casos) | 9.2 |
| 82 | Registro y gestión de defectos; escala Crítica, Mayor, Menor, Cosmética | 9.4 y 9.5 |
| 83 | Bitácora de ejecución (CP-001 a CP-003) | 9.6 |
| 84 | Informe resumen de pruebas | 9.7 |

### A.8 Tema 2.4.1 Elaboración de informes finales de certificación

| # | Contenido | Sección |
|---|---|---|
| 85 | "El peso de la firma": reputación, validez legal, acreditación | 10.1 |
| 86 | Importancia estratégica: función del informe e impacto institucional | 10.2 |
| 87 | Estándares: ISO/IEC 17021-1, ISO/IEC 17065, ISO 19011, IAF MD 4 | 10.3 y 15 |
| 88 | Estructura fundamental en seis secciones | 10.4 |
| 89 | Sección de identificación (ocho datos) | 10.5 |
| 90 | Resumen ejecutivo: propósito, elementos, extensión | 10.6 |
| 91 | Metodología en cuatro fases y transparencia metodológica | 10.7 |
| 92 | Clasificación de hallazgos | 10.8 |
| 93 | Documentación de no conformidades (cuatro pasos) | 10.9 |
| 94 | Requisitos de la evidencia objetiva | 10.10 |
| 95 | Redacción técnica: características y errores | 10.11 |
| 96 | Pausa activa "El filtro del auditor" | 10.12 |
| 97 | Conclusiones y recomendación (cuatro componentes) | 10.13 |
| 98 | Anexos A a D | 10.14 |
| 99 | Control de versiones: codificación y registro de cambios | 10.15 |
| 100 | Revisión y aprobación interna en cuatro niveles | 10.16 |
| 101 | Confidencialidad y protección de datos (cinco elementos) | 10.17 |
| 102 | Errores críticos que invalidan un informe | 10.18 |
| 103 | Herramientas digitales y beneficios de la digitalización | 10.19 |
| 104 | Mejora continua del proceso de reporte; pregunta de cierre | 10.20 |
| 105 | Bibliografía del tema | 10.3, 15 y Referencias |

### A.9 Actividad 2.4.2 Preparación y presentación de un informe de certificación

| # | Contenido | Sección |
|---|---|---|
| 106 | Resumen ejecutivo: dictamen y alcance | 11.1 y 11.6 |
| 107 | Métricas de ejecución (50, 48, 42, 4, 2) | 11.2 |
| 108 | Gestión de defectos: críticos, mayores, menores; regla de no certificación | 11.3 |
| 109 | Matriz de trazabilidad | 11.1 y 7.4 |
| 110 | Evaluación de riesgos: mitigados y aceptados | 11.4 |
| 111 | Conclusión y recomendación final | 11.5 |

### A.10 Evaluación 2 (EP3 y EP4) y herramientas del laboratorio

| # | Contenido | Sección |
|---|---|---|
| 112 | Indicadores de logro y ponderaciones | Objetivos y 14.1 |
| 113 | Contenido del encargo EP3 y formato de entrega | 14.2 |
| 114 | Formato oficial del informe y escala de criticidad (Crítico, Grave, Moderado, Leve) | 14.2 y 9.5 |
| 115 | Rúbrica EP3 | 14.3 |
| 116 | Contenido y rúbrica de la presentación EP4 | 14.4 y 14.5 |
| 117 | Herramientas del laboratorio: SonarQube, ZAP, Burp Suite, Nikto, SQLMap, John the Ripper, JMeter, Selenium | 12.1 y 12.2 |

**Resultado de la verificación:** los 117 contenidos identificados en la unidad están desarrollados en la guía.

---

## Anexo B. Autoevaluación final

Cada afirmación debe poder explicarse sin consultar el material.

**Estrategia y plan (IL2.1)**

- [ ] Distingue estrategia, nivel, tipo y técnica con un ejemplo de cada uno.
- [ ] Enumera los elementos del plan y su contenido.
- [ ] Define criterios de entrada, salida y suspensión para un ciclo.
- [ ] Prioriza módulos con una matriz de probabilidad e impacto.
- [ ] Explica por qué un entorno Docker versionado es condición de validez de los resultados y nombra cuatro buenas prácticas de seguridad en imágenes.

**Casos de prueba (IL2.2)**

- [ ] Redacta un caso completo con todos los campos del formato EP3.
- [ ] Aplica partición de equivalencia, valores límite y tablas de decisión a un requisito.
- [ ] Calcula V(G) y explica su efecto en el número de casos.
- [ ] Construye una matriz de trazabilidad y calcula la cobertura.

**Análisis estático (IL2.3)**

- [ ] Explica la diferencia entre análisis estático y dinámico, y entre SAST y DAST.
- [ ] Interpreta el panel de SonarQube: bugs, vulnerabilidades, Security Hotspots, code smells, cobertura y duplicación.
- [ ] Explica por qué un Quality Gate aprobado no garantiza seguridad en un proyecto heredado.
- [ ] Relaciona un problema de SonarQube con OWASP Top 10:2025, con el ERS y con una norma.

**Ejecución (IL2.4)**

- [ ] Describe la secuencia *smoke test* → ejecución → bitácora → reporte de defecto → resumen.
- [ ] Clasifica un defecto con la escala del formato EP3 y distingue severidad de prioridad.
- [ ] Calcula porcentajes de ejecución y de aprobación declarando la base.

**Informe (IL2.5)**

- [ ] Elige un dictamen y lo fundamenta con métricas y criterios de aceptación.
- [ ] Redacta una no conformidad con descripción, evidencia, referencia normativa y clasificación.
- [ ] Distingue riesgos mitigados de riesgos aceptados.
- [ ] Identifica los estándares de certificación y su edición vigente.

**Ética y normativa**

- [ ] Cita al menos tres normas con artículo e indica a quién obligan.
- [ ] Distingue lo vigente de lo que entrará en vigencia (Ley 21.719, 01-12-2026).
- [ ] Identifica la normativa sectorial del dominio del caso.
- [ ] Explica los límites éticos del uso de herramientas de seguridad.

**Evaluaciones**

- [ ] Conoce la exigencia de cada criterio de las rúbricas EP3 y EP4 y dónde se demuestra.
- [ ] Puede exponer el trabajo completo del grupo en 10 minutos.
