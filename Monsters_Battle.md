# Tiêu diệt quái vật bằng phép nổ

## 1. Tóm tắt đề bài
- Có `N` con quái vật, con thứ `i` có máu `H[i]`.
- Mỗi lần dùng phép nổ, ta chọn **một mục tiêu**:
  - Mục tiêu trực tiếp nhận `A` sát thương.
  - Tất cả quái vật còn lại nhận `B` sát thương.
- Biết `A > B`.
- Yêu cầu: Tìm **số lần nổ ít nhất** để tất cả quái vật có máu ≤ 0.

**Ràng buộc:**
- `1 ≤ N ≤ 2 * 10^5`
- `1 ≤ B < A ≤ 10^9`
- `1 ≤ H[i] ≤ 10^9`

## 2. Phân tích và chia bài toán con

### 2.1. Nhận xét quan trọng
- Mỗi lần nổ, **mọi quái vật đều nhận ít nhất `B` sát thương** (dù là mục tiêu hay không).
- Nếu dùng tổng cộng `m` lần nổ:
  - Mỗi quái vật nhận **`m * B` sát thương từ splash**.
  - Quái vật `i` chỉ cần được target thêm nếu `H[i] > m * B`.
  - Số lần cần target quái vật `i` là: ceil((H[i] - m * B) / (A - B))
- Tổng số lần target trên tất cả quái vật **không được vượt quá `m`**.

### 2.2. Tính đơn điệu
- Nếu `m` lần nổ đủ để giết hết quái → `m + 1` lần cũng đủ.
- Nếu `m` lần nổ không đủ → `m - 1` lần cũng không đủ.
- → Có thể **chặt nhị phân** trên `m`.

### 2.3. Bài toán con với `m` cố định
> Kiểm tra xem với `m` lần nổ, có thể tiêu diệt hết quái vật không?

**Cách kiểm tra:**
- Với mỗi quái vật `h`:
- Nếu `h ≤ m * B`: không cần target.
- Ngược lại: cần target `ceil((h - m * B) / (A - B))` lần.
- Cộng dồn số lần target cần thiết. Nếu tổng ≤ `m` → thỏa mãn.

### 2.4. Cận trên của `m`
- Trường hợp xấu nhất: `m = max(H) // B + 1`.
- Cận dưới: `m = 1`.

## 3. Thuật toán tổng quát

1. Đọc input: `N, A, B` và mảng `H`.
2. Đặt `lo = 1`, `hi = max(H) // B + 1`.
3. Chặt nhị phân:
- Với `mid = (lo + hi) // 2`, kiểm tra `check(mid)`.
- Nếu `check(mid)` đúng → ghi nhận `res = mid`, `hi = mid - 1`.
- Ngược lại → `lo = mid + 1`.
4. In `res`.

**Hàm `check(m)`:** duyệt qua từng quái vật, tính số lần target cần thiết, cộng dồn, so sánh với `m`.

## 4. Độ phức tạp
- Mỗi lần `check`: O(N).
- Số lần `check`: O(log(max(H) // B)) ≈ O(log(10^9)) ≈ 30.
- Tổng: O(N log H) ≈ 2 * 10^5 * 30 = 6 * 10^6 phép toán → chạy tốt trong Python.

## 5. Code tham khảo

```python
import sys

def check(H, a, b, m):
"""Kiểm tra với m lần nổ có giết hết quái không."""
k = 0  # tổng số lần cần target
for h in H:
    if h > m * b:
        # Sát thương còn thiếu sau khi trừ splash
        dmg = h - m * b
        # Mỗi lần target thêm được (a - b) sát thương
        k += (dmg + (a - b) - 1) // (a - b)
return k <= m


def solve():
input = iter(sys.stdin.read().split())
N = int(next(input))
A = int(next(input))
B = int(next(input))
H = [int(next(input)) for _ in range(N)]

lo = 1
hi = max(H) // B + 1
res = hi

while lo <= hi:
    mid = lo + (hi - lo) // 2
    if check(H, A, B, mid):
        res = mid
        hi = mid - 1
    else:
        lo = mid + 1

sys.stdout.write(str(res))


if __name__ == "__main__":
solve()
```