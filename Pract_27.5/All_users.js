const loadUsers = () => {
    fetch("https://fakestoreapi.com/users")
        .then((res) => res.json())
        .then((data) => displayUsers(data))
        .catch((err) => {
            console.error(err);
            const parent = document.getElementById("Table_body");
            parent.innerHTML = `<tr><td colspan="6">Failed to load user data.</td></tr>`;
        });
};

const displayUsers = (users) => {
    users.forEach((user) => {
        const parent = document.getElementById("Table_body");
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${user.id}</td>
          <td>${user.name.firstname} ${user.name.lastname}</td>
          <td>${user.email}</td>
          <td>${user.username}</td>
          <td>${user.phone}</td>
          <td>${user.address.number} ${user.address.street}, ${user.address.city}, ${user.address.zipcode}</td>
          <td><a href="single.html?UsersId=${user.id}" class="btn btn-warning" >Details</a> </td>
        `;
        parent.appendChild(row);
    });
};

loadUsers();
