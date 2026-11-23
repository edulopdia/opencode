# AGENTS.md

Alcance: solo este directorio (`/home/vespertino/opencode`).

## Estructura
- `PrimerPygame.py` — juego completo en un solo script plano (ventana 600x400, cuadrado rojo de 100x100, se mueve con flechas/WASD a `VELOCIDAD = 5`, con límites de ventana, 60 FPS).
- `test_PrimerPygame.py` — 12 pruebas unitarias, todas con mocks (no abren ventana).

## Punto crítico
- `PrimerPygame.py` **no tiene `main()` ni guarda `if __name__ == "__main__"`**: importarlo o ejecutarlo con `exec` inicia un bucle infinito `while True`. Nunca hacer `import PrimerPygame` directamente.
- Las pruebas lo evitan con `pygame` mockeado y rompiendo el bucle: `display.flip` lanza `StopIteration` tras 1 frame, y luego `exec(compile(...))` lo captura. Para pruebas nuevas, copiar el patrón de `cargar_y_ejecutar_un_frame()`.

## Comandos (ejecutar desde este directorio)
- Suite completa: `python3 -m unittest test_PrimerPygame -v`
- Una sola prueba: `python3 -m unittest test_PrimerPygame.TestPrimerPygame.<nombre> -v`
- El ayudante de pruebas abre `"PrimerPygame.py"` con ruta relativa — el cwd debe ser este directorio.
- No ejecutar `python3 PrimerPygame.py` en sesiones headless/CI (abre una ventana real y nunca termina). Solo ejecutarlo si el usuario pide jugar explícitamente.

## Convenciones
- Única dependencia: `pygame` (verificado 2.6.1). Sin archivo de requisitos ni config de venv.
- Identificadores y comentarios en español (`ventana`, `teclas`, `VELOCIDAD`); mantener ese estilo.
