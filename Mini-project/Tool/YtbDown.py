from pytubefix import YouTube

# Nhập link
link = input("Nhập link cần tải: ")

try:
    yt = YouTube(link)
    print("Đang lấy thông tin...")
    print(f"Tiêu đề: {yt.title}")
    print(f"Tác giả: {yt.author}")
    print(f"Lượt xem: {yt.views}")
    
    # Lấy stream và tải
    ys = yt.streams.get_highest_resolution()
    print(f"Đang tải video: {ys.title}...") # Báo cho người dùng biết đang tải
    ys.download()
    print("✅ Tải thành công!")

except Exception as e: # Bắt tất cả các loại lỗi (Exception)
    print(f"❌ Có lỗi xảy ra: {e}")