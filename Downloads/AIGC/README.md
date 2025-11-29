# AIGC — Hướng dẫn thiết lập môi trường


- Cài đặt Python 3.x 

---

## 🔧 1) Tạo môi trường ảo (PowerShell trên Windows)
1. Mở PowerShell (nên mở Run as Administrator nếu gặp lỗi chính sách thực thi).
2. (Tùy chọn) Nếu PowerShell chặn script, chạy tạm thời để cho phép kích hoạt venv:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
```

3. Tạo môi trường ảo trong thư mục dự án:

```powershell
python -m venv venv
```

4. Kích hoạt môi trường ảo trong PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Khi kích hoạt thành công, bạn sẽ thấy tên môi trường (ví dụ `(venv)`) xuất hiện trước dòng lệnh.

5. Nâng cấp pip (khuyến nghị):

```powershell
python -m pip install --upgrade pip
```

---

## 🛠️ 2) Cài đặt thư viện
- Cài đặt từ `requirements.txt` (nếu đã có):

```powershell
pip install -r requirements.txt
```

- Cài riêng lẻ (ví dụ `numpy`):

```powershell
pip install numpy
```

---

## 📌 3) Ghi dependencies vào `requirements.txt`
Sau khi cài các thư viện cần thiết, lưu chúng để người khác (và CI) có thể cài lại:

```powershell
pip freeze > requirements.txt
```

Bạn có thể chỉnh tay `requirements.txt` để ấn định phiên bản nếu cần.

---

## 🖥️ 4) Vô hiệu hóa môi trường ảo
Khi xong việc:

```powershell
deactivate
```

---

## 🧭 5) Ghi chú cho macOS / Linux (bash)
- Tạo venv:

```bash
python3 -m venv venv
```

- Kích hoạt:

```bash
source venv/bin/activate
```

- Sau đó dùng các lệnh `pip install`, `pip freeze > requirements.txt`, và `deactivate` như trên.

---

## 📝 6) Thêm vào `.gitignore`

```
venv/
__pycache__/
*.pyc
 Lưu ý: Kho lưu trữ này đã bao gồm một mẫu `requirements.txt` và một tệp `.gitignore`. Cập nhật `requirements.txt` với các gói mà dự án của bạn thực sự cần, hoặc chạy `pip freeze > requirements.txt` sau khi cài đặt các gói.

---

## ▶️ 7) Chạy tệp thử nghiệm
- Ví dụ chạy `test.py` trong môi trường ảo đã kích hoạt:

```powershell
python test.py
```

---
