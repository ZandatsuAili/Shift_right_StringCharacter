#07610566 นายกณิศฑี รอดเผือก CS

def shiftRight(text):
    shift_text = ""
    for i in text:
        if(ord(i) >= 65 and ord(i) <= 90 #A-Z
                or ord(i) >= 97 and ord(i) <= 122 #a-z
                or ord(i) >= 3585 and ord(i) <= 3630): #ก-ฮ check ว่าอยู่ใน scale นี้ไหม
            i = ord(i) + 1 #บวก ascii ไป 1
        else:
            i = ord(i)
        shift_text = shift_text + chr(i) #รวมอักษร
    return shift_text

def reason(priolity):
    switcher = {
        "Some chocolate bars": "พกอาหารที่ให้พลังงานแก้ร่างกายไปก่อนอันดับแรก",
        "Emergency rations": "อาหารฉุกเฉินยามติดเกาะอย่างน้อยเคสที่ดีที่สุดมคือีผู้ช่วยเหลือมาช่วยก่อนที่อาหารฉุกเฉินจะหมด",
        "floating seat or cushion": "หลังจากเรือจมสิ่งนี้จะช่วยให้เราลอยน้ำพาไปถึงฝั่งได้",
        "rope": "เชือกสารพัดประโยชน์สามารถไปผูกกับ water proof เป็นเต๊นกันน้ำฝน",
        "water container": "สามารถช่วยพยุงตัวให้ลอยน้ำและรองน้ำค้างจากเต๊น water proof ได้",
        "water proof sheet": "กันน้ำค้างตอนกลางคืน",
        "shaving mirror": "เวลามีผู้ช่วยบินผ่านหรือมีเรือผ่านใช้แสงสะท้อนขอความช่วยเหลือ"
    }
    return switcher.get(priolity)

item = ["Some chocolate bars", "Emergency rations", "floating seat or cushion",
          "rope", "water container", "water proof sheet", "shaving mirror"]

print("----------------Shift------------------")
for priority in item:
    shift_str = shiftRight(priority) + ":" + shiftRight(reason(priority))
    normal_str = priority + ":" + reason(priority)
    print(shift_str)
print("---------------------------------------")

print("----------------Normal-----------------")
for priority in item:
    shift_str = shiftRight(priority) + ":" + shiftRight(reason(priority))
    normal_str = priority + ":" + reason(priority)
    print(normal_str)
print("---------------------------------------")