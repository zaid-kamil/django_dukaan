let showBtn = document.querySelector('#show-btn')
let sidebar = document.querySelector('.sidebar')
let isVisible = false
sidebar.style.display = 'none' 

showBtn.addEventListener('click', ()=>{
    if(isVisible){
        sidebar.style.display = 'none'
        isVisible = false
        showBtn.innerHTML = 'Show Filter'
    }else{
        sidebar.style.display = 'block'
        isVisible = true
        showBtn.innerHTML = 'Hide Filter'   
    }
})