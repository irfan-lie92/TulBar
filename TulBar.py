import cv2
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

# Fungsi untuk mendeteksi fitur-fitur dalam gambar
def detect_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return edges

# Fungsi untuk menghasilkan getaran berdasarkan hasil deteksi
def generate_vibration(features):
    vibration_strength = np.sum(features) / 255
    return vibration_strength

# Fungsi untuk mendeteksi suara ketukan
def detect_knock(sound_file):
    sound = AudioSegment.from_file(sound_file)

    # Mengukur amplitudo suara (contoh: menggunakan rata-rata amplitudo)
    average_amplitude = np.mean(np.abs(sound.get_array_of_samples()))

    # Menguji ambang batas untuk mendeteksi suara ketukan
    threshold = 5000  # Sesuaikan dengan ambang batas yang sesuai dengan kebutuhan Anda
    if average_amplitude > threshold:
        return True
    else:
        return False

# Fungsi utama untuk memproses gambar dan menghasilkan getaran
def process_image(image_path, sound_file):
    image = cv2.imread(image_path)

    features = detect_features(image)
    vibration_strength = generate_vibration(features)

    # Mendeteksi suara ketukan
    is_knock = detect_knock(sound_file)

    if is_knock:
        print("Detected a knock!")
        # Lakukan sesuatu jika terdeteksi suara ketukan (misalnya, ganti pola getaran)
        # pytactx.vibrate(vibration_strength)

    cv2.imshow("Image", image)
    cv2.imshow("Features", features)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Contoh penggunaan
image_path = "objek/batu.jpeg"
sound_file = "objek/batu.wav"
process_image(image_path, sound_file)