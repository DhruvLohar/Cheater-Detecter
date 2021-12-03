const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const login_btn = document.querySelector("#login-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

login_btn.addEventListener("click", (e) => {
    e.preventDefault();
    let data = {
        email: $('#email').val(),
        password: $('#password').val()
    }
    $.ajax({
        type: "POST",
        url: "/login/auth/",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: "json",
        success: function (response) {
            if (response.success == 'true') {
                window.location.replace("/exam/physics/");
            } else {
                $('.error-text').text(response.msg);
            }
        },
    });
});