# curseforge-modpack-downloader-python
Browser driver to download the mod.jar files from curseforge.

I made this because I wanted to try a modpack, I use linux. The curseforge app does not work for minecraft on linux.
This is for modpacks which file structure is on the lines of
modpack.zip    
    manifest.json
    modlist.html
    overrides
        config
            *files and directories*

must have selenium installed with pip
Instructions:
  1. Download the zip file for the modpack
  2. move the manifest.json file into the same directory as main.py
  3. run python3 main.py
  4. move the downloaded .jar files into the mods folder
  5. May need to move resource packs into the resource pack folder (no need to unzip)
  6. copy the contents config folder from the overrides folder into the config folder of the minecraft installation (.minecraft on linux)
 
Note, ensure you are using the correct version of forge and minecraft for the modpack. (you can see the recomended forge version in the manifest.json) Also, make sure minecraft is running with the correct jvm version.
