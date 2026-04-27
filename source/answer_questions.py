import pandas as pd # Thư viện để thao tác và xử lý dữ liệu dạng bảng
import numpy as np # Thư viện hỗ trợ các phép toán trên mảng (nếu cần thiết)
import os # Thư viện hỗ trợ nối đường dẫn thư mục đa nền tảng

data_dir = 'data' # Định nghĩa thư mục chứa toàn bộ dữ liệu csv gốc

def inspect_df(df, name="DataFrame", head_n=10):
    """Hàm tiện ích in ra shape và 2 mẫu phần tử DataFrame để dễ theo dõi sau khi biến đổi cấu trúc"""
    print(f"\n[Inspect] -> {name} | Shape: {df.shape}")
    print(df.head(head_n))

def main():
    print("Loading data...") # In thông báo tiến trình cho thao tác nạp dữ liệu
    
    # Nạp dữ liệu các bảng từ thư mục data_dir vào bộ nhớ (dưới dạng DataFrame)
    orders = pd.read_csv(os.path.join(data_dir, 'orders.csv')) # Đọc bảng chứa thông tin tổng hợp của các đơn hàng
    products = pd.read_csv(os.path.join(data_dir, 'products.csv')) # Đọc bảng danh mục thông tin chi tiết từng sản phẩm
    returns = pd.read_csv(os.path.join(data_dir, 'returns.csv')) # Đọc bảng ghi nhận lịch sử các sản phẩm bị trả lại
    traffic = pd.read_csv(os.path.join(data_dir, 'web_traffic.csv')) # Đọc bảng ghi lưu thông website (traffic) hàng ngày
    order_items = pd.read_csv(os.path.join(data_dir, 'order_items.csv'), low_memory=False) # Đọc chi tiết từng nhóm sản phẩm trong một mã đơn hàng (bỏ qua cảnh báo kiểu dữ liệu)
    customers = pd.read_csv(os.path.join(data_dir, 'customers.csv')) # Đọc bảng chứa hồ sơ định danh và hành vi đăng ký của khách hàng
    geo = pd.read_csv(os.path.join(data_dir, 'geography.csv')) # Đọc thông tin vùng miền địa lý (được nối qua mã zip)
    payments = pd.read_csv(os.path.join(data_dir, 'payments.csv')) # Đọc phương thức và số kỳ trả góp tương ứng với mỗi đơn

    print("\n--- Answers ---\n") # In đoạn ngắn vạch chia phân đoạn báo cáo console

    # Q1: Trung vị khoảng cách ngày tiếp theo mua hàng của một khách (inter-order gap)
    orders['order_date'] = pd.to_datetime(orders['order_date']) # Chuyển cột chuỗi text ngày tháng sang định dạng thời gian máy tính dễ tính toán khoảng cách
    orders_sorted = orders.sort_values(['customer_id', 'order_date']) # Sắp xếp các bản ghi gom theo ID khách hàng, để trật tự lịch sử mua hàng của họ xuôi theo thời gian
    inspect_df(orders_sorted, "orders_sorted (Q1: after sort)")
    orders_sorted['days_diff'] = orders_sorted.groupby('customer_id')['order_date'].diff().dt.days # Tính ra lượng ngày chênh lệch giữa lần mua xếp sau so với lần mua liền kề phía trước của cùng 1 người
    q1_ans = orders_sorted['days_diff'].dropna().median() # Loại bỏ các giá trị trống (lần đầu tiền khách mua) rồi lấy con số ở chính giữa rổ dữ liệu chênh lệch này (trung vị).
    print(f"Q1: {q1_ans} days") # Xuất trực tiếp số đáp án của Q1 ra màn hình text

    # Q2: Tỷ suất mảng sản phẩm (segment) đạt lợi nhuận trung bình gộp cao nhất
    products['margin'] = (products['price'] - products['cogs']) / products['price'] # Quét trên toàn bộ sản phẩm và áp dụng công thức tìm biên độ lợi nhuận theo giá và vốn
    inspect_df(products.groupby('segment')['margin'].mean())
    q2_ans = products.groupby('segment')['margin'].mean().idxmax() # Gom sản phẩm thành từng phân khúc (segment), sau đó đếm số trung bình hàm margin rồi tìm ra đỉnh của danh sách
    print(f"Q2: {q2_ans}") # Xuất trực tiếp đáp án của phân khúc mục tiêu của Q2 ra màn hình text

    # Q3: Lý do khách trả hàng nhiều nhất riêng với dòng đồ Streetwear
    returns_prod = returns.merge(products, on='product_id') # Ghép dữ liệu từ bảng trả đồ với bảng thông tin sản phẩm để biết được sản phẩm đó phân loại category gì
    inspect_df(returns_prod, "returns_prod (Q3: after merge Returns & Products)")
    streetwear_returns = returns_prod[returns_prod['category'] == 'Streetwear'] # Giữ lại các bản ghi trả hàng mà sản phẩm liên đới thuộc về 'Streetwear'
    q3_ans = streetwear_returns['return_reason'].value_counts().idxmax() # Thống kê xem trong nhóm giới hạn này có bao nhiêu lượng nhãn lý do trả đồ, lấy chỉ danh có số lượng trội nhất
    print(f"Q3: {q3_ans}") # Xuất dạng đáp án Q3 vào màn console

    # Q4: Nguồn website marketing gây ra tỷ lệ thoát trang hụt (bounce) thấp nhất
    inspect_df(traffic.groupby('traffic_source')['bounce_rate'].mean())
    q4_ans = traffic.groupby('traffic_source')['bounce_rate'].mean().idxmin() # Gom rổ các nguồn truy cập web, tính mốc thoát website trung bình của nguồn rồi chọn ra nguồn có tỉ lệ rời khỏi thấp thỏi nhất
    print(f"Q4: {q4_ans}") # In text kết quả Q4 lên màn console

    # Q5: Sản phẩm mua vào bao nhiêu % có gắn nhãn mã khuyến mãi
    q5_ans = (order_items['promo_id'].notna().sum() / len(order_items)) * 100 # Đếm tổng dung lượng những dòng có khuyến mãi, sau đó chia lấy tỷ lệ phần trăm theo tổng số dòng đã mua
    print(f"Q5: {q5_ans:.2f}%") # Xoắn format hiển thị tỷ lệ % của Q5 với độ chính xác 2 chữ số

    # Q6: Tuổi của nhóm khách có độ mua lặp lại trung bình tốt nhất
    order_counts = orders.groupby('customer_id').size().reset_index(name='order_count') # Ở bảng orders, đếm tần suất lặp mã của từng ông khách (ứng với số lượng đơn họ đã đặt thành công)
    cust_orders = customers.merge(order_counts, on='customer_id', how='left') # Gắn ngược lại bảng khách hàng để đối chiếu hồ sơ người đó đã đặt bao đơn
    inspect_df(cust_orders, "cust_orders (Q6: after left merge Customers & OrderCounts)")
    cust_orders['order_count'] = cust_orders['order_count'].fillna(0) # Tránh lỗi chênh lệch rỗng, ta gán khách chưa phát sinh đơn nào cho một con số là 0
    valid_cust = cust_orders[cust_orders['age_group'].notna()] # Để xét tính chính xác theo độ nhóm tuổi, ta lược thẳng các khách bị mất hồ sơ về độ nhóm tuổi (bị null)
    q6_ans = valid_cust.groupby('age_group')['order_count'].mean().idxmax() # Gom các nhóm phân loại tuổi lại, lấy lượng đơn trung bình của nhóm và khoanh vùng loại tuổi mạnh mẽ nhất.
    print(f"Q6: {q6_ans}") # Bắn text Q6 lên console

    # Q7: Region nao co tong doanh thu cao nhat (trong giai doan sales_train)
    # sales.csv chi co [Date, Revenue, COGS] - khong co thong tin vung mien
    # => Phai tinh doanh thu theo vung thong qua orders + payments + geography
    # Buoc 1: Tach sales.csv thanh sales_train (train) va sales_test (test), luu ra file
    sales = pd.read_csv(os.path.join(data_dir, 'sales.csv'))
    sales['Date'] = pd.to_datetime(sales['Date'])
    sales_train = sales[sales['Date'] <= '2022-12-31'] # Giai doan train: 04/07/2012 -> 31/12/2022
    # Giai doan test: 01/01/2023 -> 01/07/2024 khong the lay tu sales.csv vi day la giai doan can du bao (tuong lai),
    # vi vay sales.csv chi chua lich su ban hang toi 2022-12-31. Mau cua valid submission nam o sample_submission.csv.
    sales_test_src = pd.read_csv(os.path.join(data_dir, 'sample_submission.csv'))
    sales_train.to_csv(os.path.join(data_dir, 'sales_train.csv'), index=False)
    sales_test_src.to_csv(os.path.join(data_dir, 'sales_test.csv'), index=False)
    print(f"  [Split] sales_train: {len(sales_train)} rows | sales_test: {len(sales_test_src)} rows")
    # Buoc 2: Loc orders chi trong giai doan train (khop voi sales_train)
    train_orders = orders[orders['order_date'] <= '2022-12-31']
    inspect_df(train_orders, "train_orders (Q7: filter orders <= 2022-12-31)")
    # Buoc 3: Tinh doanh thu theo vung = payments cua cac don trong giai doan train
    order_payments = payments.groupby('order_id')['payment_value'].sum().reset_index()
    train_with_pay = train_orders.merge(order_payments, on='order_id', how='left')
    train_geo = train_with_pay.merge(geo, on='zip', how='left')
    inspect_df(train_geo, "train_geo (Q7: after merge with geo)")
    q7_ans = train_geo.groupby('region')['payment_value'].sum().idxmax()
    print(f"Q7: {q7_ans}")

    # Q8: Công cụ thanh toán lúc đơn huỷ đa phần được cài bằng gì
    cancelled = orders[orders['order_status'] == 'cancelled'] # Rà ở tập đơn hàng các tập đơn dính cờ bị hủy bỏ ('cancelled')
    inspect_df(cancelled, "cancelled (Q8: filter order_status == cancelled)")
    q8_ans = cancelled['payment_method'].value_counts().idxmax() # Đếm tổng số lượng cho từng mặt thanh toán bị hủy, chắt lọc ra tên của mặt thanh toán đen vẩu nhất
    print(f"Q8: {q8_ans}") # Đẩy text giải đáp Q8 sang console
    
    # Q9: Tầm đồ size chuẩn nào mà bị back return rách việc nhất
    oi_prod = order_items.merge(products, on='product_id') # Nối bảng chi tiết đã mua vào rổ quần áo để móc ra tên size đã bán
    inspect_df(oi_prod, "oi_prod (Q9: merge order_items & products)")
    size_oi_counts = oi_prod['size'].value_counts() # Liệt kê đếm cặn xem từng size đã chốt mua là bao nhiêu mẻ
    returns_prod = returns.merge(products, on='product_id') # Tương tự với việc gỡ rổ lúc trả về để đối chiếu lấy form size
    size_ret_counts = returns_prod['size'].value_counts() # Đếm các mốc size mà đã bị hoàn trả về ròng rã
    size_ret_rate = (size_ret_counts / size_oi_counts).dropna() # Trích đoạn số lượng hoàn chia lại theo tổng mẻ đã chốt để nhìn thấy tỉ lệ rate rủi ro (lọc nan báo nhiễu)
    q9_ans = size_ret_rate.loc[['S','M','L','XL']].idxmax() # Đặc cách chỉ rút top 1 size xấu nhất nằm trong 4 loại size cơ sở đã đề cập ở Q9 .
    print(f"Q9: {q9_ans}") # Bóc phốt size xui xẻo nhất tại dòng này lên màn text Q9

    # Q10: Phương thức thanh toán trả góp đem trung bình gộp xông xênh cho tiền hóa đơn
    q10_ans = payments.groupby('installments')['payment_value'].mean().idxmax() # Gom chia theo các kì trả dần (installments) rồi lấy trung bình tiền đã chuyển trả để chọn mốc trả đem về con số giá trị lớn cực đại
    print(f"Q10: {q10_ans}") # Phản hồi số kì của đáp án Q10 bằng console

if __name__ == '__main__':
    main() # Khởi động vòng chạy main ngay khi chạy script trực tiếp ở shell
