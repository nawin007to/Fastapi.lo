const form = document.querySelector("#employee-form");
const formStatus = document.querySelector("#form-status");
const listStatus = document.querySelector("#list-status");
const employeeList = document.querySelector("#employee-list");
const submitButton = document.querySelector("#submit-button");

function setStatus(element, message, type = "") {
  element.textContent = message;
  element.className = `status ${type}`.trim();
}

async function readError(response) {
  const body = await response.json().catch(() => ({}));
  return typeof body.detail === "string" ? body.detail : `เกิดข้อผิดพลาด (${response.status})`;
}

async function loadEmployees() {
  setStatus(listStatus, "");
  try {
    const response = await fetch("/employees");
    if (!response.ok) throw new Error(await readError(response));
    const employees = await response.json();
    employeeList.replaceChildren();

    if (employees.length === 0) {
      const row = document.createElement("tr");
      const cell = document.createElement("td");
      cell.colSpan = 5;
      cell.className = "empty";
      cell.textContent = "ยังไม่มีข้อมูลพนักงาน";
      row.append(cell);
      employeeList.append(row);
      return;
    }

    for (const employee of employees) {
      const row = document.createElement("tr");
      for (const value of [employee.id, employee.name, employee.age, employee.position, employee.gender || "—"]) {
        const cell = document.createElement("td");
        cell.textContent = value;
        row.append(cell);
      }
      employeeList.append(row);
    }
  } catch (error) {
    employeeList.replaceChildren();
    setStatus(listStatus, `โหลดข้อมูลไม่ได้: ${error.message}`, "error");
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  submitButton.disabled = true;
  setStatus(formStatus, "กำลังบันทึก...");
  const formData = new FormData(form);
  const employee = {
    name: formData.get("name").trim(),
    age: Number(formData.get("age")),
    position: formData.get("position").trim(),
    gender: formData.get("gender") || null,
  };

  try {
    const response = await fetch("/employees", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(employee),
    });
    if (!response.ok) throw new Error(await readError(response));
    const savedEmployee = await response.json();
    form.reset();
    setStatus(formStatus, `บันทึกข้อมูลของ ${savedEmployee.name} แล้ว (ID ${savedEmployee.id})`, "success");
    await loadEmployees();
  } catch (error) {
    setStatus(formStatus, `บันทึกไม่สำเร็จ: ${error.message}`, "error");
  } finally {
    submitButton.disabled = false;
  }
});

document.querySelector("#refresh-button").addEventListener("click", loadEmployees);
loadEmployees();
