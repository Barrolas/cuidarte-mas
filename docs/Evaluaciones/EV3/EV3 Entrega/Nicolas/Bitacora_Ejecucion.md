# Bitácora de ejecución — Nicolás Barra (EV3 / EP5)

**Branch:** `feature/nicolas-ev3`  
**Ambiente:** Docker FE `:3333` / API `:4444`  
**Backlog:** [`BACKLOG.md`](./BACKLOG.md)

| Fecha | Item | Herramienta | Resultado | Evidencia | INC | Notas / norma |
|-------|------|-------------|-----------|-----------|-----|---------------|
| 2026-11-12 | Setup rama + herramientas | Git / winget / pip | En curso | — | — | Rama `feature/nicolas-ev3` desde `dev`; suite Selenium copiada a EV3; venv; Wireshark Windows; Docker Desktop iniciado |
| | EV3-00 Baseline Selenium | pytest | Pendiente | Evidencias/Selenium/EV3-00-* | — | Correr cuando Docker esté healthy |
| | EV3-01…07 | — | Pendiente | — | INC-01…14 | Remediación tras baseline |

## Mapa técnico (pre-remediación)

| INC | Archivos a revisar |
|-----|--------------------|
| INC-01 | `BACKEND/src/routes/auth.js`, seeds usuarios |
| INC-02 | secreto JWT / `.env` / README |
| INC-03 | logout FE + middleware auth API |
| INC-07 | router `roles` |
| INC-13 | descarga documentos → auditoría |
| INC-14 | `POST` auditoría |
