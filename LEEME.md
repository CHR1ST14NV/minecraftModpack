# Modpack del Servidor de los cuates

Minecraft Java 1.21.1 con NeoForge. Los mods se bajan y se actualizan solos cada vez que abrís el juego.

## Para jugar (una sola vez)

1. Instalá **Prism Launcher** desde [prismlauncher.org](https://prismlauncher.org) e iniciá sesión con tu cuenta de Microsoft (Minecraft original).
2. En Prism: **Agregar instancia → Importar** y pegá este enlace:

   ```
   https://github.com/CHR1ST14NV/minecraftModpack/raw/main/instancia/servidorDeLosCuates.zip
   ```

3. Abrí la instancia **Servidor de los cuates**. La primera vez baja los mods (aparece una ventanita de progreso).
4. En **Multijugador** ya está el servidor cargado: **Servidor de los cuates**. Dale a Unirse.

Desde ahí, cada vez que abras el juego se ponen al día los mods solos.

## Notas

- La instancia ya viene con 6 GB de RAM. Si tu PC tiene 8 GB o menos, bajalo a 4 GB
  (clic derecho a la instancia → Editar → Ajustes → Memoria).
- Podés agregar mods propios que sean solo visuales (shaders, minimapa) en la carpeta `mods` de tu instancia.
- Si un día no conecta, cerrá el juego y volvé a abrirlo para que se actualicen los mods.

## Para Christian: cambiar mods

Los mods están en `mods/*.pw.toml` y se manejan con [packwiz](https://packwiz.infra.link):

```
packwiz mr add nombre-del-mod     # agregar desde Modrinth
packwiz remove nombre-del-mod     # quitar
packwiz update --all              # actualizar todos
```

Un mod que solo necesita el servidor lleva `side = "server"` en su `.pw.toml`; uno solo de jugadores, `side = "client"`.
Después: commit y push. Los jugadores lo reciben al abrir el juego; el servidor, con `ACTUALIZAR.bat`
o en su próximo reinicio.
