# Manuscrito y suplemento

- `manuscript.md`: incorpora las decisiones de los autores hasta `bbbc4fe` y la revisión de cierre: estimando estandarizado, comparador de entrenamiento, Tabla S8 y precisiones editoriales. Conserva bloques `SOLO:BREVE` (SPM) y `SOLO:EXTENSA` (formato previo).
- `supplement/MATERIAL_SUPLEMENTARIO.docx`: reconstruido con el comparador corregido en S1, Figura S1 y nueva S8. S6 utiliza 29,1% como comparador de Campos-Nonato y documenta la discrepancia interna de esa fuente. El suplemento incluye sus dos referencias completas. Las demás tablas conservan las correcciones publicadas anteriormente.

El suplemento se reproduce con `analysis/21_material_suplementario.R`, incorporado y contrastado contra las tablas públicas. La fuente del manuscrito y los generadores privados de formularios son procesos distintos: esta rama no reconstruye las firmas ni acredita que el paquete de envío esté completo. Se generó un Word local de revisión con los generadores disponibles; su recuento se registra en `reproducibility/closure_validation.json`, sin sustituir la comprobación del Word final de los autores.

Los documentos de envío, contactos, cartas y declaraciones firmadas se mantienen fuera de Git o en `private/` y `submission/`, rutas ignoradas. La correspondencia del manuscrito público utiliza un marcador; no deben incorporarse firmas ni datos personales de contacto como parte de la reorganización.

La versión citada es `v1.5.2`: incluye el comparador corregido, S8 y la supresión en archivos, descargas y figuras. El responsable confirmó que las firmas están completadas; esos documentos permanecen en el paquete privado y no se redistribuyen aquí. Las etiquetas históricas del repositorio de origen no se importan; la procedencia se conserva en `reproducibility/PROVENANCE.md`.
