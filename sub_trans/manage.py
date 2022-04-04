from deep_translator import GoogleTranslator

# Set up a translator to translate English to Persian
translated = GoogleTranslator(source="en", target="fa")


def create_srt(filename):
    """Translate subtitle text and create new subtitles

    Args:
        filename (text): Make a file with the previous subtitle name with the extension (Fa)
    """

    lines = read_text_srt(filename)

    num = lines[::3]  # Separation of numbers
    time = lines[1::3]  # Time separation
    fa_text = translated.translate("\n".join(lines[2::3])).split(
        "\n"
    )  # Text translation
    # Create subtitle file
    with open(f"{filename}Fa.srt", "w+", encoding="utf-8") as file:
        for i, text in enumerate(fa_text):
            file.write(num[i] + "\n" + time[i] + "\n" + text + "\n")


def read_text_srt(filename):
    """Open the subtitle file and identify its phrases

    Args:
        filename (string): Subtitle file name

    Returns:
        list: List of phrases in the subtitle, respectively, number, time and subtitle text
    """
    with open(f"{filename}.srt", "r") as srt:
        srt_lines = srt.readlines()
    srt_clear_lines = list(
        filter(None, [srt_line.replace("\n", "").strip() for srt_line in srt_lines])
    )
    return srt_clear_lines


# Read existing files for translation
with open("sub_path.txt") as file:
    filepath = file.readlines()

# Translate files
for file in filepath:
    file = file.replace("\n", "")
    create_srt(rf"{file}")
