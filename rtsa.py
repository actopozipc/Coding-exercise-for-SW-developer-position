from rtsa_decoder.DSPStreamFileChunkSamples import DSPStreamFileChunkSamples
from rtsa_decoder.chunk_id_map import get_chunk_object
from rtsa_decoder.rtsa_decoder import get_samples_from_file
from rtsa_decoder.rtsa_processing import get_heatmap_png, get_max_hold_json


def print_file_chunks(file_object):
    chunk_object = None
    while True:
        if chunk_object is None:
            chunk_object = get_chunk_object(file_object, 0, None)
        else:
            chunk_object = chunk_object.get_next_chunk()

        if chunk_object is None:
            break
        if not isinstance(chunk_object, DSPStreamFileChunkSamples):
            print()
            print(chunk_object.get_chunk_header_data())
            print(chunk_object.get_header_data())
        else:
            print("SAMP")


if __name__ == "__main__":
    with open("DOR_KU#1_1401049243.rtsa", "rb") as file_object:
        print_file_chunks(file_object)
        samples = get_samples_from_file(file_object)
    import matplotlib.pyplot as plt
    print(samples)
    import numpy as np
    # Example data dimensions
    rows, cols = 93, 82000
    power_matrix = samples.samples  # Replace with your actual data

    # Define frequency and time axes
    frequency_axis = np.linspace(0, 100, rows)  # Example: 0 to 100 Hz for 93 rows
    time_axis = np.linspace(0, 820, cols)      # Example: 0 to 820 seconds for 82000 columns

  
    # Display using imshow with labeled axes
    plt.figure(figsize=(15, 6))
    plt.imshow(power_matrix, aspect='auto', cmap='gnuplot2', interpolation='none', extent=[time_axis[0], time_axis[-1], frequency_axis[0], frequency_axis[-1]])
    plt.colorbar(label='Power')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrum Power Measurements')
    plt.show()
    print(np.mean(samples.samples))
    print(np.max(samples.samples))
    # plt.hist(samples.samples[1],bins=10)
    # plt.show()

    heatmap_bytes = get_heatmap_png(samples)

    with open("samples.png", "wb") as heatmap_file:
        heatmap_file.write(heatmap_bytes)

    max_hold_json = get_max_hold_json(samples)

    with open("max_hold.json", "w") as max_hold_file:
        max_hold_file.write(max_hold_json)
