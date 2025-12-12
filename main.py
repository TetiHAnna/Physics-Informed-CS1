import random
import math

# --- PART 1: Data Generation (Physics Simulation) ---
def generate_synthetic_data(length=200):
    """
    Generates a data array with noise and a single hidden signal (Gaussian).
    """
    # 1. Create background noise (Poisson-like noise simulation)
    data = [random.randint(40, 60) for _ in range(length)]
    
    # 2. Add radiation "hump" (Anomaly) in the center
    center = 100
    peak_height = 30  # Weak signal (smaller than noise peaks)
    width = 10
    
    for i in range(length):
        # Gaussian formula for creating the signal profile
        signal = peak_height * math.exp(-((i - center)**2) / (2 * width**2))
        data[i] += int(signal)
        
    return data

# --- PART 2: Student Algorithm (From the Guidebook) ---
def find_weak_source(cps_data, window_size, threshold_factor):
    """
    Implementation of anomaly detection based on the 'AI-First' methodology.
    References Guidebook Chapters: 3 (Arrays), 3.4 (Processing), 6 (Search).
    """
    n = len(cps_data)
    smoothed_signal = [0.0] * n  # Array initialization
    
    # STEP A: Smoothing (Convolution via Loops)
    # This loop demonstrates the mechanics of a convolutional layer
    for i in range(n - window_size + 1):
        window_sum = 0
        # Inner loop - analog to the convolution operation
        for j in range(window_size):
            window_sum += cps_data[i + j]
        
        current_avg = window_sum / window_size
        # Assign average to the center of the window
        center_index = i + window_size // 2
        smoothed_signal[center_index] = current_avg

    # STEP B: Threshold Calibration (Background Estimation)
    # Use the first 50 points as "clean air" (background) for calibration
    background_level = sum(smoothed_signal[0:50]) / 50  
    alarm_threshold = background_level * threshold_factor
    
    print(f"--- Diagnostics ---")
    print(f"Background Level: {background_level:.2f}")
    print(f"Trigger Threshold: {alarm_threshold:.2f}")
    
    # STEP C: Search (Anomaly Detection)
    detected_peaks = []
    for k in range(n):
        if smoothed_signal[k] > alarm_threshold:
            detected_peaks.append(k)
            
    return detected_peaks

# --- PART 3: Main Execution ---
if __name__ == "__main__":
    # 1. Generate data
    my_data = generate_synthetic_data()
    print(f"Generated {len(my_data)} data points.")
    
    # 2. Run the algorithm
    # window_size=15 (width of the smoothing window)
    # threshold_factor=1.6 (detection sensitivity >60% above background)
    found_indices = find_weak_source(my_data, window_size=15, threshold_factor=1.6)
    
    # 3. Output result
    if found_indices:
        print(f"\n Anomaly (radiation) detected at points:")
        print(found_indices)
        print(f"This corresponds to the array center (around point 100).")
    else:
        print("\n No anomalies detected. Try reducing the threshold (threshold_factor).")
