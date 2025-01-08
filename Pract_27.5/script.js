const loadCategories = () => {
  fetch("https://fakestoreapi.com/products/categories/")
    .then((res) => res.json())
    .then((data) => {
      data.forEach((item) => {
        const parent = document.getElementById("drop-deg");
        const li = document.createElement("li");
        li.classList.add("dropdown-item");
        li.innerText = item;
        li.addEventListener('click', () => filterProductsByCategory(item));
        parent.appendChild(li);
      });
    });
};


const filterProductsByCategory = (category) => {
  fetch(`https://fakestoreapi.com/products/category/${category}`)
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("service-container").innerHTML = '';
      displayProduct(data);
    })
    .catch((err) => console.log(err));
};



const loadProducts = () => {
  fetch("https://fakestoreapi.com/products/")
    .then((res) => res.json())
    .then((data) => displayProduct(data))
    .catch((err) => console.log(err));
};

const displayProduct = (services) => {
  services.forEach((service) => {
    const parent = document.getElementById("service-container");
    const div = document.createElement("div");
    div.classList.add("col"); 
    div.innerHTML = `
      <div class="card shadow h-100">
        <div class="ratio ratio-16x9">
          <img
            src="${service.image}"
            class="card-img-top"
            loading="lazy"
            alt="${service.title}"
          />
        </div>
        <div class="card-body p-3 p-xl-5">
          <h3 class="card-title h5">${service.title}</h3>
          <h3 class="card-title h5">Category : ${service.category}</h3>
          <p class="card-text">
            ${service.description.slice(0, 140)}
          </p>
          <a href="ProDetails.html?serviceId=${service.id}"  class="btn btn-primary">Details</a>
          
        </div>
      </div>
    `;
    parent.appendChild(div);
  });
};


loadCategories();
loadProducts();