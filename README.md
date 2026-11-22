# PyJen001 – โปรแกรมบวกเลข + CI/CD ด้วย Jenkins

งานประจำวันที่ 27 ต.ค. 2569 (Jenkins #4) รายวิชา 832208/632218
จัดทำโดย Peeraphat Aisising รหัสนักศึกษา 6752410001 (PyJen**001** = 3 ตัวท้ายของรหัสนักศึกษา)

## โปรแกรม
```bash
python calculator.py 5 7     # 5 + 7 = 12
```

## CI/CD
เมื่อแก้โค้ดแล้ว push ขึ้น GitHub, Jenkins จะตรวจพบภายใน 2 นาที (`pollSCM('H/2 * * * *')`) แล้วทำงานอัตโนมัติ:

1. **Checkout** ดึงโค้ดล่าสุดจาก GitHub
2. **Setup Python** สร้าง venv และติดตั้ง `requirements.txt`
3. **Lint** ตรวจคุณภาพโค้ดด้วย flake8
4. **Test** รัน `test_calculator.py` ด้วย pytest (6 กรณีทดสอบ)
5. **Build** บีบอัดโค้ดเป็น `dist/PyJen001-<เลข build>.zip`
6. **Deploy** คัดลอกโปรแกรมไปที่ `C:\JenkinsDeploy\PyJen001` แล้วรันทดสอบ
