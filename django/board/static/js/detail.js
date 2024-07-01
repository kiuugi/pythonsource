const deleteAll = document.querySelectorAll(".delete");
deleteAll.forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();
    const href = e.target.getAttribute("href");
    if (confirm("정말로 삭제 하시겠습니까?")) {
      location.href = href;
    }
  });
});

const actionForm = document.querySelector("#actionForm");
document.querySelector("#list").addEventListener("click", (e) => {
  e.preventDefault();

  actionForm.action = e.target.getAttribute("href");
  actionForm.submit();
});
