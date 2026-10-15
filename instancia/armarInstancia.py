"""Arma servidorDeLosCuates.zip: la instancia de Prism Launcher que importan los jugadores.

Uso: python3 instancia/armarInstancia.py
La instancia sincroniza los mods con pack.toml cada vez que se abre el juego
y trae el servidor ya cargado en la lista de multijugador.
"""
import io
import json
import pathlib
import struct
import zipfile

URL_PACK = "https://raw.githubusercontent.com/CHR1ST14NV/minecraftModpack/main/pack.toml"
NOMBRE = "Servidor de los cuates"
DIRECCION = "ambulance-saturn.tun.ply.gg"
VERSION_MINECRAFT = "1.21.1"
VERSION_NEOFORGE = "21.1.262"
RAM_MAXIMA_MB = 6144

AQUI = pathlib.Path(__file__).resolve().parent


def nbt_texto(nombre, valor):
    datos = valor.encode("utf-8")
    nombre_bytes = nombre.encode("utf-8")
    return b"\x08" + struct.pack(">H", len(nombre_bytes)) + nombre_bytes + struct.pack(">H", len(datos)) + datos


def servers_dat():
    """Lista de servidores de Minecraft (NBT sin comprimir) con un solo servidor."""
    servidor = nbt_texto("name", NOMBRE) + nbt_texto("ip", DIRECCION) + b"\x00"
    lista = b"\x09" + struct.pack(">H", 7) + b"servers" + b"\x0a" + struct.pack(">i", 1) + servidor
    return b"\x0a" + struct.pack(">H", 0) + lista + b"\x00"


def instance_cfg():
    return "\n".join([
        "[General]",
        "ConfigVersion=1.2",
        "InstanceType=OneSix",
        f"name={NOMBRE}",
        "iconKey=default",
        "OverrideCommands=true",
        f'PreLaunchCommand="$INST_JAVA" -jar packwiz-installer-bootstrap.jar {URL_PACK}',
        "OverrideMemory=true",
        "MinMemAlloc=2048",
        f"MaxMemAlloc={RAM_MAXIMA_MB}",
        "",
    ])


def mmc_pack():
    return json.dumps({
        "components": [
            {"important": True, "uid": "net.minecraft", "version": VERSION_MINECRAFT},
            {"uid": "net.neoforged", "version": VERSION_NEOFORGE},
        ],
        "formatVersion": 1,
    }, indent=2) + "\n"


def main():
    destino = AQUI / "servidorDeLosCuates.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as archivo:
        archivo.writestr("instance.cfg", instance_cfg())
        archivo.writestr("mmc-pack.json", mmc_pack())
        archivo.write(AQUI / "packwiz-installer-bootstrap.jar", ".minecraft/packwiz-installer-bootstrap.jar")
        archivo.writestr(".minecraft/servers.dat", servers_dat())
    print(f"Listo: {destino}")


if __name__ == "__main__":
    main()
