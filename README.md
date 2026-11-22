# fastapi-starter

โปรเจกต์ฝึกเขียน FastAPI จัดโครงสร้างแบบ `src/` และจัดการ dependency ด้วย `uv` ตามรูปแบบในโฟลเดอร์ `pythonpi/task-management`

## ติดตั้งและรัน

```powershell
uv sync
uv run uvicorn fastapi_starter.main:app --host 127.0.0.1 --port 8001
```

เปิดหน้าเว็บที่ <http://127.0.0.1:8001/> และเอกสาร API ที่ <http://127.0.0.1:8001/docs>

หน้าเว็บกรอกและดูข้อมูลพนักงานจะส่งข้อมูลไปยัง `POST /employees` และอ่านรายการจาก `GET /employees` ผ่าน FastAPI

## โครงสร้าง

```text
src/fastapi_starter/
  __init__.py       คำสั่งเริ่มต้นของแพ็กเกจ
  main.py           จุดเริ่มต้นของแอป FastAPI
  router.py         API endpoints
  database.py       เตรียมไว้สำหรับเชื่อมต่อฐานข้อมูล
  model.py          เตรียมไว้สำหรับ SQLModel models
  schema.py         เตรียมไว้สำหรับ request/response schemas
static/
  index.html        โครงหน้าเว็บ
  css/style.css     รูปแบบและการจัดหน้า
  js/app.js         ส่ง/โหลดข้อมูลผ่าน API
```
