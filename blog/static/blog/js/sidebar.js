const toggleBtn = document.getElementById("menuToggle")
const sidebar = document.getElementById("sidebar")

toggleBtn.addEventListener("click", () => {
  sidebar.classList.toggle("open")
})

const menuItems = document.querySelectorAll(".sidebar-options li")

menuItems.forEach(item => {
  item.addEventListener("click", () => {

    menuItems.forEach(i => i.classList.remove("active"))

    item.classList.add("active")

  })
})