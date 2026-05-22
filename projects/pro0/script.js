function addStatus() {
    let name = document.getElementById("name").value;
    let status = document.getElementById("status").value;
    let place = document.getElementById("place").value;

    let text = "";

    if (status === "Out" && place !== "") {
        text = name + " - " + place;
    } else {
        text = name + " - " + status;
    }

    let li = document.createElement("li");
    li.innerText = text;

    document.getElementById("list").appendChild(li);

    // Clear inputs
    document.getElementById("name").value = "";
    document.getElementById("place").value = "";
}