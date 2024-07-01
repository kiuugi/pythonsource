const actionForm = document.querySelector("#actionForm");

// #top_keyword 가져오기
// 검색어 없는경우 alert()
document.querySelector("#btn_search").addEventListener("click", (e) => {
  const top_key = document.querySelector("#top_keyword").value;

  if (top_key == "") {
    alert("검색어를 입력해 주세요");
    top_key.focus();
    return;
  }

  // 있는경우
  // actionForm keyword value 에 삽입
  // page value 1로 변경
  actionForm.querySelector("#keyword").value = top_key;
  actionForm.querySelector("#page").value = 1;
  actionForm.submit();
});

// 정렬 변화가 일어나는 value 가져온 후
// actionForm 의 so value 변경
document.querySelector(".so").addEventListener("change", (e) => {
  actionForm.querySelector("#so").value = e.target.value;
  actionForm.submit();
});

// 페이지 나누기 + 검색어
// 페이지 나누기 클릭시 href 에 있는 값 가져오기
// actionForm 의 page value 변경하기
document.querySelector(".pagination").addEventListener("click", (e) => {
  e.preventDefault();
  actionForm.querySelector("#page").value = e.target.getAttribute("href");
  actionForm.submit();
});

//  제목 클릭 시 actionForm 보내기
document.querySelectorAll(".title").forEach((title) => {
  title.addEventListener("click", (e) => {
    e.preventDefault();

    // href 값 가져오기
    // actionForm  action 수정 /board/1
    // qid = e.target.getAttribute("href");
    // actionForm.action = "/board/" + qid;
    actionForm.action = `/board/${e.target.getAttribute("href")}`;

    actionForm.submit();
  });
});
