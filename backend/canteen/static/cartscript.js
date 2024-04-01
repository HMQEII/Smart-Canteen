document.addEventListener("DOMContentLoaded", () => {
  const pid = localStorage.getItem("pid");
  fetch(`/getCartItems?pid=${pid}`)
    .then((response) => response.json())
    .then((cartItems) => {
      const tbody = document.getElementById("cart-items");
      cartItems.forEach((item) => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td><a href="#" class="trash-icon"><ion-icon  name="trash-outline"></ion-icon></a></td>
          <td><img src="${item.image}" alt="" /></td>
          <td>${item.category}</td>
          <td>${item.Itemname}</td>
          <td>₹${item.price}</td>
          <td><input class="w-25 pl-1" value="1" min="1" type="number" /></td>
          <td>₹${item.price}</td>
        `;
        tbody.appendChild(row);

        // Event listener to the trash icon
        const trashIcon = row.querySelector(".trash-icon");
        trashIcon.addEventListener("click", (event) => {
          event.preventDefault();
          const pid = localStorage.getItem("pid");
          const itemName = row.querySelector("td:nth-child(4)").textContent;
          const confirmed = confirm("Are you sure you want to delete this item?");
          if (confirmed) {
            fetch(`/deleteCartItem/${pid}/${encodeURIComponent(itemName)}/`, {
                method: "DELETE",
            })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    openPopup('Item discarded successfully');
                    location.reload();
                } else {
                    openPopup("Failed to delete the item from the database.");
                }
            })
            .catch((error) => console.error(error));
          }
        });

        // Update total price when quantity changes
        const quantityInput = row.querySelector("input[type='number']");
        quantityInput.addEventListener("input", () => {
          const quantity = parseInt(quantityInput.value, 10);
          const price = item.price;
          const totalPrice = quantity * price;
          // Update the total price in the row
          row.querySelector("td:last-child").textContent = `₹${totalPrice}`;
          
          calculateTotalPrice();
        });
      });

      // Function to calculate total price
      function calculateTotalPrice() {
        let totalPrice = 0;
        const priceElements = document.querySelectorAll("#cart-items td:last-child");
        priceElements.forEach((priceElement) => {
          const priceText = priceElement.textContent;
          const priceValue = parseInt(priceText.substring(1), 10); // Remove ₹ sign
          totalPrice += priceValue;
        });
        document.getElementById("total").textContent = `₹${totalPrice.toFixed(2)}`;
      }

      // Initial calculation of total price
      calculateTotalPrice();
    })
    .catch((error) => {
      console.error("Error fetching cart items:", error);
    });
});