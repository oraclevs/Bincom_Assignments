

const todo_lists_cont = document.getElementById('todo_lists_cont')
const array_num = Array(6).fill(0)


let populate_todos = (ContainerHtml, Data) => {
    return (ContainerHtml.innerHTML = Data.map((x) => {
        let { completed, date_added, id, priority, tag, todo, todo_list_id, user_id } = x;
        return `
     <div class="todo_card" id="todo_card${id}">
                    <div class="comp_det_cont">
                        <div class="completed_check_box "><input type="checkbox"   id="checked${id}"></div>
                        <div class="todo_details">
                            <p>${date_added} <span>${priority}</span></p>
                            <h2 class="${completed ?"line_through":""}">${todo}</h2>
                        </div>
                    </div>
                    <div class="todo_hashtag">
                        <p>${tag}</p>
                    </div>
                </div>
      `;
    }).join(""));
};

// get todos

const getTodos = async () => {
    const get_csrf_T = await fetch('/get_it/');
    if (get_csrf_T.ok) {
        const response = await get_csrf_T.json();
        const csrfToken = response.td;
        const get_todos = await fetch('/get_todos/', {
            method: 'Get',
            headers: {
                'X-CSRFToken': csrfToken
            }
        });
        const todos = await get_todos.json()
        populate_todos(todo_lists_cont, todos)
        for (let i = 0; i < todos.length; i++) {
            const todo_card = document.getElementById(`todo_card${todos[i].id}`)
            const check_mrk = document.getElementById(`checked${todos[i].id}`);
            check_mrk.checked = todos[i].completed;
            check_mrk.addEventListener('click', (e) => {
                const mrk_comp = async () => {
                    const completed = e.target.checked
                    const form = new FormData()
                    form.append('completed', completed)
                    form.append('todo_id',todos[i].id)
                    request_mrk_complete = await fetch('/mark_completed/', {
                        method: 'POST',
                        body: form,
                        headers: {
                            'X-CSRFToken': csrfToken
                        }
                    })
                    if (request_mrk_complete.ok) {
                        getTodos()
                    }
                    else {
                        alert('Failed to mark as complete due to an error!')
                    }
                }
                mrk_comp()
            })
            todo_card.addEventListener('dblclick', (event) => {
                if (confirm(`Do you want to delete the todo list? ${todos[i].todo} `)) {
                    const del = async () => {
                        form = new FormData()
                        form.append('todo_id', todos[i].id)
                        request_delete = await fetch('/delete_todo/', {
                            method: 'POST',
                            body: form,
                            headers: {
                                'X-CSRFToken': csrfToken
                            }
                        })
                        if (request_delete.ok) {
                            getTodos()
                        }
                        else {
                            alert('Failed to delete due to an error!')
                        }
                    }
                    del()
                }
            });
        }
    }
}
getTodos()






const todo_dates = ['12-01-2025', '17-01-2025']


const calendarDays = document.getElementById('calendarDays');
const monthYear = document.getElementById('monthYear');
const prevMonth = document.getElementById('prevMonth');
const nextMonth = document.getElementById('nextMonth');
const day_dis = document.getElementById('day_dis')
const month_dis = document.getElementById('month_dis')

let currentDate = new Date();
day_dis.innerHTML = currentDate.getDate()
month_dis.innerHTML = currentDate.toLocaleString('default', { month: 'short' }).substring(0, 3);

function renderCalendar(todoDates = []) {
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

// form
const todo_input_form = document.getElementById('todo_input_form')
const more_options = document.getElementById('more_options')
const tag_add_input = document.getElementById('tag_add_input')
const Priority_select = document.getElementById('Priority_select')
const todo_input = document.getElementById('todo_input')

todo_input.addEventListener('input', () => {
    if (todo_input.value.length > 3) {
        more_options.style.display = 'block';
    }
    // console.log(todo_input.value)
})
todo_input_form.addEventListener('submit', async (e) => {
    e.preventDefault()
    more_options.style.display = 'none'
    if (todo_input.value.length < 3) {
        alert('Todo has to be at least 4 characters')
        return
    }
    if (tag_add_input.value.length < 3) {
        alert('Tag must be more than 3 characters')
        more_options.style.display = 'block';
        return
    }
    if (Priority_select.value === "select") {
        alert('Please select a priority for the todo')
        more_options.style.display = 'block';
        return
    }
    const data = {
        todo: todo_input.value,
        priority: Priority_select.value,
        tag: "#" + tag_add_input.value
    }
    todo_input.value = ""
    Priority_select.value = "select"
    tag_add_input.value = ""
    const form = new FormData()
    form.append("todo", data.todo)
    form.append("priority", data.priority)
    form.append("tag", data.tag)
    const get_csrf_T = await fetch('/get_it/');
    if (get_csrf_T.ok) {
        const response = await get_csrf_T.json();
        const csrfToken = response.td;
        const send_todo = await fetch('/todo/save/', {
            method: 'POST',
            body: form,
            headers: {
                'X-CSRFToken': csrfToken
            }
        });
        if (send_todo.ok) {
            getTodos()
        } else {
            alert('Failed to add todo');
        }
    } else {
        console.error("Failed to fetch CSRF token");
    }
})


