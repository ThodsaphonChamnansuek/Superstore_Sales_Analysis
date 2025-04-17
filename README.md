# 🛒 Superstore Sales Analysis

โครงการนี้เป็นการวิเคราะห์ยอดขายรายเดือนจากชุดข้อมูล Superstore โดยใช้ Python และเครื่องมือด้าน Data Visualization เช่น Pandas, Matplotlib และ Seaborn เพื่อแสดงแนวโน้มยอดขายในช่วงปีต่าง ๆ และเน้นเจาะลึกเฉพาะปี 2017

---

## 📂 ข้อมูลที่ใช้

ใช้ชุดข้อมูล `Superstore.csv` ซึ่งประกอบไปด้วยข้อมูลการขาย เช่น:
- วันที่สั่งซื้อ (`Order Date`)
- ยอดขาย (`Sales`)
- ประเภทสินค้า (`Category`, `Sub-Category`)
- ลูกค้า และภูมิภาค

---

## 📊 สิ่งที่ทำในโปรเจกต์นี้

- แปลงวันที่ให้อยู่ในรูปแบบที่เหมาะสม
- สร้างคอลัมน์ `Month`, `Year`, และ `Month_Year`
- รวมยอดขายตามเดือน (`Monthly Sales`)
- วาดกราฟยอดขายรายเดือนโดย:
  - ใช้ `Seaborn` สำหรับการวิเคราะห์แนวโน้ม
  - ปรับแกน X/Y และแสดงเส้นค่าเฉลี่ย
  - กรองข้อมูลเฉพาะปี 2017 เพื่อการวิเคราะห์เฉพาะช่วงเวลา

---

## 🛠️ เครื่องมือที่ใช้

- Python 3.x
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

---

## ▶️ วิธีการใช้งาน

1. ดาวน์โหลดหรือโคลนโปรเจกต์นี้:
   ```bash
   git clone https://github.com/your-username/superstore-sales-analysis.git
   cd superstore-sales-analysis
