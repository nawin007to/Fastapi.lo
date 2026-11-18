# fastapi-starter

โปรเจกต์ฝึกเขียน FastAPI จัดโครงสร้างแบบ `src/` และจัดการ dependency ด้วย `uv` ตามรูปแบบในโฟลเดอร์ `pythonpi/task-management`

## ติดตั้งและรัน

```powershell
uv sync
uv run fastapi dev src/fastapi_starter/main.py
```

เปิดหน้าเอกสาร API ที่ <http://127.0.0.1:8000/docs>

## โครงสร้าง

```text
src/fastapi_starter/
  __init__.py       คำสั่งเริ่มต้นของแพ็กเกจ
  main.py           จุดเริ่มต้นของแอป FastAPI
  router.py         API endpoints
  database.py       เตรียมไว้สำหรับเชื่อมต่อฐานข้อมูล
  model.py          เตรียมไว้สำหรับ SQLModel models
  schema.py         เตรียมไว้สำหรับ request/response schemas
```
