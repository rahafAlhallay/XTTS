import os
import torch
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig
from TTS.utils.io import load_fsspec

# Allowlist necessary classes for unpickling
torch.serialization.add_safe_globals([XttsConfig, XttsAudioConfig])

# Auto-agree to non-commercial license
os.environ["COQUI_TOS_AGREED"] = "1"

from TTS.api import TTS

# Load XTTS v2 model (ensure the model is pre-downloaded)
#tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
tts = TTS(model_path="/Users/rahafalhallay/Desktop/xtts/xtts_v2/", config_path="/Users/rahafalhallay/Desktop/xtts/xtts_v2/config.json", gpu=False)# Generate Arabic audio using speaker WAV
tts.tts_to_file(
    text = "مرحباً، معكم أحمد. يسعدني أن أكون معكم اليوم. دعونا نبدأ بسؤال بسيط: ما هو الشيء الذي يُلهمكم كل صباح؟ في عالم تتسارع فيه الأحداث، يصبح الابتكار أكثر من مجرد خيار... بل أسلوب حياة. نحن نعيش في وقت لا مكان فيه للجمود. من لا يتطور، يتراجع. لهذا، نسعى دائماً للتفكير خارج الصندوق، وتحويل الأفكار الجريئة إلى واقع ملموس. تخيلوا أن فكرة صغيرة اليوم، قد تكون مشروعاً رائداً غداً. وهنا يأتي دور العمل الجماعي، والتواصل، والمرونة في التكيف مع التغيير. أشكر لكم حسن استماعكم، وأتطلع إلى مشاركة رحلة الإبداع والتجديد معكم. لنبدأ الآن.",
    file_path="output(elavenlabs).wav",
    speaker_wav=["ElevenLabs_Text_to_Speech_audio.wav"],
    language="ar",
    split_sentences=True
)