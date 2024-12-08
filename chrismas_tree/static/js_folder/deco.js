let selectedDecoration = ''; 

// 장식 버튼 클릭 시 호출되는 함수
function selectDecoration(decoration) {
    if (decoration == 'decoration_1') {
        selectDecoration = 1;
    } else if (decoration == 'decoration_2') {
        selectDecoration = 2;
        // console.log(typeof(selectDecoration)) type : number 2 ?

    } else if (decoration == 'decoration_3') {
        selectDecoration = 3;
    }
    document.getElementById('decorations').value = selectDecoration; // hidden 필드에 숫자 값 저장
    
    console.log("선택된 장식:", decoration);
    console.log(decorations)
}


function submitForm(event) {
    event.preventDefault(); // 기본 폼 제출을 막고, fetch로 비동기 요청 처리

    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;

    if (!title || !content) {
        alert('제목과 내용을 입력해주세요.');
        return;
    }
    
    if (!selectedDecoration) {
        alert('장식을 선택해주세요.');
        return;
    }

    const formData = new FormData();
    formData.append('title', title); 
    formData.append('content', content);  
    formData.append('decoration', selectedDecoration);  

    // fetch API를 사용해 POST 요청 보내기
    fetch('/submit_post/', {
        method: 'POST',        
        body: formData,       
    })
    .then(response => response.json())  
    .then(data => {
        if (data.success) {
            alert('제출이 완료되었습니다!');  
        } else {
            alert('제출에 실패했습니다.');  
        }
    })
    .catch(error => {
        console.error('Error:', error);  // 오류가 발생하면 콘솔에 출력
    });
}