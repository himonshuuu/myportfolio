document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault()
        const target = document.querySelector(this.getAttribute('href'))
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start',
            })
        }
    })
})

window.addEventListener('scroll', function () {
    const scrollTop = document.getElementById('scrollTop')
    if (window.pageYOffset > 300) {
        scrollTop.style.opacity = '1'
        scrollTop.style.pointerEvents = 'auto'
    } else {
        scrollTop.style.opacity = '0'
        scrollTop.style.pointerEvents = 'none'
    }
})

document.querySelectorAll('.group').forEach(card => {
    card.addEventListener('mouseenter', function () {
        this.style.boxShadow = '0 20px 40px rgba(0,0,0,0.3), 0 0 20px rgba(245, 158, 11, 0.1)'
    })

    card.addEventListener('mouseleave', function () {
        this.style.boxShadow = ''
    })
})
const phrases = [
    'Building fast, minimal, hackable tools with personality.',
    'Full-stack developer who believes in fun developer experiences.',
    'High school student crafting elegant solutions to complex problems.',
    'Arch Linux user, Python enthusiast, and terminal tool creator.',
]

let currentPhrase = 0
const heroSubtitle = document.querySelector('main section:first-child p')

if (heroSubtitle) {
    function typeWriter() {
        setInterval(() => {
            heroSubtitle.style.opacity = '0'
            setTimeout(() => {
                heroSubtitle.innerHTML = phrases[currentPhrase]
                heroSubtitle.style.opacity = '1'
                currentPhrase = (currentPhrase + 1) % phrases.length
            }, 500)
        }, 4000)
    }
}