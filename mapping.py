from skills import browser_cmds
from skills import system_cmds



# === СЛОВНИК КОМАНД ===
COMMANDS_MAP = {
    "музик": browser_cmds.play_youtube_music,
    "ютуб": browser_cmds.play_youtube_music,
    "погод": browser_cmds.open_weather,

    #тестування нових команд
    "гучніш": system_cmds.volume_up,
    "тихіш": system_cmds.volume_down,
    "тихш": system_cmds.volume_down,
    "вимкни звук": system_cmds.mute_volume,

    #команди на відкриття програм та ігор
    "попрацю": system_cmds.start_work,
    "код": system_cmds.start_work,
    "погра": system_cmds.open_game,
    "ліг": system_cmds.open_game,
    #......
}