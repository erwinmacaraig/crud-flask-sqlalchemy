function getMeADog(){
    let xmlHttpRequest = new XMLHttpRequest();
    const dogUrl = 'https://dog.ceo/api/breeds/image/random';
    xmlHttpRequest.open("GET", dogUrl);
    xmlHttpRequest.getResponseHeader("Content-type", "application/json");
    xmlHttpRequest.onreadystatechange = function(){
        if (xmlHttpRequest.readyState == 4) {
            const obj = JSON.parse(xmlHttpRequest.responseText);
            document.getElementById('img-dog').src = obj['message'];
        }
    }
    xmlHttpRequest.send();
}
