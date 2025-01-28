const element = `<div class="todo_card">
                    <div class="comp_det_cont">
                        <div class="completed_check_box"><input type="checkbox"  id=""></div>
                        <div class="todo_details">
                            <p>27-01-2025 <span>High</span></p>
                            <h2>Running to God!</h2>
                        </div>
                    </div>
                    <div class="todo_hashtag">
                        <p>#gospel</p>
                    </div>
                </div>`

const todo_lists_cont = document.getElementById('todo_lists_cont')
const array_num = Array(6).fill(0)



array_num.map((_) => {
    return todo_lists_cont.innerHTML+= element
})

todo_lists_cont.addEventListener('dblclick', (event) => {
    const target = event.target;
    if (target.closest('.todo_card')) {
        confirm('Do you want to delete the dodo list?');
        // Add your double-click handling logic here
    }
});

const todo_dates = ['12-01-2025', '17-01-2025']


const calendarDays = document.getElementById('calendarDays');
const monthYear = document.getElementById('monthYear');
const prevMonth = document.getElementById('prevMonth');
const nextMonth = document.getElementById('nextMonth');

let currentDate = new Date();

function renderCalendar(todoDates=[]) {
    calendarDays.innerHTML = '';
    const month = currentDate.getMonth();
    const year = currentDate.getFullYear();
    monthYear.textContent = `${currentDate.toLocaleString('default', { month: 'long' })} ${year}`;

    const firstDayOfMonth = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    for (let i = 0; i < firstDayOfMonth; i++) {
        const emptyCell = document.createElement('div');
        emptyCell.classList.add('empty');
        calendarDays.appendChild(emptyCell);
    }

    const today = new Date();
    const isCurrentMonth = today.getMonth() === month && today.getFullYear() === year;

    // const todoDates = ['12-01-2025']; // Example array of dates
    const formattedTodoDates = todoDates.map(date => {
        const [day, month, year] = date.split('-');
        const todoDate = new Date(`${year}-${month}-${day}`);
        if (todoDate.getMonth() === currentDate.getMonth() && todoDate.getFullYear() === currentDate.getFullYear()) {
            return todoDate.getDate();
        }
        return null;
    }).filter(date => date !== null);

    for (let i = 1; i <= daysInMonth; i++) {
        const dayCell = document.createElement('div');
        dayCell.textContent = i;
        if (isCurrentMonth && i === today.getDate()) {
            dayCell.classList.add('today');
        }
        if (formattedTodoDates.includes(i)) {
            dayCell.classList.add('date_on_todo');
        }
        calendarDays.appendChild(dayCell);
    }
}
prevMonth.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar(todo_dates);
});

nextMonth.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar(todo_dates);
});

renderCalendar(todo_dates);