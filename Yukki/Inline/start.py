from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP, THUMBNAIL
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="π Audio Quality", callback_data="AQ"),
            InlineKeyboardButton(text="π Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="π₯ Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="βοΈ Close", callback_data="close"),
        ],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π¨Official Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="π¨Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    buttons = [
        [
            InlineKeyboardButton(
                text="π Helper Commands Menu", callback_data="shikhar"
            ),
        ],
        [
            InlineKeyboardButton(
                "β Add me to your Group",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="π¨Updates Channel", url=f"{SUPPORT_CHANNEL}"
            ),
            InlineKeyboardButton(
                text="π¨Support Group", url=f"{SUPPORT_GROUP}"
            ),
        ],
    ]
    return f"π  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="π Audio Quality", callback_data="AQ"),
            InlineKeyboardButton(text="π Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="π₯ Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="βοΈ Close", callback_data="close"),
            InlineKeyboardButton(text="π Go Back", callback_data="open_start_menu"),
        ],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="π Reset Audio Volume π", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="π Low Vol", callback_data="LV"),
            InlineKeyboardButton(text="π Medium Vol", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="π High Vol", callback_data="HV"),
            InlineKeyboardButton(text="π Amplified Vol", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="π½ Custom Volume π½", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="π Go back", callback_data="settingm")],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="πΌCustom Volume πΌ", callback_data="AV")],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="π₯ Everyone", callback_data="EVE"),
            InlineKeyboardButton(text="π Admins", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="π Authorized Users Lists", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="π Go back", callback_data="settingm")],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="βοΈ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="πΎ Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="π» Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="π½ Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="π Go back", callback_data="settingm")],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons
