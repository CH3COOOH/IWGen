function getHtml(url, async=false) {
	if (window.XMLHttpRequest) {
		xmlHttp = new XMLHttpRequest();
	} else {
		xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlHttp.open("GET", url, async);
	xmlHttp.send(null);
	return xmlHttp.responseText


}

function selectorGen() {

	var pics = getHtml('itemList.json')
	//console.log(pics)
	return JSON.parse(pics)

}

