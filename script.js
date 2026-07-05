function sendData() {
    let msg = document.getElementById("msg").value;

    fetch("/predict", {
        method: "POST",
        body: JSON.stringify({ message: msg }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = data.result;
        loadHistory();
    });
}

function loadHistory() {
    fetch("/history")
    .then(res => res.json())
    .then(data => {
        let list = document.getElementById("history");
        list.innerHTML = "";

        data.forEach(item => {
            let li = document.createElement("li");
            li.innerHTML = item.msg + " → " + item.result;
            list.appendChild(li);
        });
    });
}