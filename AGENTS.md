# Instrucciones para agentes

Conservar la estructura documentada en README.md y ejecutar las verificaciones antes de publicar.

Los commits deben usar la identidad humana configurada por el responsable. No agregar identidades de herramientas o modelos como autor, committer, Co-Authored-By, Signed-off-by ni firmas promocionales. No atribuir cambios a otra persona sin su autorización. Esta regla de metadatos no permite retirar ni minimizar la declaración de asistencia de IA del estudio.

Al iniciar trabajo en una copia nueva, activar `git config core.hooksPath .githooks`. Antes de publicar, ejecutar `python reproducibility/check_commit_metadata.py`. No desactivar los hooks para eludir esta verificación. Tras la republicación de septiembre de 2026, clonar de nuevo; no fusionar ni empujar las ramas del repositorio anterior.

Preservar los cinco autores científicos, sus contribuciones y la licencia. El primer commit de este repositorio es una publicación de una instantánea del trabajo conjunto, no una atribución individual de todo el desarrollo previo.

No publicar TEMPORAL/, submission/, results/private/, microdatos, bases individuales, correspondencia ni formularios firmados. No importar el historial Git del repositorio de origen. Los resultados municipales deben superar reproducibility/publication_privacy.py --check.

Verificaciones: python reproducibility/verify_repository.py y python reproducibility/test_publication_privacy.py. Toda regeneración del explorador usa analysis/25_explorador_html.py. No modificar modelos o resultados científicos como parte de una actualización de publicación.
