# EV56-09 — Evidencia INC-06 (corrida del 25-nov-2026)

Retest inicial, antes y después del fix, sobre `dev` (`2d0abc7`) y la rama local `sk/inc-06-errores` (`f8e2786`). El retest vigente en la rama final (27-nov) está en [`../EV56-20/`](../EV56-20/README.md), que se conserva tal cual.

| Archivo | Contenido |
|---------|-----------|
| `2026-11-25_cp17-antes.png` | Terminal del 25-nov: cinco endpoints en `dev` devolvían `invalid input syntax for type bigint` al cliente |
| `cp17_antes_dev_curl.txt` | Salida `curl` antes del fix |
| `cp17_despues_fix_curl.txt` | Salida `curl` después del fix (`f8e2786`): HTTP 500 genérico, 401/403 genéricos |
| `cp17_despues_backend_logs.txt` | Extracto de `docker logs`: código `22P02` queda en el servidor |

Bitácora: [`../../Entregables/EV56-09-INC-06-Resumen-Bitacora.md`](../../Entregables/EV56-09-INC-06-Resumen-Bitacora.md).
