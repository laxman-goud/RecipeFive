document.addEventListener("DOMContentLoaded", () => {
    const cartList = document.getElementById('cart-list');

    // Remove button functionality
    cartList.addEventListener('click', (event) => {
        if (event.target.classList.contains('remove-button')) {
            const cartItem = event.target.closest('.cart-item');
            cartItem.remove(); // Remove the item from the cart
        }
    });

    // Update quantity
    cartList.addEventListener('change', (event) => {
        if (event.target.classList.contains('quantity-input')) {
            const input = event.target;
            if (input.value < 1) {
                input.value = 1; // Ensure quantity is at least 1
            }
        }
    });
});


// // Select all remove buttons
// const removeButtons = document.querySelectorAll('.remove-button');

// // Loop through each remove button and add an event listener
// removeButtons.forEach(button => {
//     button.addEventListener('click', function (e) {
//         // Get the parent list item (the cart item) and remove it
//         const cartItem = e.target.closest('.cart-item');
//         cartItem.remove();
//     });
// });

// Select all remove buttons
const removeButtons = document.querySelectorAll('.remove-button');

// Loop through each remove button and add an event listener
removeButtons.forEach(button => {
    button.addEventListener('click', function (e) {
        // Get the parent list item (the cart item) and remove it
        const cartItem = e.target.closest('.cart-item');
        cartItem.remove();
    });
});

// Redirect to selected delivery service
document.getElementById('proceed-button').addEventListener('click', function () {
    // Get the selected radio button
    const selectedService = document.querySelector('input[name="delivery"]:checked');
    if (selectedService) {
        // Redirect to the corresponding website
        window.location.href = selectedService.value;
    }
});

function proceedToCheckout() {
    // Get the selected delivery service
    const deliveryService = document.querySelector('input[name="delivery"]:checked').value;

    // Redirect to a checkout page or handle the checkout process here
    alert("Proceeding to checkout with delivery service: " + deliveryService);
    // Optionally redirect to another page or send data to the server
    // window.location.href = '/checkout/';
}
