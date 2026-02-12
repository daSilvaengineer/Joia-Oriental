document.addEventListener("click", function (event) {

    const toggle = event.target.closest(".toggle-password");
    if (!toggle) return;

    event.preventDefault();

    const wrapper = toggle.closest(".password-wrapper");
    if (!wrapper) return;

    const input = wrapper.querySelector("input[type='password'], input[type='text']");
    if (!input) return;

    const isPassword = input.type === "password";

    input.type = isPassword ? "text" : "password";
    toggle.textContent = isPassword ? "🙈" : "👁";

    toggle.classList.toggle("active", isPassword);
});
