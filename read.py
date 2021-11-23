data = []
count = 0  #剛開始是零 因為 最開始 是還沒讀到資料
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  #count = count +1
		if count % 1000 == 0:   # %求餘數
			print(len(data))
#print(len(data))
#print(data[0])    # 印出data的第一筆資料
#print('----------------------')
#print(data[1])
print('檔案讀取完畢, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:  #data裡每一筆資料(留言 )叫d
	sum_len = sum_len +len(d) # sum_len += len(d)
	# print(sum_len)

print('留言的平均長度是', sum_len/len(data))

new = []   #篩選
for d in data: #d是每一筆留言(字串) data就是裝所有d 的(清單)
	if len(d) < 100:
		new.append(d) #小於100的留言增加在new[]裡面.
print('一共有', len(new), '筆留言長度小於100')  #print對齊new
                             #等loop for 都跑完 print才印一次
print(new[0])
print(new[1])