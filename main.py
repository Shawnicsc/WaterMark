from moviepy.editor import *
# 加载原视频文件
video = VideoFileClip("D:/pythonProject/watermark/test.mp4")

# 添加文字水印
txt_clip = (TextClip("Your Text Here", fontsize=50, color='white')
            .set_position('bottom')  # 设置水印位置
            .set_duration(video.duration))  # 设置水印时长与原视频相同

# 在原视频上叠加文字水印
video_with_watermark = CompositeVideoClip([video, txt_clip])

# 保存添加水印后的视频文件
video_with_watermark.write_videofile("D:/pythonProject/watermark/test_with_watermark.mp4")