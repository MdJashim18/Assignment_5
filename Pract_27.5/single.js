// const getUsers = () => {
//     const param = new URLSearchParams(window.location.search).get("UsersId");
//     console.log(param);
//     if (param) {
//         fetch(`https://fakestoreapi.com/users/${param}`)
//           .then((res) => res.json())
//           .then((data) => displayUsers(data))
//           .catch((err) => console.error("Error fetching service details:", err));
//     } else {
//         console.error("Service ID not found in URL");
//     }
// };


// const displayUsers = (users) => {
//     users.forEach((user) => {
//         const parent = document.getElementById("Table_body_single");
//         const row = document.createElement("tr");
//         row.innerHTML = `
//           <td>${user.id}</td>
//           <td>${user.name.firstname} ${user.name.lastname}</td>
//           <td>${user.email}</td>
//           <td>${user.username}</td>
//           <td>${user.phone}</td>
//           <td>${user.address.number} ${user.address.street}, ${user.address.city}, ${user.address.zipcode}</td>
//           <td><a href="single.html?UsersId=${user.id}" class="btn btn-warning" >Details</a> </td>
//         `;
//         parent.appendChild(row);
//     });
// };



// getUsers();




const getUsers = () => {
    const userId = new URLSearchParams(window.location.search).get("UsersId"); // Better name: "userId"
    console.log(userId);
    if (userId) {
        fetch(`https://fakestoreapi.com/users/${userId}`)
            .then((res) => {
                if (!res.ok) {
                    throw new Error("User not found");
                }
                return res.json();
            })
            .then((data) => displayUser(data))
            .catch((err) => {
                console.error("Error fetching user details:", err);
                displayError("Unable to fetch user details. Please try again later.");
            });
    } else {
        console.error("User ID not found in URL");
        displayError("User ID is missing in the URL.");
    }
};

const displayUser = (user) => {
    const parent = document.getElementById("Table_body_single");
    const row = document.createElement("tr");
    row.innerHTML = `
        <td>${user.id}</td>
        <td>${user.name.firstname} ${user.name.lastname}</td>
        <td>${user.email}</td>
        <td>${user.username}</td>
        <td>${user.phone}</td>
        <td>${user.address.city}</td>
        <td>${user.address.street} </td>
        <td>${user.address.zipcode}</td>
        <td>${user.address.number}</td>
        
    `;
    parent.appendChild(row);
};

const displayError = (message) => {
    const parent = document.getElementById("Table_body_single");
    const row = document.createElement("tr");
    row.innerHTML = `
        <td colspan="7" class="text-danger text-center">${message}</td>
    `;
    parent.appendChild(row);
};

getUsers();
