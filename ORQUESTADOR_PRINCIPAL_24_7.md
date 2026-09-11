# Informe de Orquestación Principal
## Canal YouTube 24/7 — música para concentración y sueño

**Fecha:** 10 de septiembre de 2026  
**Proyecto auditado:** `/Users/imac/Desktop/Projects/FACELESS_STREAMING_24_7_YOUTUBE_TIKTOK`  
**Rol:** Orquestador principal de arquitectura, producción, QA y despliegue.

## Veredicto actual

El proyecto tiene documentación, calendario, dashboard, miniaturas, script FFmpeg y servicio `systemd`. El repositorio local está limpio y sincronizado con GitHub. Sin embargo, no contiene el `master_stream.mp4` que debe existir en el VPS y no hay evidencia de una emisión real en producción.

**Estado: infraestructura preparada; emisión 24/7 pendiente de demostrar.**

## Arquitectura objetivo

```text
Audio y visuales originales/licenciados
              ↓
Master H.264/AAC 1080p generado localmente
              ↓ SFTP/rsync
VPS Ubuntu + usuario stream + systemd
              ↓
YouTube Live RTMP 16:9
              ↓
Logs + health-check + reinicio + revisión humana
```

TikTok vertical queda para una fase posterior, después de validar que el recorte no destruya sujetos ni textos.

## Antigravity 2.0 como herramienta principal

Antigravity 2.0 será el agente principal de implementación porque puede razonar sobre el workspace, inspeccionar y modificar archivos, ejecutar código y pruebas, crear artefactos y utilizar navegador para tareas web. Su documentación oficial también indica que las acciones sensibles del navegador requieren permiso.

Uso asignado:

1. Auditoría del repositorio y del VPS.
2. Cambios pequeños en FFmpeg, Bash y `systemd`.
3. Pruebas con `bash -n`, `ffprobe`, logs y simulaciones.
4. Creación de checklists y evidencia.
5. Asistencia en YouTube Studio, deteniéndose para login, SMS, claves, pagos y publicación.

Nunca se introducirán contraseñas, tokens o claves RTMP en prompts, Git, PDFs o capturas.

## Seis fases de ejecución

### Fase A — Master de prueba

Crear un master de 60 minutos con audio original o licencia verificable, visuales propios/licenciados, miniatura y metadata. Cierre: `ffprobe` confirma duración, 1920×1080, 30 fps, H.264 y AAC.

### Fase B — Seguridad del software

Usar usuario sin privilegios, archivo `/home/stream/.env` con permisos 600, rechazo de placeholders, logs y reinicio automático. Cierre: el servicio arranca sin exponer secretos.

### Fase C — VPS

Instalar FFmpeg, crear `/home/stream/media`, transferir el master, instalar el servicio y comprobar permisos. Cierre: `systemctl status livestream` sin errores.

### Fase D — Primera emisión

Emitir como privada o no listada durante 60 minutos. Verificar continuidad, audio, resolución, bitrate y logs. Cierre: evidencia de transmisión observada.

### Fase E — Operación 24/7

Habilitar el servicio, probar reinicio, documentar recuperación y establecer revisión diaria. Cierre: reinicio automático comprobado.

### Fase F — Escalamiento

Añadir segundo master, rotación de contenido, versión vertical y automatizaciones. Cierre: dos masters validados y procedimiento de reemplazo.

## Prompt maestro para Antigravity

```text
Actúa como ingeniero principal del proyecto faceless-streaming-24-7.
Trabaja SOLO en la fase indicada. Antes de modificar archivos:
1) inspecciona el estado real;
2) enumera archivos a cambiar;
3) explica riesgos;
4) ejecuta cambios reversibles;
5) corre pruebas;
6) entrega evidencia y criterio de cierre.

No inventes VPS, emisiones, credenciales, archivos ni resultados.
Nunca solicites ni escribas secretos en texto. Si una acción requiere login,
SMS, stream key, pago o publicación, detente y dame instrucciones exactas.
No avances de fase hasta que escriba FASE COMPLETADA.

FASE ACTUAL: [A/B/C/D/E/F]
OBJETIVO: [una sola frase]
CRITERIO DE CIERRE: [evidencia verificable]
```

## Riesgos corregibles detectados

- El script conserva un placeholder para la clave de YouTube.
- El servicio versionado usa `User=root`, mientras el instalador crea `stream`.
- El servicio no declara un `EnvironmentFile` seguro.
- El README todavía recomienda editar el script con la clave.
- No hay master local dentro del repositorio 24/7.

## Secuencia corregida de lanzamiento

Antes del master largo haremos un piloto corto:

1. **Piloto de 15 minutos:** validar audio, visuales, volumen, continuidad, textos y estética.
2. **Master de 60 minutos:** extender únicamente el piloto aprobado; no se publica el piloto como emisión 24/7 definitiva.
3. **Prueba privada de 60 minutos en YouTube:** comprobar RTMP, bitrate, estabilidad y recuperación.
4. **Emisión 24/7:** activar solo después de aprobar la prueba.

## Próxima acción

Ejecutar únicamente la Fase A-1: seleccionar o ensamblar el piloto de 15 minutos y validarlo. Después se generará el master largo y se aplicará el endurecimiento del servicio.

**Responsable de orquestación:** Codex, con Antigravity 2.0 como herramienta principal de implementación y el usuario como aprobador de autenticaciones y publicaciones.
