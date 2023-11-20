def ascending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    # Input 10 angka
    nomor = [int(input(f"Input angka ke-{i+1}: ")) for i in range(10)]

    # Merubah input 10 angka menjadi array
    array = nomor.copy()

    # Input pilihan urutan (ascending atau descending)
    pilih = input("Pilih urutan (ascending/descending): ").lower()

    # Validasi pilihan urutan
    if pilih not in ['ascending', 'descending']:
        print("Pilihan urutan tidak valid. Program berhenti.")
        return

    # Menampilkan array input
    print("\nArray Input:", array)

    # Menggunakan fungsi urutan sesuai pilihan
    if pilih == 'ascending':
        ascending(array)
        
    else:
        descending(array)

    # Menampilkan hasil array setelah diurutkan
    print("Array Setelah Diurutkan:", array)

if __name__ == "__main__":
    main()
