from pydub import AudioSegment
import os
from werkzeug.utils import secure_filename

def salvar_audio_validado(file, pasta_destino='audios'):
    if not file.filename.lower().endswith('.mp3'):
        return False

    filename = secure_filename(file.filename)
    caminho = os.path.join(pasta_destino, filename)

    # Salvar temporariamente para validar
    file.save(caminho)

    try:
        audio = AudioSegment.from_mp3(caminho)
        if len(audio) == 0:
            os.remove(caminho)
            return False
    except:
        os.remove(caminho)
        return False

    return True
