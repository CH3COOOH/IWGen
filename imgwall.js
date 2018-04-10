// function selectorGen() {
// 	var pics;
// 	$.getJSON('itemList.json').done(function (data) {
// 		pics = data;
// 	});
// 	return pics
// }

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
	return JSON.parse(pics)
	// return $.getJSON('./itemList.json').responseJSON

}