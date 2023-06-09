import os
from pydub import AudioSegment


def convert_wav_to_mp3(input_file, output_file):
    """
    Конвертирует файл WAV в MP3.

    Аргументы:
    input_file (str): Путь к исходному файлу WAV.
    output_file (str): Путь к выходному файлу MP3.
    bitrate (str): Битрейт выходного файла MP3 (по умолчанию '192k').

    """
    # Загружаем WAV-файл
    audio = AudioSegment.from_wav(input_file)

    # Конвертируем в MP3 и сохраняем
    audio.export(output_file, format='mp3')




