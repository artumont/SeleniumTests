const products = [
    { id: 1, name: 'Product 1', price: 19.99, image: '/static/ecommerce/placeholder.png' },
    { id: 2, name: 'Product 2', price: 29.99, image: '/static/ecommerce/placeholder.png' },
    { id: 3, name: 'Product 3', price: 39.99, image: '/static/ecommerce/placeholder.png' },
    { id: 4, name: 'Product 4', price: 49.99, image: '/static/ecommerce/placeholder.png' }
];

let cart = [];
let isViewingCart = false;

document.addEventListener('DOMContentLoaded', () => {
    setupAddToCartButtons();
    setupCartViewButton();
    setupCheckoutButton();
    setupPaymentForm();
    setupContinueShoppingButton();
});

function setupAddToCartButtons() {
    document.querySelectorAll('.add-to-cart-btn').forEach(button => {
        button.addEventListener('click', () => {
            const productId = parseInt(button.getAttribute('data-id'));
            addToCart(productId);
        });
    });
}

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    const existingItem = cart.find(item => item.id === productId);

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({ ...product, quantity: 1 });
    }

    updateCartCount();
    updateCartDisplay();
}

function updateCartCount() {
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    document.getElementById('cart-count').textContent = totalItems;
}

function updateCartDisplay() {
    const cartItems = document.getElementById('cart-items');
    cartItems.innerHTML = '';

    cart.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.className = 'cart-item';
        itemElement.innerHTML = `
            <div class="cart-item-info">
                <img src="${item.image}" alt="${item.name}">
                <div>
                    <h3>${item.name}</h3>
                    <p>Quantity: ${item.quantity}</p>
                    <p>$${(item.price * item.quantity).toFixed(2)}</p>
                </div>
            </div>
            <button class="remove-item-btn" data-id="${item.id}">Remove</button>
        `;

        itemElement.querySelector('.remove-item-btn').addEventListener('click', () => {
            removeFromCart(item.id);
        });

        cartItems.appendChild(itemElement);
    });

    updateCartTotal();
}

function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    updateCartCount();
    updateCartDisplay();
}

function updateCartTotal() {
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    document.getElementById('total-amount').textContent = total.toFixed(2);
}

function setupCartViewButton() {
    document.getElementById('view-cart-btn').addEventListener('click', () => {
        if (!isViewingCart) {
            document.getElementById('products').classList.add('hidden');
            document.getElementById('cart').classList.remove('hidden');
            document.getElementById('checkout-form').classList.add('hidden');
            document.getElementById('order-confirmation').classList.add('hidden');
            isViewingCart = true;
        }
        else {
            document.getElementById('products').classList.remove('hidden');
            document.getElementById('cart').classList.add('hidden');
            document.getElementById('checkout-form').classList.add('hidden');
            document.getElementById('order-confirmation').classList.add('hidden');
            isViewingCart = false;
        }
    });
}

function setupCheckoutButton() {
    document.getElementById('checkout-btn').addEventListener('click', () => {
        if (cart.length === 0) {
            alert('Your cart is empty!');
            return;
        }
        document.getElementById('cart').classList.add('hidden');
        document.getElementById('checkout-form').classList.remove('hidden');
    });
}

function setupPaymentForm() {
    document.getElementById('payment-form').addEventListener('submit', (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const address = document.getElementById('address').value;
        const cardNumber = document.getElementById('card-number').value;
        const expiryDate = document.getElementById('expiry-date').value;
        const cvv = document.getElementById('cvv').value;

        if (!validateForm(name, email, address, cardNumber, expiryDate, cvv)) {
            return;
        }

        const orderNumber = generateOrderNumber();
        document.getElementById('order-number').textContent = orderNumber;
        
        document.getElementById('checkout-form').classList.add('hidden');
        document.getElementById('order-confirmation').classList.remove('hidden');

        cart = [];
        updateCartCount();
    });
}

function validateForm(name, email, address, cardNumber, expiryDate, cvv) {
    if (!name || !email || !address || !cardNumber || !expiryDate || !cvv) {
        alert('Please fill in all fields');
        return false;
    }

    if (!/^\d{16}$/.test(cardNumber)) {
        alert('Please enter a valid 16-digit card number');
        return false;
    }

    if (!/^\d{2}\/\d{2}$/.test(expiryDate)) {
        alert('Please enter expiry date in MM/YY format');
        return false;
    }

    if (!/^\d{3}$/.test(cvv)) {
        alert('Please enter a valid 3-digit CVV');
        return false;
    }

    return true;
}

function generateOrderNumber() {
    return 'ORDER-' + Math.random().toString(36).substring(2, 10).toUpperCase();
}

function setupContinueShoppingButton() {
    document.getElementById('continue-shopping-btn').addEventListener('click', () => {
        document.getElementById('products').classList.remove('hidden');
        document.getElementById('order-confirmation').classList.add('hidden');
    });
}
