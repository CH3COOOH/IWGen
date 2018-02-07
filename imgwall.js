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

function selectorGen(){
	var classify = {};
	var rawLst = getHtml('itemList.htm').split('\n');
	var currentClass = ''

	for (var i of rawLst) {
		var ii = i.replace(String.fromCharCode(13), '');
		if (i[0] == '#') {
			classify[ii] = [];
			currentClass = ii;
		} else {
			classify[currentClass].push(ii);
		}
	}
	return classify;
}

