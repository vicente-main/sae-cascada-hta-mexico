# Historial de cambios

## v1.5.2 — 2026-09-29

- Incorporada la actualización de los autores del 28 de septiembre: 25 referencias en la versión SPM, fuentes directas de metodología de 2021 y pseudo-verosimilitud, precisión del comparador Campos-Nonato y de la analogía con VIH, y fuentes completas del suplemento.
- Sincronizados los generadores de S6 y del suplemento con los archivos actualizados, y registrados sus hashes. No se modifican las estimaciones propias, los modelos ni los datos del explorador.
- Restauradas la Tabla S8 y las aclaraciones ya aprobadas que se habían perdido en el suplemento actualizado; las celdas de S1-S7, las imágenes, la corrección de S6 y las dos referencias del suplemento se conservan.
- Nueva instantánea de publicación con identidad de Vicente en el commit inicial. Se conserva la autoría científica del equipo y la declaración de asistencia de IA. Los historiales anteriores y sus etiquetas quedan en respaldo local.
- Añadida verificación de metadatos de commits y hooks locales para detectar atribuciones automáticas a herramientas.

Las versiones anteriores describen los repositorios respaldados, no etiquetas importadas al nuevo historial.

## v1.5.1 — 2026-09-27

- Publicación independiente en `vicente-main/sae-cascada-hta-mexico`, a partir del estado final del repositorio de origen. El commit inicial corresponde a Vicente Jesús Vílchez-Díaz; se conservan todos los autores científicos y la declaración de asistencia de IA.
- Actualizados enlaces del repositorio, dashboard, manuscrito y metadatos de citación. No se importan commits, etiquetas, firmas automáticas ni archivos privados del historial anterior.
- Incorporada la corrección posterior a v1.5: el comparador de Resultados se describe como promedio ponderado de entrenamiento, de acuerdo con Métodos.
- Corregidas dos notas obsoletas del README: la supresión también rige en los archivos y la versión de publicación ya está definida. Los resultados, datos y figuras del estado de origen no cambian.
- La procedencia y equivalencia de archivos se registran en `reproducibility/PROVENANCE.md` y `repository_migration.csv`. Las entradas siguientes describen versiones del repositorio de origen, no etiquetas disponibles aquí.

## v1.5 — 2026-09-21

- Confirmado por el responsable el alcance de la supresión: se omiten estimación, intervalos, ancho y n exacto en todas las salidas municipales con denominador menor que 10. Aplicado a 29 CSV, JSON/HTML, datos de figuras y figuras de validación/incertidumbre. Se conservan identificadores y marcas de supresión.
- Los originales analíticos se conservan localmente en una ruta privada ignorada; los modelos y los resúmenes estadísticos agregados no cambian. El paso final del pipeline aplica la política y CI detecta regresiones.
- Retirada la comunicación temporal del árbol publicado e incorporada `/TEMPORAL/` a `.gitignore`. No forma parte de `v1.5`. Las firmas fueron confirmadas por el responsable; no se publican formularios privados.

- Integradas las decisiones de los autores hasta `bbbc4fe`: estimando condicional estandarizado y nombres completos; actualizados también los metadatos de citación.
- Ejecutada la corrección del comparador de validación con entrenamiento exclusivo en cada pliegue. Se conservan predicciones BYM2, observados y pliegues; no se reajusta INLA. Actualizados detalle, resumen, estratos, Tabla S1 y Figura S1.
- Añadida la Tabla S8 de características y faltantes por denominador, con generador, CSV, Excel y referencias STROBE.
- Publicado el generador del suplemento y reconstruido el Word. Verificadas celda a celda las tablas previas S2-S7; permanecen sin cambios.
- Armonizada la interpretación en objetivos, resúmenes, texto, Figura 2 y explorador; corregida la descripción del ancho del intervalo y retirada la cita del análisis de efectos compartidos no realizado.
- Actualizados manifiestos, registro de validación técnica y `reproducibility/publication_privacy.json`. Se conservan las etiquetas históricas; los cambios de publicación no reescriben objetos Git anteriores.

## Sin publicar — 2026-09-20

- Integradas las correcciones hasta `d1a6e14`: motivo de pobreza faltante en la fuente, precisión del checklist y notas de KS/conectividad en el suplemento. Se mantiene la comunicación temporal incorporada en `main`.
- Restauradas las exclusiones de `_TRABAJO_INTERNO/`, notas internas, insumos y generadores heredados que pueden permanecer al actualizar una copia antigua. Los PDF heredados en la raíz se ignoran; se permiten documentos propios bajo `manuscript/`.
- Integradas las correcciones de los autores de `147d9ef` y `23d0ccd`: panel B de S2, etiquetas y nota de S4, años de S3, p de Moran, ubicaciones STROBE y dos aclaraciones del manuscrito. Se conserva exactamente el contenido publicado por los autores; la integración no acredita el cierre de las observaciones metodológicas.
- Organización en `analysis/`, `data/`, `results/`, `manuscript/` y `reproducibility/`; `docs/` conserva el explorador de GitHub Pages.
- Actualización de rutas y eliminación de las rutas personales del cálculo opcional de altitud.
- Incorporación al ejecutor de la Tabla S7 y de la construcción del HTML del explorador; validación de argumentos y listado de pasos.
- Documentación de insumos, límites de reproducción, migración e integridad.
- Los resultados numéricos, figuras y JSON del explorador conservan el contenido de `af9aacc`. El suplemento y el checklist incorporan las correcciones de `23d0ccd`, registradas como actualizaciones explícitas. No se reajustaron los modelos.
- Se reconstruyó el HTML desde la plantilla vigente: la página conservaba el recuento antiguo de 25 089 participantes, mientras la plantilla ya indicaba 25 088. Esta actualización y las del suplemento/checklist están registradas en `reproducibility/artifact_updates.csv`.

## Referencia de la entrega de septiembre de 2026

La reorganización parte de `af9aacc3a6d843356f6044caa479bbf0c12e024a` (2026-09-18).
En el repositorio de origen, `v1.4` es el objeto de etiqueta `ca627354c1a86c85183bb4e6ec1da217a89aea4e` y referencia el commit `2824cc3024c8e939cecb8fe76935e4e5b47a3b54`.
La corrección de Figura 1, la declaración del techo fisiológico y el detalle de herramientas de IA se incorporaron después de esa etiqueta. Las etiquetas históricas se conservan; el cierre editorial deberá citar una nueva versión o el commit exacto que acompañe al envío.
