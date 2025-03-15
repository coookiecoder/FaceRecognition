sudo apt install python3
sudo apt install python3-venv
sudo apt install python3-libcamera

python3 -m venv --system-site-packages /home/1SI/Desktop/camera_env

source /home/1SI/Desktop/camera_env/bin/activate

/home/1SI/Desktop/camera_env/bin/pip install opencv-python picamera2