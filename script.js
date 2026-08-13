/* =========================================
   QR-BASED LOCAL INFORMATION SYSTEM
   MAIN JAVASCRIPT
   ========================================= */

document.addEventListener("DOMContentLoaded", function () {

    console.log("QR Local Information System loaded successfully.");


    /* =========================================
       LOGIN FORM
       ========================================= */

    const loginForm = document.getElementById("loginForm");

    if (loginForm) {

        loginForm.addEventListener("submit", function (event) {

            event.preventDefault();

            const usernameElement = document.getElementById("username");
            const passwordElement = document.getElementById("password");

            const username = usernameElement
                ? usernameElement.value.trim()
                : "";

            const password = passwordElement
                ? passwordElement.value.trim()
                : "";

            if (username === "" || password === "") {
                alert("Please enter both username and password.");
                return;
            }

            /*
             * TEMPORARY FRONTEND LOGIN
             * This is only for testing.
             * Real authentication will be connected
             * to the backend later.
             */

            if (username === "admin" && password === "admin123") {

                alert("Login successful!");

                window.location.href = "dashboard.html";

            } else {

                alert("Invalid username or password.");

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

            const page = card.getAttribute("data-page");

            if (page) {
                window.location.href = page;
            }
        });
    });


    /* =========================================
       VIEW INFORMATION BUTTONS
       ========================================= */

    const infoButtons =
        document.querySelectorAll(".info-button");

    infoButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            event.stopPropagation();

            const page = button.getAttribute("data-page");

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

        button.addEventListener("click", function () {

            const buttonText =
                button.textContent.trim().toLowerCase();


            if (buttonText.includes("hospital")) {

                window.location.href = "hospital.html";

            }

            else if (buttonText.includes("police")) {

                window.location.href = "police.html";

            }

            else if (buttonText.includes("emergency")) {

                window.location.href = "emergency.html";

            }

            else if (buttonText.includes("transport")) {

                window.location.href = "transport.html";

            }

            else if (buttonText.includes("government")) {

                window.location.href = "government.html";

            }

            else if (buttonText.includes("announcement")) {

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

        element.textContent = new Date().getFullYear();

    });

});