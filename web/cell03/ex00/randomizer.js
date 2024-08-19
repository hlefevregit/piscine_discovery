let btn = document.getElementById("b1");

btn.addEventListener("click", randomize);

function    randomize(){

    var x = Math.floor(Math.random() * 256);
    var y = Math.floor(Math.random() * 256);
    var z = Math.floor(Math.random() * 256);
    // Construct the RGB color string.
    var bgColor = "rgb(" + x + "," + y + "," + z + ")";
    // Set the background color of the document body to the generated color.
    document.body.style.background = bgColor;

}
