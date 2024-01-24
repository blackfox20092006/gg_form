import threading

from selenium.webdriver.common.by import By
from threading import Thread
from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup
import os
import random
ua_url = 'https://raw.githubusercontent.com/blackfox20092006/temp1/main/ua.txt'
a = requests.get(ua_url)
ua = list(a)[1:]
name = ["Phương Chi", "An Bình", "An Di", "An Hạ", "An Hằng", "An Khê", "An Nhiên", "An Nhàn", "Anh Chi", "Anh Hương", "Anh Mai", "Anh Phương", "Anh Thi", "Anh Thy", "Anh Thơ", "Anh Thư", "Anh Thảo", "Anh Vũ", "Anh Ðào", "Ban Mai", "Bình Minh", "Bình Yên", "Bích Chiêu", "Bích Châu", "Bích Duyên", "Bích Hiền", "Bích Huệ", "Bích Hà", "Bích Hạnh", "Bích Hải", "Bích Hảo", "Bích Hậu", "Bích Hằng", "Bích Hồng", "Bích Hợp", "Bích Lam", "Bích Liên", "Bích Loan", "Bích Nga", "Bích Ngà", "Bích Ngân", "Bích Ngọc", "Bích Như", "Bích Phượng", "Bích Quyên", "Bích Quân", "Bích San", "Bích Thoa", "Bích Thu", "Bích Thảo", "Bích Thủy", "Bích Trang", "Bích Trâm", "Bích Ty", "Bích Vân", "Bích Ðiệp", "Bích Ðào", "Băng Băng", "Băng Tâm", "Bạch Cúc", "Bạch Hoa", "Bạch Kim", "Bạch Liên", "Bạch Loan", "Bạch Mai", "Bạch Quỳnh", "Bạch Trà", "Bạch Tuyết", "Bạch Vân", "Bạch Yến", "Bảo Anh", "Bảo Bình", "Bảo Châu", "Bảo Huệ", "Bảo Hà", "Bảo Hân", "Bảo Lan", "Bảo Lễ", "Bảo Ngọc", "Bảo Phương", "Bảo Quyên", "Bảo Quỳnh", "Bảo Thoa", "Bảo Thúy", "Bảo Tiên", "Bảo Trâm", "Bảo Trân", "Bảo Trúc", "Bảo Uyên", "Bảo Vy", "Bảo Vân", "Bội Linh", "Cam Thảo", "Chi Lan", "Chi Mai", "Chiêu Dương", "Cát Cát", "Cát Linh", "Cát Ly", "Cát Tiên", "Cát Tường", "Cẩm Hiền", "Cẩm Hường", "Cẩm Hạnh", "Cẩm Linh", "Cẩm Liên", "Cẩm Ly", "Cẩm Nhi", "Cẩm Nhung", "Cẩm Thúy", "Cẩm Tú", "Cẩm Vân", "Cẩm Yến", "Di Nhiên", "Diên Vỹ", "Diễm Chi", "Diễm Châu", "Diễm Hương", "Diễm Hạnh", "Diễm Hằng", "Diễm Khuê", "Diễm Kiều", "Diễm Liên", "Diễm Lộc", "Diễm My", "Diễm Phúc", "Diễm Phương", "Diễm Phước", "Diễm Phượng", "Diễm Quyên", "Diễm Quỳnh", "Diễm Thúy", "Diễm Thư", "Diễm Thảo", "Diễm Trang", "Diễm Trinh", "Diễm Uyên", "Diệp Anh", "Diệp Vy", "Diệu Anh", "Diệu Hiền", "Diệu Hoa", "Diệu Huyền", "Diệu Hương", "Diệu Hạnh", "Diệu Hằng", "Diệu Hồng", "Diệu Lan", "Diệu Linh", "Diệu Loan", "Diệu Nga", "Diệu Ngà", "Diệu Ngọc", "Diệu Nương", "Diệu Thiện", "Diệu Thúy", "Diệu Vân", "Diệu Ái", "Duy Hạnh", "Duy Mỹ", "Duy Uyên", "Duyên Hồng", "Duyên My", "Duyên Mỹ", "Duyên Nương", "Dã Lan", "Dã Lâm", "Dã Thảo", "Dạ Hương", "Dạ Lan", "Dạ Nguyệt", "Dạ Thi", "Dạ Thảo", "Dạ Yến", "Gia Hân", "Gia Khanh", "Gia Linh", "Gia Nhi", "Gia Quỳnh", "Giang Thanh", "Giang Thiên", "Giao Hưởng", "Giao Kiều", "Giao Linh", "Giáng Ngọc", "Giáng Tiên", "Giáng Uyên", "Hiếu Giang", "Hiếu Hạnh", "Hiếu Khanh", "Hiếu Minh", "Hiền Chung", "Hiền Hòa", "Hiền Mai", "Hiền Nhi", "Hiền Nương", "Hiền Thục", "Hiểu Lam", "Hiểu Vân", "Hoa Liên", "Hoa Lý", "Hoa Thiên", "Hoa Tiên", "Hoa Tranh", "Hoài An", "Hoài Giang", "Hoài Hương", "Hoài Phương", "Hoài Thương", "Hoài Trang", "Hoài Vỹ", "Hoàn Châu", "Hoàn Vi", "Hoàng Cúc", "Hoàng Hà", "Hoàng Kim", "Hoàng Lan", "Hoàng Mai", "Hoàng Miên", "Hoàng Nguyên", "Hoàng Oanh", "Hoàng Sa", "Hoàng Thư", "Hoàng Xuân", "Hoàng Yến", "Hoạ Mi", "Huyền Anh", "Huyền Diệu", "Huyền Linh", "Huyền Ngọc", "Huyền Nhi", "Huyền Thoại", "Huyền Thư", "Huyền Trang", "Huyền Trâm", "Huyền Trân", "Huệ An", "Huệ Hương", "Huệ Hồng", "Huệ Lan", "Huệ Linh", "Huệ Lâm", "Huệ My", "Huệ Phương", "Huệ Thương", "Huệ Ân", "Huỳnh Anh", "Hà Giang", "Hà Liên", "Hà Mi", "Hà My", "Hà Nhi", "Hà Phương", "Hà Thanh", "Hà Tiên", "Hàm Duyên", "Hàm Nghi", "Hàm Thơ", "Hàm Ý", "Hương Chi", "Hương Giang", "Hương Lan", "Hương Liên", "Hương Ly", "Hương Lâm", "Hương Mai", "Hương Nhi", "Hương Thu", "Hương Thảo", "Hương Thủy", "Hương Tiên", "Hương Trang", "Hương Trà", "Hương Xuân", "Hướng Dương", "Hạ Băng", "Hạ Giang", "Hạ Phương", "Hạ Tiên", "Hạ Uyên", "Hạ Vy", "Hạc Cúc", "Hạnh Chi", "Hạnh Dung", "Hạnh Linh", "Hạnh My", "Hạnh Nga", "Hạnh Nhơn", "Hạnh Phương", "Hạnh San", "Hạnh Thảo", "Hạnh Trang", "Hạnh Vi", "Hải Anh", "Hải Châu", "Hải Duyên", "Hải Dương", "Hải Miên", "Hải My", "Hải Mỹ", "Hải Ngân", "Hải Nhi", "Hải Phương", "Hải Phượng", "Hải San", "Hải Sinh", "Hải Thanh", "Hải Thảo", "Hải Thụy", "Hải Uyên", "Hải Vy", "Hải Vân", "Hải Yến", "Hải Ân", "Hải Ðường", "Hảo Nhi", "Hằng Anh", "Hằng Nga", "Họa Mi", "Hồ Diệp", "Hồng Anh", "Hồng Bạch Thảo", "Hồng Châu", "Hồng Diễm", "Hồng Giang", "Hồng Hoa", "Hồng Hà", "Hồng Hạnh", "Hồng Khanh", "Hồng Khuê", "Hồng Khôi", "Hồng Linh", "Hồng Liên", "Hồng Lâm", "Hồng Mai", "Hồng Nga", "Hồng Ngân", "Hồng Ngọc", "Hồng Nhung", "Hồng Như", "Hồng Nhạn", "Hồng Oanh", "Hồng Phúc", "Hồng Phương", "Hồng Quế", "Hồng Thu", "Hồng Thúy", "Hồng Thư", "Hồng Thảo", "Hồng Thắm", "Hồng Thủy", "Hồng Trúc", "Hồng Tâm", "Hồng Vân", "Hồng Xuân", "Hồng Ðiệp", "Hồng Ðào", "Hồng Đăng", "Khiết Linh", "Khiết Tâm", "Khuê Trung", "Khánh Chi", "Khánh Giang", "Khánh Giao", "Khánh Huyền", "Khánh Hà", "Khánh Hằng", "Khánh Linh", "Khánh Ly", "Khánh Mai", "Khánh My", "Khánh Ngân", "Khánh Ngọc", "Khánh Quyên", "Khánh Quỳnh", "Khánh Thủy", "Khánh Trang", "Khánh Vi", "Khánh Vy", "Khánh Vân", "Khúc Lan", "Khả Khanh", "Khả Tú", "Khả Ái", "Khải Ca", "Khải Hà", "Khải Tâm", "Kim Anh", "Kim Chi", "Kim Cương", "Kim Dung", "Kim Duyên", "Kim Hoa", "Kim Hương", "Kim Khanh", "Kim Khuyên", "Kim Khánh", "Kim Lan", "Kim Liên", "Kim Loan", "Kim Ly", "Kim Mai", "Kim Ngân", "Kim Ngọc", "Kim Oanh", "Kim Phượng", "Kim Quyên", "Kim Sa", "Kim Thanh", "Kim Thoa", "Kim Thu", "Kim Thy", "Kim Thông", "Kim Thư", "Kim Thảo", "Kim Thủy", "Kim Trang", "Kim Tuyến", "Kim Tuyết", "Kim Tuyền", "Kim Xuyến", "Kim Xuân", "Kim Yến", "Kim Ánh", "Kim Đan", "Kiết Hồng", "Kiết Trinh", "Kiều Anh", "Kiều Diễm", "Kiều Dung", "Kiều Giang", "Kiều Hoa", "Kiều Hạnh", "Kiều Khanh", "Kiều Loan", "Kiều Mai", "Kiều Minh", "Kiều Mỹ", "Kiều Nga", "Kiều Nguyệt", "Kiều Nương", "Kiều Thu", "Kiều Trang", "Kiều Trinh", "Kỳ Anh", "Kỳ Diệu", "Kỳ Duyên", "Lam Giang", "Lam Hà", "Lam Khê", "Lam Ngọc", "Lam Tuyền", "Lan Anh", "Lan Chi", "Lan Hương", "Lan Khuê", "Lan Ngọc", "Lan Nhi", "Lan Phương", "Lan Thương", "Lan Trúc", "Lan Vy", "Linh Chi", "Linh Châu", "Linh Duyên", "Linh Giang", "Linh Hà", "Linh Lan", "Linh Nhi", "Linh Phương", "Linh Phượng", "Linh San", "Linh Trang", "Linh Ðan", "Liên Chi", "Liên Hoa", "Liên Hương", "Liên Như", "Liên Phương", "Liên Trân", "Liễu Oanh", "Loan Châu", "Ly Châu", "Lâm Nhi", "Lâm Oanh", "Lâm Tuyền", "Lâm Uyên", "Lê Quỳnh", "Lưu Ly", "Lệ Băng", "Lệ Chi", "Lệ Giang", "Lệ Hoa", "Lệ Huyền", "Lệ Khanh", "Lệ Nga", "Lệ Nhi", "Lệ Quyên", "Lệ Quân", "Lệ Thanh", "Lệ Thu", "Lệ Thủy", "Lộc Uyên", "Lộc Uyển", "Lục Bình", "Mai Anh", "Mai Chi", "Mai Châu", "Mai Hiền", "Mai Hà", "Mai Hương", "Mai Hạ", "Mai Khanh", "Mai Khôi", "Mai Lan", "Mai Linh", "Mai Liên", "Mai Loan", "Mai Ly", "Mai Nhi", "Mai Phương", "Mai Quyên", "Mai Thanh", "Mai Thu", "Mai Thy", "Mai Thảo", "Mai Trinh", "Mai Tâm", "Mai Vy", "Minh An", "Minh Châu", "Minh Duyên", "Minh Hiền", "Minh Huyền", "Minh Huệ", "Minh Hà", "Minh Hương", "Minh Hạnh", "Minh Hằng", "Minh Hồng", "Minh Khai", "Minh Khuê", "Minh Loan", "Minh Minh", "Minh Nguyệt", "Minh Ngọc", "Minh Nhi", "Minh Như", "Minh Phương", "Minh Phượng", "Minh Thu", "Minh Thúy", "Minh Thư", "Minh Thương", "Minh Thảo", "Minh Thủy", "Minh Trang", "Minh Tuyết", "Minh Tuệ", "Minh Tâm", "Minh Uyên", "Minh Vy", "Minh Xuân", "Minh Yến", "Minh Đan", "Mậu Xuân", "Mộc Miên", "Mộng Hoa", "Mộng Hương", "Mộng Hằng", "Mộng Lan", "Mộng Liễu", "Mộng Nguyệt", "Mộng Nhi", "Mộng Quỳnh", "Mộng Thi", "Mộng Thu", "Mộng Tuyền", "Mộng Vi", "Mộng Vy", "Mộng Vân", "Mộng Ðiệp", "Mỹ Anh", "Mỹ Diễm", "Mỹ Dung", "Mỹ Duyên", "Mỹ Hiệp", "Mỹ Hoàn", "Mỹ Huyền", "Mỹ Huệ", "Mỹ Hường", "Mỹ Hạnh", "Mỹ Khuyên", "Mỹ Kiều", "Mỹ Lan", "Mỹ Loan", "Mỹ Lệ", "Mỹ Lợi", "Mỹ Nga", "Mỹ Ngọc", "Mỹ Nhi", "Mỹ Nhân", "Mỹ Nương", "Mỹ Phương", "Mỹ Phượng", "Mỹ Phụng", "Mỹ Thuần", "Mỹ Thuận", "Mỹ Trang", "Mỹ Trâm", "Mỹ Tâm", "Mỹ Uyên", "Mỹ Vân", "Mỹ Xuân", "Mỹ Yến", "Nghi Dung", "Nghi Minh", "Nghi Xuân", "Nguyên Hồng", "Nguyên Thảo", "Nguyết Ánh", "Nguyệt Anh", "Nguyệt Cát", "Nguyệt Cầm", "Nguyệt Hà", "Nguyệt Hồng", "Nguyệt Lan", "Nguyệt Minh", "Nguyệt Nga", "Nguyệt Quế", "Nguyệt Uyển", "Nguyệt Ánh", "Ngân Anh", "Ngân Hà", "Ngân Thanh", "Ngân Trúc", "Ngọc Anh", "Ngọc Bích", "Ngọc Cầm", "Ngọc Diệp", "Ngọc Dung", "Ngọc Hiền", "Ngọc Hoa", "Ngọc Hoan", "Ngọc Hoàn", "Ngọc Huyền", "Ngọc Huệ", "Ngọc Hà", "Ngọc Hân", "Ngọc Hạ", "Ngọc Hạnh", "Ngọc Hằng", "Ngọc Khanh", "Ngọc Khuê", "Ngọc Khánh", "Ngọc Lam", "Ngọc Lan", "Ngọc Linh", "Ngọc Liên", "Ngọc Loan", "Ngọc Ly", "Ngọc Lâm", "Ngọc Lý", "Ngọc Lệ", "Ngọc Mai", "Ngọc Nhi", "Ngọc Nữ", "Ngọc Oanh", "Ngọc Phụng", "Ngọc Quyên", "Ngọc Quế", "Ngọc Quỳnh", "Ngọc San", "Ngọc Sương", "Ngọc Thi", "Ngọc Thy", "Ngọc Thơ", "Ngọc Trinh", "Ngọc Trâm", "Ngọc Tuyết", "Ngọc Tâm", "Ngọc Tú", "Ngọc Uyên", "Ngọc Uyển", "Ngọc Vy", "Ngọc Vân", "Ngọc Yến", "Ngọc Ái", "Ngọc Ánh", "Ngọc Ðiệp", "Ngọc Ðàn", "Ngọc Ðào", "Nhan Hồng", "Nhã Hương", "Nhã Hồng", "Nhã Khanh", "Nhã Lý", "Nhã Mai", "Nhã Sương", "Nhã Thanh", "Nhã Trang", "Nhã Trúc", "Nhã Uyên", "Nhã Yến", "Nhã Ý", "Như Anh", "Như Bảo", "Như Hoa", "Như Hảo", "Như Hồng", "Như Loan", "Như Mai", "Như Ngà", "Như Ngọc", "Như Phương", "Như Quân", "Như Quỳnh", "Như Thảo", "Như Trân", "Như Tâm", "Như Ý", "Nhất Thương", "Nhật Dạ", "Nhật Hà", "Nhật Hạ", "Nhật Lan", "Nhật Linh", "Nhật Lệ", "Nhật Mai", "Nhật Phương", "Nhật Ánh", "Oanh Thơ", "Oanh Vũ", "Phi Khanh", "Phi Nhung", "Phi Nhạn", "Phi Phi", "Phi Phượng", "Phong Lan", "Phương An", "Phương Anh", "Phương Chi", "Phương Châu", "Phương Diễm", "Phương Dung", "Phương Giang", "Phương Hiền", "Phương Hoa", "Phương Hạnh", "Phương Lan", "Phương Linh", "Phương Liên", "Phương Loan", "Phương Mai", "Phương Nghi", "Phương Ngọc", "Phương Nhi", "Phương Nhung", "Phương Phương", "Phương Quyên", "Phương Quân", "Phương Quế", "Phương Quỳnh", "Phương Thanh", "Phương Thi", "Phương Thùy", "Phương Thảo", "Phương Thủy", "Phương Trang", "Phương Trinh", "Phương Trà", "Phương Trâm", "Phương Tâm", "Phương Uyên", "Phương Yến", "Phước Bình", "Phước Huệ", "Phượng Bích", "Phượng Liên", "Phượng Loan", "Phượng Lệ", "Phượng Nga", "Phượng Nhi", "Phượng Tiên", "Phượng Uyên", "Phượng Vy", "Phượng Vũ", "Phụng Yến", "Quế Anh", "Quế Chi", "Quế Linh", "Quế Lâm", "Quế Phương", "Quế Thu", "Quỳnh Anh", "Quỳnh Chi", "Quỳnh Dao", "Quỳnh Dung", "Quỳnh Giang", "Quỳnh Giao", "Quỳnh Hoa", "Quỳnh Hà", "Quỳnh Hương", "Quỳnh Lam", "Quỳnh Liên", "Quỳnh Lâm", "Quỳnh Nga", "Quỳnh Ngân", "Quỳnh Nhi", "Quỳnh Nhung", "Quỳnh Như", "Quỳnh Phương", "Quỳnh Sa", "Quỳnh Thanh", "Quỳnh Thơ", "Quỳnh Tiên", "Quỳnh Trang", "Quỳnh Trâm", "Quỳnh Vân", "Sao Băng", "Sao Mai", "Song Kê", "Song Lam", "Song Oanh", "Song Thư", "Sông Hà", "Sông Hương", "Sơn Ca", "Sơn Tuyền", "Sương Sương", "Thanh Bình", "Thanh Dân", "Thanh Giang", "Thanh Hiếu", "Thanh Hiền", "Thanh Hoa", "Thanh Huyền", "Thanh Hà", "Thanh Hương", "Thanh Hường", "Thanh Hạnh", "Thanh Hảo", "Thanh Hằng", "Thanh Hồng", "Thanh Kiều", "Thanh Lam", "Thanh Lan", "Thanh Loan", "Thanh Lâm", "Thanh Mai", "Thanh Mẫn", "Thanh Nga", "Thanh Nguyên", "Thanh Ngân", "Thanh Ngọc", "Thanh Nhung", "Thanh Nhàn", "Thanh Nhã", "Thanh Phương", "Thanh Thanh", "Thanh Thiên", "Thanh Thu", "Thanh Thúy", "Thanh Thư", "Thanh Thảo", "Thanh Thủy", "Thanh Trang", "Thanh Trúc", "Thanh Tuyết", "Thanh Tuyền", "Thanh Tâm", "Thanh Uyên", "Thanh Vy", "Thanh Vân", "Thanh Xuân", "Thanh Yến", "Thanh Đan", "Thi Cầm", "Thi Ngôn", "Thi Thi", "Thi Xuân", "Thi Yến", "Thiên Di", "Thiên Duyên", "Thiên Giang", "Thiên Hà", "Thiên Hương", "Thiên Khánh", "Thiên Kim", "Thiên Lam", "Thiên Lan", "Thiên Mai", "Thiên Mỹ", "Thiên Nga", "Thiên Nương", "Thiên Phương", "Thiên Thanh", "Thiên Thêu", "Thiên Thư", "Thiên Thảo", "Thiên Trang", "Thiên Tuyền", "Thiếu Mai", "Thiều Ly", "Thiện Mỹ", "Thiện Tiên", "Thu Duyên", "Thu Giang", "Thu Hiền", "Thu Hoài", "Thu Huyền", "Thu Huệ", "Thu Hà", "Thu Hậu", "Thu Hằng", "Thu Hồng", "Thu Linh", "Thu Liên", "Thu Loan", "Thu Mai", "Thu Minh", "Thu Nga", "Thu Nguyệt", "Thu Ngà", "Thu Ngân", "Thu Ngọc", "Thu Nhiên", "Thu Oanh", "Thu Phong", "Thu Phương", "Thu Phượng", "Thu Sương", "Thu Thuận", "Thu Thảo", "Thu Thủy", "Thu Trang", "Thu Việt", "Thu Vân", "Thu Vọng", "Thu Yến", "Thuần Hậu", "Thy Khanh", "Thy Oanh", "Thy Trúc", "Thy Vân", "Thái Chi", "Thái Hà", "Thái Hồng", "Thái Lan", "Thái Lâm", "Thái Thanh", "Thái Thảo", "Thái Tâm", "Thái Vân", "Thùy Anh", "Thùy Dung", "Thùy Dương", "Thùy Giang", "Thùy Linh", "Thùy Mi", "Thùy My", "Thùy Nhi", "Thùy Như", "Thùy Oanh", "Thùy Uyên", "Thùy Vân", "Thúy Anh", "Thúy Diễm", "Thúy Hiền", "Thúy Huyền", "Thúy Hà", "Thúy Hương", "Thúy Hường", "Thúy Hạnh", "Thúy Hằng", "Thúy Kiều", "Thúy Liên", "Thúy Liễu", "Thúy Loan", "Thúy Mai", "Thúy Minh", "Thúy My", "Thúy Nga", "Thúy Ngà", "Thúy Ngân", "Thúy Ngọc", "Thúy Phượng", "Thúy Quỳnh", "Thúy Vi", "Thúy Vy", "Thúy Vân", "Thơ Thơ", "Thư Lâm", "Thư Sương", "Thương Huyền", "Thương Nga", "Thương Thương", "Thường Xuân", "Thạch Thảo", "Thảo Hương", "Thảo Hồng", "Thảo Linh", "Thảo Ly", "Thảo Mai", "Thảo My", "Thảo Nghi", "Thảo Nguyên", "Thảo Nhi", "Thảo Quyên", "Thảo Tiên", "Thảo Trang", "Thảo Uyên", "Thảo Vy", "Thảo Vân", "Thục Anh", "Thục Khuê", "Thục Nhi", "Thục Oanh", "Thục Quyên", "Thục Trang", "Thục Trinh", "Thục Tâm", "Thục Uyên", "Thục Vân", "Thục Ðoan", "Thục Ðào", "Thục Ðình", "Thụy Du", "Thụy Khanh", "Thụy Linh", "Thụy Lâm", "Thụy Miên", "Thụy Nương", "Thụy Trinh", "Thụy Trâm", "Thụy Uyên", "Thụy Vân", "Thụy Ðào", "Thủy Hằng", "Thủy Hồng", "Thủy Linh", "Thủy Minh", "Thủy Nguyệt", "Thủy Quỳnh", "Thủy Tiên", "Thủy Trang", "Thủy Tâm", "Tinh Tú", "Tiên Phương", "Tiểu Mi", "Tiểu My", "Tiểu Quỳnh", "Trang Anh", "Trang Linh", "Trang Nhã", "Trang Tâm", "Trang Ðài", "Triều Nguyệt", "Triều Thanh", "Triệu Mẫn", "Trung Anh", "Trà Giang", "Trà My", "Trâm Anh", "Trâm Oanh", "Trân Châu", "Trúc Chi", "Trúc Lam", "Trúc Lan", "Trúc Linh", "Trúc Liên", "Trúc Loan", "Trúc Ly", "Trúc Lâm", "Trúc Mai", "Trúc Phương", "Trúc Quân", "Trúc Quỳnh", "Trúc Vy", "Trúc Vân", "Trúc Ðào", "Trúc Đào", "Trầm Hương", "Tuyết Anh", "Tuyết Băng", "Tuyết Chi", "Tuyết Hoa", "Tuyết Hân", "Tuyết Hương", "Tuyết Hồng", "Tuyết Lan", "Tuyết Loan", "Tuyết Lâm", "Tuyết Mai", "Tuyết Nga", "Tuyết Nhi", "Tuyết Nhung", "Tuyết Oanh", "Tuyết Thanh", "Tuyết Trinh", "Tuyết Trầm", "Tuyết Tâm", "Tuyết Vy", "Tuyết Vân", "Tuyết Xuân", "Tuyền Lâm", "Tuệ Lâm", "Tuệ Mẫn", "Tuệ Nhi", "Tâm Hiền", "Tâm Hạnh", "Tâm Hằng", "Tâm Khanh", "Tâm Linh", "Tâm Nguyên", "Tâm Nguyệt", "Tâm Nhi", "Tâm Như", "Tâm Thanh", "Tâm Trang", "Tâm Ðoan", "Tâm Đan", "Tùng Linh", "Tùng Lâm", "Tùng Quân", "Tùy Anh", "Tùy Linh", "Tú Anh", "Tú Ly", "Tú Nguyệt", "Tú Quyên", "Tú Quỳnh", "Tú Sương", "Tú Trinh", "Tú Tâm", "Tú Uyên", "Túy Loan", "Tường Chinh", "Tường Vi", "Tường Vy", "Tường Vân", "Tịnh Lâm", "Tịnh Nhi", "Tịnh Như", "Tịnh Tâm", "Tịnh Yên", "Tố Loan", "Tố Nga", "Tố Nhi", "Tố Quyên", "Tố Tâm", "Tố Uyên", "Từ Dung", "Từ Ân", "Uyên Minh", "Uyên My", "Uyên Nhi", "Uyên Phương", "Uyên Thi", "Uyên Thy", "Uyên Thơ", "Uyên Trâm", "Uyên Vi", "Uyển Khanh", "Uyển My", "Uyển Nghi", "Uyển Nhi", "Uyển Nhã", "Uyển Như", "Vi Quyên", "Vinh Diệu", "Việt Hà", "Việt Hương", "Việt Khuê", "Việt Mi", "Việt Nga", "Việt Nhi", "Việt Thi", "Việt Trinh", "Việt Tuyết", "Việt Yến", "Vy Lam", "Vy Lan", "Vàng Anh", "Vành Khuyên", "Vân Anh", "Vân Chi", "Vân Du", "Vân Hà", "Vân Hương", "Vân Khanh", "Vân Khánh", "Vân Linh", "Vân Ngọc", "Vân Nhi", "Vân Phi", "Vân Phương", "Vân Quyên", "Vân Quỳnh", "Vân Thanh", "Vân Thúy", "Vân Thường", "Vân Tiên", "Vân Trang", "Vân Trinh", "Vũ Hồng", "Xuyến Chi", "Xuân Bảo", "Xuân Dung", "Xuân Hiền", "Xuân Hoa", "Xuân Hân", "Xuân Hương", "Xuân Hạnh", "Xuân Lan", "Xuân Linh", "Xuân Liễu", "Xuân Loan", "Xuân Lâm", "Xuân Mai", "Xuân Nghi", "Xuân Ngọc", "Xuân Nhi", "Xuân Nhiên", "Xuân Nương", "Xuân Phương", "Xuân Phượng", "Xuân Thanh", "Xuân Thu", "Xuân Thảo", "Xuân Thủy", "Xuân Trang", "Xuân Tâm", "Xuân Uyên", "Xuân Vân", "Xuân Yến", "Xuân xanh", "Yên Bằng", "Yên Mai", "Yên Nhi", "Yên Ðan", "Yên Đan", "Yến Anh", "Yến Hồng", "Yến Loan", "Yến Mai", "Yến My", "Yến Nhi", "Yến Oanh", "Yến Phương", "Yến Phượng", "Yến Thanh", "Yến Thảo", "Yến Trang", "Yến Trinh", "Yến Trâm", "Yến Ðan", "Ái Hồng", "Ái Khanh", "Ái Linh", "Ái Nhi", "Ái Nhân", "Ái Thi", "Ái Thy", "Ái Vân", "Ánh Dương", "Ánh Hoa", "Ánh Hồng", "Ánh Linh", "Ánh Lệ", "Ánh Mai", "Ánh Nguyệt", "Ánh Ngọc", "Ánh Thơ", "Ánh Trang", "Ánh Tuyết", "Ánh Xuân", "Ðan Khanh", "Ðan Quỳnh", "Ðan Thu", "Ðinh Hương", "Ðoan Thanh", "Ðoan Trang", "Ðài Trang", "Ðông Nghi", "Ðông Nhi", "Ðông Trà", "Ðông Tuyền", "Ðông Vy", "Ðông Ðào", "Ðồng Dao", "Ý Bình", "Ý Lan", "Ý Nhi", "Đan Linh", "Đan Quỳnh", "Đan Thanh", "Đan Thu", "Đan Thư", "Đan Tâm", "Đinh Hương", "Đoan Thanh", "Đoan Trang", "Đài Trang", "Đông Nghi", "Đông Trà", "Đông Tuyền", "Đông Vy", "Đơn Thuần", "Đức Hạnh", "Ấu Lăng"]
# with open('name2.txt', encoding='utf-8') as f:
#     name = [i.replace('\n', '') for i in f.readlines()]
# f.close()
# with open('ua.txt') as ff:
#     ua = [i.replace('\n', '') for i in ff.readlines()]
# ff.close()
def extract_words_from_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    content = soup.get_text()

    # Tách các từ vựng thành danh sách các từ riêng biệt
    words = content.split()

    return words
