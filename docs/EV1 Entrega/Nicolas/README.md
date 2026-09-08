# Entregables de Nicolás (Cards 6–10)

Paquete técnico listo para integrar al informe Word/PDF de la EV1.

| Card | Archivo | Sección del informe |
|------|---------|---------------------|
| 6 | [Card06_Estrategia.md](./Card06_Estrategia.md) | §4 Estrategia |
| 7 | [Card07_Recursos_Cronograma.md](./Card07_Recursos_Cronograma.md) | §5 Recursos |
| 8 | [Card08_Casos_Funcionales.md](./Card08_Casos_Funcionales.md) | §6 CP-01…CP-03 |
| 9 | [Card09_Casos_Seguridad_Rendimiento.md](./Card09_Casos_Seguridad_Rendimiento.md) | §6 CP-04…CP-05 |
| 10 | [Card10_Usabilidad_Revision.md](./Card10_Usabilidad_Revision.md) | §6 CP-06 + insumos para Skarlett |

## Cómo usarlo

1. Copia el contenido de cada card a la sección correspondiente del informe grupal.
2. Entrega a Skarlett la tabla de trazabilidad de `Card10` (bloque “Insumos para matriz”).
3. Coordina con Skarlett el ensamblaje final (Card 1) y formato AVA.

## Endpoints reales usados en los casos

- `POST /autenticacion/login`
- `/usuarios`, `/pacientes`, `/examenes`, `/documentos`, `/auditoria`
- Swagger: `http://localhost:4444/docs`
- Frontend: `http://localhost:3333`
