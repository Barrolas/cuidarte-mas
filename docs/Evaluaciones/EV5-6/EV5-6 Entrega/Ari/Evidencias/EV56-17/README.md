# EV56-17 — Wireshark bajo carga JMeter

**Estado:** capturas D (2500 VU) y E (5000 VU) archivadas.  
**Ejecutora:** Ari Araya  
**Relacionado:** EV56-13, ISO 25010 (desempeño / comportamiento bajo estrés)

Interfaz: **Adapter for loopback traffic capture** (Npcap). Filtro: `tcp.port == 4444`. Tráfico `127.0.0.1 ↔ 127.0.0.1` hacia la API Docker publicada.

## Archivos

| Archivo | Qué es |
|---------|--------|
| `EV56-17-faseD-2500.pcapng` | Captura fase D (~3:11–3:14). **No versionado** (≈1,6 GB; límite GitHub 100 MB). Queda en disco local. |
| `Wireshark-2500VU.png` | Lista TCP `:4444` durante D (~448 k paquetes) |
| `EV56-17-faseD-2500.png` | I/O Graph D: ~2–2,7 k pkt/s, ~180 s; **errores TCP ≈ 0** |
| `EV56-17-faseE-5000.pcapng` | Captura fase E (3:31–3:38). **No versionado** (≈2,9 GB). Queda en disco local. |
| `Wireshark-5000VU.png` | Lista + HTTP `GET /pacientes` 200 durante E |
| `EV56-17-faseE-5000.png` | I/O Graph E: ~2–3,5 k pkt/s, ~380 s; **errores TCP** visibles ~200–280 s |

## Lectura para Ninna

- Volumen: D ~448 k paquetes filtrados; E lista con HTTP 200 JSON (el API responde; JMeter error % = 0).
- D: I/O estable, línea roja de errores TCP en cero → cola de espera, no pérdida.
- E: aparecen **errores TCP** a mitad de prueba (retrans / desorden) mientras JMeter sigue en 0 % HTTP. Encaja con p95 GET ~14,5 s: el stack TCP se queja, la app no devuelve 5xx.
- No es INC-04 (el delay de 5 s ya no está).

DoD: anexo de red ligado a estrés **cumplido**.
