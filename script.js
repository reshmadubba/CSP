/* =========================================
   QR-BASED LOCAL INFORMATION SYSTEM
   MAIN JAVASCRIPT
   ========================================= */

document.addEventListener("DOMContentLoaded", function () {

    console.log("QR Local Information System loaded successfully.");

    /* =========================================
       BACKEND API URL
       ========================================= */

    const API_URL =
        "https://qr-local-information-system.onrender.com";


    /* =========================================
       LOGIN FORM
       ========================================= */

    const loginForm =
        document.getElementById("loginForm");

    if (loginForm) {

        loginForm.addEventListener(
            "submit",
            async function (event) {

                event.preventDefault();

                const usernameElement =
                    document.getElementById("username");

                const passwordElement =
                    document.getElementById("password");

                const username =
                    usernameElement
                        ? usernameElement.value.trim()
                        : "";

                const password =
                    passwordElement
                        ? passwordElement.value.trim()
                        : "";

                const message =
                    document.getElementById("login-message");


                if (username === "" || password === "") {

                    if (message) {
                        message.textContent =
                            "Please enter both username and password.";

                        message.style.color = "red";
                    }

                    return;
                }


                if (message) {
                    message.textContent =
                        "Checking login details...";

                    message.style.color = "";
                }


                try {

                    const response = await fetch(
                        API_URL + "/api/login",
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body: JSON.stringify({
                                username: username,
                                password: password
                            })
                        }
                    );


                    const data =
                        await response.json();


                    if (response.ok && data.success) {

                        if (message) {
                            message.textContent =
                                "Login successful!";

                            message.style.color =
                                "green";
                        }


                        localStorage.setItem(
                            "adminLoggedIn",
                            "true"
                        );


                        setTimeout(function () {

                            window.location.href =
                                "dashboard.html";

                        }, 500);

                    }

                    else {

                        if (message) {
                            message.textContent =
                                data.message ||
                                "Invalid username or password.";

                            message.style.color =
                                "red";
                        }

                    }

                }

                catch (error) {

                    console.error(
                        "Login Error:",
                        error
                    );


                    if (message) {

                        message.textContent =
                            "Unable to connect to the backend.";

                        message.style.color =
                            "red";

                    }

                }

            }
        );
    }


    /* =========================================
       SERVICE CARDS
       ========================================= */

    const serviceCards =
        document.querySelectorAll(".service-card");


    serviceCards.forEach(function (card) {

        card.addEventListener(
            "click",
            function () {

                const page =
                    card.getAttribute("data-page");

                if (page) {
                    window.location.href = page;
                }

            }
        );

    });


    /* =========================================
       VIEW INFORMATION BUTTONS
       ========================================= */

    const infoButtons =
        document.querySelectorAll(".info-button");


    infoButtons.forEach(function (button) {

        button.addEventListener(
            "click",
            function (event) {

                event.stopPropagation();

                const page =
                    button.getAttribute("data-page");

                if
