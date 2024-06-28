// #top_keyword 가져오기
// 검색어 없는경우 alert()
const actionForm = document.querySelector("#actionForm");
document.querySelector("#btn_search").addEventListener("click", (e) => {
  const top_key = document.querySelector("#top_keyword").value;
  if (top_key == "") {
    alert("검색어를 입력해 주세요");
    top_key.focus();
    return;
  }
  actionForm.querySelector("#keyword").value = top_key;
  actionForm.querySelector("#page").value = 1;
  actionForm.submit();
});
// 있는경우
// actionForm keyword value 에 삽입
// page value 1로 변경
