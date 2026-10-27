# Repaso de formato — informe EP3

**Revisora:** Skarlett Tropan  
**Fecha:** 27 de octubre de 2026  
**Archivo:** `docs/Evaluaciones/EV2/EV2 Contexto/Entregables/EP3-Informe-Cuidarte-Mas-avance.docx`  
**Pauta:** títulos en Arial, cuerpo en Arial, portada con los cuatro integrantes, y ningún «Pendiente» en el PDF de la defensa.

## Qué ya cumple

La fuente del documento es Arial. En `word/document.xml` las marcas `w:ascii` y `w:hAnsi` apuntan a Arial (3278 atributos) y no aparece Courier. La portada ya nombra a los cuatro integrantes. Las secciones 1, 2, 3, 4, 5.4, 6.1 a 6.3, 6.5, 6.7, 8 y el Anexo A no tienen marca de pendiente.

Las capturas que esta parte tiene que citar ya están en el repo:

| Uso | Carpeta |
|-----|---------|
| §5.4 SonarQube, 20 oct | `EV2 Contexto/Entregables/capturas-sonar/` (10 png) |
| CP-06 y CP-22, ciclo 2 | `EV2 Contexto/Entregables/capturas-ciclo2/` |

## Qué impide exportar el PDF

El mismo XML tiene **40** veces la palabra Pendiente, después de cerrar lo de Skarlett. El Anexo B ya cita `capturas-sonar` y `capturas-ciclo2`. Sigue pendiente la cita de las capturas de Nicolás y de Ari.

Antes de exportar, cada pendiente pasa a un resultado o a «No ejecutado», con la fecha. No se borran filas.

| Sección | Pendientes | Quién lo cierra |
|---------|------------|-----------------|
| 5.1, tablas 21 y 22 | 7 | Nicolás, con su bitácora y la de Ari |
| 5.2, Tabla 24 | 16 | Nicolás (sus 10 casos y CP-04), Ari (CP-04, 05, 15, 19, 21), Giannina (CP-23). CP-17 ya está en Fallido. |
| 5.3, Tabla 26 | 12 | Ari cierra el resto. Ya están INC-06, INC-11, INC-12, INC-14 e INC-16. |
| 6.4 y 6.6 | 2 | Giannina, cuando 5.3 tenga resultados |
| 7 | 1 | Giannina |
| Anexo B | 1 | Quien integre: citar `capturas-sonar`, `capturas-ciclo2` y las carpetas `Evidencias` de Nicolás y de Ari |

De la Tabla 24, las filas de Skarlett que ya tienen resultado son CP-06, CP-14, CP-16, CP-17, CP-18, CP-20 y CP-22.

## Al pasar a PDF

1. CP-17 y el relato de la sección 5 ya están en el Word. No volver a dejar esa fila en «Pendiente».
2. Aplicar las correcciones de §3.4 y la columna Resultado de §5.3.
3. Volver a buscar «Pendiente». Tiene que dar cero.
4. Exportar desde Word, no desde una copia anterior al 20 de octubre. El archivo vigente es `EP3-Informe-Cuidarte-Mas-avance.docx`.
