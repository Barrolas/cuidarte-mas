# EV56-18 — Evidencia SonarQube

Motor: `sonarqube:community` **26.11.0.134175**. Scanner: `sonarsource/sonar-scanner-cli` con `-Dsonar.sources=src -Dsonar.scm.disabled=true -Dsonar.qualitygate.wait=true`. Solo `localhost:9000`.

## Capturas (America/Santiago)

| Archivo | Qué muestra | SHA / fecha |
|---------|-------------|-------------|
| `2026-11-25_sonar-be-dev.png` | Backend overall, `dev` `2d0abc7` | 25-nov-2026: 4 vulnerabilidades, Security **E** |
| `2026-11-25_sonar-fe.png` | Frontend overall, mismo `dev` | 25-nov-2026: 14 bugs, 0 vulnerabilidades, Security **A** |
| `2026-11-27_sonar-be-dev-final.png` | Backend overall, `origin/dev` `5707693e2f7e9826d645800e89792533329e1b99` | 27-nov-2026 ~22:00 America/Santiago: 2 vulnerabilidades, Security **E** |
| `2026-11-27_sonar-fe-dev-final.png` | Frontend overall, mismo `5707693` | 27-nov-2026 ~22:00: 14 bugs, 0 vulnerabilidades, Security **A** (sin cambio vs EV2) |

El scan del 27-nov cubre lo ya mergeado en `dev` (**INC-04, INC-05, INC-06**). **No** incluye todavía los merges de Nicolás de **INC-01, INC-02 e INC-07**. Esa corrida final queda pendiente.

## JSON

`sonar_final_dev_*` = 27-nov sobre `5707693`. `sonar_dev_*` = 25-nov sobre `2d0abc7` (measures/qg). Las fechas internas del API de SonarQube están en UTC (`2026-11-28T01:00:47+0000` = 27-nov 22:00 America/Santiago).

Documento: [`../../Entregables/EV56-18-Retest-CP17-y-Sonar.md`](../../Entregables/EV56-18-Retest-CP17-y-Sonar.md).
