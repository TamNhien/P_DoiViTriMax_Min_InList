L = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ").split(',')))
min_index, max_index = L.index(min(L)), L.index(max(L))
L[min_index], L[max_index] = L[max_index], L[min_index]
print("Danh sách sau khi biến đổi: ", L)

