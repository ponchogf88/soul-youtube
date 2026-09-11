# REGLAS MAESTRAS DE PRODUCCIÓN Y STACK TECNOLÓGICO

Estas reglas son de cumplimiento **OBLIGATORIO** para todos los agentes involucrados en la producción y publicación de videos de los canales espirituales.

## 1. APROBACIÓN OBLIGATORIA (REGLA DEL SAMPLE DE 10 SEGUNDOS)
- **Prohibido publicar automáticamente:** Ningún video puede ser publicado o programado en YouTube sin la aprobación explícita del humano.
- **Sample de Validación:** Antes de renderizar el video completo o publicarlo, los agentes **DEBEN generar y mostrar un sample de 10 segundos** del video.
- **Criterios a evaluar en el sample:** El humano revisará el ritmo (cadencia), el volumen de la voz y música, la tipografía y colores de los subtítulos, y la composición visual general.
- **Flujo:** Solo tras recibir el "OK" explícito del humano sobre el sample de 10 segundos, se procederá a la renderización total y publicación.

## 2. STACK TECNOLÓGICO OFICIAL
El equipo de agentes tiene conocimiento y debe operar utilizando el siguiente stack tecnológico de generación:
- **Diseño y Miniaturas:** Microsoft Designer y Canva Business (con automatización Bulk Create).
- **Generación de Voz y Avatares/Video:** ElevenLabs (para voces inmersivas y emotivas) y HeyGen.
- **Orquestación y Flujos:** n8n, scripts de Python, y LaunchAgents (macOS).

## 3. GESTIÓN DE APIs Y CERO PAROS DE PRODUCCIÓN
- **Repositorio de APIs:** Existen 6 API Keys de contingencia documentadas en el archivo `apis.txt` (buscar en el sistema o espacio de trabajo).
- **Regla de Continuidad ("No hay paro por recursos"):** Si una API de pago (ej. ElevenLabs, HeyGen) agota su saldo o cuota, **LA PRODUCCIÓN NO SE DETIENE**. 
- **Alternativas y Fallbacks:** Los agentes deben buscar de forma autónoma opciones alternativas de generación. Siempre existen otras opciones gratuitas o de respaldo, incluyendo el uso de la API de **Google AI Studio** y el **Lab de Pomelli** para las campañas de difusión y generación. El objetivo es mantener el cronograma de publicaciones a toda costa sin bloqueos.
