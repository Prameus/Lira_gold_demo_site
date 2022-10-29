var updateBtns = document.getElementsByClassName('add-to-cart')
console.log(updateBtns)

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product:',productId,'action:',action)
 
        updateUserOrder(productId,action)
        if (user === 'AnonymousUser') {
            console.log('not logged in ')
        }
        else {
            console.log('user is logged in, sending data...')
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })

    .then((response) => {
    return response.json()   
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}