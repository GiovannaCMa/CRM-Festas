const links = document.querySelectorAll('.sidebar a');


links.forEach(link => {
  link.addEventListener('click', function() {
    
    links.forEach(l => l.classList.remove('active'));
    // deixa o bregueso marcado
    this.classList.add('active');

    localStorage.setItem('activeLink', this.href);
  });
});

window.addEventListener('load', () => {
  const activeLink = localStorage.getItem('activeLink'); //deixa marcado depois de atualizar a pagina
  if (activeLink) {
    links.forEach(link => {
      if (link.href === activeLink) {
        link.classList.add('active');
      }
    });
  }
});

// código para o calendário
const calendar = document.getElementById("calendar");
let currentDate = new Date();

function renderCalendar(date) {
  const year = date.getFullYear();
  const month = date.getMonth();

  const firstDay = new Date(year, month, 1);
  const lastDay = new Date(year, month + 1, 0);
  const today = new Date();

  const monthName = date.toLocaleString("pt-BR", { month: "long" });

  let daysHTML = "";
  let weekdaysHTML = "";

  const weekdays = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"];
  weekdays.forEach((d) => (weekdaysHTML += `<div>${d}</div>`));

  // espaços antes do 1º dia
  for (let i = 0; i < firstDay.getDay(); i++) {
    daysHTML += `<div></div>`;
  }

  for (let d = 1; d <= lastDay.getDate(); d++) {
    const isToday =
      d === today.getDate() &&
      month === today.getMonth() &&
      year === today.getFullYear();

    daysHTML += `<div class="day${isToday ? " today" : ""}" data-day="${d}">${d}</div>`;
  }

  calendar.innerHTML = `
    <div class="calendar-header">
      <button id="prevMonth">◀</button>
      <h3>${monthName} ${year}</h3>
      <button id="nextMonth">▶</button>
    </div>
    <div class="weekdays">${weekdaysHTML}</div>
    <div class="days">${daysHTML}</div>
  `;

  document.getElementById("prevMonth").onclick = () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar(currentDate);
  };

  document.getElementById("nextMonth").onclick = () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar(currentDate);
  };

  document.querySelectorAll(".day").forEach((day) => {
    day.addEventListener("click", (e) => {
      document.querySelectorAll(".day").forEach((d) => d.classList.remove("selected"));
      e.target.classList.add("selected");
    });
  });
}

renderCalendar(currentDate);
