from IPython.display import Audio

from torchaudio.utils import download_asset

SAMPLE_WAV = download_asset("tutorial-assets/steam-train-whistle-daniel_simon.wav")
SAMPLE_RIR = download_asset("tutorial-assets/Lab41-SRI-VOiCES-rm1-impulse-mc01-stu-clo-8000hz.wav")
SAMPLE_SPEECH = download_asset("tutorial-assets/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042-8000hz.wav")
SAMPLE_NOISE = download_asset("tutorial-assets/Lab41-SRI-VOiCES-rm1-babb-mc01-stu-clo-8000hz.wav")

'''/で実行　コマンドfind . -name "*.wav" -type f
./opt/conda/lib/python3.10/site-packages/IPython/lib/tests/test.wav
./opt/conda/pkgs/torchaudio-2.1.0-py310_cu118/info/test/test/torchaudio_unittest/assets/kaldi_file_8000.wav
./opt/conda/pkgs/torchaudio-2.1.0-py310_cu118/info/test/test/torchaudio_unittest/assets/vad-go-mono-32000.wav
./opt/conda/pkgs/torchaudio-2.1.0-py310_cu118/info/test/test/torchaudio_unittest/assets/sinewave.wav
./opt/conda/pkgs/torchaudio-2.1.0-py310_cu118/info/test/test/torchaudio_unittest/assets/vad-go-stereo-44100.wav
./opt/conda/pkgs/torchaudio-2.1.0-py310_cu118/info/test/test/torchaudio_unittest/assets/steam-train-whistle-daniel_simon.wav
./opt/conda/pkgs/torchaudio-2.1.0-py310_cu118/info/test/test/torchaudio_unittest/assets/kaldi_file.wav
./opt/conda/pkgs/torchaudio-2.1.0-py310_cu118/info/test/test/torchaudio_unittest/assets/VCTK-Corpus/wav48/p224/p224_002.wav
./opt/conda/pkgs/ipython-8.15.0-py310h06a4308_0/lib/python3.10/site-packages/IPython/lib/tests/test.wav
./root/.cache/torch/hub/torchaudio/tutorial-assets/Lab41-SRI-VOiCES-rm1-babb-mc01-stu-clo-8000hz.wav
./root/.cache/torch/hub/torchaudio/tutorial-assets/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042-8000hz.wav
./root/.cache/torch/hub/torchaudio/tutorial-assets/Lab41-SRI-VOiCES-rm1-impulse-mc01-stu-clo-8000hz.wav
./root/.cache/torch/hub/torchaudio/tutorial-assets/steam-train-whistle-daniel_simon.wav
'''