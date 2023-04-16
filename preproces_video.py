import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_frame(frame):
    plt.imshow(frame)
    plt.show()


def convert_to_mp4(path: str, filename: str):
    filename = path + filename
    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    filename = filename.replace('.MOV', '') + '.mp4'
    out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    cap.release()
    out.release()


def resize(path: str, filename: str, final_height: int, final_width: int):
    input_path = path + filename
    output_path = path + f'preprocessed_{filename}'

    cap = cv2.VideoCapture(input_path)
    input_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    input_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    if input_height > input_width:
        output_height = input_height
        output_width = input_height
    else:
        output_height = input_width
        output_width = input_width
    padding_height = (output_height - input_height) // 2
    padding_width = (output_width - input_width) // 2
    output_img = np.zeros((output_height, output_width, 3), np.uint8)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(output_path, fourcc, fps, (final_width, final_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        output_img[padding_height:padding_height+input_height, padding_width:padding_width+input_width, :] = frame
        output_img_resized = cv2.resize(output_img, (final_width, final_height))
        out.write(output_img_resized)
    cap.release()
    out.release()


def main():
    path = 'videos/'
    video_name = str(input('video name: '))
    if '.MOV' in video_name:
        print('converting to MP4')
        convert_to_mp4(path, video_name)
        video_name = video_name.replace('.MOV', '.mp4')
    print('resizing')
    resize(path, video_name, final_height=640, final_width=640)


if __name__ == '__main__':
    main()
