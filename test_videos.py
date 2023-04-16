import os
import subprocess


def get_files(path: str):
    files = []
    for f in os.listdir(path):
        if f.endswith('.mp4'):
            if ('preprocessed_' in f) and ('keypoint.mp4' not in f):
                files.append(f)
    return files


if __name__ == '__main__':
    path = 'videos/'
    test_files = get_files(path)
    for i, (f) in enumerate(test_files):
        print(f'Processing {i+1}/{len(test_files)}: {f}')
        subprocess.run(['python3', 'pose-estimate.py', '--source', path+f])
