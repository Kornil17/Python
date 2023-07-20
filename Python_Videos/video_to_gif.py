import logging

import ffmpeg
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(filename)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8')


class Converter:
    def video_to_gif(self):
        count = 0
        try:
            logging.info("Start the circle")
            for video in os.listdir("/home/kornil/Videos"):
                if video.endswith((".mp4", ".MP4")):
                    logging.info("We do the task")
                    video_name = video.split(".")[0]
                    logging.debug("Get video name") 
                    logging.debug("Get gif name")
                    stream = ffmpeg.input(f"/home/kornil/Videos/{video}")
                    gif_name = str(input("Input Gif name\n")) + "_" + str(count) + ".gif"
                    logging.debug("Get the puth")
                    stream = ffmpeg.filter(stream, "fps", fps=2)
                    stream = ffmpeg.output(stream, f"/home/kornil/Videos/{gif_name}")
                    ffmpeg.run(stream)
                    count += 1
                    logging.debug("Increase the count")
            logging.info("Complete the task")

        except Exception as ex:
            logging.error(ex)


def main():
    logging.debug("Get obg")
    obg = Converter()
    logging.debug("Start the function converter")
    obg.video_to_gif()


if __name__ == "__main__":
    main()
