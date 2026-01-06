function searchContact() {
    let val = document.getElementById("search").value.toLowerCase();
    let rows = document.querySelectorAll("#table tr");
    rows.forEach((r, i) => {
        if (i === 0) return;
        r.style.display = r.innerText.toLowerCase().includes(val) ? "" : "none";
    });
}

function toggleDark() {
    document.body.classList.toggle("dark");
}

function openEdit(name, phone, email) {
    document.getElementById("modal").style.display = "block";
    old.value = name;
    mname.value = name;
    mphone.value = phone;
    memail.value = email;
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}
