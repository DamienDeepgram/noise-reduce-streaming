from pydub import AudioSegment
import numpy as np
import noisereduce as nr

# Load MP3 file
name = "./01-86"
audio = AudioSegment.from_mp3(name + ".mp3")

# Convert AudioSegment to numpy array
data = np.array(audio.get_array_of_samples())
rate = audio.frame_rate

# Perform noise reduction
reduced_noise = nr.reduce_noise(
    y=data, 
    sr=rate,
    stationary=True,
    freq_mask_smooth_hz=4000,
    time_mask_smooth_ms=33,
    n_std_thresh_stationary=0.7
)

# Convert reduced noise numpy array back to AudioSegment
reduced_noise_audio = AudioSegment(
    reduced_noise.tobytes(), 
    frame_rate=rate, 
    sample_width=reduced_noise.dtype.itemsize, 
    channels=audio.channels
)

# Export the reduced noise audio as MP3
reduced_noise_audio.export(name + "_noise_reduced.mp3", format="mp3")
