var updateBtns = document.getElementsByClassName("update-cart")

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product id', productId,'action', action)

        addCookieItem(productId, action)
    })

}
function addCookieItem(productId, action) {
    let cartCookie = getCookie("cart")
    
    let cart = {
        ...JSON.parse(cartCookie)
    }
    console.log(cart)
    if (action === 'add') {
        console.log("Cart:", cart)
        if (cart[productId] === undefined) {
            cart[productId] = { 'quantity': 1 }
        } else {
            cart[productId]['quantity'] += 1
        }
        $("#productId_"+ productId +" .current-quantity").text(cart[productId]['quantity'])
    }
    if (action === 'remove') {
        cart[productId]['quantity'] -= 1
        
        if (cart[productId]['quantity'] < 1) {
            console.log('delete item')
            delete cart[productId]
            $("#productId_"+ productId).remove()


        }else{
            
            $("#productId_"+ productId +" .current-quantity").text(cart[productId]['quantity'])
        }

    }
    // var qtyTotal =0;
    // for (const key in cart) {
    //     if (productId===key) {
    //         var qty = cart[key]['quantity']
    //     }
    //     qtyTotal = cart[key]['quantity']
    //     }
    // if (Number(qty)<1) {
    //     location.reload()
    // }
    // try {
    //     document.getElementById(productId+"qty").innerHTML= qty;
    // document.getElementById('qty').innerHTML=qtyTotal;
    // } catch (error) {
    //     console.log(error)
    // }
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    // location.reload()
}

// function updateUserOrder(productId, action) {
//     console.log("User is authenticated")

//     var url = 'updateItem/'

//     fetch(url,{
//         method:"Post",
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFToken': csrftoken
//         },
//         body:JSON.stringify({
//             'productId':productId,
//             'action':action
//         })
//     }).then((res)=>{
//         return res.json()
//     }).then((data)=>{
//         console.log('data:',data)
//         location.reload()
//     })
// }

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}



$(document).ready(function () {
    var url = window.location.pathname;
    // url =  url.split("/")[1]
    console.log(url);
      $('nav.nav-menu a[href="'+ url +'"]').parent().addClass('active');
      $('nav.nav-menu a').filter(function() {
           return this.href == url;
      }).parent().addClass('active');
  });

//   checkout cart validation
function checkCart(){
    const cartCookie = JSON.parse(getCookie('cart'))
    if(!cartCookie) {
      $(".proceed-btn").addClass('d-none')
      $(".checkout-btn").addClass('d-none')
      return false

  
    }else if($.isEmptyObject(cartCookie)){
      //   console.log(cartCookie)
      $(".proceed-btn").addClass('d-none')
      $(".checkout-btn").addClass('d-none')
      return false
    }
}

checkCart()


  
 