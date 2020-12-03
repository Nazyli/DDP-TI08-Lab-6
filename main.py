# Nama: Evry Nazyli Ciptanto
# NIM: 0110220045
# Kelas: TI08

def jumlah_batas(nums, batas):
  # Tulis kode fungsi jumlah_batas() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  total = 0; #membuat variabel penampung total
  # membuat perulangan list nums
  for i in nums:
    # jika ada nilai lebih dari batas
    if i > batas:
      # hitung total nilai nya
      total += i
  # mengembalikan nilai total
  return total

def list_nonvokal(s):
  # Tulis kode fungsi list_nonvokal() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # membuat list kosong untuk penampung
  newList = []
  # melakukan perulangan sebanyak string s
  for i in s:
    # jika chart i tidak berupa aiueo
    if i.lower() not in "aiueo":
      # menambahkan element baru dengan nilai i
      newList.append(i) 
  # mengembalikan nilai list baru 
  return newList

def list_modify(alist, command, position, value=None):
  # Tulis kode fungsi list_modify() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # jika command add
  if command =='add':
    # jika position start
    if position == 'start':
      # insert element di index pertama
      alist.insert(0,value)
    # jika position end
    elif position =='end':
      # insert element di index terakhir
      alist.append(value)
  # jika command remove    
  elif command =='remove':
    # jika position start
    if position == 'start':
      # hapus element di index pertama
      del alist[0]
    # jika position end
    elif position =='end':
       # hapus element di index terakhir
      del alist[len(alist)-1]
  # mengembalikan nilai list baru
  return alist





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = jumlah_batas([8, 7, 6, 10, 1], 5)
  print(f"jumlah_batas([8, 7, 6, 10, 1], 5) = {r} \n(solusi: 31)")
  print()
  r = jumlah_batas([1, -7, -10, 1], -5)
  print(f"jumlah_batas([1, -7, -10, 1], -5) = {r} \n(solusi: 2)")
  print()
  r = list_nonvokal('Halo')
  print(f"list_nonvokal('Halo') = {r} \n(solusi: ['H', 'l'])")
  print()
  r = list_nonvokal('AAAAAooooo')
  print(f"list_nonvokal('AAAAAooooo') = {r} \n(solusi: [])")
  print()
  r = list_nonvokal('Saya cinta programming')
  print(f"list_nonvokal('Saya cinta programming') = {r} \n(solusi: ['S', 'y', ' ', 'c', 'n', 't', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek') = {r} \n(solusi: ['bebek', 'ayam', 'ikan', 'kucing'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek') = {r} \n(solusi: ['ayam', 'ikan', 'kucing', 'bebek'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start') = {r} \n(solusi: ['ikan', 'kucing'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end') = {r} \n(solusi: ['ayam', 'ikan'])")
  print()

if __name__ == '__main__':
  test()