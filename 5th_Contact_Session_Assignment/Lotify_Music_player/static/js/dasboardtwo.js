
// music player

const music_player = document.getElementById('audio_player')
const play_button = document.getElementById('play_btn')
const music_duration_display = document.getElementById('music_duration_display')
const time_played_display = document.getElementById('time_played_display')
const progressbar = document.getElementById('time_loader_bar')
const volume_mute = document.getElementById('volume_mute')
const music_title = document.getElementById('music_title')
const music_icon = document.getElementById('music_icon')
// 

function reset() {
    progressbar.style.width = `0%`
    play_button.innerHTML = `<i class="bi bi-play-fill"></i>`
    time_played_display.innerHTML = `00:00`;
}

function MusicListClick(path,image,name) {
    music_player.src = path
    music_icon.src = image
    music_title.innerHTML = name
    music_title.title = name
    reset()
    player()
}


play_button.addEventListener('click', () => {
    play_button.classList.toggle('play')
    if (play_button.classList.contains('play')) {
        music_player.pause()
        play_button.innerHTML = `<i class="bi bi-play-fill"></i>`
    } else {
        music_player.play()
        play_button.innerHTML = `<i class="bi bi-pause-fill"></i>`
    }
})

function player() {
    music_player.addEventListener('loadedmetadata', () => {
        const duration = music_player.duration
        const minutes = Math.floor(duration / 60)
        const seconds = Math.floor(duration % 60)
        const time_is = `${minutes}:${seconds}`
        music_duration_display.innerHTML = time_is
    })


    music_player.addEventListener('timeupdate', () => {
        const duration = music_player.duration;
        const currentTime = music_player.currentTime;
        const currentMinutes = Math.floor(currentTime / 60);
        const currentSeconds = Math.floor(currentTime % 60).toString().padStart(2, '0');
        if (currentSeconds === 'NaN') {
            currentSeconds = '00'
        }
        if (currentMinutes === 'NaN') {
            currentMinutes = '00'
        }
        const timePlayed = `${currentMinutes}:${currentSeconds}`;
        time_played_display.innerHTML = timePlayed;
        progressbar.style.width = 50
        const progressPercent = (currentTime / duration) * 100;
        progressbar.style.width = `${progressPercent}%`;
    });

    volume_mute.addEventListener('click', () => {
        volume_mute.classList.toggle('mute')
        if (volume_mute.classList.contains('mute')) {
            volume_mute.innerHTML = `<i class="bi bi-volume-mute-fill"></i>`
        } else {
            volume_mute.innerHTML = `<i class="bi bi-volume-up-fill"></i>`
        }
        music_player.muted = !music_player.muted
    })

}
