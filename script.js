const header = document.querySelector("header");
window.addEventListener ("scroll", function(){
    header.classList.toggle("sticky", this.window.scrollY > 0);
});
const formOpenBtn = document.querySelector("#form-open"),
home = document.querySelector(".home"),
fromContainer = document.querySelector(".from_container"),
formCloseBtn = document.querySelector(".form_close"),
signupBtn = document.querySelector("#signup"),
loginBtn = document.querySelector("#login")
pwShowHide = document.querySelectorAll(".pw_hide");

formOpenBtn.addEventListener("click", () => home.classList.add("show"));
formCloseBtn.addEventListener("click", () => home.classList.remove("remove"));

pwShowHide.forEach(icon => {
    icon.addEventListener("click", () => {
        let getPwInput = icon.parentElement.querySelector("input");
        if(getPwInput.type === "password"){
            getPwInput.type = "text";
            icon.classList.replace("uil-eye-slash", "uil-eye")
        }else{
            getPwInput.type = "password";
            icon.classList.replace("uil-eye", "uil-eye-slash")
        }
    })
})

signupBtn.addEventListener("click", (e) => {
    e.preventDefault();
    fromContainer.classList.add("active");
})

loginBtn.addEventListener("click", (e) => {
    e.preventDefault();
    fromContainer.classList.remove("active");
})
let menu = document.querySelector("#menu-btn");
let nav_item = document.querySelector('.nav_item');
menu.onclick = () =>{
    menu.classList.toggle('bx-x');
    nav_item.classList.toggle('open');
}