def generate(word_list, n):
    chosen_words = random.sample(word_list, n)

    paragraph = " ".join(chosen_words)

    return paragraph
wikipedia_url = "https://vi.wikipedia.org/wiki/Adolf_Hitler"


def find_until_xpath(driver, name, status, content):
    for i in range(100):
        try:
            e = driver.find_element(By.XPATH, name)
            break
        except:
            sleep(0.2)
            continue
            # for i in range(200):
            #     try:
            #         if status == 0:
            #             e.click()
            #         elif status == 1:
            #             e.send_keys(content)
            #         return
            #     except:
            #         sleep(0.2)
            #         continue
    for i in range(100):
        try:
            if status == 0:
                e.click()
            elif status == 1:
                e.send_keys(content)
                print(content)
            break
        except:
            sleep(0.2)
            continue
# Trích xuất danh sách các từ từ bài viết
word_list = extract_words_from_wikipedia(wikipedia_url)
tengv = [
    'Nguyễn Thị Hải Vân',
    'Nguyễn Thị Huệ',
    'Nguyễn Thị Xuân Tiên',
    'Ngô Thanh Huyền',
    'Tăng Việt Tân',
    'Mạc Thị Hồng Yến',
    'Quang Ngọc Yến',
    'Nguyễn Thị Mai Anh',
    'Đinh Hải Quốc',
    'Nguyễn Hoàng Anh',
    'Hồ Thị Bích Trâm',
    'Phan Thị Kim Oanh',
    'Nguyễn Thị Thu Nguyệt',
    'Nguyễn Thị Trúc Thy',
    'Đỗ Đăng Khoa',
    'Vo Thanh Danh L'
]
def run(driver):
    global count
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf6ICXMcuhVjjW1wurmkZhZHDiwO3vOB55P17HcLQBhafFCkA/viewform')
    find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, random.choice(name))
    find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, '12A'+str(random.randint(1,16)))
    find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, generate(word_list, random.randint(20, 50)))
    find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, generate(word_list, random.randint(20, 50)))
    find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, generate(word_list, random.randint(20, 50)))
    find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input', 1, random.choice(tengv))
    find_until_xpath(driver, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span', 0, '')
    driver.save_screenshot(f'{count}.png')
    os.system(f'title Running...{count}')
    count += 1
    return
count = 0
drivers = []
for i in range(10):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--disable-default-apps')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-media-source")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-webgl")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument("--disable-accelerometer")
    chrome_options.add_argument("--disable-bluetooth")
    chrome_options.add_argument("--disable-printing")
    chrome_options.add_argument("--disable-ambient-light-sensor")
    chrome_options.add_argument("--disable-web-authentication")
    chrome_options.add_argument("--disable-gamepad")
    chrome_options.add_argument("--disable-midi")
    chrome_options.add_argument("--disable-usb")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument("--disable-webrtc")
    chrome_options.add_argument("--disable-canvas-aa")
    chrome_options.add_argument("--disable-2d-canvas-clip-aa")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument(f'--user-agent="{random.choice(ua)}"')
    chrome_options.add_argument("--disable-credentials_enable_service")
    chrome_options.add_argument("--disable-profile.password_manager_enabled")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    drivers.append(driver)
while True:
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=run, args=(drivers[i],)))
    for i in range(10):
        threads[i].start()
        sleep(0.5)
    for i in range(10):
        threads[i].join()