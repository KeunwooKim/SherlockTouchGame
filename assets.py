import os

# --- 이미지 경로 설정 ---
IMAGE_DIR = "image"
IMAGES = {
    "lobby": os.path.join(IMAGE_DIR, "셜록 배경.jpg"),
    "holmes": os.path.join(IMAGE_DIR, "holmes.png"),
    "watson": os.path.join(IMAGE_DIR, "watson.png"),
    "peterson": os.path.join(IMAGE_DIR, "peterson.png"),
    "goose": os.path.join(IMAGE_DIR, "goose.png"),
    "hat": os.path.join(IMAGE_DIR, "hat.png"),
    "jewel": os.path.join(IMAGE_DIR, "jewel.png"),
    "baker": os.path.join(IMAGE_DIR, "baker.png"),
    "braxton": os.path.join(IMAGE_DIR, "braxton.png"),
    "ryder_1": os.path.join(IMAGE_DIR, "ryder_1.png"),
    "ryder_2": os.path.join(IMAGE_DIR, "ryder_2.png"),
    "ryder_crouch": os.path.join(IMAGE_DIR, "ryder_crouch.png"),
    "street": os.path.join(IMAGE_DIR, "거리배경.jpg"),

    "brexton_store": os.path.join(IMAGE_DIR, "브렉스톤가게배경.jpg"),
    "windigate_farm": os.path.join(IMAGE_DIR, "윈디케이트가게.jpg"),
}

# --- 사운드 경로 설정 ---
SOUND_DIR = "sound"
SOUNDS = {
    "click": os.path.join(SOUND_DIR, "click.mp3"),
    "main_theme": os.path.join(SOUND_DIR, "under-the-london-fog-v1-inspired-by-sherlock-holmes-270425.mp3"),
    "investigation_theme": os.path.join(SOUND_DIR, "05. Puzzles.mp3"),
    "emotional_theme": os.path.join(SOUND_DIR, "silent-snowlight-gentle-christmas-piano-amp-bells-421460.mp3"),
    "confrontation_theme": os.path.join(SOUND_DIR, "into-the-danger-zone-382994.mp3"),
    "street_ambience": os.path.join(SOUND_DIR, "street-market-gap-france-24951.mp3"),
    "door_open": os.path.join(SOUND_DIR, "sound-effect-creaking-door-01-271987.mp3"),
}
