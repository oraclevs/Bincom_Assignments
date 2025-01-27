
const search_result_modal = document.getElementById('search_result_modal')
const search_result_modal_close_btn = document.getElementById('search_result_modal_close_btn')
const search_input = document.getElementById('search_input')
const search_input_button = document.getElementById('search_input_button')

const url = new URL(window.location.href);
search_result_modal_close_btn.addEventListener('click', () => {
    search_result_modal.style.display = 'none'
    url.searchParams.delete('q')
    window.history.replaceState({}, document.title, url.href)
})
if(url.searchParams.get('q')){
    search_result_modal.style.display = 'block'
}


search_input_button.addEventListener('click', () => {
    if (search_input.value.length >= 3) {
        search_result_modal.style.display = 'block'
        const url = new URL(window.location.href);
        url.searchParams.set('q', search_input.value);
        window.location.href = url.href
        search_result_modal.style.display = 'block'
    } else if (search_input.value.length < 3) {
        search_result_modal.style.display = 'none'
        alert('Please enter at least 3 characters!')
    }
})
