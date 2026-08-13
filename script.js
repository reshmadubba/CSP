/* =========================================
   QR-BASED LOCAL INFORMATION SYSTEM
   MAIN JAVASCRIPT
   ========================================= */

document.addEventListener("DOMContentLoaded", function () {

    console.log("QR Local Information System loaded successfully.");

    const API_URL =
        "https://qr-local-information-system.onrender.com";


    /* =========================================
       ADMIN LOGIN
       ========================================= */

    const loginForm =
        document.getElementById("loginForm");

    if (loginForm) {

        loginForm.addEventListener("submit", async function (event) {

            event.preventDefault();

            const username =
                document.getElementById("username").value.trim();

            const password =
                document.getElementById("password").value.trim();

            const message =
                document.getElementById("login-message");

            if (!username || !password) {

                if (message) {
                    message.textContent =
                        "Please enter username and password.";
                    message.style.color = "red";
                }

                return;
            }

            if (message) {
                message.textContent =
                    "Checking login details...";
            }

            try {

                const response = await fetch(
                    API_URL + "/api/login",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            username: username,
                            password: password
                        })
                    }
                );

                const data = await response.json();

                if (response.ok && data.success) {

                    localStorage.setItem(
                        "adminLoggedIn",
                        "true"
                    );

                    if (message) {
                        message.textContent =
                            "Login successful!";
                        message.style.color = "green";
                    }

                    setTimeout(function () {
                        window.location.href =
                            "dashboard.html";
                    }, 500);

                } else {

                    if (message) {
                        message.textContent =
                            data.message ||
                            "Invalid username or password.";
                        message.style.color = "red";
                    }
                }

            } catch (error) {

                console.error("Login Error:", error);

                if (message) {
                    message.textContent =
                        "Unable to connect to the backend.";
                    message.style.color = "red";
                }
            }
        });
    }


    /* =========================================
       SERVICE CARDS
       ========================================= */

    const serviceCards =
        document.querySelectorAll(".service-card");

    serviceCards.forEach(function (card) {

        card.addEventListener("click", function () {

            const page =
                card.getAttribute("data-page");

            if (page) {
                window.location.href = page;
            }

        });
    });


    /* =========================================
       INFO BUTTONS
       ========================================= */

    const infoButtons =
        document.querySelectorAll(".info-button");

    infoButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            event.stopPropagation();

            const page =
                button.getAttribute("data-page");

            if (page) {
                window.location.href = page;
            }

        });
    });


    /* =========================================
       DASHBOARD BUTTONS
       ========================================= */

    const dashboardButtons =
        document.querySelectorAll(".dashboard-button");

    dashboardButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            event.stopPropagation();

            const page =
                button.closest(".service-card")
                ?.getAttribute("data-page");

            if (page) {
                window.location.href = page;
                return;
            }

            const text =
                button.textContent
                .trim()
                .toLowerCase();

            if (text.includes("hospital")) {
                window.location.href = "hospital.html";
            }

            else if (text.includes("police")) {
                window.location.href = "police.html";
            }

            else if (text.includes("emergency")) {
                window.location.href = "emergency.html";
            }

            else if (text.includes("transport")) {
                window.location.href = "transport.html";
            }

            else if (text.includes("government")) {
                window.location.href = "government.html";
            }

            else if (text.includes("announcement")) {
                window.location.href = "announcement.html";
            }

        });
    });


    /* =========================================
       CURRENT YEAR
       ========================================= */

    const yearElements =
        document.querySelectorAll(".current-year");

    yearElements.forEach(function (element) {

        element.textContent =
            new Date().getFullYear();

    });

});
