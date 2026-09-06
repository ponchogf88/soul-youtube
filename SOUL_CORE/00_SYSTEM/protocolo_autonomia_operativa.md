# PROTOCOLO DE AUTONOMÍA OPERATIVA — EL TEST DE LAS 2 HORAS

**Principio Fundamental:**
"Me voy durante 2 horas. Cuando regreso, la máquina no debe estar congelada esperando un clic o una aprobación."

---

## 1. PUNTOS DE FRICCIÓN IDENTIFICADOS Y SOLUCIÓN TÉCNICA

| Punto de Fricción | Causa Raíz | Solución Automática del Sistema |
|---|---|---|
| **"Do you want to proceed?"** | Scripts interactivos que esperan confirmación en terminal | Banderas automáticas de no-interactividad (`-y`, `--batch`, `DEBIAN_FRONTEND=noninteractive`, scripts desatendidos). |
| **Permisos / Sandbox** | Comandos que intentan tocar zonas protegidas o pedir sudo | Mantener toda la producción dentro del workspace `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL` y `/tmp` sin invocar sudo. |
| **Timeouts de procesos** | Tareas de renderizado largo que cortan la ejecución | Uso de procesos daemon en segundo plano (`IsDaemon: true` / `launchd` / `manage_task`) con sondeo pasivo. |
| **Suspensión de Mac (Sleep)** | El iMac entra en reposo y duerme los procesos | Control de energía local vía `caffeinate` durante renders pesados para evitar suspensión. |
| **APIs caídas o cuotas agotadas** | Falla de una key de ElevenLabs / HeyGen | Fallback automático a la siguiente clave documentada en `apis.txt` sin preguntar al usuario. |
| **Errores de síntesis o render** | Fallo de codec o timeout de red | `FAIL → REWORK INTERNO`: Reintento automático con parámetros secundarios (ej. render limpio en stillimage si falla concat complejo). |

---

## 2. LA REGLA HITL ESTRICTA (HUMAN-IN-THE-LOOP)
El agente **SOLO** tiene permitido marcar `HUMAN-IN-THE-LOOP REQUIRED` si:
1. Existe un bloqueo criptográfico o biométrico insalvable (ej. SMS 2FA bancario/Google que exige un dispositivo físico externo).
2. Se requiere decisión editorial o creativa suprema del Humano.

**TODO LO DEMÁS DEBE SER RESUELTO AUTÓNOMAMENTE POR EL AGENTE.**
