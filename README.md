# Proyecto Vulnerable - Ataque "Billion Laughs" en PHP

⚠️ **¡ESTE PROYECTO ES INTENCIONALMENTE INSEGURO!**

Este repositorio contiene un ejemplo **intencionalmente vulnerable** al ataque [Billion Laughs](https://wh01s17.vercel.app/blog/Ciberseguridad/dos_-_billion_laughs_attack). Es utilizado únicamente con fines educativos, pruebas de concepto y laboratorios controlados.

---

## 📌 Descripción

El proyecto simula una API REST extremadamente simple (en PHP) que acepta una solicitud POST con datos XML y los procesa **sin protección** contra expansiones exponenciales de entidades.

Su propósito es demostrar cómo un mal uso del parser XML puede ser explotado para generar un **ataque de denegación de servicio (DoS)** conocido como *Billion Laughs*.

---

## 🔧 Requisitos

- PHP 7.4 o superior


No es necesario Apache/Nginx. Solo tienes que ejecutar el servidor integrado de PHP.

## ▶️ Instrucciones de uso
1. Levantar servidor

  ```bash
  php -S 0.0.0.0:8000
  ```

Esto levanta el servicio en:
  ```bash
  http://TU_IP:8000/index.php
  ```

2. Enviar petición vulnerable
Guarda el contenido de payload.xml y ejecuta:

```bash
curl -X POST http://TU_IP:8000/index.php -H "Content-Type: application/xml" --data-binary @payload.xml
```

La respuesta tomará mucho tiempo o provocará colapso del proceso php.

## 🛑 Advertencia final
⚠️ Este proyecto es SOLO para uso:

- Académico
- Investigación de seguridad controlada
- Prácticas en laboratorios aislados

**NUNCA debe utilizarse en sistemas públicos ni expuestos.**
