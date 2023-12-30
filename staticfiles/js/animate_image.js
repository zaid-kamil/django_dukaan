let products = document.querySelectorAll('.product-card')

products.forEach(card => {
    card.addEventListener('mouseover', () =>{
        card.style.transform = 'scale(1.1) rotate(2deg)'
        card.querySelector('.product-img').style.filter = 'grayscale(0)'
    })
    card.addEventListener('mouseout', () =>{
        card.style.transform = 'scale(1) rotate(0deg)'
        card.querySelector('.product-img').style.filter = 'grayscale(100)'
    })
    // card.addEventListener('click', () =>{})
    // card.addEventListener('dblclick', () =>{})
    // card.addEventListener('contextmenu', () =>{})
})