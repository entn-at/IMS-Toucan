from FastSpeech2.FastSpeech2 import show_spectrogram as fact_spec
from InferenceInterfaces.GermanSingleSpeakerTransformerTTSInference import GermanSingleSpeakerTransformerTTSInference
from TransformerTTS.TransformerTTS import show_spectrogram as trans_spec, show_attention_plot

if __name__ == '__main__':
    show_attention_plot("Die drei Segel glitten wie senkrechte Papierwände über das abendglatte Wasser.")
    trans_spec("Die drei Segel glitten wie senkrechte Papierwände über das abendglatte Wasser.")
    fact_spec("Die drei Segel glitten wie senkrechte Papierwände über das abendglatte Wasser.")

    TTS = GermanSingleSpeakerTransformerTTSInference()
    TTS("Die drei Segel glitten wie senkrechte Papierwände über das abendglatte Wasser.")
