function generateQRCode() {
	// var data = document.getElementById("data").value
	// eel.generate_qr(data)(setImage)
	eel.dummy("hola")(function(ret){
		alert(ret);
	})
}


function LoadPath(){
	eel.LoadImagesFromPage();
	// alert("Done...")
}

function CropIm(){
	eel.CropFromPage();
}

function AnalyseIm(){
	// alert("Wait until ends")
	eel.AnalyzeFromPage();
	// alert("Done...")
}
