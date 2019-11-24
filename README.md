## data-mining-2019
#Bài tập môn khai phá dữ liệu - Học kỳ I năm học 2019-2020

- python3
- Packages: numpy, pandas, tensorflow, selenium, sklean, bs4

1. Thực hiện crawl dữ liệu từ file train.txt và file test.txt băng selenium
- Run: python3 selenium.py first_line last_line
- Chạy xong sẽ có fiel .csv với tên là data_[first_line]_[last_line].csv
- first_line : chọn dòng đầu trong tập .txt 
- last_line: chọn dòng cuối trong tập .txt
2. Thực hiện train model
- Đưa hết dữ liệu đã crawl được từ tập train.txt vào file clean_data.csv
- Đưa hết dữ liệu đã crawl được từ tập test.txt vào file data_for_test.csv
- Run: python3 training.py

