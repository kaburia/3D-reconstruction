import cv2
import os

# read the video and release the frames
def capture_and_release(video_path, output_directory='frames'):
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Could not open video")
        return
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Frame count:", frame_count)
    for i in range(frame_count):
        ret, frame = video.read()
        if not ret:
            print("Could not read frame", i)
            break
        image_path = os.path.join(output_directory, "frame%d.jpg" % i)
        cv2.imwrite(image_path, frame)
    video.release()
    cv2.destroyAllWindows()
    