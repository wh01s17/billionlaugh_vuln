# "Billion Laughs Attack" en Python - Flask
> **Aviso importante:** este repositorio contiene una **aplicación deliberadamente vulnerable** para fines educativos (demostración de la vulnerabilidad *Billion Laughs* / expansión de entidades XML). **NO** la ejecutes en producción ni la expongas a redes públicas. Usa un entorno aislado (máquina virtual o contenedor) y datos controlados.

---

## Resumen
Aplicación Flask mínima que parsea XML utilizando `lxml` con protecciones desactivadas (`resolve_entities=True`, `no_network=False`, `huge_tree=True`) para ilustrar cómo funciona un ataque de *entity expansion* (Billion Laughs). 

---

## Estructura
- `app.py` — servidor Flask vulnerable.  
- `requirements.txt` — dependencias (`Flask`, `lxml`).  
- `payload.xml` — payload con expansión de entidades XML.

---

## Requisitos
- Python 3.11+ (o la versión que uses).  
- `pip`.
- Recomendado: entorno virtual (`venv`) o Docker.

---

## Instalación (recomendada en `venv`)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar (modo enseñanza — aislado)
```bash
python app.py
```

## Enviar bomba XML
```bash
curl -X POST http://TU_IP:8000/api -H "Content-Type: application/xml" --data-binary @payload.xml
```

La respuesta tomará mucho tiempo o provocará colapso del proceso php.

## 🛑 Advertencia final
⚠️ Este proyecto es SOLO para uso:

- Académico
- Investigación de seguridad controlada
- Prácticas en laboratorios aislados

**NUNCA debe utilizarse en sistemas públicos ni expuestos.**