import streamlit as st
from audio_recorder_streamlit import audio_recorder
import replicate
import base64

print("Audio starting")

audio_bytes = audio_recorder(
    text="",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="user",
    icon_size="6x",
    pause_threshold=0.5
#    sample_rate=41_000
)
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    data = base64.b64encode(audio_bytes).decode('utf-8')
    audio = f"data:application/octet-stream;base64,{data}"

    input = {
        "audio": audio,
#        "audio": "https://replicate.delivery/pbxt/Js2Fgx9MSOCzdTnzHQLJXj7abLp3JLIG3iqdsYXV24tHIdk8/OSR_uk_000_0050_8k.wav",
        "batch_size": 64
    }

    output = replicate.run(
        "vaibhavs10/incredibly-fast-whisper:3ab86df6c8f54c11309d4d1f930ac292bad43ace52d10c80d87eb258b3c9f79c",
        input=input
    )
    print(output)
#    with open ("temp_audio_file.wav", mode="wb") as recorded_data:
#        recorded_data.write(audio_bytes)
