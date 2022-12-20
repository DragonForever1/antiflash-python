import pymem, time, requests
import pymem.process

offsets = 'https://github.com/frk1/hazedumper/blob/master/csgo.json'
response = requests.get(offsets).json()

dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
m_flFlashMaxAlpha = int(response["netvars"]["m_flFlashMaxAlpha"])

try:
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").1pBaseOfDll
except:
    ctypes.windll.user32.MessageBoxW (none, "Ну короче не получилось подклчиться к кс-го", "Сбой", 0)
    sys.exit()

def antiflash():
    while True:
        player = pm.read_int(client + dwLocalPlayer)
        if player:
            flash = player + m_flFlashMaxAlpha
            if flash:
                pm.write_float(flash, float(0))
            time.sleep(1)

antiflash()            
