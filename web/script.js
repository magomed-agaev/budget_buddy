function Signin() {
    var email = document.getElementById("loginEmail").value;
    var password_hash = document.getElementById("loginPassword").value;
    // console.log(window.Location.href);

    eel.Signin(email, password_hash);

    // window.location.href = 'index_chat.html'; 

}
// eel.expose(redirection_chat);
// function redirection_chat() {
//     window.location.href = 'index_chat.html'; 
// }

// eel.expose(getUserEmail);
// function getUserEmail() {
//     var email = document.getElementById("email").value;
//     console.log(email)
//     return email
// }

function Signup() {
    var nom = document.getElementById("signupLastname").value;
    var prenom = document.getElementById("signupFirstname").value;
    var email = document.getElementById("signupEmail").value;
    var password_hash = document.getElementById("signupPassword").value;
    eel.Signup(nom, prenom, email, password_hash);
}

function setFormMessage(formElement, type, message) {
    const messageElement = formElement.querySelector(".form__message");

    messageElement.textContent = message;
    messageElement.classList.remove("form__message--success", "form__message--error");
    messageElement.classList.add(`form__message--${type}`);
}


function setInputError(inputElement, message) {
    inputElement.classList.add("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = message;
}

function clearInputError(inputElement) {
    inputElement.classList.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = "";
}

// onclick se mets automatiquement sur le input : si DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");
    const createAccountForm = document.querySelector("#createAccount");

    document.querySelector("#linkCreateAccount").addEventListener("click", e => {
        e.preventDefault(); //arrete la redirection on clickant sur le link
        loginForm.classList.add("form--hidden"); //cashe le form login
        createAccountForm.classList.remove("form--hidden"); //montre le form create account
    });

    document.querySelector("#linkLogin").addEventListener("click", e => {
        e.preventDefault();//arrete la redirection on clickant sur le link
        loginForm.classList.remove("form--hidden"); //montre le form log in
        createAccountForm.classList.add("form--hidden");//cache le fomr create account
    });

    // loginForm.addEventListener("submit", e => {
    //     e.preventDefault();


    //     setFormMessage(loginForm, "error", "Invalid username or password");
    // });

    document.querySelectorAll(".form__input").forEach(inputElement => {
        inputElement.addEventListener("blur", e => {
            if (e.target.id === "signupFirstname" && e.target.value.length < 1) {
                setInputError(inputElement, "First-name must be at least 1 characters in length");
            }

        });
        document.querySelectorAll(".form__input").forEach(inputElement => {
            inputElement.addEventListener("blur", e => {
                if (e.target.id === "signupLastname" && e.target.value.length < 1) {
                    setInputError(inputElement, "Last-name must be at least 1 characters in length");
                }

            });
            // @ est obligatoire
            document.querySelectorAll(".form__input").forEach(inputElement => {
                inputElement.addEventListener("blur", e => {
                    if (e.target.id === "email_adress" && !e.target.value.includes("@")) {
                        setInputError(inputElement, "Email address must contain the '@' symbol.");
                    }
                });
            });
            //  Les caracteres speciaux sont obligatoires
            document.querySelectorAll(".form__input").forEach(inputElement => {
                inputElement.addEventListener("blur", e => {
                    if (e.target.id === "password" && !e.target.value.includes("@.,_?§!$*µ)([]-&~")) {
                        setInputError(inputElement, "Password must contain at least one special character: @.,_?§!$*µ)([]-&~");
                    }
                });
            });
            inputElement.addEventListener("input", e => {
                clearInputError(inputElement);
            });
        });
    });
});