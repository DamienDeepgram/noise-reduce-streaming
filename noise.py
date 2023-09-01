from scipy.io import wavfile
import noisereduce as nr

chunk_size = 1024
rate, data = wavfile.read("./sample.wav")
chunk, data = data[:chunk_size], data[chunk_size:]
# perform noise reduction
reduced_noise = nr.reduce_noise(
    y=chunk, 
    sr=rate,
    stationary=True,
    freq_mask_smooth_hz=2000,
    time_mask_smooth_ms=75,
    n_std_thresh_stationary=2
    )

wavfile.write("./sample_noise_reduced.wav", rate, reduced_noise)
