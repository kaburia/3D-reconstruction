import cv2

# read the video and release the frames
def capture_and_release(video_path, output_directory):
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
        cv2.imwrite(output_directory + "/frame%d.jpg" % i, frame)
    video.release()
    cv2.destroyAllWindows()
    