const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("serviceId");
    console.log(param);
    if (param) {
        fetch(`https://fakestoreapi.com/products/${param}`)
          .then((res) => res.json())
          .then((data) => displayDetails(data))
          .catch((err) => console.error("Error fetching service details:", err));
    } else {
        console.error("Service ID not found in URL");
    }
};


const displayDetails = (service) => {
    console.log(service);
    const parent = document.getElementById("doc-details");
    const div = document.createElement("div");
    div.classList.add("doc-details-container");
    const ratingRate = service.rating?.rate?.toFixed(2) || "N/A";
    const ratingCount = service.rating?.count || "N/A";
    div.innerHTML = `
      <div class="doctor-img col-4">
        <img src="${service.image}" alt="${service.title}" />
      </div>
      <div class="doc-info col-8">
        <h1>ID : ${service.id}</h1>
        <h1>Name : ${service.title}</h1>
        <p>Description : ${service.description}</p>
        <p>Category : ${service.category}</p>
        <h5>Rating : ${ratingRate} Count : ${ratingCount}</h5>
        <h5>Price: $${service.price}</h5>
      </div>
    `;
    parent.appendChild(div);
};



getparams();