const card_element = `<div class="card">
                            <div class="imageholder"><img src="{% static 'images/playlist1.png'%}" alt="Playlist"></div>
                            <div class="card_info">
                                <h3>Focus Cu*</h3>
                                <p class="clamp">By Spotify Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                            </div>
                        </div>`

const array = Array(10).fill(1)
// const preview_card_cont = document.getElementById('preview_playlist_card_cont')
// const preview_card_cont2 = document.getElementById('preview_playlist_card_cont2')


// // array.map((e) => {
// //     return preview_card_cont.innerHTML += card_element
// // })
// array.map((e) => {
//     return preview_card_cont2.innerHTML += card_element
// })
// console.log('seeing dashboard')

function LocChange(slug) {
    window.location.href = `/dashboard/${slug}`
    console.log(slug);

    // Add your logic here

}