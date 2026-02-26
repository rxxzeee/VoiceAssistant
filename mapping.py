from skills import browser_cmds
from skills import system_cmds
from skills import talk_cmds

# === СЛОВНИК КОМАНД ===
COMMANDS_MAP = {
    #запуск сайтів
    "музик": browser_cmds.play_youtube_music,
    "ютуб": browser_cmds.open_youtube,
    "відео": browser_cmds.open_youtube,
    "ролик": browser_cmds.open_youtube,
    "погод": browser_cmds.open_weather,
    "фільм": browser_cmds.watch_films,
    "спорт": browser_cmds.watch_sport_news,
    "їжа": browser_cmds.food_order_site,
    "їсти": browser_cmds.food_order_site,
    "їст": browser_cmds.food_order_site,
    "гіт хаб": browser_cmds.view_github_page,
    "гіт": browser_cmds.view_github_page,
    "навчан": browser_cmds.open_elearn,
    "навчат": browser_cmds.open_elearn,
    "понавч": browser_cmds.open_elearn,
    "по навч": browser_cmds.open_elearn,
    "стрім": browser_cmds.open_twitch,
    "трасляц": browser_cmds.open_twitch,
    "тревел": browser_cmds.watch_travel_channel,
    "подорож": browser_cmds.watch_travel_channel,
    #керування пк
    "гучніш": system_cmds.volume_up,
    "тихіш": system_cmds.volume_down,
    "тихш": system_cmds.volume_down,
    "вимкни звук": system_cmds.mute_volume,
    #запуск додатків
    "попрацю": system_cmds.start_work,
    "код": system_cmds.start_work,
    "погра": system_cmds.open_game,
    "ліг": system_cmds.open_game,
    #розмовні команди
    "привіт": talk_cmds.helloe,
    "прив": talk_cmds.helloe,
    "як справи": talk_cmds.howay,
    "як ти": talk_cmds.howay,
    "асистен": talk_cmds.wakeup
    #......
}